"""Read-only repository port and an explicitly seeded, nonpersistent adapter."""

from collections.abc import Iterable
from typing import Protocol

from pydantic import TypeAdapter

from robert.contracts.base import Identifier
from robert.contracts.memory import MemoryRecord
from robert.governance.inputs import OperationScope
from robert.memory.inputs import snapshot


class MemoryRepositoryError(RuntimeError):
    """An adapter could not provide a reliable snapshot; no raw backend error is exposed."""


class MemoryRepository(Protocol):
    @property
    def repository_id(self) -> str: ...

    def read(self, scope: OperationScope) -> tuple[MemoryRecord, ...]:
        """Trusted internal port. Public callers must use the governed retrieval interface."""
        ...


class InMemoryMemoryRepository:
    """Manual startup seed only. No add/update/delete/save API or durable memory writes."""

    def __init__(self, repository_id: str, records: Iterable[MemoryRecord] = ()):
        self._repository_id = TypeAdapter(Identifier).validate_python(repository_id, strict=True)
        self._records = tuple(snapshot(MemoryRecord, item) for item in records)
        ids = [record.memory_id for record in self._records]
        if len(ids) != len(set(ids)):
            raise ValueError("duplicate memory IDs are not allowed")

    @property
    def repository_id(self) -> str:
        return self._repository_id

    def read(self, scope: OperationScope) -> tuple[MemoryRecord, ...]:
        # Coarse project minimization; retrieval MUST enforce every record-level restriction.
        return tuple(
            snapshot(MemoryRecord, item)
            for item in self._records
            if item.scope.get("project") == scope.project
        )
