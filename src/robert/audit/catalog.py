"""Approved error and blocking taxonomy from the Stage 2 source specification."""

from dataclasses import dataclass
from enum import IntEnum

from robert.contracts.base import RiskLevel


class ErrorAndBlockingEvent(IntEnum):
    WARNING = 1
    CONFIRMATION_REQUIRED = 2
    FORMAL_APPROVAL_REQUIRED = 3
    MANDATORY_PAUSE = 4
    AUTOMATIC_BLOCK = 5
    USER_REQUESTED_BLOCK = 6
    PROHIBITED_ACTION = 7
    FUTURE_CAPABILITY_UNAVAILABLE = 8
    MISSING_INFORMATION = 9
    DOCUMENT_CONTRADICTION = 10
    CRITICAL_RISK = 11
    OUT_OF_SCOPE = 12
    SANDBOX_REQUIRED = 13
    SANDBOX_LIMIT_EXCEEDED = 14
    UNAUTHORIZED_EXECUTION = 15
    UNAUTHORIZED_CONNECTION = 16
    UNAUTHORIZED_AUTOMATION = 17
    UNAUTHORIZED_AGENT = 18
    SENSITIVE_DATA_DETECTED = 19
    INCORRECT_PHASE = 20


@dataclass(frozen=True, slots=True)
class ErrorAndBlockingEventDefinition:
    event: ErrorAndBlockingEvent
    display_name: str
    default_risk: RiskLevel | None
    blocks_action: bool
    parent_event: ErrorAndBlockingEvent | None = None

    @property
    def code(self) -> str:
        return f"ROBERT-EVENT-{self.event.value:02d}"

    @property
    def severity(self) -> str:
        return self.default_risk.name if self.default_risk is not None else "CONTROL_ACTION"


def _definition(
    event: ErrorAndBlockingEvent,
    display_name: str,
    default_risk: RiskLevel | None,
    *,
    blocks_action: bool,
    parent_event: ErrorAndBlockingEvent | None = None,
) -> ErrorAndBlockingEventDefinition:
    return ErrorAndBlockingEventDefinition(
        event=event,
        display_name=display_name,
        default_risk=default_risk,
        blocks_action=blocks_action,
        parent_event=parent_event,
    )


_AUTOMATIC_BLOCK = ErrorAndBlockingEvent.AUTOMATIC_BLOCK

