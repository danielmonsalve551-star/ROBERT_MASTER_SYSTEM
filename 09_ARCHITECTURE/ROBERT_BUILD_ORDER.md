# ROBERT_BUILD_ORDER

**Versión:** 0.1
**Estado:** APROBADA — integrada arquitectónicamente
**Tipo:** Especificación de orden de construcción / Implementation Readiness
**Ubicación propuesta:** `09_ARCHITECTURE/ROBERT_BUILD_ORDER.md`
**Fase relacionada:** Fase 10 — Implementation Readiness
**Implementación:** STAGES 0–6 COMPLETE / STAGE 7 NOT AUTHORIZED
**Autonomy Level:** 0
**Execution Authority:** NONE

**Dependencias principales:**

* `ROBERT_CANONICAL_MODEL v0.2`
* `ROBERT_ORCHESTRATOR_SPEC v0.1`
* `ROBERT_AGENT_ARCHITECTURE v0.1`
* `ROBERT_SKILL_ARCHITECTURE v0.1`
* `ROBERT_MODEL_INTERFACE_SPEC v0.1`
* `ROBERT_MEMORY_ARCHITECTURE v0.1`
* `ROBERT_VALIDATION_ARCHITECTURE v0.1`
* `ROBERT_TOOL_ARCHITECTURE v0.1`
* `ROBERT_IMPLEMENTATION_CONTRACTS v0.1`
* `ROBERT_PHASE_10_EXIT_CRITERIA v0.1`
* `ROBERT_SECURITY_RULES`
* `ROBERT_TECHNICAL_PERMISSIONS_AND_SCOPES_SPEC`
* `ROBERT_TECHNICAL_ERROR_AND_BLOCKING_SPEC`
* `ROBERT_TECHNICAL_AUDIT_TRAIL_SPEC`
* `ROBERT_TECHNICAL_APPROVAL_AND_AUTHORIZATION_GATE_SPEC`
* `ROBERT_TECHNICAL_DATA_CONSISTENCY_AND_CONFLICT_RESOLUTION_SPEC`

---

# 1. Propósito

Este documento define el orden recomendado para construir la primera implementación técnica de Robert.

Su función es evitar:

```text
BUILD UI BEFORE CORE

BUILD AGENTS BEFORE CONTRACTS

BUILD TOOLS BEFORE PERMISSIONS

BUILD MEMORY BEFORE GOVERNANCE

BUILD ORCHESTRATOR BEFORE INTERFACES

ENABLE EXECUTION BEFORE SECURITY
```

---

# 2. Regla principal

```text
BUILD ORDER
≠
IMPLEMENTATION AUTHORIZATION
```

La aprobación de este documento únicamente define secuencia.

No autoriza comenzar a programar.

---

# 3. Principio de dependencia

El orden de construcción debe seguir:

```text
FOUNDATIONS
↓
GOVERNANCE
↓
CONTRACTS
↓
INTERFACES
↓
SPECIALIZED COMPONENTS
↓
ORCHESTRATION
↓
APPLICATION LAYER
↓
EXTERNAL EXECUTION
```

---

# 4. Principio de mínima autoridad

La implementación inicial debe comenzar con:

```text
AUTONOMY_LEVEL = 0
EXECUTION_AUTHORITY = NONE
```

y preservar esos valores hasta decisión formal posterior.

---

# 5. Initial Implementation ≠ Full Robert

La primera implementación no intenta construir todo Robert.

Se formaliza:

```text
INITIAL IMPLEMENTATION
⊂
FULL ROBERT
```

---

# 6. Objetivo del primer build

El primer build debe demostrar que Robert puede:

```text
RECEIVE TASK
VALIDATE CONTRACT
CREATE TRACE
CHECK GOVERNANCE
ROUTE CONCEPTUALLY
CALL APPROVED MODEL INTERFACE
RETURN STRUCTURED RESULT
VALIDATE RESULT
AUDIT FLOW
```

sin:

```text
REAL TOOL EXECUTION
AUTONOMOUS AGENTS
AUTOMATIC MEMORY WRITES
EXTERNAL SIDE EFFECTS
```

---

# 7. Build Stages

El build se divide en:

```text
STAGE 0 — TECHNICAL FOUNDATION

STAGE 1 — CANONICAL CONTRACTS

STAGE 2 — ERROR / AUDIT FOUNDATION

STAGE 3 — GOVERNANCE CORE

STAGE 4 — VALIDATION CORE

STAGE 5 — CONTEXT / MEMORY INTERFACES

STAGE 6 — MODEL INTERFACE

STAGE 7 — SKILL LAYER

STAGE 8 — AGENT LAYER

STAGE 9 — TOOL ABSTRACTION

STAGE 10 — ORCHESTRATOR

STAGE 11 — APPLICATION API

STAGE 12 — BASIC UI

STAGE 13 — SANDBOX INTEGRATION

STAGE 14 — EXTERNAL CAPABILITIES

STAGE 15 — AUTONOMY EVOLUTION
```

Stages 14 y 15 no forman parte de la primera autorización de implementación salvo decisión posterior.

---

# 8. Stage 0 — Technical Foundation

## Objetivo

Crear la estructura técnica mínima del proyecto.

Puede incluir:

```text
REPOSITORY STRUCTURE
PACKAGE MANAGEMENT
CONFIGURATION
ENVIRONMENT HANDLING
TEST FOUNDATION
LINTING
FORMATTING
CI BASICS
```

