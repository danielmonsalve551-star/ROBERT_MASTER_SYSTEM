"""Task and request-context contracts owned by the coordination domain."""

from pydantic import JsonValue

from robert.contracts.base import (
    CanonicalContract,
    Identifier,
    JsonObject,
    NonEmptyString,
    TaskStatus,
    UtcDateTime,
)


class Task(CanonicalContract):
    task_id: Identifier
    created_at: UtcDateTime
    created_by: NonEmptyString
    original_request: NonEmptyString
    normalized_intent: NonEmptyString
    objective: NonEmptyString
    status: TaskStatus
    priority: NonEmptyString
    phase: NonEmptyString
    authorized_scope: JsonObject
    constraints: list[JsonValue]
    risk_context: JsonObject
    required_outputs: list[JsonValue]
    context_refs: list[Identifier]
    memory_refs: list[Identifier]
    dependencies: list[Identifier]
    current_step: NonEmptyString | None
    assigned_route: Identifier | None
    approval_state: JsonObject
    validation_state: JsonObject
    audit_refs: list[Identifier]
    result_ref: Identifier | None


class RequestContext(CanonicalContract):
    task_id: Identifier
    user_request: NonEmptyString
    conversation_context: JsonObject
    authorized_context: JsonObject
    memory_context: JsonObject
    document_context: JsonObject
    system_constraints: list[JsonValue]
    user_constraints: list[JsonValue]
    phase_constraints: list[JsonValue]
    permission_context: JsonObject
    scope_context: JsonObject
    risk_context: JsonObject
    security_context: JsonObject
