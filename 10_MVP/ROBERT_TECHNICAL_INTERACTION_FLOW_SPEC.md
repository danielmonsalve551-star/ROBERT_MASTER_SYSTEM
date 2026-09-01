# ROBERT_TECHNICAL_INTERACTION_FLOW_SPEC

**Versión:** 0.2
**Estado:** APROBADO E INTEGRADO / CANÓNICAMENTE NORMALIZADO
**Fecha original:** 03/07/2026
**Última normalización:** 31/08/2026
**Ubicación:** `10_MVP`
**Fase relacionada:** Fase 10 — Implementation Readiness
**Documento base relacionado:** `ROBERT_TECHNICAL_DATA_MODEL_SPEC v0.1`
**Documento relacionado:** `ROBERT_TECHNICAL_COMPONENTS_SPEC v0.2`

**Decisión relacionada:** DECISIÓN #014
**Cambios relacionados:** CAMBIO #022 / CAMBIO #023

---

Tags: #robert/orbita-3 #capa/5 #tipo/tecnico #robert/mvp #robert/interaction-flow

[[ROBERT_HOME]]
[[ROBERT_CONTEXT_MASTER]]
[[ROBERT_CANONICAL_MODEL]]
[[ROBERT_ORCHESTRATOR_SPEC]]
[[ROBERT_AGENT_ARCHITECTURE]]
[[ROBERT_SKILL_ARCHITECTURE]]
[[ROBERT_MODEL_INTERFACE_SPEC]]
[[ROBERT_MEMORY_ARCHITECTURE]]
[[ROBERT_VALIDATION_ARCHITECTURE]]
[[ROBERT_TOOL_ARCHITECTURE]]
[[ROBERT_IMPLEMENTATION_CONTRACTS]]
[[ROBERT_TECHNICAL_DATA_MODEL_SPEC]]
[[ROBERT_TECHNICAL_COMPONENTS_SPEC]]
[[ROBERT_TECHNICAL_SCREEN_STATE_SPEC]]
[[ROBERT_TECHNICAL_ERROR_AND_BLOCKING_SPEC]]
[[ROBERT_TECHNICAL_PERMISSIONS_AND_SCOPES_SPEC]]
[[ROBERT_TECHNICAL_AUDIT_TRAIL_SPEC]]
[[ROBERT_SECURITY_RULES]]
[[ROBERT_PHASES]]

---

# OBJETIVO

`ROBERT_TECHNICAL_INTERACTION_FLOW_SPEC` define cómo fluye conceptualmente la información entre el usuario, la interfaz y los componentes internos de Robert durante una futura implementación controlada.

Su función es describir:

* cómo entra una solicitud;
* cómo se convierte en Task;
* cómo recibe Context;
* cómo llega al Orchestrator;
* cómo se resuelve el trabajo;
* cómo participan Agents;
* cómo participan Skills;
* cómo participan Models;
* cómo se representan Tool Requests;
* cómo participa Memory;
* cómo se realiza Validation;
* cómo intervienen Permission, Scope, Risk y Approval;
* cómo se generan Results;
* cómo se registra Audit;
* cómo se proyecta el estado hacia UI.

Este documento describe **movimiento e interacción**.

No redefine Routing Authority.

No redefine Governance.

No crea Execution Authority.

---

# ESTADO DEL DOCUMENTO

Este documento está formalmente:

```text
APPROVED
INTEGRATED
```

Trazabilidad:

```text
DECISIÓN #014

CAMBIO #022
CORRECTION

CAMBIO #023
APPROVAL / INTEGRATION
```

La normalización actual no crea una nueva aprobación.

Estado:

```text
DOCUMENT:
ROBERT_TECHNICAL_INTERACTION_FLOW_SPEC

VERSION:
0.2

STATUS:
APPROVED / INTEGRATED / CANONICALLY NORMALIZED

PHASE:
10

TECHNICAL_IMPLEMENTATION:
NOT STARTED

REAL_TOOL_EXECUTION:
DISABLED

AUTONOMY_LEVEL:
0

EXECUTION_AUTHORITY:
NONE
```

---

# CANONICAL ARCHITECTURE ALIGNMENT

La autoridad semántica pertenece a:

```text
ROBERT_CANONICAL_MODEL v0.2
DECISIÓN #030
CAMBIO #053
```

La autoridad de coordinación y Routing pertenece a:

```text
ROBERT_ORCHESTRATOR_SPEC v0.1
DECISIÓN #031
CAMBIO #054
```

Los Contracts entre componentes pertenecen a:

```text
ROBERT_IMPLEMENTATION_CONTRACTS v0.1
DECISIÓN #038
CAMBIO #063
```

Este documento solo especifica:

```text
HOW INFORMATION MOVES
BETWEEN APPROVED COMPONENTS
```

Se formaliza:

```text
INTERACTION FLOW
≠
ORCHESTRATOR

INTERACTION FLOW
≠
ROUTING AUTHORITY

INTERACTION FLOW
≠
APPROVAL AUTHORITY

INTERACTION FLOW
≠
EXECUTION AUTHORITY
```

---

# REGLA CENTRAL

El flujo maestro de Robert debe seguir la arquitectura aprobada.

```text
USER
↓
TASK
↓
REQUEST_CONTEXT
↓
ORCHESTRATOR
↓
ROUTING / RESOLUTION
↓
AGENT / SKILL / MODEL / MEMORY / TOOL REQUEST AS NEEDED
↓
VALIDATION
↓
GOVERNANCE CHECKS
↓
ORCHESTRATOR_RESULT
↓
AUDIT
↓
UI / OUTPUT
```

No debe existir un segundo flujo independiente que compita con el Orchestrator.

---

# ORCHESTRATOR AS MASTER FLOW COORDINATOR

El Orchestrator es el coordinador arquitectónico principal.

Referencia:

```text
ROBERT_ORCHESTRATOR_SPEC v0.1
DECISIÓN #031
CAMBIO #054
```

