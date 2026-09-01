"""Memory candidate, record, and governed retrieval contracts."""

from pydantic import Field, JsonValue

from robert.contracts.base import (
    CanonicalContract,
    Identifier,
    JsonObject,
    MemoryType,
    NonEmptyString,
    Retention,
    UtcDateTime,
)


class MemoryCandidate(CanonicalContract):
    candidate_id: Identifier
    task_id: Identifier
    source: NonEmptyString
    content: JsonValue
    memory_type: MemoryType
    proposed_retention: Retention
    reason: NonEmptyString
    confidence: float = Field(ge=0.0, le=1.0)
    sensitivity: NonEmptyString
    scope: JsonObject
    evidence_refs: list[Identifier]
    conflict_state: JsonObject
    validation_state: JsonObject


class MemoryRecord(CanonicalContract):
    memory_id: Identifier
    content: JsonValue
    memory_type: MemoryType
    retention: Retention
    created_at: UtcDateTime
    updated_at: UtcDateTime
    source: NonEmptyString
    authority_metadata: JsonObject
    scope: JsonObject
    sensitivity: NonEmptyString
    evidence_refs: list[Identifier]
    decision_refs: list[Identifier]
    validation_state: JsonObject
    status: NonEmptyString


class MemoryRetrievalRequest(CanonicalContract):
    request_id: Identifier
    task_id: Identifier
    requester: NonEmptyString
    query: NonEmptyString
    memory_types: list[MemoryType]
    retention_classes: list[Retention]
    scope: JsonObject
    freshness_requirement: JsonObject
    confidence_requirement: float | None = Field(ge=0.0, le=1.0)
    sensitivity_constraints: list[JsonValue]
    max_results: int = Field(ge=1)
    purpose: NonEmptyString


class MemoryRetrievalResult(CanonicalContract):
    request_id: Identifier
    task_id: Identifier
    status: NonEmptyString
    records: list[MemoryRecord]
    ranking_metadata: JsonObject
    conflicts: list[JsonValue]
    warnings: list[JsonValue]
    audit_reference: Identifier | None
