"""Application type registry: production types are independent of test evaluators."""

from .openings import register
from .schema import TypeRegistry
from .testing.contract_types import type_registry as fixture_types


def type_registry() -> TypeRegistry:
    registry = fixture_types()
    register(registry)
    return registry
