"""Stage 7 governed, reusable and side-effect-free Skill Layer."""

from robert.skill.catalog import CONTRADICTION_DETECTION_MANIFEST
from robert.skill.inputs import (
    SkillCategory,
    SkillManifest,
    SkillOutputContract,
    SkillProcedureOutput,
    SkillStatus,
)
from robert.skill.procedure import ContradictionDetectionSkill, SkillProcedure
from robert.skill.registry import SkillRegistry
from robert.skill.runner import SkillRunner

__all__ = [
    "CONTRADICTION_DETECTION_MANIFEST",
    "ContradictionDetectionSkill",
    "SkillCategory",
    "SkillManifest",
    "SkillOutputContract",
    "SkillProcedure",
    "SkillProcedureOutput",
    "SkillRegistry",
    "SkillRunner",
    "SkillStatus",
]