No debe contener todavía lógica autónoma.

---

# 9. Stage 0 — Technical Decisions Required

Antes de comenzar Stage 0 deberán resolverse como mínimo:

```text
PROGRAMMING LANGUAGE
PRIMARY FRAMEWORK
REPOSITORY STRUCTURE
CONTRACT REPRESENTATION
TEST FRAMEWORK
```

---

# 10. Stage 0 — Not Required Yet

No es necesario decidir todavía:

```text
PRODUCTION DATABASE
CLOUD PROVIDER
VECTOR DATABASE
MESSAGE BUS
FULL OBSERVABILITY STACK
PRODUCTION DEPLOYMENT
```

si no bloquean el núcleo.

---

# 11. Stage 0 Exit

```text
PROJECT BOOTS

TESTS CAN RUN

CONFIG CAN LOAD

CONTRACT PACKAGE CAN EXIST

NO BUSINESS LOGIC REQUIRED
```

---

# 12. Stage 1 — Canonical Contracts
**## Stage 1 Entry Criteria

Stage 1 solo puede comenzar cuando:

ROBERT_IMPLEMENTATION_CONTRACTS v0.1
=
APPROVED AND RECONCILED

EVIDENCE:

DECISIÓN #038
CAMBIO #063

La versión utilizada para implementación debe haber preservado
compatibilidad con:

ROBERT_MODEL_INTERFACE_SPEC v0.1
ROBERT_TOOL_ARCHITECTURE v0.1
ROBERT_MEMORY_ARCHITECTURE v0.1
ROBERT_VALIDATION_ARCHITECTURE v0.1

En particular deben estar reconciliados, como mínimo:

TOOL_RESULT
→ confidence_if_applicable

MEMORY_RETRIEVAL_REQUEST
→ requester
→ freshness_requirement
→ confidence_requirement
→ sensitivity_constraints

VALIDATION_REQUEST / VALIDATION_RESULT
→ requester
→ confidence
→ limitations
→ sources
→ recommended_next_step

Regla:

APPROVED IMPLEMENTATION CONTRACT
MUST MATCH
APPROVED SPECIALIZED ARCHITECTURE

Stage 1 no puede derivar schemas técnicos de una versión
no reconciliada o físicamente desactualizada.**
## Objetivo

Convertir:

```text
ROBERT_IMPLEMENTATION_CONTRACTS v0.1
```

en tipos/schemas técnicos.

---

# 13. Stage 1 — Contract Set

Implementar primero:

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
```

---

# 14. Stage 1 — Contract Source of Truth

Debe existir una sola fuente técnica de contratos.

Regla:

```text
ONE CONTRACT DEFINITION
→
MULTIPLE CONSUMERS
```

No:

```text
API TYPES
≠
ORCHESTRATOR TYPES
≠
AGENT TYPES
```

para el mismo objeto canónico.

---

# 15. Stage 1 — Contract Validation

Cada schema debe validar:

```text
REQUIRED FIELDS
ENUMS
FIELD TYPES
REFERENCES
VERSION
```

---

# 16. Stage 1 Exit

Todos los contratos mínimos deben:

```text
PARSE
VALIDATE
SERIALIZE
REJECT INVALID INPUT
```

---

# 17. Stage 2 — Error / Audit Foundation

Debe implementarse antes de lógica compleja.

Orden:

```text
ERROR MODEL
↓
BLOCK MODEL
↓
AUDIT EVENT MODEL
↓
AUDIT WRITER
```

---

# 18. Error Mapping

Los errores técnicos deben mapearse a:

```text
ROBERT_TECHNICAL_ERROR_AND_BLOCKING_SPEC
```

sin crear una taxonomía paralela.

---

# 19. Audit First

Toda operación crítica futura deberá poder emitir Audit Events desde el comienzo.

Regla:

```text
NO CRITICAL OPERATION
WITHOUT TRACEABILITY
```
# 19.1 Architectural Growth Check — Audit Writer

WHY NEEDED:
Persistir o emitir Audit Events utilizando el sistema
de trazabilidad ya aprobado.

EXISTING COMPONENT IT EXTENDS:
ROBERT_TECHNICAL_AUDIT_TRAIL_SPEC.

NEW AUTHORITY CREATED?:
NO.

NEW TECHNICAL MODEL CREATED?:
YES — componente técnico de implementación para escribir
Audit Events.

PHASE 10 COMPATIBLE?:
YES — como diseño de Build Order; no está implementado todavía.

APPROVAL REQUIRED?:
YES — como parte de ROBERT_BUILD_ORDER v0.1.

Se formaliza:

AUDIT WRITER
≠
AUDIT AUTHORITY

AUDIT WRITER
≠
ROUTING AUTHORITY

AUDIT WRITER
≠
EXECUTION AUTHORITY

AUDIT WRITER
≠
NEW AUDIT SYSTEM

Su única responsabilidad es registrar Audit Events
según el Audit Trail aprobado.
---

# 20. Audit Storage

La primera implementación puede utilizar almacenamiento simple.

Ejemplos posibles:

```text
LOCAL FILE
STRUCTURED JSON
LIGHTWEIGHT DATABASE
```

La tecnología exacta será una decisión técnica.

---

# 21. Stage 2 Exit

Debe poder demostrarse:

```text
VALID REQUEST
→ AUDIT EVENT

INVALID REQUEST
→ ERROR
→ AUDIT EVENT

