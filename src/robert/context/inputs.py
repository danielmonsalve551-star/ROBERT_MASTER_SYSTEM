"""Explicitly supplied context fragments, never session or memory persistence."""

from typing import Literal

from robert.contracts.base import Identifier, JsonObject, NonEmptyString
from robert.governance.inputs import OperationScope
from robert.memory.inputs import MemoryInput


class ContextFragment(MemoryInput):
    ref_id: Identifier
    task_id: Identifier
    requester: NonEmptyString
    kind: Literal["CONVERSATION", "DOCUMENT"]
    scope: OperationScope
    sensitivity: Literal["PUBLIC", "INTERNAL"]
    payload: JsonObject
