# ROBERT_AGENT_ARCHITECTURE

**Versión:** 0.1
**Estado:** APROBADO — corrección de consistencia incorporada
**Tipo:** Especificación arquitectónica de Agents
**Ubicación:** `09_ARCHITECTURE/ROBERT_AGENT_ARCHITECTURE.md`
**Fase relacionada:** Fase 10 — MVP técnico básico en preparación
**Decisión de aprobación:** DECISIÓN #032
**Cambio de integración:** CAMBIO #055
CONSISTENCY_CORRECTION: #056


**Dependencias principales:**

* `ROBERT_CANONICAL_MODEL v0.2`
* `ROBERT_ORCHESTRATOR_SPEC v0.1`
* `ROBERT_SYSTEM_ARCHITECTURE`
* `ROBERT_MODULES`
* `ROBERT_CONTEXT_MASTER`
* `ROBERT_SECURITY_RULES`
* `ROBERT_COMMANDS`
* `ROBERT_TECHNICAL_PERMISSIONS_AND_SCOPES_SPEC`
* `ROBERT_TECHNICAL_DATA_CONSISTENCY_AND_CONFLICT_RESOLUTION_SPEC`
* `ROBERT_TECHNICAL_APPROVAL_AND_AUTHORIZATION_GATE_SPEC`
* `ROBERT_TECHNICAL_AUDIT_TRAIL_SPEC`
* ROBERT_SKILL_ARCHITECTURE v0.1

---

# 1. Propósito

`ROBERT_AGENT_ARCHITECTURE` define cómo funcionan conceptualmente los Agents dentro de Robert.

Su objetivo es establecer:

* qué es un Agent;
* qué responsabilidades puede tener;
* cómo recibe Tasks;
* cómo se relaciona con Modules;
* cómo utiliza Skills;
* cómo solicita capacidad de Models;
* cómo solicita acceso a Tools;
* qué Permissions necesita;
* qué Scopes debe respetar;
* cómo se evalúa Risk;
* qué nivel de Autonomy posee;
* qué Execution Authority posee;
* cómo se valida su trabajo;
* cómo escala problemas;
* cómo se registra su actividad;
* cómo puede colaborar con otros Agents.

Este documento no activa Agents reales por sí mismo.

---

# 2. Definición canónica

Según `ROBERT_CANONICAL_MODEL v0.2`:

> Un Agent es un especialista lógico que puede operar dentro de uno o más Modules para cumplir un objetivo definido.

Por tanto:

```text
AGENT ≠ MODEL
AGENT ≠ SKILL
AGENT ≠ TOOL
AGENT ≠ MODULE
AGENT ≠ USER
AGENT ≠ ROBERT
```

Un Agent coordina capacidades dentro de un objetivo especializado.

No es la capacidad en sí misma.

---

# 3. Principio arquitectónico

El Agent no debe convertirse en un mini-Robert.

```text
ROBERT
  ↓
ORCHESTRATOR
  ↓
AGENT
```

La autoridad y coordinación permanecen fuera del Agent.

El Agent opera dentro de:

```text
TASK
CONTEXT
CONSTRAINTS
PERMISSION
SCOPE
RISK
AUTONOMY
EXECUTION AUTHORITY
SECURITY
PHASE
```

Nunca fuera de ellos.

---

# 4. Posición dentro del sistema

```text
USER
  ↓
ROBERT
  ↓
ORCHESTRATOR
  ↓
MODULE
  ↓
AGENT
  ↓
CAPABILITY REQUEST
  ↓
SKILLS / MODELS / TOOLS
  ↓
VALIDATION
  ↓
OUTPUT
```

El Agent puede participar en uno o más Modules, pero siempre bajo routing y gobierno del Orchestrator.

---

# 5. Responsabilidades de un Agent

Un Agent puede:

* recibir una Task;
* interpretar un objetivo dentro de Context autorizado;
* identificar Skills necesarias;
* solicitar capacidad de Model;
* solicitar acceso a Tools;
* producir Analysis;
* producir Proposal;
* detectar Risks;
* detectar Conflicts;
* recomendar Actions;
* solicitar revisión;
* generar resultados;
* realizar Handoff;
* colaborar indirectamente con otros Agents mediante el Orchestrator.

Un Agent no puede:

* crear Permissions;
* ampliar Scope;
* crear Autonomy;
* concederse Execution Authority;
* aprobar su propia Action;
* cambiar Security Rules;
* cambiar el Canonical Model;
* modificar Decisions vigentes;
* cambiar Phase;
* ejecutar fuera del alcance autorizado;
* ocultar Conflicts;
* tratar una Proposal como Decision;
* saltarse el Orchestrator para obtener acceso privilegiado.