BLOCKED REQUEST
→ BLOCK
→ AUDIT EVENT
```

---

# 22. Stage 3 — Governance Core

Implementar:

```text
PERMISSION CHECK
SCOPE CHECK
RISK ASSESSMENT
SECURITY CHECK
APPROVAL STATE
EXECUTION AUTHORITY CHECK
```

---

# 23. Governance Order

Orden interno:

```text
PERMISSION
↓
SCOPE
↓
RISK
↓
SECURITY
↓
APPROVAL
↓
EXECUTION AUTHORITY
```

cuando aplique.

---

# 24. Stage 3 — Execution Authority

La implementación inicial debe hard-codear conceptualmente:

```text
EXECUTION_AUTHORITY = NONE
```

hasta que exista decisión formal que lo cambie.

---

# 25. Governance Failure

Si un gate falla:

```text
DO NOT CONTINUE
```

Debe producir:

```text
BLOCK
+
AUDIT EVENT
```

---

# 26. Stage 3 Exit

Deben pasar tests como:

```text
NO PERMISSION → BLOCK

OUT OF SCOPE → BLOCK

CRITICAL SECURITY CONFLICT → BLOCK

APPROVAL REQUIRED BUT MISSING → BLOCK

EXECUTION_AUTHORITY NONE → NO EXTERNAL EXECUTION
```

---

# 27. Stage 4 — Validation Core

Implementar después de Contracts y Governance.

Componentes iniciales:

```text
VALIDATION REQUEST HANDLER
RULE VALIDATOR
STRUCTURE VALIDATOR
CONTRACT VALIDATOR
VALIDATION RESULT
```

---

# 28. Validation First Scope

La primera implementación no necesita todos los tipos de Validation automatizados.

Debe priorizar:

```text
RULE
CANONICAL
STRUCTURE
COMPLETENESS
CONSISTENCY
SECURITY
SCOPE
PERMISSION
```

---

# 29. Validation Boundary

El código debe preservar:

```text
VALIDATION PASS
≠
APPROVAL
```

y:

```text
VALIDATION PASS
≠
EXECUTION AUTHORITY
```

---

# 30. Stage 4 Exit

Un Validation Result debe poder transportar:

```text
passed_checks
failed_checks
warnings
conflicts
confidence
limitations
evidence
sources
recommended_next_step
```

---

# 31. Stage 5 — Context / Memory Interfaces

No comenzar por una Memory autónoma.

Primero implementar:

```text
CONTEXT ASSEMBLY
MEMORY CONTRACTS
MEMORY REPOSITORY INTERFACE
MEMORY RETRIEVAL INTERFACE
```

---

# 32. Memory Phase 1

La primera versión puede operar con:

```text
MANUAL / CONTROLLED MEMORY RECORDS
```

sin automatic Memory Write.

---

# 33. Memory Write Boundary

Debe preservarse:

```text
MODEL RESPONSE
→ MEMORY CANDIDATE
```

no:

```text
MODEL RESPONSE
→ MEMORY RECORD
```

---

# 34. Memory Retrieval

Debe poder respetar:

```text
requester
scope
memory_type
retention
freshness_requirement
confidence_requirement
sensitivity_constraints
```

---

# 35. Stage 5 Exit

Debe poder:

```text
CREATE MEMORY CANDIDATE
VALIDATE MEMORY CANDIDATE
READ AUTHORIZED MEMORY
RETURN MEMORY RETRIEVAL RESULT
```

sin automatic persistence si aún no está autorizada.

---

# 36. Stage 6 — Model Interface

Implementar la abstracción de Models antes de Agents.

Orden:

```text
MODEL REQUEST
↓
MODEL PROVIDER INTERFACE
↓
MODEL ADAPTER
↓
MODEL RESPONSE
```

---

# 37. First Model Provider

La primera implementación puede usar un solo proveedor.

Pero el Core no debe depender directamente de él.

Debe mantenerse:

```text
ROBERT
↓
MODEL INTERFACE
↓
PROVIDER ADAPTER
↓
PROVIDER
```

---

# 38. Model Output Boundary

Todo Model Response debe volver como dato estructurado.

No debe modificar estado directamente.

---

# 39. Tool Request Boundary

Si:

```text
tool_request_allowed = true
```

el Model únicamente puede producir:

```text
STRUCTURED TOOL REQUEST
```

No ejecución.

---

# 40. Stage 6 Exit

Debe poder:

```text
SEND MODEL REQUEST
RECEIVE MODEL RESPONSE
VALIDATE RESPONSE
AUDIT CALL
HANDLE PROVIDER ERROR
```

---

# 41. Stage 7 — Skill Layer

Skills se implementan antes de Agents porque Agents pueden depender de Skills.

Orden:

```text
SKILL MANIFEST
↓
SKILL REGISTRY
↓
SKILL INVOCATION
↓
SKILL RUNNER
↓
SKILL RESULT
```

---

# 42. Skill Registry

Registry únicamente describe Skills disponibles.

```text
SKILL REGISTRY
≠
ROUTING AUTHORITY
```

---

# 43. Skill Runner

Skill Runner ejecuta procedimientos internos autorizados.

No obtiene:

```text
TOOL AUTHORIZATION
EXECUTION AUTHORITY
ROUTING AUTHORITY
```

---
# 43.1 Architectural Growth Check — Skill Runner

WHY NEEDED:
Ejecutar procedimientos internos definidos mediante
Skill Invocation y producir Skill Result.

EXISTING COMPONENT IT EXTENDS:
ROBERT_SKILL_ARCHITECTURE v0.1.

NEW AUTHORITY CREATED?:
NO.

NEW TECHNICAL MODEL CREATED?:
YES — componente técnico de runtime para ejecutar
procedimientos de Skills.

PHASE 10 COMPATIBLE?:
YES — como diseño técnico futuro.

APPROVAL REQUIRED?:
YES — como parte de ROBERT_BUILD_ORDER v0.1.

Se formaliza:

SKILL RUNNER
≠
SKILL

SKILL RUNNER
≠
ROUTING AUTHORITY

SKILL RUNNER
≠
TOOL AUTHORIZATION

SKILL RUNNER
≠
EXECUTION AUTHORITY

El Skill Runner ejecuta únicamente el procedimiento
que recibe dentro del Scope y contratos autorizados.
# 44. Stage 7 Exit

Debe existir al menos:

```text
ONE SIMPLE SKILL
```

capaz de:

```text
RECEIVE VALID INPUT
PROCESS
RETURN SKILL RESULT
AUDIT
```

sin side effects externos.

---

# 45. Stage 8 — Agent Layer

Implementar después de Skills y Model Interface.

Orden:

```text
AGENT MANIFEST
↓
AGENT REGISTRY
↓
AGENT REQUEST
↓
AGENT RUNNER
↓
AGENT RESULT
```

---

# 46. Agent Registry

```text
AGENT REGISTRY
≠
AGENT ROUTER
```

El Orchestrator mantiene routing authority.

---

# 47. First Agents

La primera implementación no necesita todos los Agents.

Puede comenzar con uno o dos Agents del catálogo aprobado
de ROBERT_AGENT_ARCHITECTURE v0.1.

Candidatos recomendados para el primer build:

ROBERT_RESEARCHER
ROBERT_CRITIC

Ambos forman parte del catálogo arquitectónico aprobado
mediante:

DECISIÓN #032
CAMBIO #055
CAMBIO #056

Su selección aquí define únicamente una recomendación
de sequencing.

No implica implementación previa, activación ni
Execution Authority.

Se mantiene:

AUTONOMY_LEVEL = 0
EXECUTION_AUTHORITY = NONE
---

# 48. Agent Restrictions

Los Agents iniciales:

```text
MUST NOT
CALL TOOLS DIRECTLY

