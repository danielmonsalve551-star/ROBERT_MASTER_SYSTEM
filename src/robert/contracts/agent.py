"""Agent interface contracts without routing or execution authority."""

from pydantic import JsonValue

from robert.contracts.base import CanonicalContract, Identifier, JsonObject, NonEmptyString


class AgentRequest(CanonicalContract):
    task_id: Identifier
    agent_id: Identifier
    role: NonEmptyString
    objective: NonEmptyString
    authorized_scope: JsonObject
    context: JsonObject
    constraints: list[JsonValue]
    allowed_skills: list[NonEmptyString]
    allowed_model_capabilities: list[NonEmptyString]
    allowed_tool_requirements: list[NonEmptyString]
    memory_context: JsonObject
    validation_requirements: list[JsonValue]
    expected_output: JsonObject


class AgentResult(CanonicalContract):
    task_id: Identifier
    agent_id: Identifier
    status: NonEmptyString
    analysis: JsonValue
    output: JsonValue
    recommendations: list[JsonValue]
    skill_results: list[Identifier]
    model_refs: list[Identifier]
    tool_requests: list[Identifier]
    memory_candidates: list[Identifier]
    validation_requests: list[Identifier]
    warnings: list[JsonValue]
    errors: list[JsonValue]
    evidence_refs: list[Identifier]
    audit_refs: list[Identifier]
