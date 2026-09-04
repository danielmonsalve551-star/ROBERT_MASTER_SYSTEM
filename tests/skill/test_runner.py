import json

import pytest
from pydantic import ValidationError

from robert.audit import AuditWriteError
from robert.contracts.skill import SkillResult
from robert.skill import SkillProcedureOutput, SkillRunner
from tests.memory.conftest import changed


def test_simple_skill_receives_processes_returns_and_audits(invocation, runner, store):
    result = runner.run(invocation, requester="ORCHESTRATOR")

    assert SkillResult.model_validate_json(result.model_dump_json()) == result
    assert result.status == "COMPLETED"
    assert result.output == {
        "conflicts": [
            {
                "subject": "current stage",
                "claim_ids": ["claim_1", "claim_2"],
                "reason": "DIFFERING_VALUES",
            }
        ],
        "conflict_count": 1,
    }
    assert result.derived_data == {"claims_processed": 3, "truth_determined": False}
    assert result.tool_requests == [] and result.model_requests == []
    event = store.read_events()[-1]
    assert event.event_type == "SKILL_RUN_COMPLETED"
    assert event.actor == "ORCHESTRATOR"
    assert event.result["external_side_effects"] is False
    assert event.result["execution_authority"] == "NONE"


def test_equal_values_are_not_reported_as_conflicts(invocation, runner):
    invocation = changed(
        invocation,
        inputs={
            "claims": [
                {"claim_id": "a", "subject": "Status", "value": {"stage": 7}},
                {"claim_id": "b", "subject": " status ", "value": {"stage": 7}},
            ]
        },
    )
    result = runner.run(invocation, requester="VALIDATOR")
    assert result.output == {"conflicts": [], "conflict_count": 0}


@pytest.mark.parametrize(
    "field,value,error",
    [
        ("skill_id", "missing_skill", "SKILL_NOT_AVAILABLE"),
        ("skill_version", "9.9", "SKILL_VERSION_MISMATCH"),
        ("inputs", {}, "MISSING_INPUT"),
        ("context", {"api_key": "secret"}, "SENSITIVE_DATA_REJECTED"),
        ("constraints", [], "CONSTRAINT_MISMATCH"),
        ("tool_requirements", ["write"], "TOOL_REQUIREMENT_MISMATCH"),
        ("model_requirements", ["reasoning"], "MODEL_REQUIREMENT_MISMATCH"),
        ("memory_requirements", ["memory"], "MEMORY_REQUIREMENT_MISMATCH"),
        ("validation_requirements", [], "VALIDATION_REQUIREMENT_MISMATCH"),
        ("expected_output", {}, "OUTPUT_CONTRACT_MISMATCH"),
        ("preconditions", ["caller says pass"], "CALLER_PRECONDITIONS_UNSUPPORTED"),
    ],
)
def test_invocation_contract_cannot_weaken_manifest(invocation, runner, field, value, error):
    result = runner.run(changed(invocation, **{field: value}), requester="ORCHESTRATOR")
    assert result.status == "BLOCKED"
    assert result.errors == [{"code": error}]


def test_unauthorized_requester_is_blocked(invocation, runner):
    result = runner.run(invocation, requester="AGENT")
    assert result.status == "BLOCKED"
    assert result.errors == [{"code": "REQUESTER_NOT_AUTHORIZED"}]


@pytest.mark.parametrize(
    "claims",
    [
        "not-a-list",
        [{}],
        [{"claim_id": "a", "subject": "", "value": 1}],
        [{"claim_id": "a", "subject": "x", "value": float("nan")}],
    ],
)
def test_invalid_skill_inputs_fail_without_partial_output(invocation, runner, claims):
    if claims and isinstance(claims, list) and isinstance(claims[0].get("value"), float):
        with pytest.raises(ValueError, match="Out of range"):
            runner.run(changed(invocation, inputs={"claims": claims}), requester="ORCHESTRATOR")
        return
    result = runner.run(changed(invocation, inputs={"claims": claims}), requester="ORCHESTRATOR")
    assert result.status == "FAILED" and result.output is None
    assert result.errors == [{"code": "INVALID_SKILL_INPUT"}]