---

# 6. Regla de mediación

Cuando un Agent requiera una Skill, Model o Tool, debe expresar la necesidad como una solicitud de capacidad al Orchestrator.

El Agent no debe invocar directamente un Model o Tool fuera del routing autorizado.

Flujo preferido:

```text
AGENT
  ↓
CAPABILITY REQUEST
  ↓
ORCHESTRATOR
  ↓
SKILL / MODEL / TOOL RESOLUTION
```

Por tanto:

```text
AGENT REQUEST ≠ DIRECT INVOCATION
```

El Agent puede expresar preferencias técnicas, pero el Orchestrator conserva la autoridad de routing.

---

# 7. Agent Definition

Cada Agent deberá poder describirse conceptualmente con:

```text
agent_id
name
purpose
primary_module
supporting_modules
responsibilities
capabilities
skills
routing_requirements
model_preferences
tool_requirements
permissions
scopes
risk_policy
autonomy_level
execution_authority
approval_requirements
inputs
outputs
validation_requirements
escalation_rules
status
version
```

Esta definición es conceptual.

No autoriza todavía un nuevo modelo técnico de datos.

---

# 8. Agent Contract

Todo Agent debe tener un contrato mínimo.

Entrada conceptual:

```text
TASK
CONTEXT
CONSTRAINTS
PERMISSIONS
SCOPE
RISK
AUTONOMY
EXECUTION AUTHORITY
EXPECTED_OUTPUT
```

Salida conceptual:

```text
ANALYSIS
PROPOSAL
RISKS
CONFLICTS
CONFIDENCE
RECOMMENDATION
NEXT_ACTION
HANDOFF_REQUIRED
```

No todos los campos son obligatorios en todos los casos.

---

# 9. Agent Lifecycle

Se documentan los siguientes estados candidatos para una futura máquina de estados de Agent:

```text
DEFINED
REVIEWED
APPROVED
AVAILABLE
ASSIGNED
ACTIVE
COMPLETED
BLOCKED
DISABLED
REVOKED
SUPERSEDED
ARCHIVED
```

Estos estados no constituyen todavía una state machine oficial.

La state machine definitiva deberá aprobarse mediante:

* una especificación técnica;
* una revisión posterior de esta arquitectura;
* Decision;
* Change Control cuando corresponda.

---

# 10. Agent Status

Un Agent puede existir documentalmente sin estar activo.

Debe distinguirse entre:

```text
DOCUMENTED
APPROVED
IMPLEMENTED
AVAILABLE
ACTIVE
```

Ejemplo:

```text
ROBERT_ARCHITECT
status: DOCUMENTED
```

no significa:

```text
status: ACTIVE
```

---

# 11. Agent Routing

El Orchestrator determina si una Task necesita un Agent.

```text
TASK
  ↓
AGENT REQUIRED?
  ├── NO → continue without dedicated Agent
  └── YES
       ↓
     AGENT ROUTER
```

El Agent Router debe considerar:

```text
domain_match
module_match
capability_match
skill_requirements
permissions
scope
risk
task_complexity
model_requirements
tool_requirements
approval_requirements
```

---

# 12. Single-Agent Tasks

Una tarea puede utilizar un solo Agent.

Ejemplo:

```text
TASK:
Revisar arquitectura de memoria

AGENT:
ROBERT_ARCHITECT
```

Flujo:

```text
ORCHESTRATOR
  ↓
ROBERT_ARCHITECT
  ↓
CAPABILITY REQUEST
  ↓
SKILLS / MODEL / TOOLS
  ↓
VALIDATOR
```

---

# 13. Multi-Agent Tasks

Una tarea compleja puede requerir varios Agents.

Ejemplo:

```text
ROBERT_ARCHITECT
      ↓
proposal
      ↓
ORCHESTRATOR
      ↓
ROBERT_SECURITY
      ↓
security review
      ↓
ORCHESTRATOR
      ↓
ROBERT_CRITIC
      ↓
adversarial review
```

El Orchestrator sigue coordinando la secuencia.

Los Agents no se autoasignan otros Agents fuera de autorización.

---

# 14. Agent Collaboration

Se permiten conceptualmente tres formas de colaboración.

## 14.1 Sequential

```text
Agent A
  ↓
ORCHESTRATOR
  ↓
Agent B
  ↓
ORCHESTRATOR
  ↓
Agent C
```

## 14.2 Parallel