MUST NOT
WRITE MEMORY DIRECTLY

MUST NOT
ROUTE OTHER AGENTS

MUST NOT
CREATE PERMISSIONS
```

---
# 48.1 Architectural Growth Check — Agent Runner

WHY NEEDED:
Ejecutar técnicamente un Agent Request contra una
definición de Agent aprobada y devolver Agent Result.

EXISTING COMPONENT IT EXTENDS:
ROBERT_AGENT_ARCHITECTURE v0.1.

NEW AUTHORITY CREATED?:
NO.

NEW TECHNICAL MODEL CREATED?:
YES — componente técnico de runtime para hospedar
la ejecución controlada de Agents.

PHASE 10 COMPATIBLE?:
YES — como diseño de implementación futura.

APPROVAL REQUIRED?:
YES — como parte de ROBERT_BUILD_ORDER v0.1.

Se formaliza:

AGENT RUNNER
≠
AGENT

AGENT RUNNER
≠
ORCHESTRATOR

AGENT RUNNER
≠
ROUTING AUTHORITY

AGENT RUNNER
≠
PERMISSION AUTHORITY

AGENT RUNNER
≠
EXECUTION AUTHORITY

El Agent Runner ejecuta únicamente el Agent seleccionado
por el Orchestrator.

No puede seleccionar unilateralmente:

ANOTHER AGENT
MODEL
TOOL
SCOPE
PERMISSION
# 49. Stage 8 Exit

Debe demostrarse:

```text
ORCHESTRATOR OR TEST HARNESS
→ AGENT REQUEST
→ AGENT
→ SKILL / MODEL IF ALLOWED
→ AGENT RESULT
```

---

# 50. Stage 9 — Tool Abstraction

Implementar únicamente la arquitectura de Tool, no Tools externas reales.

Primero:

```text
TOOL MANIFEST
TOOL REGISTRY
TOOL REQUEST
TOOL RESULT
TOOL POLICY
TOOL INTERFACE
TOOL ADAPTER INTERFACE
```

---

# 51. No Real Tool Required

Stage 9 puede usar:

```text
FAKE TOOL
MOCK TOOL
SANDBOX TOOL
```

---

# 52. Tool Execution Boundary

Mantener:

```text
REAL TOOL EXECUTION = DISABLED
```

---

# 53. Stage 9 Exit

Debe poder simular:

```text
TOOL REQUEST
↓
TOOL RESOLUTION
↓
PERMISSION
↓
SCOPE
↓
RISK
↓
SECURITY
↓
APPROVAL
↓
EXECUTION AUTHORITY = NONE
↓
BLOCK / SIMULATION
```

---

# 54. Stage 10 — Orchestrator

El Orchestrator debe construirse después de tener disponibles las interfaces que coordina.

Implementar:

```text
INTENT ROUTING
CONTEXT RESOLUTION
MODULE ROUTING
AGENT ROUTING
SKILL RESOLUTION
MODEL ROUTING
TOOL RESOLUTION
MEMORY RESOLUTION
VALIDATION RESOLUTION
```

según alcance aprobado.

---

# 55. Orchestrator First Version

La primera versión debe priorizar routing determinista.

Preferencia:

```text
RULES / CONFIG
BEFORE
MODEL-DRIVEN ROUTING
```

cuando sea posible.

---

# 56. Orchestrator ≠ Agent

```text
ORCHESTRATOR
≠
GENERAL PURPOSE AGENT
```

---

# 57. Orchestrator ≠ Model

El Orchestrator puede usar un Model para análisis.

Pero:

```text
MODEL OUTPUT
≠
ROUTING AUTHORITY
```

---

# 58. Orchestrator State

Debe mantener:

```text
task_id
route
current_step
permission_state
scope_state
risk_state
approval_state
validation_state
```

mediante contratos explícitos.

---

# 59. Stage 10 Exit

Debe poder realizar end-to-end:

```text
USER INPUT
↓
TASK
↓
ORCHESTRATOR REQUEST
↓
ROUTING
↓
AGENT / SKILL / MODEL
↓
VALIDATION
↓
ORCHESTRATOR RESULT
↓
AUDIT
```

sin ejecución externa.

---

# 60. Stage 11 — Application API

Solo después del Core.

Debe exponer operaciones controladas como:

```text
CREATE TASK
GET TASK
PROCESS TASK
GET RESULT
GET AUDIT
```

según alcance técnico futuro.

---

# 61. API ≠ Core Architecture

La API es una capa de acceso.

No debe contener lógica canónica duplicada.

---

# 62. Stage 11 Exit

La aplicación debe poder invocar Robert mediante contratos estables.

---

# 63. Stage 12 — Basic UI

UI después del Core y API.

Primera UI puede incluir:

```text
INPUT
TASK STATUS
OUTPUT
VALIDATION
BLOCKS
APPROVAL REQUESTS
AUDIT SUMMARY
```

---

# 64. UI ≠ Authority

La UI puede mostrar o solicitar Approval.

No crea Authority.

---

# 65. UI State

Debe derivar de estados reales del sistema.

No mantener una state machine incompatible paralela.

---

# 66. Stage 12 Exit

Debe poder ejecutarse un flujo completo visible:

```text
USER
→ TASK
→ PROCESS
→ RESULT
```

con estado y errores visibles.

---

# 67. Stage 13 — Sandbox Integration

Antes de conexiones reales:

```text
SANDBOX
```

debe utilizar las mismas interfaces del Core.

---

# 68. Sandbox Goal

Probar:

```text
MODEL FAILURE
TOOL FAILURE
PERMISSION DENIAL
SCOPE DENIAL
VALIDATION FAILURE
MEMORY CANDIDATE
AGENT ERROR
ROUTING FALLBACK
```

---

# 69. Mock Over Production

Preferencia:

```text
MOCK FIRST
PRODUCTION LATER
```

---

# 70. Stage 13 Exit

Los tests críticos definidos en Phase 10 Exit Criteria deben poder ejecutarse técnicamente o mediante sandbox reproducible.

---

# 71. Stage 14 — External Capabilities

**FUERA DEL INITIAL BUILD por defecto.**

Puede incluir posteriormente:

```text
REAL MODEL PROVIDERS
GITHUB
GMAIL
CALENDAR
WEB
FILESYSTEM
DATABASES
CLOUD STORAGE
OTHER APIS
```

---

# 72. Stage 14 Requires Separate Authorization

Antes de conectar cada Tool real debe definirse:

```text
PERMISSIONS
SCOPES
AUTHENTICATION
CREDENTIAL HANDLING
SIDE EFFECT POLICY
AUDIT
ERROR HANDLING
APPROVAL REQUIREMENTS
```

---

# 73. Connection ≠ Authorization

```text
CONNECTED
≠
AUTHORIZED
```

---

# 74. Read Before Write

Preferencia de evolución:

```text
READ CAPABILITIES
BEFORE
WRITE CAPABILITIES
```

cuando sea posible.

---

# 75. Write Tools

Tools que generan side effects deben introducirse después de validar Read Tools.

---

# 76. Stage 15 — Autonomy Evolution

**FUERA DE FASE 10 Y FUERA DEL INITIAL BUILD.**

Puede considerar posteriormente:

```text
AUTOMATIC ROUTING
AUTOMATIC MEMORY
AUTONOMOUS AGENT LOOPS
AUTOMATIC TOOL USE
BACKGROUND AUTOMATIONS
```

solo mediante aprobación formal futura.

---

# 77. Autonomy Must Be Earned

```text
IMPLEMENTED CAPABILITY
≠
AUTONOMY AUTHORIZATION
```

---

# 78. Recommended Initial Build Boundary

El primer scope de implementación recomendado termina en:

```text
STAGE 13
```

con Sandbox funcional.

No incluye:

```text
REAL EXTERNAL WRITE TOOLS
AUTONOMOUS AGENTS
AUTOMATIC MEMORY WRITE
PHASE 11 AUTONOMY
```

---

# 79. Minimum Viable Technical Robert

Resultado esperado:

```text
CONTRACTS
+
AUDIT
+
GOVERNANCE
+
VALIDATION
+
CONTROLLED CONTEXT
+
MODEL INTERFACE
+
SKILLS
+
AGENTS
+
TOOL ABSTRACTION
+
ORCHESTRATOR
+
API
+
BASIC UI
+
SANDBOX
```

---

# 80. Dependency Graph

```text
TECHNICAL FOUNDATION
        ↓
