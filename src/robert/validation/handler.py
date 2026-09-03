"""Canonical ValidationRequest → deterministic checks → audited ValidationResult."""

import json
from collections.abc import Callable
from datetime import UTC, datetime

from pydantic import ValidationError

from robert.audit import AuditEventBuilder, AuditWriter
from robert.contracts.base import ReviewerRole, ValidationStatus, ValidationType
from robert.contracts.validation import ValidationRequest, ValidationResult
from robert.governance.inputs import GovernanceRequest, PermissionGrant, SecurityContext
from robert.validation.context_validator import validate_context
from robert.validation.contract_validator import validate_contract
from robert.validation.findings import CheckFinding
from robert.validation.inputs import ContractExpectation, ValidationCriterion, ValidationTarget
from robert.validation.rule_validator import validate_rule
from robert.validation.structure_validator import validate_completeness, validate_structure

_SUPPORTED = frozenset(
    {
        ValidationType.RULE,
        ValidationType.CANONICAL,
        ValidationType.STRUCTURE,
        ValidationType.COMPLETENESS,
        ValidationType.CONSISTENCY,
        ValidationType.SECURITY,
        ValidationType.SCOPE,
        ValidationType.PERMISSION,
    }
)
_GUARDS = frozenset({ValidationType.SECURITY, ValidationType.SCOPE, ValidationType.PERMISSION})


def _snapshot(value):
    # Reject non-finite JSON and detach nested state without converting NaN into null.
    return type(value).model_validate_json(
        json.dumps(value.model_dump(mode="json"), allow_nan=False)
    )


def _unknown(identifier, message):
    return CheckFinding(identifier, "REQUEST", "UNKNOWN", message)