```text
          Task
           │
     ORCHESTRATOR
       /        \
  Agent A      Agent B
       \        /
        VALIDATOR
```

## 14.3 Adversarial

```text
Agent A
  ↓
Proposal
  ↓
ORCHESTRATOR
  ↓
Agent B
  ↓
Challenge
  ↓
Validator
```

---

# 15. Regla de no duplicación

Dos Agents pueden compartir Skills, pero no deben tener autoridad funcional ambigua sobre la misma Task.

Cuando exista solapamiento:

* uno debe ser `Primary`;
* el otro debe ser `Supporting`;
* el Orchestrator debe resolver ownership de la Task;
* el output final debe conservar trazabilidad.

Ejemplo:

```text
Architecture design

Primary:
ROBERT_ARCHITECT

Supporting:
ROBERT_STRATEGIST
```

Ejemplo:

```text
Roadmap prioritization

Primary:
ROBERT_STRATEGIST

Supporting:
ROBERT_ARCHITECT
```

---

# 16. Agent Authority

Un Agent no posee autoridad independiente.

```text
AGENT AUTHORITY
    ≤
AUTHORIZED TASK SCOPE
```

La autoridad efectiva depende de:

```text
USER
SECURITY
PHASE
PERMISSION
SCOPE
AUTONOMY
EXECUTION AUTHORITY
ORCHESTRATOR
```

---

# 17. Agent Permissions

Cada Agent debe operar con Permissions explícitos.

Ejemplo:

```text
ROBERT_RESEARCHER

Permission:
web_read

Scope:
research_sources_only
```

No implica:

```text
filesystem_write
github_write
email_send
```

---

# 18. Agent Scope

Scope limita dónde puede operar un Agent.

Ejemplos:

```text
single_task
single_module
single_repository
read_only
sandbox_only
no_external_action
```

Regla:

```text
AGENT PERMISSION ≠ UNLIMITED SCOPE
```

---

# 19. Agent Risk Policy

Risk clasifica el impacto, sensibilidad o peligrosidad de una Task, Proposal o Action.

Risk no define por sí mismo si un Agent puede ejecutar.

```text
RISK ≠ PERMISSION
RISK ≠ AUTONOMY
RISK ≠ EXECUTION AUTHORITY
```

Un Agent puede analizar Tasks de Risk elevado sin adquirir autoridad para ejecutarlas.

Ejemplo:

```text
ROBERT_SECURITY

analysis_allowed_risk:
0-4

execution_authority:
NONE
```

Durante Fase 10:

```text
AUTONOMY_LEVEL = 0
EXECUTION_AUTHORITY = NONE
```

para todos los Agents.

Una futura capacidad de ejecución deberá depender como mínimo de:

```text
PERMISSION
+
SCOPE
+
AUTONOMY
+
EXECUTION AUTHORITY
+
RISK EVALUATION
+
APPROVAL WHEN REQUIRED
```

Por tanto:

```text
LOW RISK ≠ AUTHORIZED EXECUTION
```

y:

```text
HIGH RISK ≠ INABILITY TO ANALYZE
```

---

# 20. Agent Autonomy

Autonomy representa el nivel autorizado de actuación independiente de un Agent.

Durante Fase 10:

```text
AUTONOMY_LEVEL = 0
```

Esto significa que los Agents permanecen:

```text
DOCUMENTAL
CONCEPTUAL
MANUAL
SUPERVISED
```

Autonomy no debe deducirse a partir de Risk.

```text
AUTONOMY ≠ RISK
```

---

# 21. Agent Execution Authority

Execution Authority determina si un Agent puede producir efectos ejecutivos reales.

Durante Fase 10:

```text
EXECUTION_AUTHORITY = NONE
```

para todos los Agents.

Esto se aplica aunque:

* el Risk sea 0;
* exista una Tool;
* exista Permission documental;
* el Model recomiende ejecutar;
* el Agent tenga Confidence alta.

```text
PERMISSION ALONE ≠ EXECUTION AUTHORITY
```

Una futura Execution Authority deberá ser explícita, acotada y compatible con Phase, Security, Scope y Approval.

---

# 22. Agent Approval Requirements

Un Agent debe conocer cuándo su resultado requiere Approval antes de continuar.

Ejemplos:

```text
canonical_change
security_policy_change
external_action
persistent_memory_change
repository_write
destructive_test
```

Regla:

```text
AGENT RECOMMENDATION
    ≠
APPROVED ACTION
```

---

# 23. Agent Skills

Un Agent no debe contener toda su lógica internamente.

Debe utilizar Skills reutilizables.

