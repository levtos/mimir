"""Two independent problem axes; only desired summaries enter the persisted outbox."""

from datetime import datetime, timedelta
from typing import Any
from uuid import uuid4

from pydantic import Field

from .model import Model, checksum
from .persistence import State


class NoticeAxis(Model):
    enabled: bool = False
    debounce_s: int = Field(default=30, ge=0, le=86400)
    clear_after_s: int = Field(default=10, ge=0, le=86400)
    min_update_s: int = Field(default=300, ge=0, le=86400)


class Notifications(Model):
    signal: NoticeAxis = NoticeAxis(enabled=True)
    configuration: NoticeAxis = NoticeAxis(debounce_s=60)
    max_items: int = Field(default=10, ge=1, le=10)


def problems(state: State, axis: str) -> dict[str, dict[str, Any]]:
    found = {}
    for key, envelope in state.tables["contract_state_current"].items():
        for name, field in envelope["fields"].items():
            signal = field["status"] in {"unknown", "unresolved"}
            incomplete = not field.get("configuration", {}).get("complete", True)
            if axis == "signal" and signal or axis == "configuration" and incomplete:
                found[f"{key}:{name}"] = {
                    "contract_id": key,
                    "field": name,
                    "causes": sorted({item["code"] for item in field.get("reasons", [])})
                    if axis == "signal"
                    else sorted(hint["code"] for hint in field["configuration"].get("hints", [])),
                }
    return found


def plan_notices(
    state: State,
    config: Any,
    now: datetime,
    installation_id: str | None,
    ingress_slug: str | None = None,
) -> None:
    if installation_id is None:
        return
    if config.notifications is None and not any(
        key.startswith("notice:") for key in state.tables["service_state"]
    ):
        return
    from .user_text import user_text

    rows, jobs = state.tables["service_state"], state.tables["service_job"]
    for axis in ("signal", "configuration"):
        identity = f"notice:{axis}"
        policy = getattr(config.notifications, axis) if config.notifications else NoticeAxis()
        row = rows.setdefault(identity, {"seen": {}, "acknowledged": "", "desired": ""})
        row["eligible_epoch"] = state.epoch_id
        current = problems(state, axis) if policy.enabled else {}
        row["seen"] = {key: row["seen"].get(key, now.isoformat()) for key in current}
        eligible = {
            key: item
            for key, item in current.items()
            if now
            >= datetime.fromisoformat(row["seen"][key]) + timedelta(seconds=policy.debounce_s)
        }
        digest = checksum(eligible) if eligible else ""
        if digest != row["desired"]:
            row.update(desired=digest, desired_since=now.isoformat())
            previous = jobs.get(row.get("job_id", ""), {})
            if previous.get("status") == "planned":
                previous["status"] = "cancelled"
        row["deadlines"] = [
            (datetime.fromisoformat(since) + timedelta(seconds=policy.debounce_s)).isoformat()
            for since in row["seen"].values()
        ]
        existing = jobs.get(row.get("job_id", ""), {})
        if existing.get("status") == "sent":
            continue
        if digest == row["acknowledged"]:
            continue
        due = datetime.fromisoformat(row["desired_since"]) + timedelta(
            seconds=0 if digest else policy.clear_after_s
        )
        if digest and row.get("last_sent_at"):
            due = max(
                due,
                datetime.fromisoformat(row["last_sent_at"])
                + timedelta(seconds=policy.min_update_s),
            )
        if row.get("retry_at"):
            due = max(due, datetime.fromisoformat(row["retry_at"]))
        row["next_at"] = due.isoformat()
        if now < due or existing.get("status") == "planned":
            continue
        names = {
            item.contract_id: item.display_name or item.contract_id for item in config.contracts
        }
        lines = []
        if digest:
            maximum = config.notifications.max_items if config.notifications else 10
            for item in list(
                sorted(eligible.values(), key=lambda item: (item["contract_id"], item["field"]))
            )[:maximum]:
                causes = [
                    user_text(
                        f"codes.{code}",
                        fallback="codes.input_unknown"
                        if axis == "signal"
                        else "alpha9.notifications.configTitle",
                    )
                    for code in item["causes"][:2]
                ]
                lines.append(
                    f"- {names.get(item['contract_id'], item['contract_id'])[:128]}: {', '.join(causes)}"
                )
        title_key = "signalTitle" if axis == "signal" else "configTitle"
        summary_key = "signalSummary" if axis == "signal" else "configSummary"
        arguments = (
            {
                "title": user_text(f"alpha9.notifications.{title_key}"),
                "message": user_text(f"alpha9.notifications.{summary_key}", count=len(eligible))
                + "\n\n"
                + "\n".join(lines)
                + (
                    f"\n\n[Mimir](/hassio/ingress/{ingress_slug}/#/?axis={axis})"
                    if ingress_slug
                    else ""
                ),
            }
            if digest
            else {}
        )
        identifier = str(uuid4())
        jobs[identifier] = {
            "job_id": identifier,
            "request_id": identifier,
            "kind": "notice",
            "state_key": identity,
            "digest": digest,
            "revision": state.active_revision,
            "operation": "problem_notice_put" if digest else "problem_notice_remove",
            "target_ids": [f"mimir_{installation_id}_{axis}"],
            "arguments": arguments,
            "status": "planned",
            "created_at": now.isoformat(),
        }
        row["job_id"] = identifier


def complete_notice(
    state: State, job: dict[str, Any], response: dict[str, Any], now: datetime
) -> None:
    row = state.tables["service_state"].get(job["state_key"])
    if not row or row.get("job_id") != job["job_id"]:
        return
    if response.get("outcome") == "completed":
        row.update(acknowledged=job["digest"], last_sent_at=now.isoformat())
        row.pop("retry_at", None)
    else:
        row["retry_at"] = (now + timedelta(seconds=30)).isoformat()
