import copy

import pytest

from core_contracts.editorial import EditorialWrite
from core_contracts.registry import fingerprints

from .conftest import activate
from .test_runtime import obs
from .test_workbench_api import api_client


def request(identity="fixture.echo", *, version=0, category="climate", draft=None):
    return {
        "object": {"kind": "contract", "id": identity},
        "expected_editorial_version": version,
        "category": category,
        "room": {"mode": "manual", "name": "Arbeitszimmer", "icon": "mdi:desk"},
        **(
            {"draft_id": draft["draft_id"], "draft_version": draft["draft_version"]}
            if draft
            else {}
        ),
    }


async def save(runtime, data):
    return await runtime.submit(
        "editorial_put", {"request": data, "_actor": {"kind": "token", "role": "admin"}}
    )


async def test_editorial_changes_do_not_evaluate_change_checksum_or_restart_state(
    runtime, config, monkeypatch
):
    await activate(runtime, config)
    await runtime.submit("observation", obs(runtime))
    snapshot = copy.deepcopy(runtime.snapshot())
    nodes = copy.deepcopy(runtime.state.tables["node_state"])
    fingerprint = fingerprints(runtime.config, runtime.types)
    revision = copy.deepcopy(await runtime.store.get("registry_revision", "1"))
    monkeypatch.setattr(
        runtime,
        "_evaluate",
        lambda *args, **kwargs: pytest.fail("editorial change evaluated contracts"),
    )
    saved = await save(runtime, request())
    assert saved["editorial_version"] == 1
    assert runtime.snapshot() == snapshot and runtime.state.tables["node_state"] == nodes
    assert fingerprints(runtime.config, runtime.types) == fingerprint
    assert await runtime.store.get("registry_revision", "1") == revision
    assert "category" not in runtime.config.model_dump()["contracts"][0]


async def test_rollback_historical_draft_restart_and_database_recovery_keep_current_organization(
    runtime, config
):
    first = await activate(runtime, config)
    backup = copy.deepcopy(runtime.store.state)
    saved = await save(runtime, request())
    another = copy.deepcopy(config)
    another["contracts"][0]["display_name"] = "Anderer Name"
    await activate(runtime, another)
    await runtime.submit(
        "rollback",
        {"revision": first["revision"], "expected_active_revision": runtime.state.active_revision},
    )
    assert runtime.state.tables["editorial_current"]["contract:fixture.echo"] == saved
    old = await runtime.store.get("registry_revision", str(first["revision"]))
    await runtime.submit("draft_create", {"config": old["config"]})
    assert runtime.state.tables["editorial_current"]["contract:fixture.echo"] == saved
    await runtime._restore("process_restart")
    assert runtime.state.tables["editorial_current"]["contract:fixture.echo"] == saved
    runtime.store.state = backup
    await runtime.submit("recover")
    assert runtime.state.tables["editorial_current"]["contract:fixture.echo"] == saved


async def test_new_object_metadata_is_bound_to_draft_version_and_activated_atomically(
    runtime, config
):
    await activate(runtime, config)
    data = copy.deepcopy(config)
    data["contracts"].append({**data["contracts"][0], "contract_id": "example.new"})
    draft = await runtime.submit(
        "draft_create", {"config": data, "editorial": [request("example.new")]}
    )
    assert not runtime.state.tables["editorial_current"]
    assert (
        list(runtime.state.tables["editorial_draft"].values())[0]["draft_version"]
        == draft["draft_version"]
    )
    with pytest.raises(ValueError, match="draft_version_conflict"):
        await save(runtime, request("example.new", version=1, draft={**draft, "draft_version": 99}))
    changed = await runtime.submit("draft_update", {**draft, "config": data})
    assert (
        list(runtime.state.tables["editorial_draft"].values())[0]["draft_version"]
        == changed["draft_version"]
    )
    await runtime.submit(
        "activate", {**changed, "expected_active_revision": runtime.state.active_revision}
    )
    assert (
        runtime.state.tables["editorial_current"]["contract:example.new"]["category"] == "climate"
    )
    assert not runtime.state.tables["editorial_draft"]


