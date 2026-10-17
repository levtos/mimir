"""Read-only calendar windows and deterministic, bounded response normalization."""

from collections import Counter
from datetime import UTC, date, datetime, time, timedelta
from typing import Any, Literal, Self
from zoneinfo import ZoneInfo

from pydantic import Field, model_validator

from .model import Model, canonical, checksum, utc


class CalendarWindow(Model):
    timezone: Literal["Europe/Berlin"] = "Europe/Berlin"
    past_days: int = Field(default=1, ge=0, le=30)
    future_days: int = Field(default=14, ge=1, le=31)

    @model_validator(mode="after")
    def bounded(self) -> Self:
        if self.past_days + self.future_days > 31:
            raise ValueError("calendar_window_too_large")
        return self

    def bounds(self, now: datetime) -> tuple[datetime, datetime]:
        zone = ZoneInfo(self.timezone)
        today = now.astimezone(zone).date()
        return (
            datetime.combine(today - timedelta(days=self.past_days), time(), zone),
            datetime.combine(today + timedelta(days=self.future_days), time(), zone),
        )


def normalize_events(
    response: Any, entity: str, start: datetime, end: datetime, timezone: str
) -> list[dict[str, Any]]:
    """A missing calendar is an error. Preserve multiplicity when HA has no UID."""
    if not isinstance(response, dict) or entity not in response:
        raise ValueError("calendar_response_missing")
    data = response[entity]
    events = data.get("events") if isinstance(data, dict) else None
    if (
        not isinstance(events, list)
        or len(events) > 1000
        or len(canonical(response).encode()) > 1048576
    ):
        raise ValueError("calendar_response_limit")
    zone = ZoneInfo(timezone)
    result: list[dict[str, Any]] = []
    counts: Counter[str] = Counter()
    for event in events:
        if not isinstance(event, dict):
            raise ValueError("calendar_event_invalid")

        def stamp(key: str) -> tuple[datetime, bool]:
            value = event.get(key)
            if not isinstance(value, str):
                raise ValueError("calendar_event_invalid")
            if len(value) == 10:
                return datetime.combine(date.fromisoformat(value), time(), zone), True
            return utc(datetime.fromisoformat(value)), False

        event_start, all_day = stamp("start")
        event_end, all_day_end = stamp("end")
        if all_day != all_day_end or event_end.astimezone(UTC) <= event_start.astimezone(UTC):
            raise ValueError("calendar_event_invalid")
        if event_start.astimezone(UTC) >= end.astimezone(UTC) or event_end.astimezone(
            UTC
        ) <= start.astimezone(UTC):
            continue
        summary, location = event.get("summary", ""), event.get("location") or ""
        if (
            not isinstance(summary, str)
            or not isinstance(location, str)
            or max(len(summary), len(location)) > 4096
        ):
            raise ValueError("calendar_event_invalid")
        row: dict[str, Any] = {
            "summary": summary,
            "start": event_start.astimezone(UTC).isoformat(),
            "end": event_end.astimezone(UTC).isoformat(),
            "all_day": all_day,
            "location": location,
        }
        identity = checksum({"uid": event.get("uid"), **row})
        counts[identity] += 1
        result.append({"key": f"{identity}:{counts[identity]}", **row})
    return sorted(result, key=lambda row: (row["start"], row["end"], row["key"]))
