"""Activation is a revision, for interval edits AND unrelated configuration changes.

The unrelated cases also run unchanged against b3 (23d200f). In particular a
due refresh attempt is consumed as missed, without dispatch or quota charge.
"""

from copy import deepcopy
from datetime import timedelta
from uuid import uuid4

import pytest

from core_contracts.registry import storage_document

from .conftest import activate
from .test_alpha9_refresh import complete, edge, setup
from .test_declarative import definition, machine_definition, observation, registry, schema
from .test_phase1a import add_source


def heartbeat(config):
    config["sources"][0]["freshness"] = dict(
        mode="report_heartbeat", interval_s=1000, future_tolerance_s=1
    )
    return config


def changed(runtime, change):
    document = storage_document(runtime.config)
    if change == "interval":
        document["sources"][0]["freshness_selection"]["rule"]["interval_s"] *= 2
    else:
        add_source(document, "independent")
    return document


def initial(document, change):
    if change == "interval":
        from core_contracts.freshness_templates import upgrade_document

        return upgrade_document(document)
    return document


async def revision_after(runtime, document, seconds):
    from .test_beta3_authoring import envelope

    draft = await runtime.submit("draft_create", {"config": document})
    request = await envelope(runtime, draft)
    advance_without_tick(runtime, seconds)
    await runtime.submit("activate", request)


def advance_without_tick(runtime, seconds):
    # Make the activation itself the first transaction at the due instant.
    if runtime.evaluation_alarm:
        runtime.evaluation_alarm.cancel()
    runtime.clock.advance(seconds)


@pytest.mark.parametrize("change", ["interval", "unrelated"])
async def test_revision_preserves_machine_episode_transition_budget_quota_and_deadline(
    runtime, config, change, monkeypatch
):
    from core_contracts.statemachine import Machine

    document = registry(heartbeat(config), machine_definition())
    await activate(runtime, initial(document, change))
    await runtime.submit("observation", observation(runtime, True))
    result = await runtime.submit(
        "command",
        dict(
            command_id=str(uuid4()),
            contract_id="fixture.echo",
            command="start",
            args={"confirm": True},
            origin=dict(kind="test", actor="test", client_name="test"),
            issued_at=runtime.clock.now_utc(),
            valid_until=runtime.clock.now_utc() + timedelta(seconds=30),
        ),
    )
    assert result["status"] == "accepted"
    machine = runtime.state.tables["sm_instance"]["fixture.echo"]
    assert machine["state"] == "active" and machine["deadline"]
    tables = ("sm_instance", "sm_episode", "sm_transition", "deadline", "service_job")
    before = {key: deepcopy(runtime.state.tables[key]) for key in tables}
    quotas = deepcopy(runtime.state.tables["service_state"])
    baselines = []
    prepare = Machine.prepare

    def record(self, current, inputs, now, *, baseline=False):
        baselines.append(baseline)
        return prepare(self, current, inputs, now, baseline=baseline)

    monkeypatch.setattr(Machine, "prepare", record)
    await revision_after(runtime, changed(runtime, change), 1)
    assert baselines and all(baselines)
    assert {key: runtime.state.tables[key] for key in tables} == before
    assert runtime.state.tables["service_state"] == quotas


@pytest.mark.parametrize("change", ["interval", "unrelated"])
async def test_revision_consumes_due_refresh_as_missed_like_b3(runtime, config, change):
    # Reference: executed unchanged with change=unrelated on actual b3 23d200f.
    # Its existing run consumes offset 10 as missed; no new job/quota/episode.
    await setup(runtime, heartbeat(config))
    if change == "interval":
        await activate(runtime, initial(storage_document(runtime.config), change))
    await edge(runtime, True)
    await complete(runtime)
    before = deepcopy(runtime.state.tables["service_state"]["refresh:fixture.echo"])
    jobs = deepcopy(runtime.state.tables["service_job"])
    quota = {
        key: deepcopy(row)
        for key, row in runtime.state.tables["service_state"].items()
        if key.startswith("refresh_quota:")
    }
    assert quota and before["run"]["consumed"] == [0]
    await revision_after(runtime, changed(runtime, change), 10)
    after = runtime.state.tables["service_state"]["refresh:fixture.echo"]
    assert after["run"]["consumed"] == [0, 1]
    assert after["run"]["attempts"][-1]["outcome"] == "missed"
    for key in ("run_id", "started_at", "end_at", "revision"):
        assert after["run"][key] == before["run"][key]
    assert after["cooldown_until"] == before["cooldown_until"]
    assert runtime.state.tables["service_job"] == jobs
    assert {
        key: row
        for key, row in runtime.state.tables["service_state"].items()
        if key.startswith("refresh_quota:")
    } == quota


@pytest.mark.parametrize("change", ["interval", "unrelated"])
async def test_revision_only_plans_due_notifications_at_commit_like_b3(
    runtime, config, change, monkeypatch
):
    from core_contracts import notifications

    from .test_alpha9_notifications import document

    runtime.installation_id = str(uuid4())
    await activate(runtime, initial(document(heartbeat(config)).model_dump(mode="json"), change))
    await runtime.submit("snapshot", [])
    before = deepcopy(runtime.state.tables["service_state"])
    assert "notice:signal" in before
    calls = []
    original = notifications.plan_notices

    def record(*args, **kwargs):
        calls.append(args[2])
        return original(*args, **kwargs)

    monkeypatch.setattr(notifications, "plan_notices", record)
    await revision_after(runtime, changed(runtime, change), 30)
    # Draft creation commits at the old time; activation commits at the new time.
    # b3 intentionally plans an eligible notice at commit, never in revision evaluation.
    assert calls.count(runtime.clock.now_utc()) == 1
    jobs = [job for job in runtime.state.tables["service_job"].values() if job["kind"] == "notice"]
    assert len(jobs) == 1 and jobs[0]["operation"] == "problem_notice_put"
    assert (
        runtime.state.tables["service_state"]["notice:signal"]["seen"]
        == before["notice:signal"]["seen"]
    )