CONTRACTS
        ↓
ERROR / AUDIT
        ↓
GOVERNANCE
        ↓
VALIDATION
        ↓
CONTEXT / MEMORY
        ↓
MODEL INTERFACE
        ↓
SKILLS
        ↓
AGENTS
        ↓
TOOL ABSTRACTION
        ↓
ORCHESTRATOR
        ↓
APPLICATION API
        ↓
BASIC UI
        ↓
SANDBOX
```

---

# 81. Why Orchestrator Is Late

Aunque Orchestrator es central arquitectónicamente, implementarlo demasiado pronto obligaría a simular interfaces inexistentes.

Por tanto:

```text
ARCHITECTURALLY CENTRAL
≠
FIRST COMPONENT TO CODE
```

---

# 82. Why UI Is Late

UI depende del comportamiento del Core.

```text
UI FIRST
→
HIGH REWORK RISK
```

---

# 83. Why Tools Are Late

Real Tools pueden producir side effects.

Por eso:

```text
TOOL ABSTRACTION
BEFORE
REAL TOOL EXECUTION
```

---

# 84. Why Agents Are After Skills

```text
AGENT
MAY USE
SKILLS
```

Por tanto Skill infrastructure debe existir primero.

---

# 85. Why Governance Is Early

Permission, Scope, Risk, Security y Audit deben existir antes de capacidades complejas.

```text
GOVERNANCE
BEFORE
POWER
```

---

# 86. Build Gate

Cada Stage debe tener:

```text
ENTRY CRITERIA
IMPLEMENTATION SCOPE
TESTS
EXIT CRITERIA
```

---

# 87. No Stage Skipping by Default

```text
STAGE N+1
SHOULD NOT START
UNTIL
STAGE N CRITICAL EXIT CRITERIA PASS
```

Excepciones técnicas requieren justificación explícita.

---

# 88. Parallel Work

Algunas tareas pueden desarrollarse en paralelo si no rompen dependencias.

Ejemplo:

```text
ERROR CONTRACTS
+
AUDIT CONTRACTS
```

pueden desarrollarse paralelamente después de Stage 1.

---

# 89. Parallel Work ≠ Dependency Bypass

```text
PARALLELIZATION
≠
SKIPPING FOUNDATIONS
```

---

# 90. Build Priority

Dentro de cada Stage:

```text
P0 = BLOCKING FOUNDATION

