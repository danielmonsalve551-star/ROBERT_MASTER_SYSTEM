"""Audited memory proposals and deterministic validation, without record promotion."""

from collections.abc import Callable
from datetime import UTC, datetime
from uuid import uuid4

from pydantic import Field, JsonValue

from robert.audit import AuditEventBuilder, AuditWriter
from robert.contracts.base import Identifier, MemoryType, NonEmptyString, Retention
from robert.contracts.memory import MemoryCandidate
from robert.contracts.validation import ValidationRequest, ValidationResult
from robert.governance import GovernanceEngine
from robert.governance.inputs import (
    GovernanceRequest,
    OperationScope,
    PermissionGrant,
    SecurityContext,
)
from robert.memory.inputs import MemoryInput, checked_now, snapshot
from robert.validation import ValidationHandler, ValidationTarget


class CandidateDraft(MemoryInput):
    task_id: Identifier
    source: NonEmptyString
    content: JsonValue
    memory_type: MemoryType
    proposed_retention: Retention
    reason: NonEmptyString
    confidence: float = Field(ge=0, le=1, strict=True)
    sensitivity: NonEmptyString
    scope: OperationScope
    evidence_refs: tuple[Identifier, ...] = ()


class MemoryCandidateService:
    def __init__(self, writer: AuditWriter, *, clock: Callable[[], datetime] | None = None):
        self._writer = writer
        self._clock = clock or (lambda: datetime.now(UTC))

    def create(self, draft: CandidateDraft, *, requester: str) -> MemoryCandidate:
        draft = snapshot(CandidateDraft, draft)
        now = checked_now(self._clock())
        candidate = MemoryCandidate(
            contract_version="0.1",
            candidate_id=f"memory_candidate_{uuid4().hex}",
            **draft.model_dump(mode="json"),
            conflict_state={"status": "NONE_REPORTED"},
            validation_state={"status": "PENDING"},
        )
        self._writer.write(
            AuditEventBuilder(clock=lambda: now).build(
                task_id=candidate.task_id,
                event_type="MEMORY_CANDIDATE_CREATED",
                actor=requester,
                component="MEMORY_CANDIDATES",
                action="CREATE_CANDIDATE",
                target=candidate.candidate_id,
                output_refs=[candidate.candidate_id],
                result={
                    "status": "PROPOSED",
                    "persisted_memory": False,
                    "execution_authority": "NONE",
                },
            )
        )
        return candidate

    def validate(
        self,
        candidate: MemoryCandidate,
        *,
        requester: str,
        governance: GovernanceRequest | None = None,
        grant: PermissionGrant | None = None,
        security: SecurityContext | None = None,
    ) -> ValidationResult:
        candidate = snapshot(MemoryCandidate, candidate)
        governance = snapshot(GovernanceRequest, governance) if governance is not None else None
        if governance is not None and governance.operation != "PREPARE_DRAFT":
            raise ValueError("candidate validation requires PREPARE_DRAFT context")
        if governance is not None:
            outcome = GovernanceEngine(self._writer, clock=self._clock).evaluate(
                governance, grant=grant, security=security
            )
            if outcome.status != "ALLOWED":
                raise PermissionError("Candidate validation is not authorized")
        rules = []
        for field in ("source", "reason", "content"):
            rules.append(
                {
                    "criterion_id": f"candidate_{field}",
                    "validation_type": "RULE",
                    "method": "NON_EMPTY",
                    "path": [field],
                }
            )
        for field, expected in (
            ("conflict_state", {"status": "NONE_REPORTED"}),
            ("validation_state", {"status": "PENDING"}),
        ):
            rules.append(
                {
                    "criterion_id": f"candidate_{field}",
                    "validation_type": "RULE",
                    "method": "EQUALS",
                    "path": [field],
                    "expected": expected,
                }
            )
        rules.append(
            {
                "criterion_id": "candidate_sensitivity",
                "validation_type": "SECURITY",
                "method": "ONE_OF",
                "path": ["sensitivity"],
                "expected": ["PUBLIC", "INTERNAL"],
            }
        )
        if governance is not None:
            rules.append(
                {
                    "criterion_id": "candidate_scope",
                    "validation_type": "SCOPE",
                    "method": "EQUALS",
                    "path": ["scope"],
                    "expected": governance.scope.model_dump(mode="json"),
                }
            )
        request = ValidationRequest(
            contract_version="0.1",
            validation_id=f"validation_{uuid4().hex}",
            task_id=candidate.task_id,
            requester=requester,
            target_type="MEMORY_CANDIDATE",
            target_ref=candidate.candidate_id,
            validation_types=["CANONICAL", "RULE", "SECURITY", "SCOPE", "PERMISSION"],
            reviewer_roles=["RULE_SYSTEM"],
            criteria=rules,
            constraints=[],
            evidence_requirements=[],
            source_requirements=[],
            canonical_requirements=[],
            security_requirements=[],
            risk_context={},
            permission_context={},
            scope_context={},
            expected_contract={"name": "MEMORY_CANDIDATE", "version": "0.1"},
            severity="MEDIUM",
            blocking_policy={"fail_closed": True},
        )
        result = ValidationHandler(self._writer, clock=self._clock).validate(
            request,
            ValidationTarget(
                target_ref=candidate.candidate_id,
                task_id=candidate.task_id,
                target_type="MEMORY_CANDIDATE",
                payload=candidate.model_dump(mode="json"),
            ),
            governance=governance,
            grant=grant,
            security=security,
        )
        return result.model_copy(
            update={
                "limitations": [
                    *result.limitations,
                    "Candidate checks do not establish source truth, semantic uniqueness "
                    "or long-term eligibility",
                    "NONE_REPORTED is not independent conflict detection; "
                    "PASS never promotes or persists memory",
                ]
            }
        )
