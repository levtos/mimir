"""Positive attribution only. Account IDs and parent links are never proof by themselves."""

from collections import OrderedDict
from datetime import datetime, timedelta
from typing import Literal

from pydantic import Field

from .model import Model

type ProofBasis = Literal["registered_context", "ha_run"]


class HAContext(Model):
    id: str | None = Field(default=None, max_length=128)
    user_id: str | None = Field(default=None, max_length=128)
    parent_id: str | None = Field(default=None, max_length=128)


class Attribution(Model):
    kind: Literal["known_automatic", "known_user", "unknown"] = "unknown"
    basis: Literal["registered_context", "ha_run", "interactive", "unknown"] = "unknown"
    matched_context_id: str | None = Field(default=None, max_length=128)


class ContextProducer(Model):
    producer_id: str = Field(pattern=r"^[a-z][a-z0-9_.-]{1,127}$")
    display_name: str = Field(min_length=1, max_length=128)
    kind: Literal["policy", "apply"]


class ContextRegistration(Model):
    context: HAContext
    producer_id: str
    ha_epoch_id: str = Field(min_length=1, max_length=128)
    lifetime_s: int = Field(ge=1, le=600)


class ContextIndex:
    def __init__(self) -> None:
        self.epoch: str | None = None
        self.links: OrderedDict[str, tuple[HAContext, datetime]] = OrderedDict()
        self.proofs: OrderedDict[str, tuple[ProofBasis, datetime]] = OrderedDict()

    def set_epoch(self, epoch: str | None) -> None:
        if self.epoch != epoch:
            self.links.clear()
            self.proofs.clear()
            self.epoch = epoch

    def observe(self, context: HAContext, now: datetime) -> None:
        self._expire(now)
        if context.id is None or self.epoch is None:
            return
        if context.id not in self.links:
            self.links[context.id] = context, now + timedelta(seconds=600)
        elif self.links[context.id][0] != context:
            self.links.pop(context.id, None)
            self.proofs.pop(context.id, None)
            return
        while len(self.links) > 1024:
            key, _ = self.links.popitem(last=False)
            self.proofs.pop(key, None)

    def register(
        self,
        context: HAContext,
        now: datetime,
        *,
        lifetime_s: int = 600,
        basis: ProofBasis = "registered_context",
    ) -> None:
        if self.epoch is None or context.id is None or not 0 < lifetime_s <= 600:
            raise ValueError("context_registration_invalid")
        self.observe(context, now)
        if context.id not in self.links:
            raise ValueError("context_registration_invalid")
        expires = min(self.links[context.id][1], now + timedelta(seconds=lifetime_s))
        self.proofs[context.id] = basis, expires
        while len(self.proofs) > 1024:
            self.proofs.popitem(last=False)

    def attribution(self, context: HAContext, now: datetime) -> Attribution:
        self.observe(context, now)
        visited: set[str] = set()
        key = context.id
        matched = Attribution()
        for _ in range(9):
            if key is None:
                return matched
            if key in visited:
                return Attribution()
            visited.add(key)
            if key in self.proofs:
                basis, _ = self.proofs[key]
                matched = Attribution(kind="known_automatic", basis=basis, matched_context_id=key)
            link = self.links.get(key)
            if link is None:
                return matched
            key = link[0].parent_id
        return matched if key is None else Attribution()

    def clear_registered(self) -> None:
        for key, (basis, _) in tuple(self.proofs.items()):
            if basis == "registered_context":
                del self.proofs[key]

    def _expire(self, now: datetime) -> None:
        for key, (_, until) in tuple(self.links.items()):
            if until <= now:
                del self.links[key]
                self.proofs.pop(key, None)
        for key, (_, until) in tuple(self.proofs.items()):
            if until <= now:
                del self.proofs[key]
