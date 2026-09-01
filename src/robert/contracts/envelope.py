"""Transport envelope shared by canonical Robert messages."""

from robert.contracts.base import (
    CanonicalContract,
    ContractName,
    Identifier,
    JsonObject,
    NonEmptyString,
    UtcDateTime,
)


class ContractEnvelope(CanonicalContract):
    message_id: Identifier
    message_type: ContractName
    task_id: Identifier
    parent_id: Identifier | None
    correlation_id: Identifier
    created_at: UtcDateTime
    source_component: NonEmptyString
    target_component: NonEmptyString
    phase: NonEmptyString
    scope: JsonObject
    metadata: JsonObject
    payload: JsonObject
