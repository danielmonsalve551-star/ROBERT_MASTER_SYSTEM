"""Single technical registry for every canonical Stage 1 contract."""

from dataclasses import dataclass

from robert.contracts.agent import AgentRequest, AgentResult
from robert.contracts.audit import AuditEvent, EvidenceRef
from robert.contracts.base import CanonicalContract, ContractName
from robert.contracts.envelope import ContractEnvelope
from robert.contracts.errors import Block, Error
from robert.contracts.governance import (
    ApprovalRequest,
    ApprovalResult,
    PermissionCheck,
    RiskAssessment,
    ScopeCheck,
)
from robert.contracts.memory import (
    MemoryCandidate,
    MemoryRecord,
    MemoryRetrievalRequest,
    MemoryRetrievalResult,
)
from robert.contracts.model import ModelRequest, ModelResponse
from robert.contracts.orchestration import OrchestratorRequest, OrchestratorResult, Route
from robert.contracts.skill import SkillInvocation, SkillResult
from robert.contracts.task import RequestContext, Task
from robert.contracts.tool import ToolRequest, ToolResult
from robert.contracts.validation import ValidationRequest, ValidationResult

ContractType = type[CanonicalContract]


@dataclass(frozen=True, slots=True)
class ContractRegistration:
    """Describes ownership and schema output for one canonical contract."""

    name: ContractName
    model: ContractType
    owner: str

    @property
    def schema_path(self) -> str:
        filename = f"{self.name.value.lower()}.schema.json"
        return f"schemas/contracts/{self.owner}/{filename}"


CONTRACT_REGISTRY: tuple[ContractRegistration, ...] = (
    ContractRegistration(ContractName.CONTRACT_ENVELOPE, ContractEnvelope, "transport"),
    ContractRegistration(ContractName.TASK, Task, "task"),
    ContractRegistration(ContractName.REQUEST_CONTEXT, RequestContext, "task"),
    ContractRegistration(ContractName.ORCHESTRATOR_REQUEST, OrchestratorRequest, "orchestration"),
    ContractRegistration(ContractName.ORCHESTRATOR_RESULT, OrchestratorResult, "orchestration"),
    ContractRegistration(ContractName.ROUTE, Route, "orchestration"),
    ContractRegistration(ContractName.AGENT_REQUEST, AgentRequest, "agent"),
    ContractRegistration(ContractName.AGENT_RESULT, AgentResult, "agent"),
    ContractRegistration(ContractName.SKILL_INVOCATION, SkillInvocation, "skill"),
    ContractRegistration(ContractName.SKILL_RESULT, SkillResult, "skill"),
    ContractRegistration(ContractName.MODEL_REQUEST, ModelRequest, "model"),
    ContractRegistration(ContractName.MODEL_RESPONSE, ModelResponse, "model"),
    ContractRegistration(ContractName.TOOL_REQUEST, ToolRequest, "tool"),
    ContractRegistration(ContractName.TOOL_RESULT, ToolResult, "tool"),
    ContractRegistration(ContractName.MEMORY_CANDIDATE, MemoryCandidate, "memory"),
    ContractRegistration(ContractName.MEMORY_RECORD, MemoryRecord, "memory"),
    ContractRegistration(
        ContractName.MEMORY_RETRIEVAL_REQUEST,
        MemoryRetrievalRequest,
        "memory",
    ),
    ContractRegistration(
        ContractName.MEMORY_RETRIEVAL_RESULT,
        MemoryRetrievalResult,
        "memory",
    ),
    ContractRegistration(ContractName.VALIDATION_REQUEST, ValidationRequest, "validation"),
    ContractRegistration(ContractName.VALIDATION_RESULT, ValidationResult, "validation"),
    ContractRegistration(ContractName.PERMISSION_CHECK, PermissionCheck, "governance"),
    ContractRegistration(ContractName.SCOPE_CHECK, ScopeCheck, "governance"),
    ContractRegistration(ContractName.RISK_ASSESSMENT, RiskAssessment, "governance"),
    ContractRegistration(ContractName.APPROVAL_REQUEST, ApprovalRequest, "governance"),
    ContractRegistration(ContractName.APPROVAL_RESULT, ApprovalResult, "governance"),
    ContractRegistration(ContractName.ERROR, Error, "error"),
    ContractRegistration(ContractName.BLOCK, Block, "error"),
    ContractRegistration(ContractName.AUDIT_EVENT, AuditEvent, "audit"),
    ContractRegistration(ContractName.EVIDENCE_REF, EvidenceRef, "audit"),
)

CONTRACTS_BY_NAME: dict[ContractName, ContractType] = {
    registration.name: registration.model for registration in CONTRACT_REGISTRY
}