Responsabilidades relacionadas:

* Task intake;
* Context coordination;
* Module Routing;
* Agent Routing;
* Skill Resolution;
* Model Routing;
* Tool Resolution;
* Memory Resolution;
* Validation coordination;
* next-step coordination;
* result assembly.

Regla:

```text
ORCHESTRATOR
=
MASTER ROUTING AUTHORITY
```

Por tanto:

```text
COMMAND CENTER
≠
ROUTER

RISK BADGE
≠
RISK AUTHORITY

APPROVAL GATE
≠
APPROVAL AUTHORITY

DECISION INBOX
≠
DECISION AUTHORITY

UI
≠
SYSTEM GOVERNOR
```

---

# IMPLEMENTATION CONTRACT ALIGNMENT

Los intercambios entre componentes deben derivarse de:

```text
ROBERT_IMPLEMENTATION_CONTRACTS v0.1
```

Contracts relevantes:

```text
TASK
REQUEST_CONTEXT

ORCHESTRATOR_REQUEST
ORCHESTRATOR_RESULT
ROUTE

AGENT_REQUEST
AGENT_RESULT

SKILL_INVOCATION
SKILL_RESULT

MODEL_REQUEST
MODEL_RESPONSE

TOOL_REQUEST
TOOL_RESULT

MEMORY_CANDIDATE
MEMORY_RECORD
MEMORY_RETRIEVAL_REQUEST
MEMORY_RETRIEVAL_RESULT

VALIDATION_REQUEST
VALIDATION_RESULT

PERMISSION_CHECK
SCOPE_CHECK
RISK_ASSESSMENT

APPROVAL_REQUEST
APPROVAL_RESULT

ERROR
BLOCK
AUDIT_EVENT
```

Regla:

```text
INTERACTION FLOW
MUST USE
APPROVED CONTRACT BOUNDARIES
```

---

# ESTADO ACTUAL DE ROBERT

```text
PHASE = 10
```

Estado vigente:

```text
CORE_ARCHITECTURE = CLOSED

TOOL_ARCHITECTURE = CLOSED

IMPLEMENTATION_CONTRACTS = APPROVED

PHASE_10_EXIT_CRITERIA = APPROVED

BUILD_ORDER = APPROVED

TECHNICAL_IMPLEMENTATION = NOT STARTED

REAL_TOOL_EXECUTION = DISABLED

AUTOMATIC_MEMORY_WRITE = DISABLED

AUTONOMOUS_AGENTS = DISABLED

AUTONOMY_LEVEL = 0

EXECUTION_AUTHORITY = NONE
```

---

# ALCANCE AUTORIZADO

Este documento puede:

* definir flujos conceptuales;
* mapear componentes;
* mapear Contracts;
* definir puntos de pausa;
* definir puntos de Validation;
* definir interacción con Approval;
* definir interacción con Memory;
* definir interacción con Models;
* definir interacción con Agents;
* definir interacción con Skills;
* definir interacción con Tool Requests;
* definir proyección hacia UI;
* definir Audit points.

---

# ALCANCE NO AUTORIZADO

Este documento no autoriza:

* programación por sí mismo;
* ejecución real;
* Tool execution real;
* base de datos productiva;
* Automatic Memory Write;
* Agent autonomy;
* conexiones externas;
* Automation real;
* Phase 11;
* aumento de Autonomy;
* aumento de Execution Authority.

---

# PRINCIPIO DE SEPARACIÓN ENTRE UI Y CONTROL

Los componentes visuales representan estado e interacción humana.

No deben convertirse en autoridades de backend.

Se formaliza:

```text
UI COMPONENT
≠
GOVERNANCE AUTHORITY
```

y:

```text
DISPLAY
≠
DECISION
```

---

# COMPONENTES VISUALES PRINCIPALES

Se conservan los 10 componentes principales definidos en `ROBERT_TECHNICAL_COMPONENTS_SPEC v0.2`:

1. AppShell
2. TopBar
3. LeftSidebar
4. CommandCenter
5. ModeSelector
6. RiskBadge
7. ApprovalGate
8. DecisionInbox
9. DocumentStatusMap
10. CurrentStatePanel

Estos componentes pertenecen principalmente a Presentation.

No sustituyen las arquitecturas internas.

---

# APPSHELL

AppShell es el contenedor raíz de Presentation.

Puede:

* alojar componentes;
* recibir UI State;
* organizar layout;
* mostrar navegación.

No puede:

```text
ROUTE TASKS
APPROVE
ASSESS RISK
GRANT PERMISSION
EXPAND SCOPE
EXECUTE TOOLS
WRITE MEMORY
```

---

# TOPBAR

TopBar muestra estado resumido.

Puede recibir:

```text
current_phase
active_mode
execution_status
risk_summary
last_decision
last_change
pending_count
system_health
```

No toma Decisions ni modifica estado canónico.

---

# LEFTSIDEBAR

LeftSidebar representa navegación.

Puede enviar:

```text
navigation_target
selected_document
selected_module
```

La navegación no equivale a Routing arquitectónico.

```text
UI NAVIGATION
≠
ORCHESTRATOR ROUTING
```

---

# COMMANDCENTER

CommandCenter es el punto visual de entrada de una instrucción.

Su función correcta es:

```text
USER INPUT
↓
COMMAND CENTER
↓
TASK CREATION / REQUEST PREPARATION
↓
ORCHESTRATOR
```

CommandCenter no debe:

* decidir Routing;
* seleccionar Agent por autoridad propia;
* seleccionar Tool por autoridad propia;
* ejecutar;
* aprobar;
* otorgar Permission.

---

# MODESELECTOR

ModeSelector representa el Mode seleccionado o disponible.

Puede producir una solicitud de cambio de Mode.

No puede alterar Autonomy o Execution Authority por sí solo.

```text
SELECTED MODE
≠
AUTHORIZED AUTONOMY
```

---

# RISKBADGE

RiskBadge es un componente visual.

Muestra resultados de:

```text
RISK_ASSESSMENT
```

No calcula necesariamente el Risk por sí mismo.

No tiene autoridad para autorizar o bloquear.

```text
RISK BADGE
=
DISPLAY OF RISK STATE
```

No:

```text
RISK BADGE
=
RISK GOVERNOR
```

---

# APPROVALGATE

ApprovalGate representa visualmente el estado de Approval.

Puede mostrar:

```text
APPROVAL REQUIRED
APPROVAL PENDING
APPROVED
REJECTED
BLOCKED
```

No aprueba por sí mismo.

La Approval válida debe provenir de la autoridad autorizada.

```text
APPROVAL GATE
≠
APPROVAL AUTHORITY
```

---

# DECISIONINBOX

DecisionInbox muestra Decisions pendientes o resueltas.

No crea Decisions.

```text
DECISION INBOX
≠
DECISION AUTHORITY
```

---

# DOCUMENTSTATUSMAP

DocumentStatusMap representa estado documental.

No modifica documentos por sí mismo.

Puede visualizar:

* Document status;
* version;
* Decision refs;
* Change refs;
* lifecycle;
* relationships.

---

# CURRENTSTATEPANEL

CurrentStatePanel representa el estado consolidado visible.

Puede mostrar:

* Phase;
* Mode;
* active Task;
* Risk;
* Permission;
* Scope;
* Approval;
* Validation;
* last Decision;
* last Change;
* Blocks;
* next allowed step.

No constituye Source of Truth por sí mismo.

```text
UI STATE
≠
CANONICAL STATE AUTHORITY
```

---

# MODELOS LEGACY DEL DATA MODEL

Los 11 modelos originales continúan disponibles como View / Document Models:

1. SystemState
2. RobertDocument
3. DecisionRecord
4. ChangeRecord
5. RiskRecord
6. CommandRequest
7. PendingDecision
8. ModeState
9. ComponentState
10. GitHubBackupStatus
11. ObsidianGraphStatus

Se formaliza:

```text
LEGACY MVP VIEW MODEL
≠
CORE IMPLEMENTATION CONTRACT
```

Estos modelos pueden alimentar UI.

Los Contracts gobiernan interacción entre runtime components.

---

# FLUJO MAESTRO

El flujo maestro aprobado para futura implementación es:

```text
USER
↓
INPUT
↓
TASK
↓
REQUEST_CONTEXT
↓
ORCHESTRATOR_REQUEST
↓
ORCHESTRATOR
↓
ROUTE
↓
RESOLVERS / SPECIALIZED COMPONENTS
↓
VALIDATION
↓
GOVERNANCE
↓
ORCHESTRATOR_RESULT
↓
AUDIT_EVENT
↓
PRESENTATION
↓
USER
```

---

# FLUJO 1 — USER INPUT → TASK

## Objetivo

Convertir una interacción del usuario en una unidad de trabajo estructurada.

## Flujo

```text
USER
↓
COMMAND CENTER
↓
INPUT NORMALIZATION
↓
TASK
```

Task debe representar la intención de trabajo sin otorgarle Authority adicional.

## Regla

```text
USER INPUT
≠
DIRECT EXECUTION
```

---

# FLUJO 2 — TASK → REQUEST_CONTEXT

## Objetivo

Construir Context suficiente y autorizado para procesar la Task.

Puede incluir:

* current Phase;
* active Mode;
* selected Module;
* relevant document refs;
* Permission context;
* Scope context;
* relevant prior state.

Reglas:

```text
CONTEXT
≠
MEMORY

REQUEST CONTEXT
≠
FULL USER CONTEXT
```

Solo debe transferirse información necesaria.

---

# FLUJO 3 — REQUEST_CONTEXT → ORCHESTRATOR

La Task y RequestContext se encapsulan en:

```text
ORCHESTRATOR_REQUEST
```

El Orchestrator recibe la solicitud.

A partir de este punto la coordinación de Routing pertenece al Orchestrator.

---

# FLUJO 4 — ROUTE RESOLUTION

El Orchestrator determina qué capabilities son necesarias.

Puede resolver:

```text
MODULE
AGENT
SKILL
MODEL
MEMORY
VALIDATION
TOOL
```

según la Task.

Resultado conceptual:

```text
ROUTE
```

Reglas:

```text
ROUTE
≠
ROUTING AUTHORITY

ROUTE
=
OUTPUT OF ROUTING AUTHORITY
```

---

# FLUJO 5 — AGENT INTERACTION

Cuando se requiera un Agent:

```text
ORCHESTRATOR
↓
AGENT_REQUEST
↓
AGENT
↓
AGENT_RESULT
↓
ORCHESTRATOR
```

El Agent:

* recibe Scope limitado;
* realiza trabajo especializado;
* devuelve Result.

No puede ampliar su Scope.

No puede convertirse en Orchestrator.

```text
AGENT
≠
ORCHESTRATOR
```

---

# FLUJO 6 — SKILL INTERACTION

Cuando se requiera una Skill:

```text
ORCHESTRATOR / AUTHORIZED AGENT CONTEXT
↓
SKILL_INVOCATION
↓
SKILL
↓
SKILL_RESULT
```

La ejecución técnica futura puede utilizar Skill Runner.

Pero:

```text
SKILL RUNNER
≠
EXECUTION AUTHORITY
```

---

# FLUJO 7 — MODEL INTERACTION

Cuando se requiera un Model:

```text
ORCHESTRATOR
↓
MODEL_REQUEST
↓
MODEL INTERFACE
↓
MODEL
↓
MODEL_RESPONSE
↓
ORCHESTRATOR
```

Los Models pueden incluir:

* Claude;
* ChatGPT;
* future Models.

Reglas:

```text
MODEL ≠ TOOL

MODEL OUTPUT ≠ DECISION

MODEL OUTPUT ≠ TRUTH

MODEL OUTPUT ≠ ROUTING AUTHORITY

MODEL OUTPUT ≠ MEMORY WRITE
```