class ValidationHandler:
    """Internal rule-system reviewer. Does not invoke models, grant rights or execute targets."""

    def __init__(self, writer: AuditWriter, *, clock: Callable[[], datetime] | None = None):
        self._writer = writer
        self._clock = clock or (lambda: datetime.now(UTC))

    def validate(
        self,
        request: ValidationRequest,
        target: ValidationTarget,
        *,
        governance: GovernanceRequest | None = None,
        grant: PermissionGrant | None = None,
        security: SecurityContext | None = None,
    ) -> ValidationResult:
        request, target = _snapshot(request), _snapshot(target)
        governance = _snapshot(governance) if governance else None
        grant = _snapshot(grant) if grant else None
        security = _snapshot(security) if security else None
        now = self._clock()
        if now.tzinfo is None or now.utcoffset() is None:
            raise ValueError("validation clock must be timezone-aware")
        findings = []
        if (request.task_id, request.target_ref, request.target_type) != (
            target.task_id,
            target.target_ref,
            target.target_type,
        ) or ("task_id" in target.payload and target.payload["task_id"] != request.task_id):
            findings.append(
                CheckFinding(
                    "binding:target",
                    "CANONICAL",
                    "FAIL",
                    "Validation request and target binding mismatch",
                )
            )
        else:
            findings.append(
                CheckFinding("binding:target", "CANONICAL", "PASS", "Target binding matches")
            )
        if not request.validation_types or len(set(request.validation_types)) != len(
            request.validation_types
        ):
            findings.append(
                _unknown("request:types", "Nonempty, unique validation types are required")
            )
        if request.reviewer_roles != [ReviewerRole.RULE_SYSTEM]:
            findings.append(
                _unknown("request:reviewers", "Only a single RULE_SYSTEM reviewer is implemented")
            )
        if request.blocking_policy not in ({}, {"fail_closed": True}):
            findings.append(_unknown("request:policy", "Requested blocking policy is unsupported"))
        for field in ("risk_context", "permission_context", "scope_context"):
            if getattr(request, field):
                findings.append(
                    _unknown(
                        f"request:{field}",
                        "Serialized context is not authority; use the trusted adapter inputs",
                    )
                )
        expected = None
        if request.expected_contract:
            try:
                expected = ContractExpectation.model_validate(request.expected_contract)
            except ValidationError:
                findings.append(
                    _unknown("request:contract", "Unknown contract, version or expectation fields")
                )
            else:
                if expected.name.value != request.target_type:
                    findings.append(
                        CheckFinding(
                            "request:contract_type",
                            "CANONICAL",
                            "FAIL",
                            "Contract name does not match target type",
                        )
                    )
        criteria = self._criteria(request, findings)
        for kind in request.validation_types:
            if kind not in _SUPPORTED:
                findings.append(
                    CheckFinding(
                        f"type:{kind.value}",
                        kind.value,
                        "UNKNOWN",
                        "Validation capability not implemented",
                    )
                )
                continue
            before = len(findings)
            if kind == ValidationType.CANONICAL:
                if expected:
                    findings.append(validate_contract(target.payload, expected))
                else:
                    findings.append(
                        CheckFinding(
                            "canonical:contract",
                            kind.value,
                            "UNKNOWN",
                            "Registered contract expectation required",
                        )
                    )
            elif expected and kind == ValidationType.STRUCTURE:
                findings.append(validate_structure(target.payload, expected))
            elif expected and kind == ValidationType.COMPLETENESS:
                findings.append(validate_completeness(target.payload, expected))
            elif kind in _GUARDS:
                findings.append(
                    validate_context(
                        kind,
                        request,
                        target,
                        governance=governance,
                        grant=grant,
                        security=security,
                        now=now,
                    )
                )
            for criterion, mandatory in criteria:
                if criterion.validation_type == kind:
                    findings.append(
                        validate_rule(
                            target.payload, criterion, force_required=mandatory or kind in _GUARDS
                        )
                    )
            if len(findings) == before:
                findings.append(
                    CheckFinding(
                        f"type:{kind.value}",
                        kind.value,
                        "UNKNOWN",
                        "No concrete criteria supplied for this validation type",
                    )
                )
        self._reference_requirements(request, target, findings)
        return self._result(request, target, findings, now)

    @staticmethod
    def _criteria(request, findings):
        parsed = []
        seen = set()
        for field in ("criteria", "constraints", "canonical_requirements", "security_requirements"):
            for index, value in enumerate(getattr(request, field)):
                try:
                    criterion = ValidationCriterion.model_validate(value)
                except (ValidationError, TypeError):
                    findings.append(
                        _unknown(f"request:{field}:{index}", "Unrecognized declarative criterion")
                    )
                    continue
                if criterion.criterion_id in seen:
                    findings.append(
                        _unknown(f"request:{field}:{index}", "Duplicate criterion identity")
                    )
                    continue
                seen.add(criterion.criterion_id)
                if criterion.validation_type not in request.validation_types:
                    findings.append(
                        _unknown(f"request:{field}:{index}", "Criterion type was not requested")
                    )
                    continue
                required_type = {
                    "canonical_requirements": ValidationType.CANONICAL,
                    "security_requirements": ValidationType.SECURITY,
                }.get(field)
                if required_type and criterion.validation_type != required_type:
                    findings.append(
                        _unknown(
                            f"request:{field}:{index}",
                            "Requirement is assigned to the wrong validation type",
                        )
                    )
                    continue
                parsed.append((criterion, field != "criteria"))
        return parsed

    @staticmethod
    def _reference_requirements(request, target, findings):
        for field, provided in (
            ("evidence_requirements", target.evidence),
            ("source_requirements", target.sources),
        ):
            identifiers = {reference.ref_id for reference in provided}
            for index, required in enumerate(getattr(request, field)):
                present = isinstance(required, str) and bool(required) and required in identifiers
                findings.append(
                    CheckFinding(
                        f"reference:{field}:{index}",
                        "COMPLETENESS",
                        "PASS" if present else "UNKNOWN",
                        "Required reference supplied (content not verified)"
                        if present
                        else "Required reference missing or requirement format unsupported",
                    )
                )

    def _result(self, request, target, findings, now):
        failures = any(item.required and item.status == "FAIL" for item in findings)
        unknowns = any(item.required and item.status == "UNKNOWN" for item in findings)
        warnings = any(not item.required and item.status != "PASS" for item in findings)
        if failures:
            status = ValidationStatus.FAIL
        elif unknowns:
            status = ValidationStatus.INCONCLUSIVE
        elif warnings:
            status = ValidationStatus.PASS_WITH_WARNINGS
        else:
            status = ValidationStatus.PASS
        blocking = failures or unknowns
        next_step = (
            "Resolve failed checks or unavailable requirements, then request validation again"
            if blocking
            else "Return to the caller; obtain any required approval separately"
        )
        limitations = [
            "Deterministic checks only; validation is not truth, approval or execution authority",
            "Trusted adapters supply security/governance inputs; no authentication is provided",
            "Evidence/source references are supplied, not independently fetched or verified",
            "Confidence is uncalibrated and intentionally null",
        ]
        event = AuditEventBuilder(clock=lambda: now).build(
            task_id=request.task_id,
            event_type="VALIDATION_COMPLETED",
            actor=request.requester,
            component="VALIDATION_CORE",
            action="VALIDATE_TARGET",
            target=request.target_ref,
            input_refs=[request.validation_id, request.target_ref],
            output_refs=[request.validation_id],
            validation_state={"status": status.value, "blocking": blocking},
            result={
                "status": status.value,
                "blocking": blocking,
                "execution_authority": "NONE",
                "approved": False,
                "executed": False,
            },
            metadata={
                "check_count": len(findings),
                "failed_checks": sum(item.status == "FAIL" for item in findings),
                "unknown_checks": sum(item.status == "UNKNOWN" for item in findings),
            },
        )
        result = ValidationResult(
            contract_version="0.1",
            validation_id=request.validation_id,
            task_id=request.task_id,
            requester=request.requester,
            target_ref=request.target_ref,
            status=status,
            checks=[item.as_check() for item in findings],
            issues=[issue for item in findings if (issue := item.as_issue()) is not None],
            severity="BLOCKING" if blocking else "OPTIONAL",
            evidence=[item.model_dump(mode="json") for item in target.evidence],
            sources=[item.model_dump(mode="json") for item in target.sources],
            confidence=None,
            limitations=limitations,
            recommendations=[next_step],
            recommended_next_step=next_step,
            blocking=blocking,
            reviewer_refs=["validator:rule_system"],
            timestamp=now,
            audit_reference=event.event_id,
        )
        self._writer.write(event)
        return result
