"""HA rejects reused IDs; test real client traffic against the strict fixture."""

import asyncio
import logging

import aiohttp
import pytest

from core_contracts.adapters.ha import BridgeAdapter, request_error
from dev.fake_ha import FakeHA

from .conftest import activate
from .test_beta_openings import with_connectivity


async def until(predicate):
    async with asyncio.timeout(5):
        while not predicate():
            await asyncio.sleep(0)  # noqa: TID251


def field(runtime, contract="fixture.echo"):
    return runtime.snapshot()["contracts"][contract]["fields"]["value"]


def assert_increasing(fake):
    for requests in fake.connections:
        ids = [request["id"] for request in requests]
        assert ids == list(range(1, len(ids) + 1))


@pytest.mark.parametrize("linked", [False, True])
async def test_connected_snapshot_readiness_protocol_version_and_service_id(
    runtime, config, aiohttp_server, linked
):
    if not linked:
        config["sources"] = []
        config["bindings"] = []
        config["contracts"] = []
    data = with_connectivity(config)
    data["fingerprint_version"] = 2
    data["contracts"][-1]["contract_id"] = "connectivity.home_assistant"
    await activate(runtime, data)
    assert "first_bridge_snapshot_pending" in runtime.readiness_reasons
    now = runtime.clock.now_utc().isoformat()
    fake = FakeHA(
        {
            "sensor.example_1": {
                "state": True,
                "attributes": {},
                "last_updated": now,
                "last_changed": now,
                "last_reported": now,
            }
        },
        v2=True,
    )
    server = await aiohttp_server(fake.application())
    async with aiohttp.ClientSession() as session:
        adapter = BridgeAdapter(runtime, session, str(server.make_url("/websocket")), "synthetic")
        task = asyncio.create_task(adapter.connect(runtime.config))
        try:
            await until(lambda: runtime.first_snapshot and adapter.socket is not None)
            assert runtime.bridge == "connected"
            assert field(runtime, "connectivity.home_assistant")["value"] == "ready"
            assert "first_bridge_snapshot_pending" not in runtime.readiness_reasons
            assert runtime.ready and runtime.service_state()["ready"]
            assert runtime.bridge_protocol_selected == 2
            assert runtime.bridge_version == "test"
            if linked:
                assert field(runtime)["value"] is True, field(runtime)
            previous = max(request["id"] for request in fake.requests)
            replies = await asyncio.gather(
                *(
                    adapter.service_call("calendar_events", ["calendar.example"], {})
                    for _ in range(3)
                )
            )
            assert all(reply["outcome"] == "completed" for reply in replies)
            assert all(request["id"] > previous for request in fake.requests[-3:])
            assert_increasing(fake)
        finally:
            runtime.resubscribe.set()
            await task


async def test_stop_disconnect_reconnect_resets_ids_and_snapshot_does_not_revive_stale_sensor(
    runtime, config, aiohttp_server
):
    config["fingerprint_version"] = 2
    config["sources"][0]["freshness"] = {
        "mode": "report_heartbeat",
        "interval_s": 10,
        "future_tolerance_s": 0,
    }
    await activate(runtime, with_connectivity(config))
    original = runtime.clock.now_utc().isoformat()
    state = {"state": True, "attributes": {}, "last_reported": original, "last_updated": original}
    fake = FakeHA({"sensor.example_1": state}, v2=True)
    retry_wait = asyncio.Event()
    original_sleep = runtime.clock.sleep

    async def observed_sleep(seconds):
        retry_wait.set()
        await original_sleep(seconds)

    runtime.clock.sleep = observed_sleep
    server = await aiohttp_server(fake.application())
    async with aiohttp.ClientSession() as session:
        adapter = BridgeAdapter(runtime, session, str(server.make_url("/websocket")), "synthetic")
        task = asyncio.create_task(adapter.run())
        try:
            await until(lambda: runtime.first_snapshot and adapter.socket is not None)
            assert field(runtime)["status"] == "valid"
            await fake.lifecycle("homeassistant_stop")
            await until(lambda: runtime.ha == "stopping")
            assert field(runtime, "test.connectivity")["value"] == "starting"
            runtime.clock.advance(11)
            await runtime.submit("tick")
            assert field(runtime)["status"] == "unknown"
            await fake.disconnect()
            await until(lambda: runtime.ha == "disconnected" and adapter.socket is None)
            await asyncio.wait_for(retry_wait.wait(), timeout=5)
            runtime.clock.advance(2)
            await until(lambda: len(fake.connections) == 2 and adapter.socket is not None)
            await runtime.queue.join()
            assert sum(r["type"] == "traber/subscribe" for r in fake.requests) == 2
            assert field(runtime, "test.connectivity")["value"] == "ready"
            assert field(runtime)["status"] == "unknown"
            assert "input_stale" in {r["code"] for r in field(runtime)["reasons"]}
            observation = runtime.state.tables["source_observation_current"]["binding.a"]
            assert observation["ha_last_reported"] == original.replace("+00:00", "Z")
            assert_increasing(fake)
        finally:
            task.cancel()
            await asyncio.gather(task, return_exceptions=True)


