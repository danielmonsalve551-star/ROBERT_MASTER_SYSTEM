"""Orchestrator request, route, and result contracts."""

from pydantic import JsonValue

from robert.contracts.base import CanonicalContract, Identifier, JsonObject, NonEmptyString
from robert.contracts.task import RequestContext, Task


class OrchestratorRequest(CanonicalContract):
    task: Task
    request_context: RequestContext
    intent: NonEmptyString
    requested_operation: NonEmptyString
    required_capabilities: list[NonEmptyString]
    constraints: list[JsonValue]
    permission_context: JsonObject
    scope_context: JsonObject
    risk_context: JsonObject
    approval_context: JsonObject
    validation_requirements: list[JsonValue]
    expected_output: JsonObject


class Route(CanonicalContract):
    route_id: Identifier
    task_id: Identifier
    module: NonEmptyString | None
    agent: NonEmptyString | None
    skills: list[NonEmptyString]
    model: NonEmptyString | None
    tool_capabilities: list[NonEmptyString]
    memory_requirements: list[JsonValue]
    validation_requirements: list[JsonValue]
    sequence: list[NonEmptyString]
    fallbacks: list[JsonValue]
    constraints: list[JsonValue]


class OrchestratorResult(CanonicalContract):
    task_id: Identifier
    route: Route
    selected_module: NonEmptyString | None
    selected_agent: NonEmptyString | None
    selected_skills: list[NonEmptyString]
    selected_model: NonEmptyString | None
    selected_tool_capability: NonEmptyString | None
    memory_plan: JsonObject
    validation_plan: JsonObject
    permission_state: JsonObject
    scope_state: JsonObject
    risk_state: JsonObject
    approval_state: JsonObject
    execution_authority_state: JsonObject
    next_action: NonEmptyString | None
    status: NonEmptyString
    warnings: list[JsonValue]
    errors: list[JsonValue]
    audit_refs: list[Identifier]
