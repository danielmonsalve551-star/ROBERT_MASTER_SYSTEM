"""Provider-independent model request and response contracts."""

from pydantic import Field, JsonValue

from robert.contracts.base import CanonicalContract, Identifier, JsonObject, NonEmptyString


class ModelRequest(CanonicalContract):
    request_id: Identifier
    task_id: Identifier
    model_role: NonEmptyString
    provider_requirement: NonEmptyString | None
    objective: NonEmptyString
    instructions: list[NonEmptyString]
    context: JsonObject
    inputs: JsonObject
    constraints: list[JsonValue]
    output_contract: JsonObject
    tool_request_allowed: bool = False
    memory_write_allowed: bool = False
    validation_requirements: list[JsonValue]
    sensitivity: NonEmptyString


class ModelResponse(CanonicalContract):
    request_id: Identifier
    task_id: Identifier
    model_id: NonEmptyString
    provider: NonEmptyString
    status: NonEmptyString
    output: JsonValue
    structured_output: JsonObject | None
    reasoning_summary_if_available: NonEmptyString | None
    tool_requests: list[Identifier]
    memory_candidates: list[Identifier]
    validation_requests: list[Identifier]
    confidence_if_applicable: float | None = Field(ge=0.0, le=1.0)
    citations_or_evidence: list[Identifier]
    warnings: list[JsonValue]
    errors: list[JsonValue]
    usage_metadata: JsonObject