@pytest.mark.parametrize("registry_error", [None, "unknown_command", "unauthorized"])
async def test_discovery_preview_and_metadata_use_connection_local_ids(
    runtime, aiohttp_server, registry_error
):
    fake = FakeHA(
        {f"sensor.test_{i}": {"state": "1", "attributes": {}} for i in range(401)},
        registries={
            f"config/{kind}_registry/list": registry_error or []
            for kind in ("area", "device", "entity")
        },
        v2=True,
    )
    server = await aiohttp_server(fake.application())
    async with aiohttp.ClientSession() as session:
        adapter = BridgeAdapter(runtime, session, str(server.make_url("/websocket")), "synthetic")
        assert len(await adapter.discover(preview=True)) == 401
        assert len(await adapter.discover()) == 401
    assert len(fake.connections) == 2
    assert [r["type"] for r in fake.connections[0]].count("traber/source_metadata") == 3
    assert_increasing(fake)


@pytest.mark.parametrize("bad_id", [1, 2])
async def test_fake_ha_rejects_nonincreasing_id(aiohttp_server, bad_id):
    fake = FakeHA()
    server = await aiohttp_server(fake.application())
    async with aiohttp.ClientSession() as session:
        async with session.ws_connect(server.make_url("/websocket")) as socket:
            await socket.receive_json()
            await socket.send_json({"type": "auth", "access_token": "synthetic"})
            await socket.receive_json()
            for number, success in [(2, True), (bad_id, False), (3, True)]:
                await socket.send_json({"id": number, "type": "get_config"})
                response = await socket.receive_json()
                assert response["success"] is success
                if not success:
                    assert response["error"]["code"] == "id_reuse"


async def test_request_failure_logs_only_type_and_code(runtime, config, aiohttp_server, caplog):
    fake = FakeHA()
    server = await aiohttp_server(fake.application())
    await activate(runtime, config)
    async with aiohttp.ClientSession() as session:
        adapter = BridgeAdapter(runtime, session, str(server.make_url("/websocket")), "synthetic")
        original_result = adapter._result

        async def reused_result(connection, request):
            if request["type"] == "get_config":
                connection.number = 0
            return await original_result(connection, request)

        adapter._result = reused_result
        with caplog.at_level(logging.WARNING):
            task = asyncio.create_task(adapter.run())
            try:
                await until(lambda: any(r.msg == "bridge_disconnected" for r in caplog.records))
            finally:
                task.cancel()
                await asyncio.gather(task, return_exceptions=True)
    records = [
        r for r in caplog.records if r.msg in {"bridge_request_failed", "bridge_disconnected"}
    ]
    assert {r.msg for r in records} == {"bridge_request_failed", "bridge_disconnected"}
    assert all(r.request_type == "get_config" and r.ha_error_code == "id_reuse" for r in records)
    assert "synthetic" not in caplog.text


def test_arbitrary_remote_error_data_is_not_logged(caplog):
    with caplog.at_level(logging.WARNING):
        error = request_error(
            "get_config", {"error": {"code": "private-value", "message": "private-payload"}}
        )
    assert error.ha_error_code == "unknown_error"
    assert "private" not in caplog.text
    assert "private" not in str(vars(caplog.records[-1]))
