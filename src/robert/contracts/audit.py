"""Audit event and evidence-reference contracts."""

from robert.contracts.base import (
    CanonicalContract,
    Identifier,
    JsonObject,
    NonEmptyString,
    UtcDateTime,
)


class AuditEvent(CanonicalContract):
    event_id: Identifier
    task_id: Identifier
    timestamp: UtcDateTime
    event_type: NonEmptyString
    actor: NonEmptyString
    component: NonEmptyString
    action: NonEmptyString
    target: NonEmptyString
    input_refs: list[Identifier]
    output_refs: list[Identifier]
    permission_state: JsonObject
    scope_state: JsonObject
    risk_state: JsonObject
    approval_state: JsonObject
    validation_state: JsonObject
    result: JsonObject
    error_ref: Identifier | None
    metadata: JsonObject


class EvidenceRef(CanonicalContract):
    ref_id: Identifier
    source_type: NonEmptyString
    source_location: NonEmptyString
    source_authority: NonEmptyString
    created_at: UtcDateTime
    freshness: NonEmptyString