---

# FLUJO 8 — MEMORY RETRIEVAL

Cuando se requiera Memory:

```text
ORCHESTRATOR
↓
MEMORY RETRIEVAL REQUEST
↓
MEMORY RESOLVER
↓
AUTHORIZED MEMORY SOURCES
↓
MEMORY RETRIEVAL RESULT
↓
ORCHESTRATOR
```

La Request debe poder incluir:

```text
requester
query
memory_types
retention_classes
scope
freshness_requirement
confidence_requirement
sensitivity_constraints
max_results
purpose
```

Reglas:

```text
CONTEXT ≠ MEMORY

MEMORY RETRIEVAL SCOPE
≠
AUTHORIZED OPERATIONAL SCOPE
```

---

# FLUJO 9 — MEMORY CANDIDATE

Cuando una salida pueda convertirse en candidato de Memory:

```text
RESULT
↓
MEMORY_CANDIDATE
↓
MEMORY GOVERNANCE
↓
POTENTIAL FUTURE MEMORY_RECORD
```

Durante Fase 10:

```text
AUTOMATIC_MEMORY_WRITE = DISABLED
```

Por tanto:

```text
MEMORY_CANDIDATE
≠
AUTOMATIC MEMORY WRITE
```

---

# FLUJO 10 — TOOL REQUEST

Cuando una capability técnica requiera una Tool:

```text
ORCHESTRATOR
↓
TOOL RESOLUTION
↓
TOOL_REQUEST
↓
PERMISSION / SCOPE / SECURITY / APPROVAL CHECK
↓
TOOL INTERFACE
```

Durante Fase 10 el flujo termina antes de ejecución real:

```text
REAL_TOOL_EXECUTION = DISABLED
```

Reglas:

```text
TOOL REQUEST
≠
TOOL AUTHORIZATION

TOOL AVAILABLE
≠
TOOL ALLOWED

MODEL TOOL REQUEST
≠
DIRECT TOOL EXECUTION

AGENT TOOL REQUEST
≠
DIRECT TOOL EXECUTION
```

---

# FLUJO 11 — FUTURE TOOL RESULT

En una fase futura autorizada:

```text
TOOL INTERFACE
↓
TOOL ADAPTER
↓
PROVIDER
↓
TOOL_RESULT
↓
VALIDATION
↓
ORCHESTRATOR
```

Tool Result no es verdad automática.

```text
TOOL RESULT
≠
TRUTH

TOOL RESULT
≠
MEMORY WRITE
```

---

# FLUJO 12 — VALIDATION

Validation puede aplicarse en distintos puntos.

Flujo conceptual:

```text
TARGET
↓
VALIDATION_REQUEST
↓
VALIDATION RESOLVER
↓
VALIDATOR ROLE / RULE SYSTEM
↓
VALIDATION_RESULT
↓
ORCHESTRATOR
```

La arquitectura reconoce:

```text
VALIDATION_TYPE
≠
REVIEWER_ROLE
```

Validation no autoriza.

```text
VALIDATION
≠
APPROVAL

VALIDATION
≠
EXECUTION AUTHORITY

VALIDATION PASS
≠
TRUTH
```

---

# FLUJO 13 — PERMISSION CHECK

Cuando una operación requiera Permission:

```text
REQUEST
↓
PERMISSION_CHECK
↓
ALLOW / DENY / REQUIRED STATE
```

Regla:

```text
PERMISSION
≠
SCOPE

PERMISSION
≠
EXECUTION AUTHORITY
```

---

# FLUJO 14 — SCOPE CHECK

```text
REQUESTED OPERATION
↓
SCOPE_CHECK
↓
WITHIN SCOPE / OUTSIDE SCOPE
```

Regla:

```text
REQUESTED SCOPE
≠
AUTHORIZED SCOPE
```

Una operación fuera de Scope debe producir Block o safe failure según Governance.

---

# FLUJO 15 — RISK ASSESSMENT

```text
TASK / OPERATION
↓
RISK_ASSESSMENT
↓
RISK STATE
```

Escala oficial:

```text
0 — INFORMATIONAL
1 — LOW
2 — MEDIUM
3 — HIGH
4 — CRITICAL
```

Reglas:

```text
RISK
≠
PERMISSION

RISK
≠
AUTONOMY

RISK
≠
EXECUTION AUTHORITY
```

Importante:

El Risk Level por sí mismo no define automáticamente el comportamiento completo.

La respuesta depende también de:

* Permission;
* Scope;
* Security;
* Approval requirements;
* Phase;
* operation type;
* side effects;
* specialized policies.

---

# FLUJO 16 — APPROVAL

Cuando una operación requiere Approval:

```text
ACTION PROPOSAL
↓
APPROVAL_REQUEST
↓
AUTHORIZED HUMAN / AUTHORITY
↓
APPROVAL_RESULT
↓
ORCHESTRATOR
```

La UI puede representar este estado con ApprovalGate.

Pero:

```text
APPROVAL GATE
≠
APPROVAL AUTHORITY
```

---

# FLUJO 17 — BLOCK

Si una condición bloqueante existe:

```text
REQUEST
↓
CHECK
↓
BLOCK
↓
AUDIT_EVENT
↓
SAFE RESPONSE
```

El Block debe expresar:

* reason;
* relevant policy;
* affected operation;
* next allowed step cuando aplique.

---

# FLUJO 18 — ERROR

Cuando ocurre un Error:

```text
COMPONENT
↓
ERROR
↓
ERROR / BLOCKING HANDLING
↓
AUDIT
↓
SAFE RESULT / RETRY / STOP
```

La taxonomía principal pertenece a:

```text
ROBERT_TECHNICAL_ERROR_AND_BLOCKING_SPEC v0.2
```

Interaction Flow no crea una segunda taxonomía.

---

# FLUJO 19 — ORCHESTRATOR RESULT

Después de coordinar trabajo y checks:

```text
ORCHESTRATOR
↓
ORCHESTRATOR_RESULT
```

El Result puede contener:

* status;
* output;
* references;
* Validation state;
* Risk state;
* Approval state;
* Block;
* next step.

El Orchestrator Result no autoriza por sí mismo acciones futuras.

---

# FLUJO 20 — AUDIT

Actividad relevante produce:

```text
AUDIT_EVENT
```

El Audit debe permitir reconstruir:

* Task;
* Actor;
* component;
* action;
* Permission state;
* Scope state;
* Risk state;
* Approval state;
* Validation state;
* Result;
* evidence.

Regla:

```text
AUDIT
≠
AUTHORITY
```

---

# FLUJO 21 — PRESENTATION

Los resultados autorizados llegan a Presentation.

```text
ORCHESTRATOR_RESULT
+
SYSTEM STATE
+
AUDITABLE STATUS
↓
UI STATE
↓
USER
```

Los componentes UI pueden mostrar información.

No crean estado canónico solo por mostrarlo.

---

# FLUJO 22 — DOCUMENT DRAFT

Para una solicitud documental:

```text
USER
↓
TASK
↓
ORCHESTRATOR
↓
DOCUMENT-RELATED CAPABILITY
↓
DRAFT
↓
VALIDATION
↓
USER
```

Regla:

```text
DRAFT
≠
APPROVAL
```

---

# FLUJO 23 — DOCUMENT APPROVAL

Cuando el usuario aprueba explícitamente un documento:

```text
USER APPROVAL
↓
APPROVAL_RESULT
↓
DECISION
↓
CHANGE IF APPLIED
↓
DOCUMENT STATE UPDATE
↓
AUDIT
↓
UI STATE UPDATE
```

Reglas:

```text
APPROVAL
≠
CHANGE

DECISION
≠
CHANGE

DOCUMENT APPROVAL
≠
CODE AUTHORIZATION
```

---

# FLUJO 24 — DOCUMENT CHANGE

Cuando una corrección es aplicada:

```text
AUTHORIZED CHANGE REQUEST
↓
CHANGE
↓
DOCUMENT UPDATE
↓
AUDIT
↓
STATE UPDATE
```

No debe registrarse un Change que no haya ocurrido realmente.

---

# FLUJO 25 — PENDING DECISION

Cuando se requiere intervención humana:

```text
TASK
↓
APPROVAL / DECISION REQUIRED
↓
PENDING STATE
↓
DECISION INBOX
↓
USER
```

No se resuelve automáticamente.

---

# FLUJO 26 — SYSTEM STATE UPDATE

`SystemState` puede utilizarse como View Model agregado.

Debe actualizarse cuando exista un cambio material como:

* Phase;
* Mode;
* Decision;
* Change;
* Block;
* Approval state relevante;
* implementation state;
* current capability state.

No toda respuesta requiere SystemState mutation.

```text
RESPONSE
≠
STATE CHANGE
```

---

# FLUJO 27 — SIMPLE INFORMATION RESPONSE

Para una consulta puramente informativa:

```text
USER
↓
TASK
↓
ORCHESTRATOR
↓
RELEVANT CAPABILITY
↓
RESULT
↓
USER
```

No necesita crear:

```text
DECISION
CHANGE
MEMORY WRITE
FORMAL AUDIT RECORD
```

salvo que alguna política específica lo requiera.

---

# FLUJO 28 — MANUAL GITHUB BACKUP

Durante Fase 10:

```text
LOCAL DOCUMENT CHANGE
↓
USER MANUAL ACTION
↓
GITHUB
↓
USER CONFIRMATION
↓
GitHubBackupStatus VIEW UPDATE
```

Robert no debe afirmar que GitHub fue actualizado sin evidencia o confirmación.

```text
SUGGESTED COMMIT
≠
COMPLETED COMMIT
```

---

# FLUJO 29 — OBSIDIAN GRAPH VIEW

```text
DOCUMENT METADATA
↓
ObsidianGraphStatus
↓
VISUAL REPRESENTATION
```

Regla:

```text
GRAPH VIEW
≠
SYSTEM EXECUTION
```

---

# FLUJO 30 — COMPONENT STATE

`ComponentState` representa estado de componentes.

Puede alimentar UI.

Estados conceptuales pueden incluir:

* Defined;
* Approved;
* Not implemented;
* Blocked;
* Future;
* Deprecated.

Pero:

```text
COMPONENT DEFINED
≠
COMPONENT IMPLEMENTED
```

---

# RELACIÓN CON AGENT RUNNER

Durante futura implementación puede existir un `Agent Runner`.

Flujo:

```text
ORCHESTRATOR
↓
AGENT_REQUEST
↓
AGENT_RUNNER
↓
SELECTED AGENT
↓
AGENT_RESULT
```

Architectural Growth Check:

```text
ENTITY:
AGENT RUNNER

TYPE:
TECHNICAL RUNTIME COMPONENT

NEW CANONICAL AUTHORITY:
NO

ROUTING AUTHORITY:
NO

PERMISSION AUTHORITY:
NO

EXECUTION AUTHORITY:
NO
```

Regla:

```text
AGENT RUNNER
≠
ROUTING AUTHORITY
```

---

# RELACIÓN CON SKILL RUNNER

Futuro flujo:

```text
SKILL_INVOCATION
↓
SKILL_RUNNER
↓
SKILL
↓
SKILL_RESULT
```

Architectural Growth Check:

```text
ENTITY:
SKILL RUNNER

TYPE:
TECHNICAL RUNTIME COMPONENT

NEW CANONICAL AUTHORITY:
NO

ROUTING AUTHORITY:
NO

TOOL AUTHORIZATION:
NO

EXECUTION AUTHORITY:
NO
```

---

# RELACIÓN CON AUDIT WRITER

Futuro flujo:

```text
AUDITABLE EVENT
↓
AUDIT WRITER
↓
AUDIT_EVENT
↓
AUDIT STORAGE
```

Architectural Growth Check:

```text
ENTITY:
AUDIT WRITER

TYPE:
TECHNICAL RUNTIME COMPONENT

NEW CANONICAL AUTHORITY:
NO

ROUTING AUTHORITY:
NO

APPROVAL AUTHORITY:
NO

EXECUTION AUTHORITY:
NO
```

---

# DATA MINIMIZATION DURING FLOW

Los componentes solo deben recibir la información mínima necesaria.

Regla:

```text
COMPONENT INPUT
=
MINIMUM NECESSARY DATA
```

No enviar automáticamente:

```text
FULL MEMORY
FULL SESSION
FULL USER PROFILE
FULL DOCUMENT STORE
FULL MODEL HISTORY
```

a cada componente.

---

# SENSITIVE DATA FLOW

Credenciales y secretos no deben circular como payload general.

```text
SECRET
≠
GENERAL CONTEXT FIELD
```

Ejemplos:

* API keys;
* tokens;
* passwords;
* provider secrets;
* private credentials.

La futura implementación deberá usar infraestructura segura especializada.

---

# VALIDATION POINTS

Validation puede ocurrir:

1. después de input normalization;
2. después de Context retrieval;
3. después de Model Response;
4. después de Agent Result;
5. después de Skill Result;
6. después de Tool Result;
7. antes de final Result;
8. antes de Memory Candidate acceptance;
9. antes de side effects futuros cuando aplique.

Validation exacta depende del Route y del Risk.

---

# APPROVAL POINTS

Approval puede requerirse antes de:

* modificar estado oficial;
* integrar documentos;
* ejecutar side effects;
* utilizar Tools de escritura;
* operaciones externas;
* operaciones sensibles;
* avanzar de Phase;
* cambios de Governance;
* cambios de Autonomy.

Approval requirements no son definidos únicamente por este documento.

---

# AUDIT POINTS

Audit puede producirse en:

```text
TASK CREATED
ROUTE SELECTED
AGENT INVOKED
SKILL INVOKED
MODEL CALLED
MEMORY RETRIEVED
TOOL REQUESTED
TOOL RESULT RECEIVED
VALIDATION COMPLETED
PERMISSION CHECKED
SCOPE CHECKED
RISK ASSESSED
APPROVAL REQUESTED
APPROVAL RESOLVED
BLOCK CREATED
ERROR CREATED
DECISION CREATED
CHANGE APPLIED
RESULT RETURNED
```

según relevancia.

---

# ERROR PROPAGATION

Errors no deben perderse silenciosamente entre componentes.

Flujo:

```text
LOWER COMPONENT ERROR
↓
STANDARD ERROR CONTRACT
↓
ORCHESTRATOR
↓
POLICY
↓
RETRY / BLOCK / SAFE FAILURE
↓
AUDIT
↓
USER-FACING STATE
```

---

# RETRY FLOW

Cuando Retry esté permitido:

```text
ERROR
↓
RETRY POLICY CHECK
↓
RETRY
↓
RESULT
```

Cada intento debe conservar correlación.

Retry no debe duplicar side effects.

---

# IDEMPOTENCY FLOW

Para futuras operaciones con side effects:

```text
REQUEST
↓
IDEMPOTENCY CHECK
↓
EXECUTION
↓
RESULT
```

El Contract o Tool Policy correspondiente definirá detalles.

---

# TIMEOUT FLOW

Una futura integración debe poder manejar:

```text
REQUEST
↓
TIMEOUT
↓
ERROR
↓
RETRY / BLOCK / FALLBACK
```

según política.

---

# FALLBACK FLOW

Fallback solo puede utilizarse si está autorizado.

```text
PRIMARY CAPABILITY FAILED
↓
FALLBACK POLICY
↓
AUTHORIZED ALTERNATIVE
```

Regla:

```text
FALLBACK
≠
SILENT PROVIDER SWITCH WITH NEW AUTHORITY
```

---

# PROVIDER INDEPENDENCE

El flujo debe depender de interfaces canónicas.

```text
ROBERT
↓
MODEL INTERFACE / TOOL INTERFACE
↓
ADAPTER
↓
PROVIDER
```

No:

```text
CORE LOGIC
→
DIRECT PROVIDER DEPENDENCY
```

---

# FLOW AND BUILD ORDER

La implementación debe respetar:

```text
ROBERT_BUILD_ORDER v0.1
DECISIÓN #040
CAMBIO #065
```

Este Interaction Flow no modifica el orden de construcción.

```text
INTERACTION FLOW
≠
BUILD ORDER
```

---

# COMPONENT DATA FLOW — APPSHELL

Recibe:

```text
ui_state
system_state
component_state
active_document
navigation_state
```

Produce:

```text
layout rendering
user interaction surfaces
```

No produce Routing Decisions.

---

# COMPONENT DATA FLOW — TOPBAR

Recibe:

```text
current_phase
active_mode
execution_state
risk_summary
last_decision
last_change
pending_count
```

Produce:

```text
visual state
```

---

# COMPONENT DATA FLOW — LEFTSIDEBAR

Recibe:

```text
document_list
module_list
navigation_structure
active_document
```

Produce:

```text
navigation_selection
```

Navigation selection se convierte en Context input.

No en Routing Authority.

---

# COMPONENT DATA FLOW — COMMANDCENTER

Recibe:

```text
user_input
active_ui_context
```

Produce:

```text
task_input
```

La creación técnica final de Task debe seguir Implementation Contracts.

---

# COMPONENT DATA FLOW — MODESELECTOR

Recibe:

```text
available_modes
active_mode
mode_constraints
```

Produce:

```text
mode_change_request
```

No modifica Governance directamente.

---

# COMPONENT DATA FLOW — RISKBADGE

Recibe:

```text
risk_assessment
```

Produce:

```text
risk_display
```

---

# COMPONENT DATA FLOW — APPROVALGATE

Recibe:

```text
approval_request
approval_result
block_state
```

Produce:

```text
approval_ui_state
user_approval_input
```

