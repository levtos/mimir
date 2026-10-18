"""Selected metadata and fixed refresh profiles from actual loaded HA integrations."""

from homeassistant.helpers import area_registry, device_registry, entity_registry
from homeassistant.helpers.entity_component import DATA_INSTANCES

from .service_channel import Rejected


def polling_entity(hass, entity_id):
    component = hass.data.get(DATA_INSTANCES, {}).get(entity_id.partition(".")[0])
    entity = component.get_entity(entity_id) if component else None
    return entity if entity is not None and entity.should_poll else None


def companion_service(hass, entity_id):
    # Use the registered target -> webhook mapping. A guessed service name is not proof.
    if not entity_id.startswith("device_tracker."):
        raise Rejected("not_allowed")
    registered = entity_registry.async_get(hass).async_get(entity_id)
    entry = (
        hass.config_entries.async_get_entry(registered.config_entry_id)
        if registered and registered.config_entry_id
        else None
    )
    if entry is None or entry.domain != "mobile_app" or registered.platform != "mobile_app":
        raise Rejected("not_allowed")
    notifier = hass.data.get("mobile_app", {}).get("notify")
    webhook = entry.data.get("webhook_id")
    targets = getattr(notifier, "registered_targets", {})
    matching = [
        service
        for service, target in targets.items()
        if target == webhook
        and service.startswith("mobile_app_")
        and hass.services.has_service("notify", service)
    ]
    if not webhook or len(matching) != 1:
        raise Rejected("not_allowed")
    return matching[0]


def refresh_action(hass, profile, data):
    entity = data["entity_id"]
    if profile == "entity_poll":
        if polling_entity(hass, entity) is None:
            raise Rejected("not_allowed")
        return "homeassistant", "update_entity", {"entity_id": entity}
    if profile == "companion_location" and data.get("permission_confirmed") is True:
        return "notify", companion_service(hass, entity), {"message": "request_location_update"}
    raise Rejected("not_allowed")


def source_metadata(hass, entity_ids):
    registry = entity_registry.async_get(hass)
    devices = device_registry.async_get(hass)
    areas = area_registry.async_get(hass)
    result = []
    for entity_id in entity_ids:
        entry = registry.async_get(entity_id)
        device = devices.async_get(entry.device_id) if entry and entry.device_id else None
        area_id = (entry.area_id if entry else None) or (device.area_id if device else None)
        area = areas.async_get_area(area_id) if area_id else None
        profiles = []
        if polling_entity(hass, entity_id):
            profiles.append("entity_poll")
        try:
            companion_service(hass, entity_id)
            profiles.append("companion_location")
        except Rejected:
            pass
        result.append(
            {
                "entity_id": entity_id,
                "area_id": area_id,
                "area_name": area.name if area else None,
                "area_icon": area.icon if area else None,
                "refresh_profiles": profiles,
            }
        )
    return result
