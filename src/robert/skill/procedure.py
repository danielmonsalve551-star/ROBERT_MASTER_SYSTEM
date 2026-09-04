"""Procedure port and the first deterministic, side-effect-free Skill."""

import json
from collections.abc import Mapping
from typing import Protocol

from robert.contracts.skill import SkillInvocation
from robert.skill.inputs import SkillProcedureOutput


class SkillProcedure(Protocol):
    skill_id: str
    version: str

    def process(self, invocation: SkillInvocation) -> SkillProcedureOutput: ...


class ContradictionDetectionSkill:
    """Find differing values asserted for the same normalized subject."""

    skill_id = "contradiction_detection"
    version = "0.1"

    def process(self, invocation: SkillInvocation) -> SkillProcedureOutput:
        claims = invocation.inputs["claims"]
        if not isinstance(claims, list):
            raise ValueError("claims must be a list")
        grouped: dict[str, list[tuple[str, object]]] = {}
        for claim in claims:
            if not isinstance(claim, Mapping) or set(claim) != {"claim_id", "subject", "value"}:
                raise ValueError("each claim requires claim_id, subject and value")
            claim_id, subject = claim["claim_id"], claim["subject"]
            if not isinstance(claim_id, str) or not claim_id or not isinstance(subject, str):
                raise ValueError("claim identity and subject must be nonempty strings")
            normalized_subject = " ".join(subject.casefold().split())
            if not normalized_subject:
                raise ValueError("claim subject must be nonempty")
            grouped.setdefault(normalized_subject, []).append((claim_id, claim["value"]))
        conflicts = []
        for subject in sorted(grouped):
            entries = grouped[subject]
            values = {
                json.dumps(value, ensure_ascii=False, sort_keys=True, allow_nan=False)
                for _, value in entries
            }
            if len(values) > 1:
                conflicts.append(
                    {
                        "subject": subject,
                        "claim_ids": sorted(claim_id for claim_id, _ in entries),
                        "reason": "DIFFERING_VALUES",
                    }
                )
        return SkillProcedureOutput(
            output={"conflicts": conflicts, "conflict_count": len(conflicts)},
            derived_data={"claims_processed": len(claims), "truth_determined": False},
            warnings=("CONTRADICTION_DETECTION_DOES_NOT_DETERMINE_TRUTH",),
        )