User input debe regresar a Governance/Orchestrator.

No resolverse dentro del UI.

---

# COMPONENT DATA FLOW — DECISIONINBOX

Recibe:

```text
pending_decisions
decision_status
```

Produce:

```text
user_decision_input
```

---

# COMPONENT DATA FLOW — DOCUMENTSTATUSMAP

Recibe:

```text
document_state
decision_refs
change_refs
lifecycle_state
```

Produce:

```text
document_selection
visual_document_map
```

---

# COMPONENT DATA FLOW — CURRENTSTATEPANEL

Recibe:

```text
system_state
task_state
risk_state
permission_state
scope_state
approval_state
validation_state
audit_summary
```

Produce:

```text
human-readable system status
```

---

# LEGACY FLOW RECONCILIATION

El flujo histórico:

```text
CommandCenter
→
ModeSelector
→
RiskBadge
→
ApprovalGate
→
DecisionInbox
→
Robert prepares response
```

se conserva únicamente como:

```text
UI REPRESENTATION OF
THE INTERNAL FLOW
```

No como backend architecture.

El flujo interno correcto es:

```text
TASK
→
ORCHESTRATOR
→
GOVERNED ROUTING
→
RESULT
```

---

# RISK LEVEL 2 CORRECTION

La versión original establecía un comportamiento demasiado rígido para Risk 2.

La arquitectura actual establece:

```text
RISK LEVEL
ALONE
DOES NOT DETERMINE
APPROVAL REQUIREMENT
```

Risk 2 puede requerir:

* warning;
* Validation;
* Scope Check;
* Approval;

o simplemente continuar,

dependiendo de la política de la operación.

Por tanto, se elimina la regla global:

```text
RISK 2
=
ALWAYS CONFIRM SCOPE
```

como obligación universal.

---

# RISK LEVEL 3 AND 4

Tampoco deben interpretarse exclusivamente por una tabla UI.

La política específica puede bloquear, requerir Approval o limitar acción.

La escala permanece:

```text
0–4
```

pero:

```text
RISK
≠
PERMISSION

RISK
≠
EXECUTION AUTHORITY
```

---

# RULES FOR PAUSE

Una operación puede pausar cuando:

* falta información requerida;
* falta Approval;
* Scope es ambiguo;
* existe Validation incompleta;
* existe Conflict;
* existe una dependencia faltante;
* una política obliga a esperar input humano.

Pausa no implica automáticamente Error.

---

# RULES FOR BLOCK

Una operación debe Block cuando una política vinculante lo requiera.

Ejemplos:

* Permission denied;
* Scope exceeded;
* prohibited operation;
* unauthorized Tool execution;
* unauthorized Agent autonomy;
* incorrect Phase;
* Critical security conflict.

El tipo exacto debe seguir Error & Blocking Spec.

---

# RULES FOR APPROVAL

Approval debe basarse en:

* operation type;
* policy;
* Scope;
* Risk;
* side effects;
* document authority;
* Phase;
* user authority.

No debe basarse únicamente en el componente visual ApprovalGate.

---

# DATA PROTECTION

Los flujos deben minimizar exposición de:

* sensitive data;
* credentials;
* private documents;
* external provider secrets.

Cuando sea posible:

```text
REFERENCE
OVER
FULL PAYLOAD
```

---

# SYSTEM STATE UPDATE RULE

Actualizar SystemState únicamente cuando exista estado material nuevo.

Ejemplos:

* Phase;
* implementation status;
* Mode;
* active Block;
* Decision;
* Change;
* significant capability state.

No actualizarlo solo porque:

* se explicó algo;
* se generó texto;
* se hizo análisis;
* se consultó información.

---

# UI STATE UPDATE RULE

UI State sí puede cambiar sin que cambie SystemState.

Ejemplos:

* selected tab;
* selected document;
* expanded panel;
* temporary loading state;
* temporary Validation display.

Se formaliza:

```text
UI STATE
≠
SYSTEM STATE
```

---

# CONTRACT FAILURE

Si un componente recibe un Contract inválido:

```text
CONTRACT VALIDATION FAIL
↓
ERROR
↓
BLOCK / SAFE FAILURE
↓
AUDIT
```

No debe continuar con campos críticos faltantes mediante inferencia silenciosa.

---

# MISSING DATA

Debe distinguirse:

```text
MISSING
```

de:

```text
NULL
```

cuando la semántica del Contract lo requiera.

---

# FLOW OBSERVABILITY

Una futura implementación debe permitir correlación mediante:

```text
task_id
request_id
route_id
audit_event_id
```

cuando aplique.

Esto permite reconstruir el recorrido de una Task.

---

# NO AUTONOMOUS AGENT-TO-AGENT MESSAGING

Agents no deben crear una red autónoma de mensajes directos.

Comunicación conceptual:

```text
AGENT A
↓
ORCHESTRATOR / CONTROLLED CONTEXT TRANSFER
↓
AGENT B
```

No:

```text
AGENT A
↔
AGENT B
AUTONOMOUSLY
```

---

# CONTEXT TRANSFER

Todo Context Transfer debe:

* tener propósito;
* limitar contenido;
* respetar Scope;
* minimizar datos;
* evitar secretos innecesarios;
* ser mediado por Orchestrator cuando atraviese componentes especializados.

---

# TOOL FLOW BOUNDARY IN PHASE 10

Aunque Tool Architecture está aprobada:

```text
TOOL REQUEST
CAN BE REPRESENTED
```

pero:

```text
REAL TOOL EXECUTION
=
DISABLED
```

Este documento no debe mostrar un Tool Result real como si hubiese ocurrido.

---

# MEMORY FLOW BOUNDARY IN PHASE 10

Memory Architecture está aprobada.

Pero:

```text
AUTOMATIC MEMORY WRITE
=
DISABLED
```

Por tanto:

```text
RESULT
→
MEMORY_CANDIDATE
```

puede representarse conceptualmente.

No:

```text
RESULT
→
AUTOMATIC MEMORY_RECORD
```

---

# AGENT FLOW BOUNDARY IN PHASE 10

Agent Architecture está aprobada.

Pero:

```text
AUTONOMOUS AGENTS
=
DISABLED
```

Agent flows pueden diseñarse.

No deben interpretarse como runtime activo actual.

---

# CRITERIOS DE ACEPTACIÓN

Este documento cumple cuando:

* el Orchestrator es Routing Authority;
* Interaction Flow no crea Routing paralelo;
* UI components no se presentan como Authorities;
* `TASK` inicia el flujo técnico;
* `REQUEST_CONTEXT` está integrado;
* `ORCHESTRATOR_REQUEST` está integrado;
* `ROUTE` está integrado;
* Agent flow está integrado;
* Skill flow está integrado;
* Model flow está integrado;
* Memory Retrieval está integrado;
* Memory Candidate está integrado;
* Tool Request está integrado;
* Validation está integrada;
* Permission Check está integrado;
* Scope Check está integrado;
* Risk Assessment está integrado;
* Approval Request / Result están integrados;
* Error y Block están integrados;
* Orchestrator Result está integrado;
* Audit Event está integrado;
* Presentation recibe estado sin gobernarlo;
* Legacy Data Models quedan como View Models;
* Risk no se confunde con Permission;
* ApprovalGate no es Approval Authority;
* RiskBadge no es Risk Authority;
* CommandCenter no es Router;
* Data Minimization está incorporada;
* provider independence está incorporada;
* no existe Agent-to-Agent messaging autónomo;
* Fase 10 continúa sin ejecución real.

---

# RISK DEL DOCUMENTO

Tipo:

```text
TECHNICAL DOCUMENTATION /
INTERACTION FLOW
```

Risk histórico:

```text
INITIAL = 3
FINAL = 2
```

Esta normalización no altera la evaluación histórica.

Escala vigente:

```text
0–4
```

---

# CURRENT ARCHITECTURAL INTEGRATION STATE

```text
DOCUMENT:
ROBERT_TECHNICAL_INTERACTION_FLOW_SPEC

VERSION:
0.2

STATUS:
APPROVED / INTEGRATED / CANONICALLY NORMALIZED

ORIGINAL DECISION:
#014

ORIGINAL CHANGES:
#022
#023

CANONICAL_MODEL:
INTEGRATED

ORCHESTRATOR:
MASTER ROUTING AUTHORITY

IMPLEMENTATION_CONTRACTS:
INTEGRATED

AGENT_ARCHITECTURE:
INTEGRATED

SKILL_ARCHITECTURE:
INTEGRATED

MODEL_INTERFACE:
INTEGRATED

MEMORY_ARCHITECTURE:
INTEGRATED

VALIDATION_ARCHITECTURE:
INTEGRATED

TOOL_ARCHITECTURE:
INTEGRATED

DATA_MODEL:
INTEGRATED

ERROR_BLOCKING:
INTEGRATED

AUDIT_TRAIL:
INTEGRATED

UI_COMPONENTS:
PRESENTATION ONLY

TECHNICAL_IMPLEMENTATION:
NOT STARTED

REAL_TOOL_EXECUTION:
DISABLED

AUTOMATIC_MEMORY_WRITE:
DISABLED

AUTONOMOUS_AGENTS:
DISABLED

AUTONOMY_LEVEL:
0

EXECUTION_AUTHORITY:
NONE
```

---

# EFECTO DE ESTA NORMALIZACIÓN

Esta normalización:

```text
DOES NOT CREATE
A NEW DECISION

DOES NOT CREATE
A NEW APPROVAL

DOES NOT AUTHORIZE
IMPLEMENTATION

DOES NOT AUTHORIZE
TOOL EXECUTION

DOES NOT AUTHORIZE
AUTONOMOUS AGENTS
```

Sí:

* subordina Interaction Flow al Orchestrator;
* integra Implementation Contracts;
* convierte el flujo UI antiguo en representación visual del flujo interno;
* elimina `RiskBadge` como pseudo Risk evaluator con autoridad;
* elimina `ApprovalGate` como pseudo Approval authority;
* elimina `CommandCenter` como pseudo Router;
* integra Agents;
* integra Skills;
* integra Models;
* integra Memory;
* integra Tools;
* integra Validation;
* integra Permission;
* integra Scope;
* integra Audit;
* integra Error / Blocking;
* añade Data Minimization;
* añade Context Transfer controlado;
* añade contract validation;
* añade observability;
* mantiene límites estrictos de Fase 10.

---

# RESTRICCIONES

Se mantiene:

```text
TECHNICAL_IMPLEMENTATION = NOT STARTED

REAL_TOOL_EXECUTION = DISABLED

AUTOMATIC_MEMORY_WRITE = DISABLED

AUTONOMOUS_AGENTS = DISABLED

AUTONOMY_LEVEL = 0

EXECUTION_AUTHORITY = NONE
```

---

# CIERRE

`ROBERT_TECHNICAL_INTERACTION_FLOW_SPEC v0.2` permanece como la especificación técnica aprobada de interacción de Robert.

Su función actual es:

```text
DEFINE
HOW INFORMATION MOVES
WITHOUT REDEFINING
WHO HAS AUTHORITY
```

Regla final:

```text
USER
SETS AUTHORIZED INTENT

ORCHESTRATOR
COORDINATES AND ROUTES

AGENTS
SPECIALIZE

SKILLS
PROVIDE PROCEDURES

MODELS
PROVIDE INTELLIGENCE

TOOLS
PROVIDE TECHNICAL CAPABILITY

MEMORY
PROVIDES AUTHORIZED CONTEXTUAL RETRIEVAL

VALIDATION
CHECKS

GOVERNANCE
CONTROLS

AUDIT
RECORDS

UI
PRESENTS
```

Y siempre:

```text
INTERACTION FLOW
≠
ROUTING AUTHORITY
```
