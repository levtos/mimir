"""Portable configuration snapshots and explicitly staged, atomic import plans."""

import copy
import json
from typing import Any
from uuid import uuid4

from . import __version__
from .catalog_models import CatalogWrite, EntryChange, ManagedCatalog
from .editorial import EditorialWrite, ObjectRef, Room
from .managed_catalog import definition_digest, head, head_key, identity, invalidate, prepare
from .model import canonical, checksum
from .registry import RegistryConfig, resolve_ref, safe_document, storage_document, validate

GROUPS = {
    "dependencies": "dependency_id",
    "sources": "source_id",
    "bindings": "binding_id",
    "contracts": "contract_id",
    "catalogs": "catalog_id",
    "definitions": "type_id",
    "context_producers": "producer_id",
}
MAX_BYTES = 50 * 1024 * 1024


def strict_json(text: str) -> Any:
    if len(text.encode("utf-8")) > MAX_BYTES:
        raise ValueError("import_size_limit")

    def pairs(items: list[tuple[str, Any]]) -> dict[str, Any]:
        result: dict[str, Any] = {}
        for key, value in items:
            if key in result:
                raise ValueError("import_duplicate_key")
            result[key] = value
        return result

    def invalid(value: str) -> None:
        raise ValueError("import_nonfinite")

    return json.loads(text, object_pairs_hook=pairs, parse_constant=invalid)


def objects(document: dict[str, Any]) -> dict[str, Any]:
    return {
        f"{group}:{row[field]}" + (f"@{row['type_version']}" if group == "definitions" else ""): row
        for group, field in GROUPS.items()
        for row in document.get(group, [])
    }


def closure(config: RegistryConfig, root: str) -> dict[str, Any]:
    document = storage_document(config)
    contracts = {c.contract_id: c for c in config.contracts}
    sources = {s.source_id: s for s in config.sources}
    dependencies = {d.dependency_id: d for d in config.dependencies}
    selected: dict[str, set[str]] = {group: set() for group in GROUPS}

    def reference(ref: str) -> None:
        key, field = resolve_ref(ref, config)
        contract(key) if field is not None else source(key)

    def source(key: str) -> None:
        if key in selected["sources"]:
            return
        selected["sources"].add(key)
        item = sources[key]
        dependency = dependencies[item.dependency_id]
        selected["dependencies"].add(dependency.dependency_id)
        if dependency.source_id:
            source(dependency.source_id)
        if item.freshness.liveness_source:
            source(item.freshness.liveness_source)
        if item.sensor_profile and item.sensor_profile.stuck.reference:
            source(item.sensor_profile.stuck.reference.ref)
        for binding in config.bindings:
            if binding.source_id == key:
                selected["bindings"].add(binding.binding_id)
                if binding.transform and binding.transform.catalog_id:
                    selected["catalogs"].add(binding.transform.catalog_id)

    def rule_catalogs(value: Any) -> None:
        if isinstance(value, dict):
            if value.get("op") == "managed_catalog_lookup":
                selected["catalogs"].add(value["catalog_id"])
            for child in value.values():
                rule_catalogs(child)
        elif isinstance(value, list):
            for child in value:
                rule_catalogs(child)

    def contract(key: str) -> None:
        if key in selected["contracts"]:
            return
        selected["contracts"].add(key)
        item = contracts[key]
        for entry in item.inputs:
            reference(entry.ref)
        for definition in config.definitions:
            if (definition.type_id, definition.type_version) == (item.type_id, item.type_version):
                selected["definitions"].add(f"{definition.type_id}@{definition.type_version}")
                rule_catalogs(definition.model_dump(mode="json"))
        if item.refresh_plan:
            reference(item.refresh_plan.trigger_ref)
            if item.refresh_plan.stop_when:
                reference(item.refresh_plan.stop_when.reference())
            for target in item.refresh_plan.targets:
                source(target)

    contract(root)
    # Context proofs are global declarations; retain the explicit allowlist.
    selected["context_producers"] = {p.producer_id for p in config.context_producers}
    for group, field in GROUPS.items():
        if group in document:
            document[group] = [
                row
                for row in document[group]
                if (f"{row[field]}@{row['type_version']}" if group == "definitions" else row[field])
                in selected[group]
            ]
    document.pop("notifications", None)
    return document