P1 = REQUIRED FOR INITIAL BUILD

P2 = USEFUL BUT DEFERRABLE

P3 = FUTURE
```

---

# 91. Initial P0 Components

```text
CONTRACTS
ERROR
AUDIT
PERMISSION
SCOPE
SECURITY
EXECUTION AUTHORITY CHECK
VALIDATION
```

---

# 92. Initial P1 Components

```text
CONTEXT
MEMORY INTERFACE
MODEL INTERFACE
SKILLS
AGENTS
TOOL INTERFACE
ORCHESTRATOR
API
SANDBOX
```

---

# 93. Initial P2 Components

```text
ADVANCED UI
MULTI-MODEL ROUTING
ADVANCED MEMORY SEARCH
ADVANCED OBSERVABILITY
COST OPTIMIZATION
```

---

# 94. Initial P3 Components

```text
AUTONOMOUS AGENT LOOPS
AUTOMATIC TOOL EXECUTION
BACKGROUND AUTOMATION
ADVANCED MULTI-AGENT SYSTEMS
PHASE 11+ FEATURES
```

---
# 94.1 Priority-to-Stage Mapping

Las prioridades P0-P3 no constituyen una segunda secuencia
de construcción.

Complementan los Stages.

Mapeo general:

P0
→ principalmente Stages 0-4
→ foundations, contracts, audit, governance, validation

P1
→ principalmente Stages 5-13
→ controlled functional initial build

P2
→ mejoras dentro o después del initial build
→ no bloquean el núcleo cuando están explícitamente diferidas

P3
→ Stages 14-15 y capacidades futuras
→ fuera del initial build por defecto

Regla:

PRIORITY
≠
BUILD STAGE

Priority indica importancia.

Stage indica dependencia y orden.
# 95. Implementation Decision Gates

Antes de código deben aprobarse todavía decisiones técnicas sobre:

```text
LANGUAGE
FRAMEWORK
CONTRACT TECHNOLOGY
TEST FRAMEWORK
REPOSITORY STRUCTURE
```

---

# 96. Database Decision

No debe elegirse una base de datos solo porque eventualmente habrá Memory.

Primero:

```text
DATA ACCESS INTERFACE
```

Después:

```text
DATABASE IMPLEMENTATION
```

---

# 97. Provider Decision

No acoplar:

```text
MODEL INTERFACE
```

directamente a un único proveedor.

---

# 98. Tool Provider Decision

Igual:

```text
TOOL INTERFACE
↓
ADAPTER
↓
PROVIDER
```

---

# 99. Testing Strategy by Stage

Cada Stage debe incluir:

```text
UNIT TESTS
CONTRACT TESTS
BOUNDARY TESTS
FAILURE TESTS
```

cuando corresponda.

---

# 100. Integration Tests

Comenzar después de que dos o más componentes tengan contratos estables.

---

# 101. End-to-End Test

Primer E2E obligatorio:

```text
USER REQUEST
↓
TASK
↓
ORCHESTRATOR
↓
MODEL / SKILL / AGENT
↓
VALIDATION
↓
RESULT
↓
AUDIT
```

sin Tool externo.

---

# 102. Second End-to-End Test

```text
USER REQUEST
↓
TOOL REQUEST GENERATED
↓
GOVERNANCE CHECKS
↓
EXECUTION AUTHORITY NONE
↓
BLOCK / SANDBOX RESULT
↓
AUDIT
```

---

# 103. Security Test Gate

Antes de cualquier Stage 14:

```text
SECURITY TESTS
MUST PASS
```

---

# 104. Real Tool Gate

No conectar Tool real hasta demostrar:

```text
PERMISSION CHECK WORKS

