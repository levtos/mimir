"""Bounded requests for new evidence. A service acknowledgement is never evidence."""

from datetime import UTC, datetime, timedelta
from typing import TYPE_CHECKING, Any, Literal, Self
from uuid import uuid4

from pydantic import Field, model_validator

from .model import Model, checksum
from .persistence import State

if TYPE_CHECKING:
    from .registry import RegistryConfig


class RefreshCapability(Model):
    profile: Literal["entity_poll", "companion_location"]
    permission_confirmed: bool = False

    @model_validator(mode="after")
    def permission(self) -> Self:
        if self.profile == "companion_location" and not self.permission_confirmed:
            raise ValueError("location_permission_required")
        return self


class StopWhen(Model):
    ref: str = Field(min_length=1, max_length=256)
    field: str | None = Field(default=None, max_length=128)

    def reference(self) -> str:
        return self.ref + ("." + self.field if self.field else "")


class RefreshPlan(Model):
    trigger_ref: str = Field(min_length=1, max_length=256)
    targets: tuple[str, ...] = Field(min_length=1, max_length=20)
    attempt_offsets_s: tuple[int, ...] = Field(min_length=1, max_length=5)
    window_s: int = Field(gt=0, le=300)
    cooldown_s: int = Field(gt=0, le=86400)
    stop_when: StopWhen | None = None

    @model_validator(mode="after")
    def bounded(self) -> Self:
        offsets = self.attempt_offsets_s
        if (
            tuple(sorted(set(offsets))) != offsets
            or offsets[0] != 0
            or offsets[-1] >= self.window_s
            or self.cooldown_s < self.window_s
            or len(set(self.targets)) != len(self.targets)
        ):
            raise ValueError("invalid_refresh_plan")
        return self


def _field(state: State, config: RegistryConfig, ref: str) -> dict[str, Any] | None:
    from .registry import resolve_ref

    try:
        key, field = resolve_ref(ref, config)
    except ValueError:
        return None
    value = state.tables["contract_state_current"].get(key, {}).get("fields", {}).get(field)
    return value if isinstance(value, dict) else None


def _boolean(field: dict[str, Any] | None) -> bool | None:
    if (
        field
        and field["status"] == "valid"
        and field["quality"] == "healthy"
        and type(field["value"]) is bool
    ):
        return field["value"] is True
    return None


def _quota(state: State, profile: str, entity: str, now: datetime) -> bool:
    # Conservative ceilings also cover other plans sharing a source/device profile.
    key = f"refresh_quota:{profile}:" + (entity if profile == "entity_poll" else "all")
    row = state.tables["service_state"].setdefault(
        key, {"times": [], "day": now.astimezone(UTC).date().isoformat(), "daily_count": 0}
    )
    day = now.astimezone(UTC).date().isoformat()
    if day > row["day"]:
        row.update(day=day, daily_count=0)
    times = [
        datetime.fromisoformat(at)
        for at in row["times"]
        if datetime.fromisoformat(at) + timedelta(seconds=300) > now
    ]
    minimum, maximum, daily = (10, 5, 10000) if profile == "entity_poll" else (60, 3, 50)
    if (
        times
        and (now - times[-1]).total_seconds() < minimum
        or len(times) >= maximum
        or row["daily_count"] >= daily
    ):
        return False
    row["times"] = [at.isoformat() for at in times] + [now.isoformat()]
    row["daily_count"] += 1
    return True


