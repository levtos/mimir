"""Actual HA state engine + event helpers + our decorated Bridge callback.

Runs in the dedicated HA CI job. This is not a Supervisor installation test.
"""

import json
from pathlib import Path
from types import SimpleNamespace
from uuid import uuid4

import pytest

pytest.importorskip("homeassistant")
from homeassistant.components import websocket_api
from homeassistant.core import Context, HomeAssistant, SupportsResponse, callback

from custom_components.bifrost import async_setup_entry


@pytest.mark.ha
async def test_real_state_reported_callback_and_unsubscribe(tmp_path, monkeypatch):
    hass = HomeAssistant(str(tmp_path))
    commands = {}
    monkeypatch.setattr(
        websocket_api,
        "async_register_command",
        lambda hass, handler: commands.update({handler.__name__: handler}),
    )
    unload = []
    entry = SimpleNamespace(async_on_unload=unload.append)
    events = []
    connection = SimpleNamespace(
        user=SimpleNamespace(is_admin=True),
        subscriptions={},
        send_result=lambda *args: None,
        send_event=lambda identifier, event: events.append(event),
        send_error=lambda *args: events.append({"error": args[1]}),
    )
    await async_setup_entry(hass, entry)
    hass.states.async_set("sensor.fixture", "on")
    await hass.async_block_till_done()
    commands["subscribe"](
        hass, connection, {"id": 1, "protocol_version": 1, "entity_ids": ["sensor.fixture"]}
    )
    # The state engine itself emits state_reported with its real event.data.
    hass.states.async_set("sensor.fixture", "on")
    await hass.async_block_till_done()
    reports = [event for event in events if event.get("kind") == "reported"]
    assert len(reports) == 1
    assert (
        reports[0]["last_reported"] == hass.states.get("sensor.fixture").last_reported.isoformat()
    )
    for number in range(2, 102):
        commands["subscribe"](
            hass,
            connection,
            {
                "id": number,
                "protocol_version": 1,
                "entity_ids": ["sensor.fixture"],
                "report_entity_ids": [],
            },
        )
        connection.subscriptions.pop(number)()
    assert len(unload) == 1
    assert len(hass.data["bifrost"]) == 1
    connection.subscriptions.pop(1)()
    count = len(events)
    hass.states.async_set("sensor.fixture", "on")
    await hass.async_block_till_done()
    assert len(events) == count
    unload[0]()
    commands["subscribe"](hass, connection, {"id": 103, "protocol_version": 1, "entity_ids": []})
    assert events[-1]["error"] == "bridge_unloaded"