Ejemplo:

```text
ROBERT_ARCHITECT
  ↓
skills:
- architecture_review
- dependency_analysis
- contradiction_detection
```

Esto permite que otros Agents reutilicen las mismas capacidades.

---

# 24. Agent Model Usage

Un Agent puede expresar una necesidad o preferencia de Model.

Ejemplo:

```text
ROBERT_ARCHITECT

model_preference:
Claude
```

Pero:

```text
AGENT ≠ MODEL
```

y:

```text
MODEL PREFERENCE ≠ MODEL SELECTION AUTHORITY
```

La selección final corresponde al Orchestrator / Model Router.

---

# 25. Model Independence

Preferencia arquitectónica:

```text
AGENT
  ↓
CAPABILITY REQUEST
  ↓
SKILL
  ↓
MODEL INTERFACE
  ↓
MODEL
```

No:

```text
AGENT
  ↓
CLAUDE-SPECIFIC LOGIC
```

Los adaptadores específicos se definirán en `ROBERT_MODEL_INTERFACE_SPEC`.

---

# 26. Agent Tool Usage

Un Agent puede solicitar una Tool cuando sea necesaria.

Ejemplo:

```text
ROBERT_RESEARCHER
  ↓
request:
web_read
```

o:

```text
ROBERT_CODER
  ↓
request:
filesystem / terminal / GitHub
```

Pero:

```text
REQUEST TOOL
    ≠
AUTHORIZED TOOL USE
```

El Orchestrator debe validar:

* Permission;
* Scope;
* Risk;
* Autonomy;
* Execution Authority;
* Phase;
* Approval.

---

# 27. Agent Memory Access

El acceso a Memory debe limitarse.

Un Agent puede requerir acceso a:

```text
CORE
SEMANTIC
EPISODIC
DECISIONAL
PROCEDURAL
```

pero no todos los Agents necesitan todos los tipos.

Ejemplo:

```text
ROBERT_ARCHITECT

memory_access:
- CORE
- SEMANTIC
- DECISIONAL
```

---

# 28. Agent Context

El Orchestrator debe entregar al Agent el Context mínimo suficiente.

Principio:

```text
MINIMUM SUFFICIENT CONTEXT
```

No debe entregarse automáticamente:

* toda la memoria;
* todos los documentos;
* todos los mensajes;
* todas las decisiones históricas.

Esto reduce:

* ruido;
* costo;
* riesgo;
* contradicciones;
* exposición innecesaria.

---

# 29. Agent Validation

El resultado de un Agent puede requerir validación.

Tipos:

```text
SELF_VALIDATION
RULE_VALIDATION
AGENT_REVIEW
MODEL_REVIEW
SECURITY_REVIEW
USER_REVIEW
```

La validación dependerá de:

```text
risk
impact
task_type
output_type
external_effect
canonical_effect
```

Validation no concede autoridad ejecutiva.

```text
VALIDATION ≠ AUTHORIZATION
```

---

# 30. Agent Escalation

Un Agent debe escalar cuando exista:

```text
permission_missing
scope_exceeded
risk_too_high
conflict_detected
context_missing
uncertainty_high
security_issue
approval_required
task_outside_domain
validation_failure
execution_authority_missing
```

Flujo:

```text
AGENT
  ↓
ESCALATE
  ↓
ORCHESTRATOR
  ↓
USER / SECURITY / VALIDATOR
```

---

# 31. Agent Failure

Si un Agent falla:

```text
AGENT_FAILURE
  ↓
CLASSIFY
  ↓
CAN RETRY?
  ├── YES → controlled retry
  └── NO
       ↓
FALLBACK / ESCALATE / BLOCK
```

Posibles fallos:

```text
INVALID_OUTPUT
MODEL_FAILURE
TOOL_FAILURE
CONTEXT_FAILURE
PERMISSION_FAILURE
SCOPE_FAILURE
VALIDATION_FAILURE
ROUTING_FAILURE
EXECUTION_AUTHORITY_FAILURE
```

---

# 32. Agent Replacement

En fases futuras, un Agent podrá cambiar de Model sin cambiar su identidad.

Ejemplo:

```text
ROBERT_ARCHITECT
  ↓
Claude unavailable
  ↓
ORCHESTRATOR
  ↓
ChatGPT
```

El contrato del Agent debe permanecer igual.

---

# 33. Agent Versioning

Cada Agent debe poder registrar:

```text
agent_version
definition_version
skill_dependencies
model_interface_version
```

Ejemplo:

```text
ROBERT_ARCHITECT
version: 0.1
```