def plan_refreshes(
    state: State,
    config: RegistryConfig,
    now: datetime,
    origin: str,
    connected: bool,
    fingerprints: dict[str, str],
) -> None:
    rows, jobs = state.tables["service_state"], state.tables["service_job"]
    bindings = {binding.source_id: binding for binding in config.bindings}
    active = set()
    for contract in config.contracts:
        plan = contract.refresh_plan
        if plan is None or not contract.enabled:
            continue
        key = f"refresh:{contract.contract_id}"
        active.add(key)
        signature = checksum(
            {
                "plan": plan.model_dump(mode="json"),
                "owner": fingerprints[contract.contract_id],
                "targets": {target: fingerprints[target] for target in plan.targets},
            }
        )
        trigger = _field(state, config, plan.trigger_ref)
        high = _boolean(trigger)
        row = rows.get(key, {})
        if row.get("fingerprint") != signature:
            row = rows[key] = {
                "fingerprint": signature,
                "previous_high": high,
                "cooldown_until": row.get("cooldown_until"),
                "run": None,
            }
        before = row["previous_high"]
        row["previous_high"] = high
        if origin not in {"input", "timer"}:
            # A snapshot/restart/activation establishes a baseline, never a missed trigger.
            if origin == "restore":
                row["restored_at"] = now.isoformat()
        run = row.get("run")
        running = bool(run and run["status"] == "running")
        if (
            not running
            and origin in {"input", "timer"}
            and high is True
            and before is False
            and trigger
            and trigger.get("evidence")
            and (
                not row.get("cooldown_until")
                or datetime.fromisoformat(row["cooldown_until"]) <= now
            )
        ):
            run = row["run"] = {
                "run_id": str(uuid4()),
                "revision": state.active_revision,
                "started_at": now.isoformat(),
                "trigger_evidence": trigger["evidence"],
                "end_at": (now + timedelta(seconds=plan.window_s)).isoformat(),
                "consumed": [],
                "status": "running",
                "received": [],
                "attempts": [],
            }
            row["cooldown_until"] = (now + timedelta(seconds=plan.cooldown_s)).isoformat()
            running = True
        if not running or run is None:
            row.pop("next_at", None)
            continue
        if (
            now >= datetime.fromisoformat(run["end_at"])
            or plan.stop_when
            and _boolean(_field(state, config, plan.stop_when.reference())) is True
        ):
            run["status"] = "stopped"
            row.pop("next_at", None)
            continue
        for target in plan.targets:
            observation = state.tables["source_observation_current"].get(
                bindings[target].binding_id, {}
            )
            stamp = (
                observation.get("device_time")
                or observation.get("ha_last_reported")
                or observation.get("ha_time_fired")
            )
            if (
                stamp
                and datetime.fromisoformat(stamp) > datetime.fromisoformat(run["started_at"])
                and observation.get("observation_kind") in {"report", "live_change"}
                and target not in run["received"]
            ):
                run["received"].append(target)
        for number, offset in enumerate(plan.attempt_offsets_s):
            if number in run["consumed"]:
                continue
            due = datetime.fromisoformat(run["started_at"]) + timedelta(seconds=offset)
            if due > now:
                continue
            run["consumed"].append(number)
            missed = (
                origin in {"restore", "revision", "snapshot"}
                or row.get("restored_at")
                and due <= datetime.fromisoformat(row["restored_at"])
            )
            for target in plan.targets:
                if target in run["received"] or target in run.get("blocked", []):
                    continue
                binding = bindings[target]
                capability = binding.refresh
                assert capability and binding.adapter.ha_entity_id
                reason = (
                    "missed"
                    if missed
                    else "ha_unavailable"
                    if not connected
                    else "pending"
                    if any(
                        job["kind"] == "refresh"
                        and job.get("source_id") == target
                        and job["status"] in {"planned", "sent"}
                        for job in jobs.values()
                    )
                    else None
                )
                if reason is None and not _quota(
                    state, capability.profile, binding.adapter.ha_entity_id, now
                ):
                    reason = "quota"
                run["attempts"].append(
                    {
                        "number": number,
                        "source_id": target,
                        "at": now.isoformat(),
                        "outcome": reason or "planned",
                    }
                )
                if reason:
                    continue
                identifier = str(uuid4())
                jobs[identifier] = {
                    "job_id": identifier,
                    "request_id": identifier,
                    "kind": "refresh",
                    "state_key": key,
                    "run_id": run["run_id"],
                    "fingerprint": signature,
                    "number": number,
                    "source_id": target,
                    "revision": state.active_revision,
                    "operation": "source_refresh",
                    "target_ids": [binding.adapter.ha_entity_id],
                    "arguments": {
                        "profile": capability.profile,
                        **(
                            {"permission_confirmed": True}
                            if capability.profile == "companion_location"
                            else {}
                        ),
                    },
                    "status": "planned",
                    "created_at": now.isoformat(),
                }
        future = [
            datetime.fromisoformat(run["started_at"]) + timedelta(seconds=offset)
            for number, offset in enumerate(plan.attempt_offsets_s)
            if number not in run["consumed"]
        ]
        row["next_at"] = min([datetime.fromisoformat(run["end_at"]), *future]).isoformat()
    for key, row in rows.items():
        if key.startswith("refresh:") and key not in active:
            if row.get("run"):
                row["run"]["status"] = "cancelled"
            row.pop("next_at", None)
    for job in jobs.values():
        if job["kind"] != "refresh" or job["status"] not in {"planned", "sent"}:
            continue
        row = rows.get(job["state_key"], {})
        if (
            row.get("fingerprint") != job["fingerprint"]
            or (row.get("run") or {}).get("status") != "running"
        ):
            job["status"] = "cancelled"


def complete_refresh(state: State, job: dict[str, Any], response: dict[str, Any]) -> None:
    row = state.tables["service_state"].get(job["state_key"], {})
    run = row.get("run")
    if not run or run["run_id"] != job["run_id"]:
        return
    for attempt in run["attempts"]:
        if attempt["number"] == job["number"] and attempt["source_id"] == job["source_id"]:
            attempt["outcome"] = response.get("outcome", "indeterminate")
    if response.get("outcome") in {"rejected", "failed"}:
        blocked = run.setdefault("blocked", [])
        if job["source_id"] not in blocked:
            blocked.append(job["source_id"])


def prepare_legacy_refresh(
    state: State, config: RegistryConfig, source_id: str, now: datetime
) -> dict[str, Any] | None:
    """Existing code-declared refreshes share the same persisted quota/transport boundary."""
    binding = next((binding for binding in config.bindings if binding.source_id == source_id), None)
    if (
        binding is None
        or binding.adapter.kind not in {"ha_state", "ha_attribute"}
        or not binding.adapter.ha_entity_id
    ):
        raise ValueError("refresh_not_supported")
    profile = binding.refresh.profile if binding.refresh else "entity_poll"
    if not _quota(state, profile, binding.adapter.ha_entity_id, now):
        return None
    identifier = str(uuid4())
    job = {
        "job_id": identifier,
        "request_id": identifier,
        "kind": "legacy_refresh",
        "state_key": f"legacy_refresh:{source_id}",
        "revision": state.active_revision,
        "operation": "source_refresh",
        "target_ids": [binding.adapter.ha_entity_id],
        "arguments": {
            "profile": profile,
            **(
                {"permission_confirmed": True}
                if binding.refresh and binding.refresh.permission_confirmed
                else {}
            ),
        },
        "status": "sent",
        "created_at": now.isoformat(),
        "sent_at": now.isoformat(),
    }
    state.tables["service_job"][identifier] = job
    return job