ERROR_AND_BLOCKING_EVENT_CATALOG = {
    ErrorAndBlockingEvent.WARNING: _definition(
        ErrorAndBlockingEvent.WARNING, "Advertencia", RiskLevel.MEDIUM, blocks_action=False
    ),
    ErrorAndBlockingEvent.CONFIRMATION_REQUIRED: _definition(
        ErrorAndBlockingEvent.CONFIRMATION_REQUIRED,
        "Confirmación requerida",
        RiskLevel.MEDIUM,
        blocks_action=False,
    ),
    ErrorAndBlockingEvent.FORMAL_APPROVAL_REQUIRED: _definition(
        ErrorAndBlockingEvent.FORMAL_APPROVAL_REQUIRED,
        "Aprobación formal requerida",
        RiskLevel.HIGH,
        blocks_action=True,
    ),
    ErrorAndBlockingEvent.MANDATORY_PAUSE: _definition(
        ErrorAndBlockingEvent.MANDATORY_PAUSE,
        "Pausa obligatoria",
        None,
        blocks_action=True,
    ),
    ErrorAndBlockingEvent.AUTOMATIC_BLOCK: _definition(
        ErrorAndBlockingEvent.AUTOMATIC_BLOCK,
        "Bloqueo automático",
        RiskLevel.CRITICAL,
        blocks_action=True,
    ),
    ErrorAndBlockingEvent.USER_REQUESTED_BLOCK: _definition(
        ErrorAndBlockingEvent.USER_REQUESTED_BLOCK,
        "Bloqueo manual solicitado",
        None,
        blocks_action=True,
    ),
    ErrorAndBlockingEvent.PROHIBITED_ACTION: _definition(
        ErrorAndBlockingEvent.PROHIBITED_ACTION,
        "Acción prohibida",
        RiskLevel.CRITICAL,
        blocks_action=True,
    ),
    ErrorAndBlockingEvent.FUTURE_CAPABILITY_UNAVAILABLE: _definition(
        ErrorAndBlockingEvent.FUTURE_CAPABILITY_UNAVAILABLE,
        "Capacidad futura no disponible",
        RiskLevel.MEDIUM,
        blocks_action=True,
    ),
    ErrorAndBlockingEvent.MISSING_INFORMATION: _definition(
        ErrorAndBlockingEvent.MISSING_INFORMATION,
        "Falta de información",
        RiskLevel.MEDIUM,
        blocks_action=True,
    ),
    ErrorAndBlockingEvent.DOCUMENT_CONTRADICTION: _definition(
        ErrorAndBlockingEvent.DOCUMENT_CONTRADICTION,
        "Contradicción documental",
        RiskLevel.HIGH,
        blocks_action=True,
    ),
    ErrorAndBlockingEvent.CRITICAL_RISK: _definition(
        ErrorAndBlockingEvent.CRITICAL_RISK,
        "Riesgo crítico",
        RiskLevel.CRITICAL,
        blocks_action=True,
    ),
    ErrorAndBlockingEvent.OUT_OF_SCOPE: _definition(
        ErrorAndBlockingEvent.OUT_OF_SCOPE,
        "Fuera de alcance",
        RiskLevel.HIGH,
        blocks_action=True,
    ),
    ErrorAndBlockingEvent.SANDBOX_REQUIRED: _definition(
        ErrorAndBlockingEvent.SANDBOX_REQUIRED,
        "Sandbox requerido",
        RiskLevel.HIGH,
        blocks_action=True,
    ),
    ErrorAndBlockingEvent.SANDBOX_LIMIT_EXCEEDED: _definition(
        ErrorAndBlockingEvent.SANDBOX_LIMIT_EXCEEDED,
        "Sandbox excedido",
        RiskLevel.CRITICAL,
        blocks_action=True,
    ),
    ErrorAndBlockingEvent.UNAUTHORIZED_EXECUTION: _definition(
        ErrorAndBlockingEvent.UNAUTHORIZED_EXECUTION,
        "Ejecución no autorizada",
        RiskLevel.CRITICAL,
        blocks_action=True,
        parent_event=_AUTOMATIC_BLOCK,
    ),
    ErrorAndBlockingEvent.UNAUTHORIZED_CONNECTION: _definition(
        ErrorAndBlockingEvent.UNAUTHORIZED_CONNECTION,
        "Conexión no autorizada",
        RiskLevel.CRITICAL,
        blocks_action=True,
        parent_event=_AUTOMATIC_BLOCK,
    ),
    ErrorAndBlockingEvent.UNAUTHORIZED_AUTOMATION: _definition(
        ErrorAndBlockingEvent.UNAUTHORIZED_AUTOMATION,
        "Automatización no autorizada",
        RiskLevel.CRITICAL,
        blocks_action=True,
        parent_event=_AUTOMATIC_BLOCK,
    ),
    ErrorAndBlockingEvent.UNAUTHORIZED_AGENT: _definition(
        ErrorAndBlockingEvent.UNAUTHORIZED_AGENT,
        "Agente no autorizado",
        RiskLevel.CRITICAL,
        blocks_action=True,
        parent_event=_AUTOMATIC_BLOCK,
    ),
    ErrorAndBlockingEvent.SENSITIVE_DATA_DETECTED: _definition(
        ErrorAndBlockingEvent.SENSITIVE_DATA_DETECTED,
        "Dato sensible detectado",
        RiskLevel.CRITICAL,
        blocks_action=True,
        parent_event=_AUTOMATIC_BLOCK,
    ),
    ErrorAndBlockingEvent.INCORRECT_PHASE: _definition(
        ErrorAndBlockingEvent.INCORRECT_PHASE,
        "Fase incorrecta",
        RiskLevel.CRITICAL,
        blocks_action=True,
        parent_event=_AUTOMATIC_BLOCK,
    ),
}