Las modificaciones sustanciales requieren Change Control.

---

# 34. Agent Observability

Cada ejecución futura deberá poder registrar:

```text
agent_id
task_id
module
skills_requested
skills_used
models_requested
models_used
tools_requested
tools_used
risk
permissions
scope
autonomy
execution_authority
approval
result
validation
errors
duration
```

Esto deberá integrarse con Audit.

---

# 35. Catálogo inicial aprobado

La v0.1 reconoce **8 Agents iniciales**.

```text
ROBERT_ARCHITECT
ROBERT_RESEARCHER
ROBERT_CRITIC
ROBERT_SECURITY
ROBERT_MEMORY
ROBERT_CODER
ROBERT_TESTER
ROBERT_STRATEGIST
```

El catálogo está aprobado documentalmente mediante DECISIÓN #032.

No implica implementación ni activación.

---

# 36. ROBERT_ARCHITECT

**Propósito:** diseñar y revisar arquitectura.

Responsabilidades:

* arquitectura de Robert;
* componentes;
* relaciones;
* dependencias;
* límites;
* modularidad;
* escalabilidad conceptual;
* coherencia estructural.

Modules principales:

```text
ARCHITECTURE
SYSTEM
```

Skills futuras:

```text
architecture_design
architecture_review
dependency_analysis
contradiction_detection
```

Ownership principal:

```text
architecture_design
system_structure
technical_dependency_design
```

Estado en Fase 10:

```text
AUTONOMY_LEVEL: 0
EXECUTION_AUTHORITY: NONE
```

---

# 37. ROBERT_RESEARCHER

**Propósito:** investigar información externa o interna.

Responsabilidades:

* documentación;
* tecnologías;
* herramientas;
* papers;
* estándares;
* alternativas;
* evidencia.

Skills:

```text
web_research
source_validation
comparison
evidence_synthesis
```

Tools futuras:

```text
web
documents
```

Estado en Fase 10:

```text
AUTONOMY_LEVEL: 0
EXECUTION_AUTHORITY: NONE
```

---

# 38. ROBERT_CRITIC

**Propósito:** desafiar propuestas.

Responsabilidades:

* encontrar errores;
* detectar contradicciones;
* identificar supuestos;
* detectar sobreingeniería;
* evaluar trade-offs;
* producir contraargumentos.

Skills:

```text
adversarial_review
contradiction_detection
assumption_analysis
tradeoff_analysis
```

Principio:

```text
CRITIC ≠ DECISION MAKER
```

Estado en Fase 10:

```text
AUTONOMY_LEVEL: 0
EXECUTION_AUTHORITY: NONE
```

---

# 39. ROBERT_SECURITY

**Propósito:** revisar seguridad y gobierno.

Responsabilidades:

* Permission;
* Scope;
* Risk;
* Security Rules;
* Approval requirements;
* Tool access;
* autonomy limits;
* execution authority;
* data exposure.

Skills:

```text
security_review
permission_analysis
scope_analysis
risk_assessment
```

Puede analizar Risk 0-4.

No puede autoaprobar Actions.

Estado:

```text
analysis_allowed_risk: 0-4
AUTONOMY_LEVEL: 0
EXECUTION_AUTHORITY: NONE
```

---

# 40. ROBERT_MEMORY

**Propósito:** gestionar el diseño conceptual de Memory.

Responsabilidades:

* Memory Type;
* Retention;
* memory eligibility;
* source;
* authority;
* confidence;
* conflicts;
* memory lifecycle.

Skills:

```text
memory_classification
memory_extraction
memory_conflict_detection
retention_analysis
```

En Fase 10 no almacena Memory automáticamente.

Estado:

```text
AUTONOMY_LEVEL: 0
EXECUTION_AUTHORITY: NONE
```

---

# 41. ROBERT_CODER

**Propósito:** diseñar y producir trabajo técnico de software.

Responsabilidades futuras:

* código;
* debugging;
* refactoring;
* tests;
* technical implementation;
* integration.

Skills:

```text
code_generation
code_review
debugging
testing
refactoring
```

Tools futuras:

```text
filesystem
terminal
GitHub
```

Durante Fase 10 puede producir código como output documental o trabajar dentro de Sandbox cuando exista autorización explícita.

Fuera de ello:

```text
AUTONOMY_LEVEL: 0
EXECUTION_AUTHORITY: NONE
```

---

# 42. ROBERT_TESTER

**Propósito:** intentar romper diseños y sistemas de forma controlada.

Responsabilidades:

* edge cases;
* failure modes;
* integration failures;
* security tests;
* routing tests;
* permission tests;
* conflict tests.

