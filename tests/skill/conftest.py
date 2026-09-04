import pytest

from robert.audit import AuditWriter, JsonLinesAuditStore
from robert.contracts.skill import SkillInvocation
from robert.skill import (
    CONTRADICTION_DETECTION_MANIFEST,
    ContradictionDetectionSkill,
    SkillRegistry,
    SkillRunner,
)


@pytest.fixture
def store(tmp_path):
    return JsonLinesAuditStore(tmp_path / "skill_audit.jsonl")


@pytest.fixture
def writer(store):
    return AuditWriter(store)


@pytest.fixture
def manifest():
    return CONTRADICTION_DETECTION_MANIFEST


@pytest.fixture
def registry(manifest):
    return SkillRegistry((manifest,))


@pytest.fixture
def runner(registry, writer):
    return SkillRunner(registry, (ContradictionDetectionSkill(),), writer)


@pytest.fixture
def invocation(manifest):
    return SkillInvocation(
        contract_version="0.1",
        task_id="task_skill_1",
        skill_id=manifest.skill_id,
        skill_version=manifest.version,
        objective="Identify contradictions without determining truth",
        inputs={
            "claims": [
                {"claim_id": "claim_1", "subject": "Current Stage", "value": 7},
                {"claim_id": "claim_2", "subject": " current  stage ", "value": 6},
                {"claim_id": "claim_3", "subject": "Phase", "value": 10},
            ]
        },
        context={},
        preconditions=[],
        constraints=list(manifest.constraints),
        tool_requirements=list(manifest.tool_requirements),
        model_requirements=list(manifest.model_requirements),
        memory_requirements=list(manifest.memory_requirements),
        expected_output=manifest.output_contract.model_dump(mode="json"),
        validation_requirements=list(manifest.validation_requirements),
    )
