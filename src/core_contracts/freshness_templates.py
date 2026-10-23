"""Revision-owned freshness selections; runtime resolution has one authority."""

import copy
from typing import Annotated, Any, Literal

from pydantic import Field, model_validator

from .evidence import Freshness
from .model import Model

SensorKind = Literal["contact", "temperature", "motion", "counter"]


class TemplateRule(Model):
    mode: Literal["report_heartbeat", "liveness_source", "periodic_ttl", "event_stateful"]
    future_tolerance_s: float = Field(ge=0, strict=True, allow_inf_nan=False)
    interval_s: float | None = Field(default=None, gt=0, strict=True, allow_inf_nan=False)

    @model_validator(mode="after")
    def complete(self) -> TemplateRule:
        if self.mode != "event_stateful" and self.interval_s is None:
            raise ValueError("freshness interval required")
        return self


class FreshnessTemplate(Model):
    template_id: str = Field(pattern=r"^freshness\.[a-zA-Z0-9_.-]+$")
    display_name: str = Field(min_length=1, max_length=256)
    sensor_kind: SensorKind
    rule: TemplateRule


class OwnFreshness(Model):
    kind: Literal["own"]
    rule: Freshness
    comparison_template_id: str | None = None


class SharedFreshness(Model):
    kind: Literal["shared"]
    template_id: str
    liveness_source: str | None = None


FreshnessSelection = Annotated[OwnFreshness | SharedFreshness, Field(discriminator="kind")]


def upgrade_document(document: dict[str, Any]) -> dict[str, Any]:
    """Produce an editable v4 copy. Never rewrite an immutable historical revision."""
    result = copy.deepcopy(document)
    if result.get("config_schema_version") == 4:
        return result
    result.update(config_schema_version=4, fingerprint_version=4, freshness_templates=[])
    for source in result.get("sources", []):
        source["freshness_selection"] = {"kind": "own", "rule": source.pop("freshness")}
    return result


def effective_freshness(config: Any) -> dict[str, Any]:
    templates = {template.template_id: template for template in config.freshness_templates}
    sources = {}
    usage = {}
    for source in config.sources:
        selection = source.freshness_selection
        template_id = (
            (
                selection.template_id
                if selection.kind == "shared"
                else selection.comparison_template_id
            )
            if selection
            else None
        )
        template = templates.get(template_id)
        comparison = template.rule.model_dump() if template else None
        rule = source.freshness.model_dump(mode="json")
        comparable = {key: value for key, value in rule.items() if key != "liveness_source"}
        sources[source.source_id] = {
            "rule": rule,
            "origin": selection.kind if selection else "own",
            "template_id": template_id,
            "sensor_kind": source.sensor_kind,
            "differs": comparison is not None and comparison != comparable,
        }
    for template_id in templates:
        shared = {
            key
            for key, row in sources.items()
            if row["origin"] == "shared" and row["template_id"] == template_id
        }
        own = {
            key
            for key, row in sources.items()
            if row["origin"] == "own" and row["template_id"] == template_id
        }
        contracts = {
            contract.contract_id
            for contract in config.contracts
            if any(item.ref in shared for item in contract.inputs)
        }
        usage[template_id] = {
            "source_ids": sorted(shared),
            "own_source_ids": sorted(own),
            "deviation_source_ids": sorted(key for key in own if sources[key]["differs"]),
            "contract_ids": sorted(contracts),
        }
    return {"sources": sources, "templates": usage}
