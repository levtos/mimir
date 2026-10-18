"""Opt-in numeric plausibility; fresh repeated reports are distinct from new values."""

from datetime import datetime, timedelta
from typing import Annotated, Any, Self

from pydantic import Field, model_validator

from .declarative_models import ParameterDefinition, ParameterRule
from .model import Model
from .quality import FieldValue, Reason, ReasonCode

Number = Annotated[float, Field(strict=True)] | ParameterRule


class Reference(Model):
    ref: str = Field(pattern=r"^source\.[a-zA-Z0-9_.-]+$", max_length=128)
    min_delta: Number


class Stuck(Model):
    unchanged_for_s: Number
    tolerance: Number
    min_reports: Number
    recovery_reports: Number = 2
    reference: Reference | None = None


class SensorProfile(Model):
    id: str = Field(pattern=r"^[a-zA-Z][a-zA-Z0-9_.-]{0,127}$")
    version: int = Field(ge=1)
    display_name: str = Field(default="", max_length=128)
    stuck: Stuck
    parameter_schema: dict[str, ParameterDefinition] = Field(
        default_factory=dict, max_length=16, exclude_if=lambda value: not value
    )

    @model_validator(mode="after")
    def slots(self) -> Self:
        slots = [
            self.stuck.unchanged_for_s,
            self.stuck.tolerance,
            self.stuck.min_reports,
            self.stuck.recovery_reports,
        ]
        if self.stuck.reference:
            slots.append(self.stuck.reference.min_delta)
        if any(
            isinstance(slot, ParameterRule) and slot.name not in self.parameter_schema
            for slot in slots
        ) or any(
            item.field_schema.type != "number" or not item.field_schema.required
            for item in self.parameter_schema.values()
        ):
            raise ValueError("invalid_sensor_parameter")
        if not self.parameter_schema:
            self.resolve({})
        return self

    def resolve(self, parameters: dict[str, float]) -> dict[str, float]:
        if parameters.keys() != self.parameter_schema.keys():
            raise ValueError("sensor_parameters_required")
        for name, value in parameters.items():
            declaration = self.parameter_schema[name]
            if (
                type(value) not in {int, float}
                or declaration.minimum is not None
                and value < declaration.minimum
                or declaration.maximum is not None
                and value > declaration.maximum
            ):
                raise ValueError("sensor_parameter_bounds")

        def number(value: Number) -> float:
            return float(parameters[value.name] if isinstance(value, ParameterRule) else value)

        result = {
            name: number(getattr(self.stuck, name))
            for name in ("unchanged_for_s", "tolerance", "min_reports", "recovery_reports")
        }
        if (
            not 0 < result["unchanged_for_s"] <= 31536000
            or result["tolerance"] < 0
            or not 2 <= result["min_reports"] <= 10000
            or not result["min_reports"].is_integer()
            or not 1 <= result["recovery_reports"] <= 100
            or not result["recovery_reports"].is_integer()
        ):
            raise ValueError("invalid_sensor_thresholds")
        if self.stuck.reference:
            result["min_delta"] = number(self.stuck.reference.min_delta)
            if result["min_delta"] <= 0:
                raise ValueError("invalid_sensor_reference_delta")
        return result


def assess_sensor(
    value: FieldValue,
    observation: Any,
    source: Any,
    reference: FieldValue | None,
    rows: dict[str, dict[str, Any]],
    fingerprint: str,
    now: datetime,
    *,
    new_report: bool,
) -> FieldValue:
    profile = source.sensor_profile
    if profile is None:
        return value
    settings = profile.resolve(source.sensor_parameters)
    key = f"sensor:{source.source_id}"
    if (
        not value.usable(now)
        or type(value.value) not in {int, float}
        or profile.stuck.reference
        and (reference is None or not reference.usable(now) or reference.quality != "healthy")
    ):
        rows.pop(key, None)
        return value.model_copy(update={"plausibility": "unchecked"})
    row = rows.get(key)
    if row is None or row["fingerprint"] != fingerprint:
        row = rows[key] = {
            "fingerprint": fingerprint,
            "plausibility": "unchecked",
            "report_count": 0,
            "profile_version": profile.version,
            "recovery_count": 0,
            "evidence": [],
        }
    stamp = value.measured_at
    genuinely_new = (
        new_report
        and observation
        and observation.observation_kind in {"report", "live_change"}
        and stamp
        and (not row.get("last_at") or stamp > datetime.fromisoformat(row["last_at"]))
    )
    if genuinely_new:
        assert stamp
        gap = (
            row.get("last_at")
            and source.freshness.interval_s
            and (stamp - datetime.fromisoformat(row["last_at"])).total_seconds()
            > source.freshness.interval_s
        )
        changed = "anchor" in row and abs(value.value - row["anchor"]) > settings["tolerance"]
        if changed and row["plausibility"] == "suspicious" and not gap:
            row["recovery_count"] += 1
            changed = row["recovery_count"] >= settings["recovery_reports"]
        elif not changed:
            row["recovery_count"] = 0
        if gap or changed or "anchor" not in row:
            row.update(
                anchor=value.value,
                unchanged_since=stamp.isoformat(),
                report_count=0,
                recovery_count=0,
                plausibility="plausible",
                evidence=[],
                reference_low=None,
                reference_high=None,
            )
        row["report_count"] += 1
        row["last_at"] = stamp.isoformat()
        row["evidence"] = list(dict.fromkeys([*row["evidence"][:1], *value.evidence]))[:4]
    if (
        row.get("unchanged_since")
        and reference
        and reference.measured_at
        and reference.measured_at >= datetime.fromisoformat(row["unchanged_since"])
    ):
        row["reference_low"] = min(
            row.get("reference_low") if row.get("reference_low") is not None else reference.value,
            reference.value,
        )
        row["reference_high"] = max(
            row.get("reference_high") if row.get("reference_high") is not None else reference.value,
            reference.value,
        )
        row["reference"] = {"evidence": list(reference.evidence)[:4]}
    reference_proven = (
        not profile.stuck.reference
        or row.get("reference_low") is not None
        and row["reference_high"] - row["reference_low"] >= settings["min_delta"]
    )
    if (
        row.get("unchanged_since")
        and row["report_count"] >= settings["min_reports"]
        and now
        >= datetime.fromisoformat(row["unchanged_since"])
        + timedelta(seconds=settings["unchanged_for_s"])
        and reference_proven
    ):
        row["plausibility"] = "suspicious"
    if row["plausibility"] == "suspicious":
        row.pop("next_at", None)
        return value.model_copy(
            update={
                "quality": "degraded",
                "plausibility": "suspicious",
                "reasons": value.reasons
                + (
                    Reason(
                        code=ReasonCode.SENSOR_STUCK,
                        input=source.source_id,
                        since=datetime.fromisoformat(row["unchanged_since"]),
                    ),
                ),
            }
        )
    if row.get("unchanged_since"):
        at = datetime.fromisoformat(row["unchanged_since"]) + timedelta(
            seconds=settings["unchanged_for_s"]
        )
        if at > now:
            row["next_at"] = at.isoformat()
        else:
            row.pop("next_at", None)
    if profile.stuck.reference and not reference_proven:
        return value.model_copy(update={"plausibility": "unchecked"})
    return value.model_copy(update={"plausibility": row["plausibility"]})