SCOPE CHECK WORKS

RISK CHECK WORKS

SECURITY CHECK WORKS

APPROVAL FLOW WORKS

AUDIT WORKS

SIDE EFFECT HANDLING WORKS
```

---

# 105. Memory Automation Gate

No automatic Memory Write hasta demostrar:

```text
MEMORY CANDIDATE
→ VALIDATION
→ GOVERNANCE
→ CONTROLLED WRITE
```

---

# 106. Agent Autonomy Gate

No Agent autonomy hasta demostrar:

```text
SCOPE CONTROL
ROUTING CONTROL
TOOL BOUNDARY
MEMORY BOUNDARY
FAILURE CONTAINMENT
AUDIT
```

---

# 107. Build Stop Conditions

Detener avance de Stage si aparece:

```text
ARCHITECTURAL CONFLICT
CONTRACT CONFLICT
SECURITY GAP
AUTHORITY LEAKAGE
UNRESOLVED BLOCKER
UNTRACEABLE SIDE EFFECT
```

---

# 108. Build Stop ≠ Project Failure

```text
BUILD STOP
=
GOVERNANCE CONTROL
```

---

# 109. Architectural Change During Build

Si durante implementación aparece una necesidad arquitectónica real:

```text
STOP
↓
PROPOSE CHANGE
↓
REVIEW
↓
DECISION
↓
CHANGE CONTROL
↓
RESUME
```

No modificar silenciosamente la arquitectura desde código.

---

# 110. Code ≠ Source of Governance Truth

```text
IMPLEMENTATION
MUST FOLLOW
APPROVED ARCHITECTURE
```

No:

```text
ARCHITECTURE
CHANGED SILENTLY
TO MATCH CODE
```

---

# 111. Recommended First Milestone

```text
MILESTONE 1
CORE FOUNDATION
```

Incluye:

```text
STAGE 0
STAGE 1
STAGE 2
STAGE 3
STAGE 4
```

Resultado:

```text
CONTRACTS + GOVERNANCE + AUDIT + VALIDATION
```

---

# 112. Recommended Second Milestone

```text
MILESTONE 2
INTELLIGENCE FOUNDATION
```

Incluye:

```text
STAGE 5
STAGE 6
STAGE 7
STAGE 8
```

Resultado:

```text
CONTEXT + MEMORY INTERFACE + MODEL + SKILLS + AGENTS
```

---

# 113. Recommended Third Milestone

```text
MILESTONE 3
ORCHESTRATED CORE
```

Incluye:

```text
STAGE 9
STAGE 10
```

Resultado:

```text
TOOL ABSTRACTION + ORCHESTRATOR
```

---

# 114. Recommended Fourth Milestone

```text
MILESTONE 4
USABLE TECHNICAL MVP
```

Incluye:

```text
STAGE 11
STAGE 12
STAGE 13
```

Resultado:

```text
API + BASIC UI + SANDBOX
```

---

# 115. Future Milestone

```text
MILESTONE 5
CONTROLLED EXTERNAL INTEGRATION
```

Stage 14.

Requiere aprobación posterior.

---

# 116. Future Autonomy Milestone

```text
MILESTONE 6
CONTROLLED AUTONOMY
```

Stage 15.

Requiere fase y gobernanza futuras.

---

# 117. Initial Implementation Completion

La implementación inicial puede considerarse técnicamente completa cuando:

```text
MILESTONE 1 = PASS
MILESTONE 2 = PASS
MILESTONE 3 = PASS
MILESTONE 4 = PASS
```

sin requerir Milestone 5 o 6.

---

# 118. Build Order and Phase 10

Build Order debe estar aprobado para cerrar Fase 10.

Pero:

```text
BUILD ORDER APPROVED
≠
BUILD STARTED
```

---

# 119. Phase 10 Exit Relationship

Una vez aprobado este documento podrá evaluarse:

```text
I1 — Build Order Exists
I2 — Dependency Order Verified
I3 — Governance Precedes Execution
I4 — Initial MVP Boundary Defined
```

dentro de `ROBERT_PHASE_10_EXIT_CRITERIA`.

---

# 120. Build Authorization

Después del Phase 10 Exit Audit deberá existir una decisión separada:

```text
AUTHORIZE INITIAL IMPLEMENTATION
```

---

# 121. Suggested Authorization Scope

Una futura autorización inicial debería limitarse a:

```text
STAGE 0 → STAGE 13
```

con:

```text
REAL EXTERNAL EXECUTION = DISABLED
```

salvo decisión específica distinta.

---

# 122. Code Authorization ≠ Tool Authorization

```text
PERMISSION TO BUILD TOOL INTERFACE
≠
PERMISSION TO EXECUTE REAL TOOL
```

---

# 123. Code Authorization ≠ Autonomy

```text
IMPLEMENTATION AUTHORIZED
≠
AUTONOMY AUTHORIZED
```

---

# 124. Build Order Acceptance Criteria

Este documento podrá aprobarse cuando:

1. respete dependencias arquitectónicas;
2. Contracts estén antes del Orchestrator;
3. Audit esté antes de capacidades con impacto;
4. Governance esté antes de ejecución;
5. Validation esté antes del flujo completo;
6. Model Interface esté antes de Agents que la utilizan;
7. Skills estén antes de Agents que dependen de Skills;
8. Tool abstraction esté antes de real Tool execution;
9. Orchestrator se construya después de sus interfaces;
10. API esté después del Core;
11. UI esté después del API/Core;
12. Sandbox preceda integraciones externas;
13. external Tools no formen parte obligatoria del initial build;
14. autonomía quede fuera del initial build;
15. se preserve `AUTONOMY_LEVEL = 0`;
16. se preserve `EXECUTION_AUTHORITY = NONE`;
17. existan gates entre Stages;
18. exista estrategia de tests;
19. exista una frontera clara para el MVP inicial;
20. no se autorice código mediante este documento.

---

# 125. Adversarial Review Checklist

Revisar especialmente:

```text
WRONG DEPENDENCY ORDER