async def test_invalid_activation_and_discard_cannot_partially_publish_metadata(runtime, config):
    await activate(runtime, config)
    data = copy.deepcopy(config)
    data["contracts"].append(
        {**data["contracts"][0], "contract_id": "example.bad", "type_id": "unknown.template"}
    )
    draft = await runtime.submit(
        "draft_create", {"config": data, "editorial": [request("example.bad")]}
    )
    with pytest.raises(ValueError):
        await runtime.submit(
            "activate", {**draft, "expected_active_revision": runtime.state.active_revision}
        )
    assert not runtime.state.tables["editorial_current"]
    assert runtime.state.tables["editorial_draft"]
    await runtime.submit("draft_delete", draft)
    assert not runtime.state.tables["editorial_draft"]


async def test_editorial_optimistic_concurrency_and_commit_failure_preserve_previous(
    runtime, config
):
    await activate(runtime, config)
    first = await save(runtime, request())
    with pytest.raises(ValueError, match="editorial_version_conflict"):
        await save(runtime, request(category="media"))
    runtime.store.before_commit = lambda: (_ for _ in ()).throw(OSError("failure"))
    try:
        with pytest.raises(OSError):
            await save(runtime, request(version=1, category="media"))
        assert runtime.state.tables["editorial_current"]["contract:fixture.echo"] == first
    finally:
        runtime.store.before_commit = None


async def test_area_refresh_preserves_manual_room_and_marks_removed_suggestion(runtime, config):
    await activate(runtime, config)
    saved = await save(runtime, request())
    await runtime.submit(
        "editorial_area_refresh",
        [{"area_id": "office", "area_name": "Neu", "area_icon": "mdi:home"}],
    )
    assert runtime.state.tables["editorial_current"]["contract:fixture.echo"] == saved
    data = request(version=1)
    data["room"] = {"mode": "suggested", "area_id": "office", "name": "Büro", "icon": "mdi:desk"}
    await save(runtime, data)
    await runtime.submit(
        "editorial_area_refresh",
        [
            {
                "area_id": "office",
                "area_name": "Arbeitszimmer",
                "area_icon": "https://bad.example/a.svg",
            }
        ],
    )
    room = runtime.state.tables["editorial_current"]["contract:fixture.echo"]["room"]
    assert room["name"] == "Arbeitszimmer" and room["icon"] == "mdi:home"
    await runtime.submit("editorial_area_refresh", [])
    room = runtime.state.tables["editorial_current"]["contract:fixture.echo"]["room"]
    assert room["missing"] and room["name"] == "Arbeitszimmer"


async def test_editorial_api_remains_administrative(runtime, config, aiohttp_client, tmp_path):
    await activate(runtime, config)
    api, client, headers = await api_client(runtime, aiohttp_client, tmp_path)
    consumer = {"Authorization": "Bearer " + api.tokens.values["consumer"]}
    assert (await client.get("/api/v1/editorial", headers=consumer)).status == 403
    assert (await client.put("/api/v1/editorial", headers=consumer, json=request())).status == 403
    assert (await client.put("/api/v1/editorial", headers=headers, json=request())).status == 200
    assert (await client.put("/api/v1/editorial", headers=headers, json=request())).status == 409
    assert (
        len((await (await client.get("/api/v1/editorial", headers=headers)).json())["items"]) == 1
    )


async def test_existing_metadata_requires_current_scope_and_preserves_concurrent_changes(
    runtime, config
):
    await activate(runtime, config)
    draft = await runtime.submit("draft_create", {"config": config})
    first = await save(runtime, request())
    with pytest.raises(ValueError, match="editorial_scope_conflict"):
        await save(runtime, request(version=1, draft=draft))
    assert runtime.state.tables["editorial_current"]["contract:fixture.echo"] == first


@pytest.mark.parametrize(
    "category", ["climate", "light_cover", "presence", "sleep_wake", "media", "other"]
)
def test_fixed_categories_and_room_validation(category):
    assert EditorialWrite.model_validate(request(category=category)).category == category
    with pytest.raises(ValueError):
        EditorialWrite.model_validate(request(category="another"))
    data = request()
    data["room"] = {"mode": "manual", "name": "  "}
    with pytest.raises(ValueError):
        EditorialWrite.model_validate(data)
    data["room"] = {"mode": "manual", "name": "Zimmer", "icon": "https://example.org/icon.svg"}
    with pytest.raises(ValueError):
        EditorialWrite.model_validate(data)
