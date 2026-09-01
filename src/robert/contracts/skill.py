"""Reusable skill invocation and result contracts."""

from pydantic import JsonValue

from robert.contracts.base import CanonicalContract, Identifier, JsonObject, NonEmptyString


class SkillInvocation(CanonicalContract):
    task_id: Identifier
    skill_id: Identifier
    skill_version: NonEmptyString
    objective: NonEmptyString
    inputs: JsonObject
    context: JsonObject
    preconditions: list[JsonValue]
    constraints: list[JsonValue]
    tool_requirements: list[NonEmptyString]
    model_requirements: list[NonEmptyString]
    memory_requirements: list[JsonValue]
    expected_output: JsonObject
    validation_requirements: list[JsonValue]


class SkillResult(CanonicalContract):
    task_id: Identifier
    skill_id: Identifier
    skill_version: NonEmptyString
    status: NonEmptyString
    output: JsonValue
    derived_data: JsonObject
    tool_requests: list[Identifier]
    model_requests: list[Identifier]
    memory_candidates: list[Identifier]
    validation_requests: list[Identifier]
    warnings: list[JsonValue]
    errors: list[JsonValue]
    audit_refs: list[Identifier]