@pytest.mark.ha
async def test_v2_negotiation_manifest_admin_services_and_context(tmp_path, monkeypatch):
    hass = HomeAssistant(str(tmp_path))
    commands, results, errors, events, calls = {}, {}, [], [], []
    monkeypatch.setattr(
        websocket_api,
        "async_register_command",
        lambda hass, handler: commands.update({handler.__name__: handler}),
    )
    unload = []
    await async_setup_entry(hass, SimpleNamespace(async_on_unload=unload.append))
    connection = SimpleNamespace(
        user=SimpleNamespace(is_admin=True),
        subscriptions={},
        send_result=lambda identifier, result=None: results.update({identifier: result}),
        send_error=lambda *args: errors.append(args),
        send_event=lambda identifier, event: events.append(event),
    )
    commands["info"](hass, connection, {"id": 1})
    manifest = json.loads(
        (Path(__file__).parents[1] / "custom_components/bifrost/manifest.json").read_text()
    )
    assert results[1]["bridge_version"] == manifest["version"]
    assert results[1]["protocol_version"] == 1
    msg = {
        "id": 2,
        "protocol_version": 2,
        "request_id": str(uuid4()),
        "operation": "calendar_events",
        "target_ids": ["calendar.example"],
        "arguments": {"start": "2026-10-17T00:00:00Z", "end": "2026-10-18T00:00:00Z"},
    }
    commands["service_call"](hass, connection, msg)
    await hass.async_block_till_done()
    assert errors[-1][1] == "unsupported_protocol"
    commands["negotiate"](hass, connection, {"id": 3, "supported_versions": [1, 2]})
    assert results[3]["protocol_selected"] == 2
    assert results[3]["bridge_version"] == manifest["version"]

    async def calendar(call):
        calls.append(call)
        return {"calendar.example": {"events": []}}

    hass.services.async_register(
        "calendar", "get_events", calendar, supports_response=SupportsResponse.ONLY
    )
    commands["service_call"](hass, connection, {**msg, "id": 4})
    await hass.async_block_till_done()
    assert results[4]["outcome"] == "completed"
    assert calls[0].data["entity_id"] == "calendar.example"
    assert len(calls) == 1
    commands["service_call"](hass, connection, {**msg, "id": 5})
    await hass.async_block_till_done()
    assert results[5] == results[4] and len(calls) == 1
    commands["negotiate"](hass, connection, {"id": 6, "supported_versions": [1]})
    commands["service_call"](hass, connection, {**msg, "id": 7})
    await hass.async_block_till_done()
    assert errors[-1][1] == "unsupported_protocol"
    connection.user.is_admin = False
    commands["negotiate"](hass, connection, {"id": 8, "supported_versions": [2]})
    assert errors[-1][1] == "unauthorized"
    connection.user.is_admin = True
    commands["negotiate"](hass, connection, {"id": 9, "supported_versions": [2]})
    commands["subscribe"](
        hass, connection, {"id": 10, "protocol_version": 2, "entity_ids": ["sensor.fixture"]}
    )
    context = Context(user_id="fixture-user", parent_id="fixture-parent")
    hass.states.async_set("sensor.fixture", "on", context=context)
    await hass.async_block_till_done()
    assert (
        next(event for event in events if event.get("kind") == "changed")["context"]
        == context.as_dict()
    )
    hass.states.async_set("sensor.fixture", "on", context=context)
    await hass.async_block_till_done()
    assert (
        next(event for event in events if event.get("kind") == "reported")["context"]
        == context.as_dict()
    )
    unload[0]()


@pytest.mark.ha
async def test_refresh_rejects_push_entities_and_accepts_actual_polling(tmp_path, monkeypatch):
    from homeassistant.helpers.entity_component import DATA_INSTANCES

    hass = HomeAssistant(str(tmp_path))
    commands, results, calls = {}, {}, []
    monkeypatch.setattr(
        websocket_api,
        "async_register_command",
        lambda hass, handler: commands.update({handler.__name__: handler}),
    )
    await async_setup_entry(hass, SimpleNamespace(async_on_unload=lambda callback: None))
    connection = SimpleNamespace(
        user=SimpleNamespace(is_admin=True),
        subscriptions={},
        send_result=lambda identifier, result=None: results.update({identifier: result}),
        send_error=lambda *args: pytest.fail(str(args)),
    )
    commands["negotiate"](hass, connection, {"id": 1, "supported_versions": [2]})
    entity = SimpleNamespace(should_poll=False)
    hass.data[DATA_INSTANCES] = {"sensor": SimpleNamespace(get_entity=lambda identifier: entity)}

    @callback
    def update(call):
        calls.append(call.data)

    hass.services.async_register("homeassistant", "update_entity", update)
    msg = {
        "id": 2,
        "protocol_version": 2,
        "request_id": str(uuid4()),
        "operation": "source_refresh",
        "target_ids": ["sensor.example"],
        "arguments": {"profile": "entity_poll"},
    }
    commands["service_call"](hass, connection, msg)
    await hass.async_block_till_done()
    assert results[2]["outcome"] == "rejected" and calls == []
    entity.should_poll = True
    commands["service_call"](hass, connection, {**msg, "id": 3, "request_id": str(uuid4())})
    await hass.async_block_till_done()
    assert results[3]["outcome"] == "completed" and calls == [{"entity_id": "sensor.example"}]