def payload_digest(package: dict[str, Any]) -> str:
    return checksum(
        {key: package[key] for key in ("config", "editorial", "catalog_contents", "scope")}
        | {"roots": package["manifest"]["roots"]}
    )


def export(runtime: Any, state: Any, request: dict[str, Any]) -> dict[str, Any]:
    if request.get("expected_active_revision") != state.active_revision:
        raise ValueError("active_revision_conflict")
    if request.get("draft_id"):
        draft = state.tables["registry_draft"][request["draft_id"]]
        if draft["draft_version"] != request.get("draft_version"):
            raise ValueError("draft_version_conflict")
        config = validate(draft["config"], runtime.types)
    else:
        config = runtime._config(state)
    if config is None:
        raise ValueError("export_no_configuration")
    if request.get("draft_id") and draft.get("portable"):
        apply(runtime, state, draft, config, runtime.clock.now_utc())
    roots = [request["contract_id"]] if request.get("contract_id") else []
    document = closure(config, roots[0]) if roots else storage_document(config)
    checked = validate(document, runtime.types)
    refs = {f"contract:{c.contract_id}" for c in checked.contracts} | {
        f"template:{d.type_id}" for d in checked.definitions
    }
    editorial = [
        {key: row[key] for key in ("object", "category", "room")}
        for ref, row in state.tables["editorial_current"].items()
        if ref in refs
    ]
    if request.get("draft_id"):
        pending = [
            row
            for row in state.tables["editorial_draft"].values()
            if row["draft_id"] == request["draft_id"]
        ]
        for row in pending:
            if ObjectRef.model_validate(row["object"]).key in refs:
                editorial = [r for r in editorial if r["object"] != row["object"]] + [
                    {key: row[key] for key in ("object", "category", "room")}
                ]
    contents = []
    for catalog in checked.catalogs:
        if isinstance(catalog, ManagedCatalog):
            current = head(state, catalog)
            contents.append(
                {
                    "catalog_id": catalog.catalog_id,
                    "definition_version": catalog.version,
                    "definition_digest": current["definition_digest"],
                    "source_revision": current["revision"],
                    "entries": [row for _, row in sorted(current["entries"].items())],
                }
            )
    if sum(len(c["entries"]) for c in contents) > 100_000:
        raise ValueError("export_entry_limit")
    result: dict[str, Any] = {
        "format": "wuschel.configuration",
        "format_version": 1,
        "scope": "contract" if roots else "configuration",
        "producer": {"name": "Wuschel", "version": __version__},
        "config": document,
        "editorial": editorial,
        "catalog_contents": contents,
        "manifest": {
            "roots": roots,
            "object_digests": {key: checksum(row) for key, row in objects(document).items()},
            "config_digest": checksum(document),
        },
    }
    result["manifest"]["payload_digest"] = payload_digest(result)
    safe_document(result)
    if len(canonical(result).encode()) > MAX_BYTES:
        raise ValueError("export_size_limit")
    return result


