"""Fixed Stage 3 operation policies; no environment override grants execution."""

from dataclasses import dataclass
from types import MappingProxyType
from typing import Literal

from robert.contracts.base import RiskLevel
from robert.governance.inputs import Operation

EXECUTION_AUTHORITY: Literal["NONE"] = "NONE"
AUTONOMY_LEVEL = 0


@dataclass(frozen=True)
class OperationPolicy:
    risk_floor: RiskLevel
    approval_required: bool = False
    execution_required: bool = False


OPERATION_POLICIES = MappingProxyType(
    {
        Operation.READ_DOCUMENT: OperationPolicy(RiskLevel.INFORMATIONAL),
        Operation.PREPARE_DRAFT: OperationPolicy(RiskLevel.MEDIUM),
        Operation.UPDATE_DOCUMENT: OperationPolicy(RiskLevel.HIGH, approval_required=True),
        Operation.DELETE_RESOURCE: OperationPolicy(RiskLevel.CRITICAL, True, True),
        Operation.EXTERNAL_ACTION: OperationPolicy(RiskLevel.HIGH, True, True),
        Operation.CONNECT_TOOL: OperationPolicy(RiskLevel.HIGH, True, True),
        Operation.RUN_CODE: OperationPolicy(RiskLevel.HIGH, True, True),
        Operation.ACTIVATE_AGENT: OperationPolicy(RiskLevel.HIGH, True, True),
        Operation.AUTOMATE: OperationPolicy(RiskLevel.HIGH, True, True),
        Operation.CHANGE_PHASE: OperationPolicy(RiskLevel.HIGH, True, True),
    }
)
