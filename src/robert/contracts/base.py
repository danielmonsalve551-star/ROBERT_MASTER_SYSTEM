"""Shared primitives and canonical enums for Robert contracts."""

from datetime import UTC, datetime
from enum import IntEnum, StrEnum
from typing import Annotated, Literal

from pydantic import AfterValidator, AwareDatetime, BaseModel, ConfigDict, Field, JsonValue

ContractVersion = Literal["0.1"]
Identifier = Annotated[str, Field(min_length=1, pattern=r"^[A-Za-z0-9][A-Za-z0-9._:-]*$")]
NonEmptyString = Annotated[str, Field(min_length=1)]
JsonObject = dict[str, JsonValue]


def _normalize_to_utc(value: datetime) -> datetime:
    """Normalize aware timestamps to UTC and reject ambiguous naive values."""

    if value.tzinfo is None or value.utcoffset() is None:
        raise ValueError("timestamp must include timezone information")
    return value.astimezone(UTC)


UtcDateTime = Annotated[datetime, AwareDatetime(), AfterValidator(_normalize_to_utc)]


class CanonicalContract(BaseModel):
    """Strict immutable base for every canonical Stage 1 contract."""

    model_config = ConfigDict(extra="forbid", frozen=True, validate_default=True)

    contract_version: ContractVersion


class ContractName(StrEnum):
    CONTRACT_ENVELOPE = "CONTRACT_ENVELOPE"
    TASK = "TASK"
    REQUEST_CONTEXT = "REQUEST_CONTEXT"
    ORCHESTRATOR_REQUEST = "ORCHESTRATOR_REQUEST"
    ORCHESTRATOR_RESULT = "ORCHESTRATOR_RESULT"
    ROUTE = "ROUTE"
    AGENT_REQUEST = "AGENT_REQUEST"
    AGENT_RESULT = "AGENT_RESULT"
    SKILL_INVOCATION = "SKILL_INVOCATION"
    SKILL_RESULT = "SKILL_RESULT"
    MODEL_REQUEST = "MODEL_REQUEST"
    MODEL_RESPONSE = "MODEL_RESPONSE"
    TOOL_REQUEST = "TOOL_REQUEST"
    TOOL_RESULT = "TOOL_RESULT"
    MEMORY_CANDIDATE = "MEMORY_CANDIDATE"
    MEMORY_RECORD = "MEMORY_RECORD"
    MEMORY_RETRIEVAL_REQUEST = "MEMORY_RETRIEVAL_REQUEST"
    MEMORY_RETRIEVAL_RESULT = "MEMORY_RETRIEVAL_RESULT"
    VALIDATION_REQUEST = "VALIDATION_REQUEST"
    VALIDATION_RESULT = "VALIDATION_RESULT"
    PERMISSION_CHECK = "PERMISSION_CHECK"
    SCOPE_CHECK = "SCOPE_CHECK"
    RISK_ASSESSMENT = "RISK_ASSESSMENT"
    APPROVAL_REQUEST = "APPROVAL_REQUEST"
    APPROVAL_RESULT = "APPROVAL_RESULT"
    ERROR = "ERROR"
    BLOCK = "BLOCK"
    AUDIT_EVENT = "AUDIT_EVENT"
    EVIDENCE_REF = "EVIDENCE_REF"


class TaskStatus(StrEnum):
    CREATED = "CREATED"
    NORMALIZED = "NORMALIZED"
    ROUTED = "ROUTED"
    IN_PROGRESS = "IN_PROGRESS"
    WAITING_INPUT = "WAITING_INPUT"
    WAITING_APPROVAL = "WAITING_APPROVAL"
    WAITING_TOOL = "WAITING_TOOL"
    WAITING_VALIDATION = "WAITING_VALIDATION"
    BLOCKED = "BLOCKED"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"
    CANCELLED = "CANCELLED"


class MemoryType(StrEnum):
    CORE = "CORE"
    SEMANTIC = "SEMANTIC"
    EPISODIC = "EPISODIC"
    DECISIONAL = "DECISIONAL"
    PROCEDURAL = "PROCEDURAL"


class Retention(StrEnum):
    ACTIVE = "ACTIVE"
    TEMPORARY = "TEMPORARY"
    PERSISTENT = "PERSISTENT"


class ValidationType(StrEnum):
    RULE = "RULE"
    CANONICAL = "CANONICAL"
    STRUCTURE = "STRUCTURE"
    COMPLETENESS = "COMPLETENESS"
    CONSISTENCY = "CONSISTENCY"
    EVIDENCE = "EVIDENCE"
    SOURCE = "SOURCE"
    SECURITY = "SECURITY"
    SCOPE = "SCOPE"
    PERMISSION = "PERMISSION"
    MEMORY = "MEMORY"
    MODEL_OUTPUT = "MODEL_OUTPUT"


class ReviewerRole(StrEnum):
    RULE_SYSTEM = "RULE_SYSTEM"
    AGENT = "AGENT"
    MODEL = "MODEL"
    USER = "USER"
    AUTHORIZED_ROBERT_FUNCTION = "AUTHORIZED_ROBERT_FUNCTION"


class ValidationStatus(StrEnum):
    PASS = "PASS"
    PASS_WITH_WARNINGS = "PASS_WITH_WARNINGS"
    FAIL = "FAIL"
    INCONCLUSIVE = "INCONCLUSIVE"
    NOT_APPLICABLE = "NOT_APPLICABLE"


class PermissionStatus(StrEnum):
    ALLOWED = "ALLOWED"
    DENIED = "DENIED"
    NOT_FOUND = "NOT_FOUND"
    EXPIRED = "EXPIRED"
    CONDITIONAL = "CONDITIONAL"


class ScopeStatus(StrEnum):
    WITHIN_SCOPE = "WITHIN_SCOPE"
    OUT_OF_SCOPE = "OUT_OF_SCOPE"
    PARTIAL = "PARTIAL"
    UNKNOWN = "UNKNOWN"


class RiskLevel(IntEnum):
    INFORMATIONAL = 0
    LOW = 1
    MEDIUM = 2
    HIGH = 3
    CRITICAL = 4


class ApprovalStatus(StrEnum):
    PENDING = "PENDING"
    APPROVED = "APPROVED"
    REJECTED = "REJECTED"
    EXPIRED = "EXPIRED"
    REVOKED = "REVOKED"
    NOT_REQUIRED = "NOT_REQUIRED"