def read_package(value: Any) -> dict[str, Any]:
    safe_document(value)
    if len(canonical(value).encode("utf-8")) > MAX_BYTES:
        raise ValueError("import_size_limit")
    if not isinstance(value, dict):
        raise ValueError("import_object_required")
    if "format" not in value:
        document = value.get("config", value)
        if not isinstance(document, dict):
            raise ValueError("import_object_required")
        if document.get("config_schema_version") not in (1, 2) or (
            "config" in value and set(value) - {"config", "display_name"}
        ):
            raise ValueError("import_legacy_format_unknown")
        return {
            "scope": "configuration",
            "config": document,
            "editorial": [],
            "catalog_contents": [],
            "legacy": True,
        }
    if (
        set(value)
        != {
            "format",
            "format_version",
            "scope",
            "producer",
            "config",
            "editorial",
            "catalog_contents",
            "manifest",
        }
        or value["format"] != "wuschel.configuration"
        or value["format_version"] != 1
        or value["scope"] not in {"configuration", "contract"}
    ):
        raise ValueError("import_format_unknown")
    manifest = value["manifest"]
    if (
        not isinstance(value["config"], dict)
        or not isinstance(manifest, dict)
        or set(manifest) != {"roots", "object_digests", "config_digest", "payload_digest"}
    ):
        raise ValueError("import_format_unknown")
    if (
        not isinstance(manifest["roots"], list)
        or not all(isinstance(root, str) for root in manifest["roots"])
        or not isinstance(manifest["object_digests"], dict)
    ):
        raise ValueError("import_format_unknown")
    if (value["scope"] == "configuration" and manifest["roots"]) or (
        value["scope"] == "contract" and len(manifest["roots"]) != 1
    ):
        raise ValueError("import_format_unknown")
    if (
        not isinstance(value["editorial"], list)
        or len(value["editorial"]) > 100_000
        or any(not isinstance(row, dict) for row in value["editorial"])
    ):
        raise ValueError("import_format_unknown")
    if not isinstance(value["catalog_contents"], list) or any(
        not isinstance(content, dict)
        or set(content)
        != {"catalog_id", "definition_version", "definition_digest", "source_revision", "entries"}
        or not isinstance(content["entries"], list)
        or any(not isinstance(row, dict) for row in content["entries"])
        for content in value["catalog_contents"]
    ):
        raise ValueError("import_format_unknown")
    RegistryConfig.model_validate(value["config"])
    if (
        checksum(value["config"]) != value["manifest"]["config_digest"]
        or payload_digest(value) != value["manifest"]["payload_digest"]
    ):
        raise ValueError("import_digest_mismatch")
    if {key: checksum(row) for key, row in objects(value["config"]).items()} != value["manifest"][
        "object_digests"
    ]:
        raise ValueError("import_object_digest_mismatch")
    if (
        not isinstance(value["catalog_contents"], list)
        or sum(len(c["entries"]) for c in value["catalog_contents"]) > 100_000
    ):
        raise ValueError("import_entry_limit")
    for row in value["editorial"]:
        EditorialWrite.model_validate({**row, "expected_editorial_version": 0})
    return value