@pytest.mark.parametrize("change", ["interval", "unrelated"])
@pytest.mark.parametrize("adapter", ["scheduler", "connectivity"])
async def test_revision_internal_observations_are_snapshots_like_b3(
    runtime, config, change, adapter
):
    auxiliary = deepcopy(config)
    add_source(auxiliary, "independent")
    document = registry(heartbeat(config), definition())
    if adapter == "scheduler":
        data = definition()
        data["inputs"][0]["schema"] = schema("number")
        data["schema"]["fields"]["value"] = schema("number")
        document = registry(document, data)
        document["dependencies"][0]["kind"] = "clock"
        document["bindings"][0]["adapter"] = dict(
            kind="scheduler", calendar=dict(projection="minute_of_day")
        )
    else:
        data = definition()
        state_schema = schema("enum", value_catalog=["ready", "starting", "unavailable"])
        data["inputs"][0]["schema"] = state_schema
        data["schema"]["fields"]["value"] = state_schema
        document = registry(document, data)
        document["dependencies"][0]["kind"] = "connectivity"
        document["bindings"][0]["adapter"] = dict(kind="connectivity")
    document["bindings"][0].pop("transform", None)
    # An independent HA source supplies the unrelated-change fixture safely.
    await activate(runtime, initial(document, change))
    old = deepcopy(runtime.state.tables["source_observation_current"]["binding.a"])
    if adapter == "connectivity":
        # Status changes before this transaction, without a bridge event/tick.
        runtime.bridge, runtime.ha = "connected", "connected"
    next_document = storage_document(runtime.config)
    if change == "interval":
        next_document["sources"][0]["freshness_selection"]["rule"]["interval_s"] *= 2
    else:
        next_document["dependencies"].append(
            dict(dependency_id="dep.test.ha", kind="ha", monitor="internal")
        )
        source = auxiliary["sources"][-1]
        source["dependency_id"] = "dep.test.ha"
        next_document["sources"].append(source)
        next_document["bindings"].append(auxiliary["bindings"][-1])
    await revision_after(runtime, next_document, 60)
    current = runtime.state.tables["source_observation_current"]["binding.a"]
    assert current["value_raw"] != old["value_raw"]
    assert current["observation_kind"] == "snapshot"
    assert current["adapter"] == adapter


@pytest.mark.parametrize("change", ["interval", "unrelated"])
async def test_revision_keeps_unchanged_declarative_trace_like_b3(runtime, config, change):
    await activate(runtime, initial(registry(heartbeat(config), definition()), change))
    await runtime.submit("observation", observation(runtime, True))
    before = deepcopy(runtime.state.tables["node_state"]["fixture.echo"]["trace"])
    assert before["origin"] == "input"
    await revision_after(runtime, changed(runtime, change), 1)
    after = runtime.state.tables["node_state"]["fixture.echo"]["trace"]
    assert after["origin"] == "revision"
    assert after["registry_revision"] == runtime.state.active_revision
    assert {
        key: row for key, row in after.items() if key not in {"origin", "at", "registry_revision"}
    } == {
        key: row for key, row in before.items() if key not in {"origin", "at", "registry_revision"}
    }


@pytest.mark.parametrize("change", ["interval", "source"])
@pytest.mark.parametrize("running_grace", [False, True])
async def test_revision_opening_hint_neither_arms_nor_extends_grace(change, running_grace):
    from .test_beta4_freshness import legacy, running, shared
    from .test_beta_openings import field

    document = shared(legacy(), 8400)
    runtime = await running(document)
    try:
        if running_grace:
            runtime.clock.advance(8401)
            await runtime.submit("tick")
        previous = deepcopy(runtime.state.tables["node_state"]["test.opening0"]["temporal"])
        candidate = deepcopy(document)
        if change == "interval":
            candidate["freshness_templates"][0]["rule"]["interval_s"] = 8300
        else:
            source, binding = deepcopy(candidate["sources"][0]), deepcopy(candidate["bindings"][0])
            source.update(
                source_id="source.test.independent", physical_source_key="test.independent"
            )
            binding.update(binding_id="source.test.independent", source_id=source["source_id"])
            binding["adapter"]["mqtt_topic"] = "test/beta/independent"
            candidate["sources"].append(source)
            candidate["bindings"].append(binding)
        await revision_after(runtime, candidate, 1 if running_grace else 8401)
        after = runtime.state.tables["node_state"]["test.opening0"]["temporal"]
        assert after["grace_until"] == previous["grace_until"]
        if running_grace:
            assert field(runtime)["status"] == "held"
        else:
            assert field(runtime)["status"] == "unknown" and not after["grace_armed"]
            await runtime.submit("tick")
            assert field(runtime)["status"] == "unknown"
    finally:
        await runtime.stop()
