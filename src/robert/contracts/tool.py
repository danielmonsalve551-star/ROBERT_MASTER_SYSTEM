"""Tool request and result contracts; requests never imply authorization."""

from pydantic import Field, JsonValue

from robert.contracts.base import (
    CanonicalContract,
    Identifier,
    JsonObject,
    NonEmptyString,
    UtcDateTime,
)


class ToolRequest(CanonicalContract):
    request_id: Identifier
    task_id: Identifier
    requester: NonEmptyString
    tool_capability: NonEmptyString
    operation: NonEmptyString
    target: JsonValue
    inputs: JsonObject
    purpose: NonEmptyString
    expected_result: JsonObject
    permission_requirements: list[JsonValue]
    scope_requirements: list[JsonValue]
    risk_context: JsonObject
    approval_requirements: list[JsonValue]
    side_effect_class: NonEmptyString
    data_sensitivity: NonEmptyString
    timeout_policy: JsonObject
    retry_policy: JsonObject
    validation_requirements: list[JsonValue]


class ToolResult(CanonicalContract):
    request_id: Identifier
    task_id: Identifier
    tool_id: Identifier
    operation: NonEmptyString
    status: NonEmptyString
    result: JsonValue
    metadata: JsonObject
    source: NonEmptyString
    timestamp: UtcDateTime
    side_effects: list[JsonValue]
    warnings: list[JsonValue]
    errors: list[JsonValue]
    confidence_if_applicable: float | None = Field(ge=0.0, le=1.0)
    validation_required: bool
    audit_reference: Identifier | None