Skills:

```text
test_design
edge_case_analysis
failure_injection
adversarial_testing
```

Estado:

```text
AUTONOMY_LEVEL: 0
EXECUTION_AUTHORITY: NONE
```

Las pruebas destructivas requerirán autorización específica cuando lleguen a existir técnicamente.

---

# 43. ROBERT_STRATEGIST

**Propósito:** priorización y roadmap.

Responsabilidades:

* prioridades;
* sequencing;
* roadmap;
* trade-offs;
* build vs defer;
* complexity control;
* phase planning.

Skills:

```text
prioritization
roadmapping
tradeoff_analysis
dependency_planning
```

Ownership principal:

```text
roadmap_prioritization
build_sequence
phase_planning
```

No sustituye al Architect en decisiones de diseño arquitectónico.

Estado:

```text
AUTONOMY_LEVEL: 0
EXECUTION_AUTHORITY: NONE
```

---

# 44. Agent Matrix

| Agent             | Primary Purpose    | Analysis Risk | Tool Need | Execution Authority |
| ----------------- | ------------------ | ------------- | --------- | ------------------- |
| ROBERT_ARCHITECT  | Architecture       | Variable      | Low       | NONE                |
| ROBERT_RESEARCHER | Research           | Variable      | Medium    | NONE                |
| ROBERT_CRITIC     | Adversarial review | Variable      | Low       | NONE                |
| ROBERT_SECURITY   | Security review    | 0–4           | Low       | NONE                |
| ROBERT_MEMORY     | Memory design      | Variable      | Low       | NONE                |
| ROBERT_CODER      | Software           | Variable      | High      | NONE                |
| ROBERT_TESTER     | Testing            | Variable      | Medium    | NONE                |
| ROBERT_STRATEGIST | Strategy           | Variable      | Low       | NONE                |

Risk describe la tarea.

No concede Execution Authority.

---

# 45. Agent Selection Examples

## Example A

Task:

```text
Diseña una nueva arquitectura de memoria.
```

Routing:

```text
Primary:
ROBERT_MEMORY

Supporting:
ROBERT_ARCHITECT
ROBERT_SECURITY
ROBERT_CRITIC
```

---

## Example B

Task:

```text
Busca qué vector database conviene.
```

Routing:

```text
Primary:
ROBERT_RESEARCHER

Supporting:
ROBERT_ARCHITECT
ROBERT_SECURITY
```

---

## Example C

Task:

```text
Encuentra los errores de este diseño.
```

Routing:

```text
Primary:
ROBERT_CRITIC

Supporting:
ROBERT_TESTER
```

---

## Example D

Task:

```text
Define qué construir primero durante los próximos tres meses.
```

Routing:

```text
Primary:
ROBERT_STRATEGIST

Supporting:
ROBERT_ARCHITECT
```

---

# 46. Agent Composition

Un Agent puede componerse conceptualmente de:

```text
AGENT
│
├── IDENTITY
├── ROLE
├── MODULES
├── CAPABILITIES
├── SKILLS
├── ROUTING REQUIREMENTS
├── MODEL POLICY
├── TOOL POLICY
├── MEMORY POLICY
├── PERMISSIONS
├── SCOPES
├── RISK POLICY
├── AUTONOMY
├── EXECUTION AUTHORITY
├── APPROVAL REQUIREMENTS
├── VALIDATION
└── ESCALATION
```

---

# 47. Agent Manifest

Cada Agent futuro deberá tener un manifest.

Formato conceptual:

```yaml
agent:
  id:
  name:
  version:
  purpose:

modules:
  primary:
  supporting:

capabilities:

skills:

routing:
  requirements:

models:
  preferred:
  allowed:
  fallback:

tools:
  requested:
  allowed:

memory:
  allowed_types:
  allowed_retention:

permissions:

scopes:

risk:
  analysis_range:
  recommendation_range:
  escalation_threshold:

autonomy:
  level:

execution:
  authority:

approval:
  requirements:

validation:

escalation:
```

Durante Fase 10:

```yaml
autonomy:
  level: 0

execution:
  authority: NONE
```

El formato técnico exacto se definirá posteriormente.

---

# 48. Agent Communication

Los Agents no deben comunicarse libremente sin coordinación.

Preferencia:

```text
Agent A
  ↓
ORCHESTRATOR
  ↓
Agent B
```

No:

```text
Agent A ↔ Agent B
```

sin trazabilidad.

Esto permite:

* control;
* auditoría;
* routing;
* permisos;
* contexto consistente.