class BadOutputProcedure:
    skill_id = "contradiction_detection"
    version = "0.1"

    def __init__(self, output):
        self.output = output

    def process(self, invocation):
        if isinstance(self.output, Exception):
            raise self.output
        return self.output


@pytest.mark.parametrize(
    "output,error",
    [
        (SkillProcedureOutput(output={"conflicts": []}), "OUTPUT_CONTRACT_FAILED"),
        (
            SkillProcedureOutput(
                output={"conflicts": [], "conflict_count": 0}, tool_requests=("tool_1",)
            ),
            "UNAUTHORIZED_TOOL_REQUEST",
        ),
        (
            SkillProcedureOutput(
                output={"conflicts": [], "conflict_count": 0}, model_requests=("model_1",)
            ),
            "UNAUTHORIZED_MODEL_REQUEST",
        ),
        (
            SkillProcedureOutput(
                output={"conflicts": [], "conflict_count": 0},
                memory_candidates=("memory_1",),
            ),
            "UNAUTHORIZED_MEMORY_CANDIDATE",
        ),
        (
            SkillProcedureOutput(
                output={"conflicts": [], "conflict_count": 0, "api_key": "secret"}
            ),
            "SENSITIVE_OUTPUT_REJECTED",
        ),
    ],
)
def test_procedure_outputs_fail_closed(invocation, registry, writer, output, error):
    runner = SkillRunner(registry, (BadOutputProcedure(output),), writer)
    result = runner.run(invocation, requester="ORCHESTRATOR")
    assert result.status == "FAILED" and result.output is None
    assert result.errors == [{"code": error}]
    assert "secret" not in result.model_dump_json()


def test_unexpected_procedure_error_is_normalized(invocation, registry, writer):
    runner = SkillRunner(
        registry,
        (BadOutputProcedure(RuntimeError("secret implementation detail")),),
        writer,
    )
    result = runner.run(invocation, requester="ORCHESTRATOR")
    assert result.errors == [{"code": "SKILL_PROCEDURE_FAILED"}]
    assert "secret implementation detail" not in result.model_dump_json()


def test_missing_or_mismatched_procedure_blocks(invocation, registry, writer):
    assert SkillRunner(registry, (), writer).run(invocation, requester="ORCHESTRATOR").errors == [
        {"code": "SKILL_PROCEDURE_UNAVAILABLE"}
    ]
    procedure = BadOutputProcedure(SkillProcedureOutput(output={}))
    procedure.version = "2.0"
    assert SkillRunner(registry, (procedure,), writer).run(
        invocation, requester="ORCHESTRATOR"
    ).errors == [{"code": "SKILL_PROCEDURE_UNAVAILABLE"}]


def test_audit_failure_prevents_result_disclosure(invocation, runner, writer, monkeypatch):
    monkeypatch.setattr(
        writer,
        "write",
        lambda event: (_ for _ in ()).throw(AuditWriteError("offline")),
    )
    with pytest.raises(AuditWriteError):
        runner.run(invocation, requester="ORCHESTRATOR")


def test_audit_contains_no_full_skill_input_or_output(invocation, runner, store):
    unique_value = "confidential-but-not-secret-value"
    invocation = changed(
        invocation,
        inputs={
            "claims": [
                {"claim_id": "a", "subject": "status", "value": unique_value},
                {"claim_id": "b", "subject": "status", "value": "different"},
            ]
        },
    )
    runner.run(invocation, requester="ORCHESTRATOR")
    encoded = "\n".join(json.dumps(event.model_dump(mode="json")) for event in store.read_events())
    assert unique_value not in encoded


def test_result_is_immutable(invocation, runner):
    result = runner.run(invocation, requester="ORCHESTRATOR")
    with pytest.raises(ValidationError):
        result.status = "ALTERED"
