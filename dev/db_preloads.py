"""Pure allowlist used by the prepared, never automatically executed DB runbook."""


def parse_preloads(value: str) -> tuple[str, ...]:
    """Only no modules or TimescaleDB; reject every unknown or empty list item."""
    if not value.strip():
        return ()
    names = tuple(part.strip() for part in value.split(","))
    if any(name != "timescaledb" for name in names):
        raise ValueError("preload_module_not_allowed")
    return names
