"""Governed, deterministic lexical retrieval; never an authority or memory-write gate."""

import json
import re
from collections.abc import Callable
from datetime import UTC, datetime
from typing import Protocol

from pydantic import ValidationError

from robert.audit import AuditEventBuilder, AuditWriter
from robert.audit.redaction import redact_sensitive_values
from robert.contracts.base import PermissionStatus
from robert.contracts.memory import MemoryRecord, MemoryRetrievalRequest, MemoryRetrievalResult
from robert.governance import GovernanceEngine
from robert.governance.checks import check_permission
from robert.governance.inputs import (
    GovernanceRequest,
    OperationScope,
    PermissionGrant,
    SecurityContext,
)
from robert.memory.inputs import (
    FreshnessRequirement,
    MemoryAuthority,
    RecordValidation,
    checked_now,
    snapshot,
)
from robert.memory.repository import MemoryRepository, MemoryRepositoryError

MAX_RESULTS = 50
MAX_SCAN_RECORDS = 10000
LIMITATION = "Lexical retrieval is not truth, source precedence, approval or execution authority"


class MemoryRetrieval(Protocol):
    def retrieve(
        self,
        request: MemoryRetrievalRequest,
        *,
        grant: PermissionGrant | None = None,
        security: SecurityContext | None = None,
    ) -> MemoryRetrievalResult: ...


def scope_contains(outer: OperationScope, inner: OperationScope) -> bool:
    return (
        inner.project == outer.project
        and inner.phase == outer.phase == 10
        and inner.mode == outer.mode
        and "*" not in inner.sections
        and "*" not in outer.sections
        and set(inner.sections).issubset(outer.sections)
    )


