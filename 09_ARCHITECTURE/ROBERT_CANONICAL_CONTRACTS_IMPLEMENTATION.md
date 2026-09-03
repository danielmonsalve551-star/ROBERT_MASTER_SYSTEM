# ROBERT_CANONICAL_CONTRACTS_IMPLEMENTATION

**Versión:** 0.1
**Estado:** IMPLEMENTED / VERIFIED
**Fecha:** 01/09/2026
**Decisión:** #043
**Cambio:** #069
**Build Stage:** 1 — CANONICAL CONTRACTS

---

# 1. Fuente técnica única

```text
src/robert/contracts
=
SINGLE TECHNICAL CONTRACT SOURCE
```

Los JSON Schemas en `schemas/contracts` son outputs generados y no fuentes paralelas.

---

# 2. Decisiones de implementación

| Tema | Decisión |
|---|---|
| Contract source | Modelos Pydantic v2 |
| Schema output | JSON Schema Draft 2020-12 |
| Unknown fields | Strict rejection mediante `extra="forbid"` |
| Contract version | Campo obligatorio `contract_version="0.1"` |
| Mutation | `frozen=True` impide reasignar campos, no mutar listas/dicts internos. Aclaración de CAMBIO #071: copiar y revalidar en límites de confianza |
| IDs | Strings estables, no vacíos y con patrón controlado |
| Timestamps | Obligatoriamente timezone-aware y normalizados a UTC |
| Optionality | Campos ausentes se rechazan; campos nullable deben estar presentes salvo defaults canónicos explícitos |
| Ownership | Módulos separados por dominio |
| Registry | Un registro técnico único con nombre, modelo, owner y schema path |

---

# 3. Contratos implementados

```text
ContractEnvelope
Task
RequestContext
OrchestratorRequest
OrchestratorResult
Route
AgentRequest
AgentResult
SkillInvocation
SkillResult
ModelRequest
ModelResponse
ToolRequest
ToolResult
MemoryCandidate
MemoryRecord
MemoryRetrievalRequest
MemoryRetrievalResult
ValidationRequest
ValidationResult
PermissionCheck
ScopeCheck
RiskAssessment
ApprovalRequest
ApprovalResult
Error
Block
AuditEvent
EvidenceRef
```

Total:

```text
29 CANONICAL CONTRACTS
29 GENERATED JSON SCHEMAS
```

---

# 4. Compatibilidad especializada preservada

Se verifican explícitamente:

```text
ToolResult.confidence_if_applicable

MemoryRetrievalRequest.requester
MemoryRetrievalRequest.scope
MemoryRetrievalRequest.freshness_requirement
MemoryRetrievalRequest.confidence_requirement
MemoryRetrievalRequest.sensitivity_constraints

ValidationResult.requester
ValidationResult.confidence
ValidationResult.limitations
ValidationResult.sources
ValidationResult.recommended_next_step
```

---

# 5. Resultado de verificación

```text
CONTRACT_COUNT: 29
SCHEMA_COUNT: 29
PARSE: PASS
VALIDATE: PASS
SERIALIZE: PASS
REJECT INVALID INPUT: PASS
SPECIALIZED COMPATIBILITY: PASS
RUFF CHECK: PASS
RUFF FORMAT CHECK: PASS
PYTEST: 100 PASSED
```

---

# 6. Límite de autorización

```text
STAGE_0: COMPLETE
STAGE_1: COMPLETE
AUTHORIZED_BUILD_BOUNDARY: STAGE 1
STAGE_2: NOT AUTHORIZED
REAL_TOOL_EXECUTION: DISABLED
AUTONOMY_LEVEL: 0
EXECUTION_AUTHORITY: NONE
```

Los contratos representan datos. No ejecutan routing, aprobación, memoria, Tools ni acciones externas.
