"""Initial Stage 7 catalog with one small reusable Skill."""

from robert.skill.inputs import (
    SkillCategory,
    SkillManifest,
    SkillOutputContract,
    SkillStatus,
)

CONTRADICTION_DETECTION_MANIFEST = SkillManifest(
    skill_id="contradiction_detection",
    name="Contradiction Detection",
    version="0.1",
    purpose="Identify differing values asserted for the same normalized subject",
    category=SkillCategory.ANALYSIS,
    capabilities=("contradiction_detection",),
    required_inputs=("claims",),
    required_context=(),
    constraints=("DO_NOT_DETERMINE_TRUTH", "NO_EXTERNAL_EFFECTS"),
    tool_requirements=(),
    model_requirements=(),
    memory_requirements=(),
    output_contract=SkillOutputContract(
        required=("conflicts", "conflict_count"), allow_additional=False
    ),
    validation_requirements=("RULE_VALIDATION",),
    failure_modes=("MISSING_INPUT", "INVALID_SKILL_INPUT", "OUTPUT_CONTRACT_FAILED"),
    compatible_requesters=("ORCHESTRATOR", "VALIDATOR"),
    dependencies=(),
    overlap_notes="Primary reusable capability; check this Skill before creating a duplicate",
    status=SkillStatus.IMPLEMENTED,
    external_effects_allowed=False,
)