def preview(runtime: Any, state: Any, request: dict[str, Any]) -> dict[str, Any]:
    package = copy.deepcopy(
        read_package(
            strict_json(request["package_text"])
            if "package_text" in request
            else request["package"]
        )
    )
    incoming = validate(package["config"], runtime.types)
    active = runtime._config(state)
    existing = storage_document(active) if active else {}
    target = None
    if package["scope"] == "contract":
        target = state.tables["registry_draft"].get(request.get("target_draft_id", ""))
        if target is None:
            raise ValueError("import_target_draft_required")
        if target["draft_version"] != request.get("target_draft_version"):
            raise ValueError("draft_version_conflict")
        if target.get("portable"):
            raise ValueError("import_target_has_plan")
        existing = storage_document(validate(target["config"], runtime.types))
    incoming_doc = storage_document(incoming)
    old_objects, new_objects = objects(existing), objects(incoming_doc)
    conflicts = [
        key
        for key, row in new_objects.items()
        if key in old_objects and checksum(row) != checksum(old_objects[key])
    ]
    resolutions = request.get("resolutions", {})
    remaps: dict[str, str] = {}
    for key in conflicts:
        resolution = resolutions.get(key)
        if isinstance(resolution, dict) and set(resolution) == {"new_id"}:
            group, old_id = key.split(":", 1)
            if group == "definitions":
                old_id = old_id.rsplit("@", 1)[0]
            new_id = resolution["new_id"]
            if (
                sum(
                    row[field] == old_id
                    for group_name, field in GROUPS.items()
                    for row in incoming_doc.get(group_name, [])
                )
                != 1
            ):
                raise ValueError("import_ambiguous_remap")
            if not isinstance(new_id, str) or any(
                row[field] == new_id
                for group_name, field in GROUPS.items()
                for row in existing.get(group_name, [])
            ):
                raise ValueError("import_remap_conflict")
            if old_id in remaps and remaps[old_id] != new_id:
                raise ValueError("import_remap_conflict")
            remaps[old_id] = new_id
    if len(set(remaps.values())) != len(remaps):
        raise ValueError("import_remap_conflict")

    def remap(value: Any, field: str = "") -> Any:
        if isinstance(value, dict):
            return {key: remap(child, key) for key, child in value.items()}
        if isinstance(value, list):
            return [remap(child, field) for child in value]
        if isinstance(value, str):
            if field in {*GROUPS.values(), "id", "catalog_id", "liveness_source", "targets"}:
                return remaps.get(value, value)
            if field in {"ref", "trigger_ref"}:
                for before, after in sorted(
                    remaps.items(), key=lambda pair: len(pair[0]), reverse=True
                ):
                    if value == before or value.startswith(before + "."):
                        return after + value[len(before) :]
        return value

    incoming_doc = remap(incoming_doc)
    package["editorial"] = remap(package["editorial"])
    package["catalog_contents"] = remap(package["catalog_contents"])
    incoming = validate(incoming_doc, runtime.types)
    for content in package["catalog_contents"]:
        if content["catalog_id"] in remaps.values():
            catalog = next(
                c
                for c in incoming.catalogs
                if c.catalog_id == content["catalog_id"]
                and c.version == content["definition_version"]
            )
            assert isinstance(catalog, ManagedCatalog)
            content["definition_digest"] = definition_digest(catalog)
    unresolved = [
        key
        for key in conflicts
        if resolutions.get(key) != "keep" and not isinstance(resolutions.get(key), dict)
    ]
    document = copy.deepcopy(incoming_doc)
    for group, field in GROUPS.items():
        rows = document.get(group, [])
        for index, row in enumerate(rows):
            key = f"{group}:{row[field]}" + (
                f"@{row['type_version']}" if group == "definitions" else ""
            )
            if key in conflicts and resolutions.get(key) == "keep":
                rows[index] = copy.deepcopy(old_objects[key])
        if package["scope"] == "contract":
            identities = {(r[field], r.get("type_version")) for r in rows}
            rows = [
                *copy.deepcopy(
                    [
                        r
                        for r in existing.get(group, [])
                        if (r[field], r.get("type_version")) not in identities
                    ]
                ),
                *rows,
            ]
        if group in document or rows:
            document[group] = rows
    if package["scope"] == "contract":
        for name in ("notifications", "history_retention"):
            if name in existing:
                document[name] = existing[name]
            else:
                document.pop(name, None)
        document["config_schema_version"] = max(
            incoming.config_schema_version, existing.get("config_schema_version", 1)
        )
        document["fingerprint_version"] = max(
            incoming.fingerprint_version, existing.get("fingerprint_version", 1)
        )
    if not unresolved:
        validate(document, runtime.types)
    heads = {
        head_key(c): head(state, c)["revision"]
        for c in incoming.catalogs
        if isinstance(c, ManagedCatalog)
    }
    for content in package["catalog_contents"]:
        content_catalog = next(
            (
                c
                for c in incoming.catalogs
                if isinstance(c, ManagedCatalog)
                and (c.catalog_id, c.version)
                == (content["catalog_id"], content["definition_version"])
            ),
            None,
        )
        if (
            content_catalog is None
            or definition_digest(content_catalog) != content["definition_digest"]
        ):
            raise ValueError("import_catalog_definition")
        seen: set[str] = set()
        for row in content["entries"]:
            entry = EntryChange.model_validate(
                {k: v for k, v in row.items() if k not in {"master_identity", "normalized_key"}}
            )
            key = identity(entry.scope, entry.media_type, entry.signal_type, entry.key)
            if key in seen:
                raise ValueError("import_catalog_duplicate")
            seen.add(key)
            previous = head(state, content_catalog)["entries"].get(key)
            if previous and previous != row:
                conflict = f"catalog-entry:{head_key(content_catalog)}:{key}"
                conflicts.append(conflict)
                if resolutions.get(conflict) != "keep":
                    unresolved.append(conflict)
    editorial_versions = {
        ObjectRef.model_validate(row["object"]).key: state.tables["editorial_current"]
        .get(ObjectRef.model_validate(row["object"]).key, {})
        .get("editorial_version", 0)
        for row in package["editorial"]
    }
    result = {
        "config": document,
        "package": package,
        "conflicts": conflicts,
        "unresolved": unresolved,
        "added": len(new_objects.keys() - old_objects.keys()),
        "reused": sum(row == old_objects.get(key) for key, row in new_objects.items()),
        "expected_active_revision": state.active_revision,
        "catalog_heads": heads,
        "editorial_versions": editorial_versions,
        "editorial_choices": request.get("editorial_choices", {}),
        "resolutions": resolutions,
        "catalog_entries": sum(len(content["entries"]) for content in package["catalog_contents"]),
        "editorial_entries": len(package["editorial"]),
        "target_draft_id": target["draft_id"] if target else None,
        "target_draft_version": target["draft_version"] if target else None,
    }
    if not unresolved:
        probe = state.clone()
        apply(
            runtime,
            probe,
            {
                "config": document,
                "portable": {
                    **result,
                    "config_digest": checksum(document),
                    "actor": request.get("_actor"),
                },
            },
            validate(document, runtime.types),
            runtime.clock.now_utc(),
        )
    result["plan_digest"] = checksum(result)
    return result