---

# 49. Structured Context Transfer

El Orchestrator puede transferir entre Agents:

* resumen estructurado;
* análisis;
* artefacto;
* evidencia;
* output parcial;
* Context autorizado.

Esto no se considera comunicación autónoma Agent-to-Agent.

Flujo:

```text
Agent A
  ↓
structured output
  ↓
ORCHESTRATOR
  ↓
authorized context
  ↓
Agent B
```

El Orchestrator determina qué información es necesaria para el siguiente Agent.

---

# 50. Agent Handoff

Un Agent puede devolver:

```text
HANDOFF_REQUIRED
```

acompañado de:

```text
target_capability
reason
context_summary
risk
unresolved_questions
recommended_next_step
```

El Agent puede recomendar una capacidad siguiente.

El Orchestrator decide el siguiente Agent.

```text
HANDOFF RECOMMENDATION ≠ ROUTING AUTHORITY
```

---

# 51. Agent Conflict

Dos Agents pueden producir conclusiones incompatibles.

Ejemplo:

```text
ROBERT_ARCHITECT:
"Implementar X"

ROBERT_SECURITY:
"X viola Scope"
```

Resultado:

```text
CONFLICT
  ↓
ORCHESTRATOR
  ↓
CONFLICT RESOLUTION
```

Nunca:

```text
FIRST AGENT WINS
```

ni:

```text
MAJORITY OF AGENTS = TRUTH
```

---

# 52. Agent Confidence

Los Agents pueden reportar Confidence.

Ejemplo:

```text
confidence: 0.68
```

Pero:

```text
CONFIDENCE ≠ AUTHORITY
CONFIDENCE ≠ PERMISSION
CONFIDENCE ≠ TRUTH
CONFIDENCE ≠ EXECUTION AUTHORITY
```

---

# 53. Agent Proposal Rule

Salida de un Agent:

```text
PROPOSAL
```

no se convierte automáticamente en:

```text
DECISION
```

Flujo correcto:

```text
AGENT
  ↓
PROPOSAL
  ↓
VALIDATION
  ↓
ORCHESTRATOR
  ↓
USER / AUTHORITY
  ↓
DECISION
```

---

# 54. Security Invariants

Ningún Agent puede:

```text
BYPASS SECURITY
CREATE PERMISSIONS
EXPAND SCOPE
CREATE AUTONOMY
CREATE EXECUTION AUTHORITY
SELF-APPROVE
ALTER PHASE
ALTER CANONICAL MODEL
HIDE CONFLICT
EXECUTE OUTSIDE AUTHORITY
BYPASS ORCHESTRATOR ROUTING
```

---

# 55. Governance Invariants

```text
USER > AGENT

ROBERT > AGENT

ORCHESTRATOR ROUTING > AGENT SELF-ASSIGNMENT

SECURITY > AGENT OBJECTIVE

PERMISSION > AGENT CAPABILITY

SCOPE > AGENT INTENT

APPROVED DECISION > AGENT PROPOSAL

VALIDATION ≠ AUTHORIZATION

RISK ≠ AUTONOMY

RISK ≠ EXECUTION AUTHORITY

PERMISSION ≠ EXECUTION AUTHORITY
```

---

# 56. Fase 10

Durante Fase 10, los Agents definidos aquí son:

```text
DOCUMENTAL
CONCEPTUAL
MANUAL
SUPERVISED
```

Y para todos:

```text
AUTONOMY_LEVEL = 0
EXECUTION_AUTHORITY = NONE
```

No existen como procesos autónomos reales.

---

# 57. Permitido en Fase 10

Sí se permite:

* definir Agents;
* simular routing;
* asignar Agents manualmente;
* diseñar manifests;
* diseñar Skills;
* diseñar tests;
* comparar Models;
* probar workflows en Sandbox;
* producir Analysis;
* producir Proposals;
* producir código como output documental cuando corresponda.

---

# 58. No permitido en Fase 10

No se permite:

* ejecución autónoma;
* Agents persistentes ejecutándose solos;
* loops automáticos;
* Tool access automático;
* Memory writes automáticos;
* Agent-to-Agent messaging autónomo;
* self-modification;
* self-replication;
* self-approval;
* routing fuera del Orchestrator;
* creación autónoma de Permissions;
* creación autónoma de Scope;
* creación autónoma de Execution Authority.

---

# 59. Sandbox Tests futuros