ORCHESTRATOR BUILT TOO EARLY

UI BUILT TOO EARLY

REAL TOOLS BUILT TOO EARLY

AGENT AUTHORITY LEAKAGE

TOOL AUTHORITY LEAKAGE

MEMORY WRITE LEAKAGE

VALIDATION → APPROVAL LEAKAGE

IMPLEMENTATION → AUTONOMY LEAKAGE

PROVIDER COUPLING

DATABASE PREMATURE COMMITMENT

MISSING AUDIT FOUNDATION

MISSING SECURITY GATE

MISSING TEST GATE

MISSING STOP CONDITION

PHASE 10 → CODE AUTHORIZATION LEAKAGE
```

---
**# 125.1 Invariantes Globales del Build Order

Este Build Order preserva:

BUILD ORDER
≠
IMPLEMENTATION AUTHORIZATION

ARCHITECTURALLY CENTRAL
≠
FIRST COMPONENT TO CODE

CONTRACT
≠
IMPLEMENTATION

ROUTE
≠
ROUTING AUTHORITY

AUDIT WRITER
≠
AUDIT AUTHORITY

SKILL RUNNER
≠
EXECUTION AUTHORITY

AGENT RUNNER
≠
ROUTING AUTHORITY

MODEL OUTPUT
≠
ROUTING AUTHORITY

MODEL TOOL REQUEST
≠
TOOL EXECUTION

TOOL ABSTRACTION
≠
REAL TOOL EXECUTION

CONNECTED
≠
AUTHORIZED

IMPLEMENTED CAPABILITY
≠
AUTONOMY AUTHORIZATION

IMPLEMENTATION AUTHORIZED
≠
AUTONOMY AUTHORIZED

CODE AUTHORIZATION
≠
TOOL AUTHORIZATION

PHASE 10 COMPLETE
≠
IMPLEMENTATION AUTHORIZED**
# 126. Current Status

DOCUMENT: ROBERT_BUILD_ORDER

VERSION: 0.1

STATUS: APPROVED

AUTHORITY: ARCHITECTURAL

DECISION: #040
CHANGE: #065

PHASE: 10

BUILD_ORDER: APPROVED

IMPLEMENTATION: STAGES 0–6 COMPLETE

IMPLEMENTATION_AUTHORIZATION: GRANTED — STAGES 0–6 ONLY

AUTHORIZED_BUILD_BOUNDARY: STAGE 6

STAGE_6: COMPLETE

STAGE_7: NOT AUTHORIZED

REAL_TOOL_EXECUTION: DISABLED

AUTONOMY_LEVEL: 0

EXECUTION_AUTHORITY: NONE

# 127. Estado posterior a las autorizaciones iniciales

Stage 0 fue autorizado mediante:

```text
DECISIÓN #042
CAMBIO #068
```

Resultado:

```text
STAGE_0 = COMPLETE
STAGE_1 = COMPLETE
STAGE_2 = COMPLETE
STAGE_3 = COMPLETE
STAGE_4 = COMPLETE
STAGE_5 = COMPLETE
STAGE_6 = COMPLETE
STAGE_7 = NOT AUTHORIZED
```

Stage 1 fue autorizado e implementado mediante:

```text
DECISIÓN #043
CAMBIO #069
```

Stage 2 fue autorizado e implementado mediante:

```text
DECISIÓN #044
CAMBIO #070
```

Stage 3 y el chequeo previo quedaron autorizados mediante DECISIÓN #045 y verificados mediante CAMBIO #071.

Stage 4 — Validation Core quedó autorizado mediante DECISIÓN #046 y verificado mediante CAMBIO #072.

Stage 5 — Context / Memory Interfaces quedó autorizado mediante DECISIÓN #047 y verificado
localmente mediante CAMBIO #073. No se habilitan escrituras automáticas ni proveedores externos.

Stage 6 — Model Interface quedó autorizado mediante DECISIÓN #048 y verificado mediante CAMBIO #074.
La implementación usa un puerto de proveedor inyectado y pruebas locales; no habilita conexiones
reales, Tool execution, escritura automática de Memory ni Agents.

La siguiente transición permitida es una decisión humana separada sobre:

```text
AUTHORIZE STAGE 7 — SKILL LAYER?
```

Hasta entonces, el límite obligatorio es `STAGE 6`.