class MemoryRetriever:
    def __init__(
        self,
        repository: MemoryRepository,
        writer: AuditWriter,
        *,
        clock: Callable[[], datetime] | None = None,
    ):
        self._repository = repository
        self._writer = writer
        self._clock = clock or (lambda: datetime.now(UTC))

    def retrieve(self, request, *, grant=None, security=None) -> MemoryRetrievalResult:
        request = snapshot(MemoryRetrievalRequest, request)
        grant = snapshot(PermissionGrant, grant) if grant is not None else None
        security = snapshot(SecurityContext, security) if security is not None else None
        now = checked_now(self._clock())
        try:
            scope = OperationScope.model_validate(request.scope)
            freshness = FreshnessRequirement.model_validate(request.freshness_requirement)
            tokens = set(re.findall(r"\w+", request.query.casefold()))
            if (
                not tokens
                or len(request.query) > 2000
                or not request.purpose.strip()
                or not request.memory_types
                or len(set(request.memory_types)) != len(request.memory_types)
                or not request.retention_classes
                or len(set(request.retention_classes)) != len(request.retention_classes)
                or not request.sensitivity_constraints
                or any(
                    item not in ("PUBLIC", "INTERNAL") for item in request.sensitivity_constraints
                )
                or request.max_results > MAX_RESULTS
            ):
                raise ValueError("unsupported request")
        except (ValidationError, ValueError, TypeError):
            return self._result(
                request, "INCONCLUSIVE", [], [], ["Unsupported retrieval request"], now
            )
        governance = GovernanceRequest(
            request_id=request.request_id,
            task_id=request.task_id,
            requester=request.requester,
            operation="READ_DOCUMENT",
            target=self._repository.repository_id,
            scope=scope,
        )
        outcome = GovernanceEngine(self._writer, clock=lambda: now).evaluate(
            governance, grant=grant, security=security
        )
        if outcome.status != "ALLOWED":
            return self._result(request, "DENIED", [], [], ["Memory access is not authorized"], now)
        try:
            # The port must return a bounded materialized tuple, never an unbounded lazy stream.
            records = self._repository.read(scope)
            if not isinstance(records, tuple) or len(records) > MAX_SCAN_RECORDS:
                raise MemoryRepositoryError("unsupported repository snapshot")
            records = tuple(snapshot(MemoryRecord, item) for item in records)
            if len({item.memory_id for item in records}) != len(records):
                raise MemoryRepositoryError("duplicate repository identity")
        except (MemoryRepositoryError, ValidationError, ValueError, TypeError, AttributeError):
            return self._result(
                request, "INCONCLUSIVE", [], [], ["Memory repository unavailable"], now
            )
        ranked = []
        conflicts = []
        # A slow repository must not let an expired grant disclose a cached snapshot.
        now = checked_now(self._clock())
        if check_permission(governance, grant, now).status != PermissionStatus.ALLOWED:
            return self._result(
                request, "DENIED", [], [], ["Permission expired during retrieval"], now
            )
        for record in records:
            try:
                record_scope = OperationScope.model_validate(record.scope)
                authority = MemoryAuthority.model_validate(record.authority_metadata)
                validation = RecordValidation.model_validate(record.validation_state)
            except (ValidationError, ValueError, TypeError):
                continue
            # Do not disclose IDs, counts, content or conflict metadata for unauthorized records.
            if (
                not scope_contains(scope, record_scope)
                or request.requester not in authority.readers
                or record.memory_type not in request.memory_types
                or record.retention not in request.retention_classes
                or record.sensitivity not in request.sensitivity_constraints
                or redact_sensitive_values(record.model_dump(mode="json"))
                != record.model_dump(mode="json")
            ):
                continue
            if record.status not in ("ACTIVE", "CONFLICTED"):
                continue
            if (
                not record.source.strip()
                or record.content is None
                or (isinstance(record.content, str) and not record.content.strip())
                or (isinstance(record.content, (list, dict)) and not record.content)
                or not record.created_at <= record.updated_at <= now
                or (authority.expires_at is not None and authority.expires_at <= now)
                or (record.retention == "TEMPORARY" and authority.expires_at is None)
                or (record.retention == "ACTIVE" and authority.task_id != request.task_id)
                or (authority.task_id is not None and authority.task_id != request.task_id)
                or validation.verified_at is None
                or not record.updated_at <= validation.verified_at <= now
                or (
                    request.confidence_requirement is not None
                    and (
                        authority.confidence is None
                        or authority.confidence < request.confidence_requirement
                    )
                )
                or (
                    freshness.max_age_seconds is not None
                    and (now - validation.verified_at).total_seconds() > freshness.max_age_seconds
                )
                or (
                    freshness.verified_after is not None
                    and validation.verified_at < freshness.verified_after
                )
            ):
                continue
            words = set(
                re.findall(r"\w+", json.dumps(record.content, ensure_ascii=False).casefold())
            )
            score = len(tokens & words)
            if not score:
                continue
            if (
                record.status == "CONFLICTED"
                or validation.status == "CONFLICTED"
                or validation.conflict_refs
            ):
                conflicts.append({"memory_id": record.memory_id, "reason": "UNRESOLVED_CONFLICT"})
                continue
            if validation.status != "PASS":
                continue
            ranked.append((score, record))
        ranked.sort(key=lambda pair: (-pair[0], -pair[1].updated_at.timestamp(), pair[1].memory_id))
        selected = []
        seen = set()
        for _, record in ranked:
            # Only exact duplicates; do not collapse different provenance or classifications.
            key = json.dumps(
                [
                    record.content,
                    record.source,
                    record.memory_type,
                    record.retention,
                    record.scope,
                    record.sensitivity,
                    record.evidence_refs,
                    record.decision_refs,
                ],
                sort_keys=True,
            )
            if key not in seen:
                seen.add(key)
                selected.append(record)
            if len(selected) == request.max_results:
                break
        warnings = [
            LIMITATION,
            "Only eligible, explicitly shared records are returned; exclusions are not disclosed",
        ]
        if conflicts:
            warnings.append("Conflicted records excluded; human resolution required")
        return self._result(
            request, "SUCCESS" if selected else "EMPTY", selected, conflicts, warnings, now
        )

    def _result(self, request, status, records, conflicts, warnings, now):
        event = AuditEventBuilder(clock=lambda: now).build(
            task_id=request.task_id,
            event_type="MEMORY_RETRIEVAL_COMPLETED",
            actor=request.requester,
            component="MEMORY_RETRIEVAL",
            action="RETRIEVE_MEMORY",
            target=self._repository.repository_id,
            input_refs=[request.request_id],
            output_refs=[record.memory_id for record in records],
            result={
                "status": status,
                "returned_count": len(records),
                "persisted_memory": False,
                "execution_authority": "NONE",
            },
        )
        audit = self._writer.write(event)
        return MemoryRetrievalResult(
            contract_version="0.1",
            request_id=request.request_id,
            task_id=request.task_id,
            status=status,
            records=records,
            ranking_metadata={
                "method": "LEXICAL_THEN_UPDATED_AT_THEN_ID",
                "rank_is_authority": False,
            },
            conflicts=conflicts,
            warnings=warnings,
            audit_reference=audit.event_id,
        )