def stage(
    runtime: Any, state: Any, request: dict[str, Any], actor: Any, now: Any
) -> dict[str, Any]:
    plan = preview(runtime, state, request)
    if request.get("plan_digest") != plan["plan_digest"]:
        raise ValueError("import_plan_conflict")
    if plan["unresolved"]:
        raise ValueError("import_unresolved_conflicts")
    target = state.tables["registry_draft"].get(plan["target_draft_id"])
    if target is None and len(state.tables["registry_draft"]) >= 100:
        raise ValueError("draft_limit")
    key = target["draft_id"] if target else str(uuid4())
    draft = {
        **(target or {}),
        "draft_id": key,
        "draft_version": target["draft_version"] + 1 if target else 1,
        "config": plan["config"],
        "base_revision": state.active_revision,
        "created_at": target["created_at"] if target else now.isoformat(),
        "updated_at": now.isoformat(),
        "display_name": target.get("display_name", "Import") if target else "Import",
        "portable": {**plan, "config_digest": checksum(plan["config"]), "actor": actor},
    }
    state.tables["registry_draft"][key] = draft
    return draft


def apply(
    runtime: Any, state: Any, draft: dict[str, Any], config: RegistryConfig, now: Any
) -> dict[str, Any]:
    plan = draft.get("portable")
    if not plan:
        return dict(runtime.latches)
    if state.active_revision != plan["expected_active_revision"]:
        raise ValueError("import_plan_conflict")
    from .managed_catalog import definition

    latches = runtime.latches
    for content in plan["package"]["catalog_contents"]:
        catalog = definition(config, content["catalog_id"], content["definition_version"])
        current = head(state, catalog)
        if (
            current["revision"] != plan["catalog_heads"][head_key(catalog)]
            or definition_digest(catalog) != content["definition_digest"]
        ):
            raise ValueError("catalog_content_conflict")
        changes = [
            EntryChange.model_validate(
                {k: v for k, v in row.items() if k not in {"master_identity", "normalized_key"}}
            )
            for row in content["entries"]
        ]
        changes = [
            entry
            for entry in changes
            if plan["resolutions"].get(
                f"catalog-entry:{head_key(catalog)}:{identity(entry.scope, entry.media_type, entry.signal_type, entry.key)}"
            )
            != "keep"
        ]
        # One staged mutation and one DB commit, including cross-row parent links.
        if changes:
            body = CatalogWrite(
                catalog_id=catalog.catalog_id,
                definition_version=catalog.version,
                expected_active_revision=state.active_revision,
                expected_content_revision=head(state, catalog)["revision"],
                request_id=str(uuid4()),
                changes=(changes[0],),
                reason="Konfiguration eingelesen",
            )
            body = body.model_copy(update={"changes": tuple(changes)})
            result = prepare(state, config, body, plan["actor"], now, expanded_limit=100_000)
            latches = invalidate(state, result, latches)
    for row in plan["package"]["editorial"]:
        ref = ObjectRef.model_validate(row["object"])
        old = state.tables["editorial_current"].get(ref.key)
        if old and plan["editorial_choices"].get(ref.key) != "file":
            continue
        version = old["editorial_version"] if old else 0
        if version != plan["editorial_versions"][ref.key]:
            raise ValueError("editorial_version_conflict")
        state.tables["editorial_current"][ref.key] = {
            "object": ref.model_dump(),
            "category": row["category"],
            "room": Room.model_validate(row["room"]).model_dump(),
            "editorial_version": version + 1,
            "updated_at": now.isoformat(),
        }
    return dict(latches)