```text
TEST 1
Correct Agent selected

TEST 2
Wrong Module rejected

TEST 3
Permission missing

TEST 4
Scope exceeded

TEST 5
Agent conflict

TEST 6
Model unavailable

TEST 7
Tool unavailable

TEST 8
High risk escalation

TEST 9
Agent handoff

TEST 10
Multi-Agent validation

TEST 11
Agent attempts direct Tool access

TEST 12
Agent attempts direct Model invocation

TEST 13
Primary / Supporting ownership conflict

TEST 14
Low Risk but no Execution Authority

TEST 15
High Risk analysis without execution

TEST 16
Agent attempts to create Autonomy

TEST 17
Agent attempts to create Execution Authority
```

---

# 60. Métricas futuras

```text
agent_selection_accuracy
task_success_rate
handoff_rate
validation_failure_rate
conflict_detection_rate
tool_request_efficiency
context_efficiency
user_correction_rate
risk_escalation_accuracy
routing_bypass_attempts
unauthorized_execution_attempts
```

---

# 61. Skill Architecture vigente

`ROBERT_SKILL_ARCHITECTURE v0.1` está aprobada mediante DECISIÓN #033 y CAMBIO #057.

Los Agents deberán solicitar capacidades mediante:

```text
AGENT
  ↓
CAPABILITY REQUEST
  ↓
ORCHESTRATOR
  ↓
SKILL RESOLVER
  ↓
SKILL
---

# 62. Dependencia con Model Interface

Los Agents no deberán invocar Claude o ChatGPT directamente mediante lógica propietaria.

La relación futura será:

```text
AGENT
  ↓
CAPABILITY REQUEST
  ↓
SKILL
  ↓
MODEL INTERFACE
  ↓
MODEL
```

---

# 63. Dependencia con Memory Architecture

El acceso de cada Agent a Memory deberá definirse en:

```text
ROBERT_MEMORY_ARCHITECTURE
```

Agent Architecture únicamente establece:

```text
MINIMUM NECESSARY MEMORY ACCESS
```

---

# 64. Dependencia con Validation Architecture

Las políticas comunes de evaluación de outputs deberán formalizarse posteriormente en:

```text
ROBERT_VALIDATION_ARCHITECTURE
```

Los Agents únicamente declaran qué tipo de validación requieren.

---

# 65. Orden de construcción

Después de cerrar este documento:

```text
AGENT ARCHITECTURE
      ↓
SKILL ARCHITECTURE
      ↓
MODEL INTERFACE
      ↓
MEMORY ARCHITECTURE
      ↓
VALIDATION ARCHITECTURE
```

---

# 66. Decisiones pendientes antes de v1.0

Todavía deberán resolverse:

1. criterios exactos de Agent Router;
2. estructura final de Agent Manifest;
3. lifecycle técnico;
4. reglas de multi-Agent parallelism;
5. reglas técnicas de Handoff;
6. límite de Agents simultáneos;
7. políticas definitivas de Memory Access;
8. políticas definitivas de Tool Access;
9. Model preferences;
10. fallback behavior;
11. auditoría técnica;
12. formato técnico de Capability Request;
13. ownership rules completas;
14. política futura de Autonomy;
15. política futura de Execution Authority.

---

# 67. Estado actual

```text
DOCUMENT: ROBERT_AGENT_ARCHITECTURE
VERSION: 0.1
STATUS: APPROVED
AUTHORITY: ARCHITECTURAL
DECISION: #032
CHANGE: #055
CONSISTENCY_CORRECTION: #056_PENDING_REGISTRATION
PHASE: 10
IMPLEMENTATION: NONE
AUTONOMY_LEVEL: 0
EXECUTION_AUTHORITY: NONE
```

---

# 68. Corrección de consistencia incorporada

Esta versión incorpora la separación formal entre:

```text
RISK
AUTONOMY
EXECUTION AUTHORITY
```

Reglas resultantes:

```text
RISK ≠ AUTONOMY
RISK ≠ EXECUTION AUTHORITY
PERMISSION ≠ EXECUTION AUTHORITY
LOW RISK ≠ AUTHORIZED EXECUTION
```

La corrección deberá registrarse formalmente como:

```text
CAMBIO #056 — Separación de Risk, Autonomy y Execution Authority en Agent Architecture
```

---

# 69. Próximo paso recomendado

Después de registrar CAMBIO #056, el siguiente documento será:

```text
ROBERT_SKILL_ARCHITECTURE v0.1
```

Esto permitirá mantener explícitamente:

```text
AGENT = quién trabaja
SKILL = cómo trabaja
MODEL = quién procesa
TOOL = con qué interactúa
ORCHESTRATOR = quién coordina
ROBERT = quién gobierna el sistema
```
