# ROBERT_SKILL_ARCHITECTURE

**Versión:** 0.1
**Estado:** APROBADA
**Tipo:** Especificación arquitectónica de Skills
**Ubicación propuesta:** `09_ARCHITECTURE/ROBERT_SKILL_ARCHITECTURE.md`
**Fase relacionada:** Fase 10 — MVP técnico básico en preparación

**Dependencias principales:**

* `ROBERT_CANONICAL_MODEL v0.2`
* `ROBERT_ORCHESTRATOR_SPEC v0.1`
* `ROBERT_AGENT_ARCHITECTURE v0.1`
* `ROBERT_SYSTEM_ARCHITECTURE`
* `ROBERT_MODULES`
* `ROBERT_SECURITY_RULES`
* `ROBERT_CONTEXT_MASTER`
* `ROBERT_TECHNICAL_PERMISSIONS_AND_SCOPES_SPEC`
* `ROBERT_TECHNICAL_DATA_CONSISTENCY_AND_CONFLICT_RESOLUTION_SPEC`
* `ROBERT_TECHNICAL_APPROVAL_AND_AUTHORIZATION_GATE_SPEC`

---

# 1. Propósito

`ROBERT_SKILL_ARCHITECTURE` define cómo funcionan conceptualmente las Skills dentro de Robert.

Una Skill representa un procedimiento reutilizable para realizar una clase concreta de trabajo.

Su función es separar:

```text
AGENT = quién trabaja
SKILL = cómo trabaja
MODEL = quién procesa
TOOL = con qué interactúa
ORCHESTRATOR = quién coordina
ROBERT = quién gobierna
```

Este documento no activa Skills ejecutables reales.

---

# 2. Definición canónica

Según `ROBERT_CANONICAL_MODEL v0.2`:

> Una Skill define cómo realizar una clase reutilizable de trabajo.

Por tanto:

```text
SKILL ≠ AGENT
SKILL ≠ MODEL
SKILL ≠ TOOL
SKILL ≠ MODULE
SKILL ≠ COMMAND
SKILL ≠ ROBERT
```

Una Skill describe procedimiento.

No posee identidad operativa independiente.

---

# 3. Principio fundamental

Una Skill debe ser lo más independiente posible del proveedor.

Preferencia:

```text
SKILL
  ↓
MODEL INTERFACE
  ↓
MODEL
```

No:

```text
SKILL
  ↓
CLAUDE-SPECIFIC PROMPT
```

salvo que exista un Adapter específico autorizado.

---

# 4. Posición arquitectónica

```text
USER
  ↓
ROBERT
  ↓
ORCHESTRATOR
  ↓
AGENT
  ↓
CAPABILITY REQUEST
  ↓
SKILL RESOLVER
  ↓
SKILL
  ↓
MODEL / TOOL WHEN REQUIRED
  ↓
VALIDATION
  ↓
OUTPUT
```

Una Skill no se autoejecuta.

Debe ser seleccionada dentro de routing autorizado.

---

# 5. Responsabilidad de una Skill

Una Skill puede definir:

* objetivo;
* procedimiento;
* entradas;
* salidas;
* pasos;
* restricciones;
* precondiciones;
* postcondiciones;
* evidencias requeridas;
* fuentes requeridas;
* criterios de calidad;
* Model requirements;
* Tool requirements;
* Permission requirements;
* Scope requirements;
* Risk considerations;
* Approval requirements;
* Validation requirements;
* Failure behavior.

---

# 6. Lo que una Skill NO puede hacer

Una Skill no puede:

* elegir unilateralmente un Agent;
* crear Permissions;
* poseer Permissions propios;
* ampliar Scope;
* poseer Scope propio;
* crear Autonomy;
* crear Execution Authority;
* autoaprobar una Action;
* modificar Canonical Model;
* cambiar Phase;
* invocar Tools fuera del routing;
* invocar Models fuera del routing;
* ocultar Conflicts;
* persistir Memory por sí sola;
* crear routing paralelo al Orchestrator.

---

# 7. Skill Definition

Cada Skill deberá poder describirse conceptualmente con:

```text
skill_id
name
version
purpose
description
category
capabilities
inputs
outputs
preconditions
procedure
postconditions
evidence_requirements
source_requirements
model_requirements
tool_requirements
permission_requirements
scope_requirements
risk_policy
approval_requirements
validation_requirements
failure_modes
fallback_behavior
compatible_agents
dependencies
overlap_notes
status
```

Esto es conceptual.

No crea todavía un nuevo modelo técnico de datos.

---

# 8. Skill Contract

Entrada conceptual:

```text
TASK
CONTEXT
INPUTS
CONSTRAINTS
PERMISSIONS
SCOPE
RISK
EVIDENCE_REQUIREMENTS
SOURCE_REQUIREMENTS
EXPECTED_OUTPUT
```

Salida conceptual:

```text
RESULT
EVIDENCE
SOURCES
RISKS
CONFLICTS
CONFIDENCE
LIMITATIONS
VALIDATION_STATUS
NEXT_RECOMMENDATION
```

No todos los campos son obligatorios para todas las Skills.

---

# 9. Skill Reusability

Una Skill debe poder reutilizarse entre distintos Agents cuando tenga sentido.

Ejemplo:

```text
contradiction_detection
```

puede ser utilizada por:

```text
ROBERT_ARCHITECT
ROBERT_CRITIC
ROBERT_SECURITY
ROBERT_MEMORY
```

Esto evita duplicar procedimientos.

---

# 10. Skill Ownership

Una Skill no pertenece exclusivamente a un Agent salvo necesidad explícita.

Preferencia:

```text
SHARED SKILL
```

antes que:

```text
AGENT-SPECIFIC DUPLICATE
```

Ejemplo incorrecto:

```text
architect_contradiction_detection
critic_contradiction_detection
security_contradiction_detection
```

si todos realizan esencialmente el mismo procedimiento.

Preferencia:

```text
contradiction_detection
```

con distintos parámetros o Context.

---

# 11. Skill Resolver

El Orchestrator determina qué Skill necesita una Task.

```text
TASK
  ↓
CAPABILITY NEED
  ↓
SKILL RESOLVER
  ↓
SKILL
```

Criterios:

```text
capability_match
task_type
agent_role
inputs_available
evidence_requirements
source_requirements
model_requirements
tool_requirements
permissions
scope
risk
validation_requirements
```

---

# 12. Capability Request

Un Agent no debe invocar una Skill unilateralmente fuera del routing.

Flujo:

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
```

Regla:

```text
AGENT REQUEST ≠ SKILL EXECUTION AUTHORITY
```

---

# 13. Skill Categories

Se proponen inicialmente las siguientes categorías:

```text
ANALYSIS
RESEARCH
ARCHITECTURE
SECURITY
MEMORY
CODE
TESTING
STRATEGY
VALIDATION
DOCUMENTATION
```

Estas categorías son conceptuales y podrán evolucionar.

---

# 14. Skill Types

Se distinguen inicialmente tres tipos.

## 14.1 Cognitive Skill

No requiere efecto externo.

Ejemplos:

```text
architecture_review
tradeoff_analysis
contradiction_detection
```

## 14.2 Retrieval Skill

Necesita recuperar información.

Ejemplos:

```text
web_research
document_retrieval
evidence_collection
```

Puede requerir Tools.

## 14.3 Action-Oriented Skill

Describe un procedimiento que potencialmente produce una Action.

Ejemplos futuros:

```text
repository_update
send_message
database_update
```

Durante Fase 10:

```text
EXECUTION_AUTHORITY = NONE
```

por lo que estas Skills permanecen documentales.

---

# 15. Skill Procedure

Cada Skill debe definir un procedimiento reproducible.

Ejemplo:

```text
contradiction_detection

1. Identify claims.
2. Normalize concepts.
3. Retrieve canonical definitions.
4. Compare claims.
5. Detect incompatibilities.
6. Classify conflict.
7. Produce evidence.
8. Identify limitations.
9. Recommend resolution.
```

Una Skill no debe ser únicamente:

```text
"Analyze this carefully."
```

Debe contener estructura reutilizable.

---

# 16. Preconditions

Una Skill puede requerir precondiciones.

Ejemplo:

```text
architecture_review

preconditions:
- architecture document available
- canonical model available
- current phase known
```

Si faltan:

```text
PRECONDITION_FAILURE
```

y debe escalarse o solicitarse Context.

---

# 17. Postconditions

Una Skill puede declarar qué debe ser verdad al completarse.

Ejemplo:

```text
contradiction_detection

postconditions:
- conflicts classified
- evidence attached
- sources identified when applicable
- unresolved items identified
- limitations reported
```

---

# 18. Skill Inputs

Los Inputs deben ser explícitos.

Ejemplo:

```text
architecture_review

inputs:
- target_document
- canonical_definitions
- related_decisions
- security_constraints
```

Esto reduce dependencia de prompts ambiguos.

---

# 19. Skill Outputs

Los Outputs deben ser estructurables.

Ejemplo:

```text
architecture_review

outputs:
- findings
- conflicts
- evidence
- sources
- risks
- recommendations
- limitations
- confidence
```

---

# 20. Evidence Requirements

Una Skill puede requerir evidencia explícita.

Ejemplo:

```text
web_research

evidence_requirements:
- factual claims supported
- relevant sources identified
- uncertainty disclosed
```

Cuando una Skill no necesite evidencia externa, este requisito puede ser:

```text
NONE
```

---

# 21. Source Requirements

Una Skill puede declarar requisitos de fuente.

Ejemplo:

```text
source_validation

source_requirements:
- identifiable source
- relevant provenance
- freshness when applicable
- authority assessment
```

La existencia de una Source no garantiza que sea correcta.

```text
SOURCE ≠ TRUTH
```

---

# 22. Model Requirements

Una Skill puede necesitar ciertas capacidades del Model.

Ejemplo:

```text
architecture_review

model_requirements:
- long_context
- structured_reasoning
- document_analysis
```

Pero no debe exigir directamente:

```text
Claude
```

salvo una necesidad explícita y documentada.

---

# 23. Model Preference

Una Skill puede expresar preferencias de capacidad:

```text
preferred_model_capabilities:
- long_context
- high_reasoning
```

No debería establecer como regla rígida:

```text
preferred_model: Claude
```

La selección corresponde al Model Router.

---

# 24. Tool Requirements

Una Skill puede requerir Tools.

Ejemplo:

```text
web_research

tool_requirements:
- web_read
```

Pero:

```text
TOOL REQUIREMENT ≠ TOOL AUTHORIZATION
```

El Orchestrator debe comprobar Permission y Scope.

---

# 25. Permission Requirements

Una Skill puede declarar:

```text
permission_requirements
```

Ejemplo:

```text
web_research:
- web_read
```

o:

```text
repository_update:
- github_write
```

Declarar un Permission requerido no lo concede.

---

# 26. Regla de requisitos de autorización

Una Skill puede declarar qué Permission y Scope son necesarios para utilizarla en una operación determinada.

La Skill no posee Permissions ni Scope propios.

```text
SKILL DECLARES REQUIREMENTS
        ≠
SKILL OWNS AUTHORIZATION
```

La autorización efectiva pertenece al contexto operativo y debe ser validada por el Orchestrator.

Por tanto:

```text
SKILL REQUIREMENT ≠ PERMISSION
SKILL REQUIREMENT ≠ SCOPE
```

---

# 27. Scope Requirements

La Skill debe declarar el Scope necesario cuando corresponda.

Ejemplo:

```text
repository_update

scope_requirement:
- repository_current
```

No implica:

```text
all_repositories
```

El Scope efectivo debe provenir del contexto autorizado.

---

# 28. Risk Policy

Una Skill puede analizar Risk o declarar factores de Risk.

Pero:

```text
RISK ≠ PERMISSION
RISK ≠ AUTONOMY
RISK ≠ EXECUTION AUTHORITY
```

Una Skill de alto impacto puede existir documentalmente sin poder ejecutarse.

---

# 29. Autonomy

Una Skill no tiene Autonomy propia.

```text
SKILL AUTONOMY = NONE
```

La Autonomy pertenece al contexto operativo autorizado del sistema.

Durante Fase 10:

```text
AUTONOMY_LEVEL = 0
```

---

# 30. Execution Authority

Una Skill no puede concederse Execution Authority.

Durante Fase 10:

```text
EXECUTION_AUTHORITY = NONE
```

para cualquier uso operativo de Skills.

Una Skill puede describir una Action futura sin autorizarla.

```text
ACTION PROCEDURE ≠ AUTHORIZED ACTION
```

---

# 31. Approval Requirements

Una Skill debe poder declarar cuándo su uso o resultado requiere Approval.

Ejemplos:

```text
persistent_memory_write
repository_write
external_message_send
security_policy_change
canonical_change
destructive_test
```

Declarar Approval Required no constituye aprobación.

---

# 32. Skill Validation

Cada Skill podrá especificar cómo debe validarse su resultado.

Ejemplo:

```text
architecture_review

validation:
- canonical_compliance
- contradiction_check
- completeness_check
```

Tipos posibles:

```text
SELF_VALIDATION
RULE_VALIDATION
AGENT_REVIEW
MODEL_REVIEW
SECURITY_REVIEW
USER_REVIEW
```

---

# 33. Skill Failure Modes

Una Skill debe poder declarar fallos previsibles.

Ejemplos:

```text
MISSING_INPUT
MISSING_CONTEXT
MISSING_EVIDENCE
SOURCE_FAILURE
MODEL_FAILURE
TOOL_FAILURE
PERMISSION_DENIED
SCOPE_VIOLATION
VALIDATION_FAILED
CONFLICT_UNRESOLVED
```

---

# 34. Skill Fallback

Una Skill puede declarar una estrategia de fallback.

Ejemplo:

```text
web_research

primary_requirement:
web

fallback:
internal_documents
```

Pero el fallback debe ser autorizado por Orchestrator.

```text
FALLBACK DEFINITION ≠ FALLBACK ROUTING AUTHORITY
```

---

# 35. Skill Composition

Una Skill puede componerse de otras Skills.

Ejemplo:

```text
architecture_audit
│
├── document_analysis
├── dependency_analysis
├── contradiction_detection
├── risk_review
└── recommendation_synthesis
```

---

# 36. Regla de composición

Una Composite Skill puede definir dependencias o una secuencia lógica entre procedimientos, pero no puede decidir autónomamente qué Agent, Model o Tool debe utilizarse.

Ejemplo permitido:

```text
architecture_audit

requires:
- dependency_analysis
- contradiction_detection
- canonical_compliance_check
```

La resolución concreta continúa siendo:

```text
COMPOSITE SKILL
      ↓
ORCHESTRATOR
      ↓
SKILL / MODEL / TOOL RESOLUTION
```

Por tanto:

```text
COMPOSITION ≠ ROUTING AUTHORITY
```

---

# 37. Composite Skills

Una Composite Skill coordina conceptualmente varias capacidades procedimentales.

Pero:

```text
COMPOSITE SKILL ≠ ORCHESTRATOR
```

No puede:

* asignar Agents;
* seleccionar unilateralmente Models;
* conceder Tool access;
* ampliar Scope;
* aprobar Actions.

---

# 38. Atomic Skills

Preferencia arquitectónica:

```text
SMALL
REUSABLE
COMPOSABLE
```

antes que Skills gigantes.

Ejemplo preferido:

```text
contradiction_detection
source_validation
dependency_analysis
```

frente a:

```text
do_everything_architecture_skill
```

---

# 39. Skill Independence

Las Skills deben minimizar dependencia de:

* un Agent concreto;
* un Model concreto;
* una Tool concreta;
* un prompt concreto.

Esto maximiza reutilización.

---

# 40. Skill Versioning

Cada Skill deberá tener:

```text
skill_id
version
definition_version
dependencies
compatibility
```

Ejemplo:

```text
contradiction_detection
version: 0.1
```

Los cambios sustanciales deberán pasar por Change Control cuando la Skill sea oficial.

---

# 41. Skill Status

Debe distinguirse entre:

```text
DOCUMENTED
APPROVED
IMPLEMENTED
AVAILABLE
ACTIVE
```

Durante Fase 10, las Skills estarán principalmente:

```text
DOCUMENTED
CONCEPTUAL
MANUAL
```

Aprobar una Skill no significa implementarla.

---

# 42. Skill Manifest

Formato conceptual:

```yaml
skill:
  id:
  name:
  version:
  category:
  purpose:

capabilities:

inputs:

outputs:

preconditions:

procedure:

postconditions:

evidence:
  requirements:

sources:
  requirements:

models:
  requirements:

tools:
  required:

permissions:
  required:

scopes:
  required:

risk:
  factors:
  escalation_threshold:

autonomy:
  level: 0

execution:
  authority: NONE

approval:
  requirements:

validation:

failure_modes:

fallback:

compatible_agents:

dependencies:

overlap_notes:
```

---

# 43. Skill Registry Rule

Toda Skill aprobada deberá registrarse en un catálogo único.

Antes de crear una Skill nueva deberá verificarse:

1. si ya existe una Skill equivalente;
2. si existe una Skill parcialmente equivalente;
3. si la necesidad puede resolverse mediante composición;
4. si realmente requiere una nueva capacidad.

Cada entrada futura del Registry deberá contener al menos:

```text
skill_id
purpose
category
version
status
compatible_agents
dependencies
overlap_notes
```

Objetivo:

```text
ONE CAPABILITY
      ↓
ONE PRIMARY SKILL DEFINITION
```

cuando sea razonablemente posible.

---

# 44. Skill Registry

Se propone conceptualmente:

```text
ROBERT_SKILL_REGISTRY
```

como catálogo único de Skills.

Durante Fase 10 puede permanecer como estructura documental dentro de esta arquitectura o como documento futuro separado si el catálogo crece.

No se crea automáticamente un componente técnico nuevo.

---

# 45. Catálogo inicial propuesto

Se propone un catálogo inicial de Skills agrupado por dominio.

El catálogo es provisional.

---

# 46. Architecture Skills

```text
architecture_design
architecture_review
dependency_analysis
contradiction_detection
system_decomposition
interface_analysis
```

Principalmente utilizadas por:

```text
ROBERT_ARCHITECT
ROBERT_CRITIC
ROBERT_STRATEGIST
```

---

# 47. Research Skills

```text
web_research
source_validation
evidence_collection
comparison
evidence_synthesis
```

Principalmente:

```text
ROBERT_RESEARCHER
```

pero reutilizables por otros Agents.

---

# 48. Critical Thinking Skills

```text
adversarial_review
assumption_analysis
tradeoff_analysis
contradiction_detection
failure_mode_analysis
```

Principalmente:

```text
ROBERT_CRITIC
ROBERT_TESTER
ROBERT_ARCHITECT
```

---

# 49. Security Skills

```text
security_review
permission_analysis
scope_analysis
risk_assessment
approval_requirement_analysis
data_exposure_analysis
```

Principalmente:

```text
ROBERT_SECURITY
```

---

# 50. Memory Skills

```text
memory_classification
memory_extraction
retention_analysis
memory_conflict_detection
memory_eligibility_analysis
```

Principalmente:

```text
ROBERT_MEMORY
```

---

# 51. Coding Skills

```text
code_generation
code_review
debugging
refactoring
test_generation
technical_design
```

Principalmente:

```text
ROBERT_CODER
```

Durante Fase 10 estas Skills producen outputs documentales o trabajan en Sandbox autorizado.

---

# 52. Testing Skills

```text
test_design
edge_case_analysis
failure_injection
adversarial_testing
integration_test_design
routing_test_design
```

Principalmente:

```text
ROBERT_TESTER
```

---

# 53. Strategy Skills

```text
prioritization
roadmapping
tradeoff_analysis
dependency_planning
build_vs_defer_analysis
phase_planning
```

Principalmente:

```text
ROBERT_STRATEGIST
```

---

# 54. Validation Skills

```text
output_validation
canonical_compliance_check
evidence_validation
consistency_check
completeness_check
```

Podrán ser compartidas por:

```text
ORCHESTRATOR
VALIDATOR
AGENTS
```

según futura Validation Architecture.

---

# 55. Documentation Skills

```text
document_structuring
change_summary
decision_summary
specification_drafting
technical_document_review
```

Podrán reutilizarse entre múltiples Agents.

---

# 56. Initial Skill Matrix

| Skill                      | Primary Agents                | Model Need       | Tool Need     |
| -------------------------- | ----------------------------- | ---------------- | ------------- |
| architecture_design        | Architect                     | High reasoning   | Low           |
| architecture_review        | Architect / Critic            | High reasoning   | Low           |
| contradiction_detection    | Critic / Architect / Security | Reasoning        | Low           |
| web_research               | Researcher                    | Research capable | Web           |
| source_validation          | Researcher                    | Reasoning        | Web/Documents |
| security_review            | Security                      | High reasoning   | Low           |
| risk_assessment            | Security                      | Reasoning        | Low           |
| memory_classification      | Memory                        | Reasoning        | Low           |
| code_generation            | Coder                         | Coding           | Optional      |
| code_review                | Coder / Tester                | Coding           | Optional      |
| adversarial_testing        | Tester / Critic               | Reasoning        | Optional      |
| prioritization             | Strategist                    | Reasoning        | Low           |
| canonical_compliance_check | Multiple                      | Reasoning        | Documents     |

La matriz no concede Permissions ni Execution Authority.

---

# 57. Skill Reuse Example

Task:

```text
Revisar arquitectura de memoria
```

Puede utilizar:

```text
ROBERT_MEMORY
  ↓
memory_classification
dependency_analysis
contradiction_detection
```

y:

```text
ROBERT_SECURITY
  ↓
risk_assessment
permission_analysis
```

`contradiction_detection` no necesita duplicarse.

---

# 58. Skill Composition Example

```text
architecture_review
  ↓
document_analysis
  ↓
dependency_analysis
  ↓
contradiction_detection
  ↓
canonical_compliance_check
  ↓
recommendation_synthesis
```

El Orchestrator determina qué partes son necesarias y cómo se resuelven.

---

# 59. Skill Conflict

Dos Skills pueden producir resultados incompatibles.

Ejemplo:

```text
performance_analysis:
"Use architecture X"

security_review:
"Architecture X creates unacceptable exposure"
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
FIRST SKILL WINS
```

---

# 60. Skill Confidence

Una Skill puede producir Confidence cuando resulte útil.

Pero:

```text
CONFIDENCE ≠ AUTHORITY
CONFIDENCE ≠ TRUTH
CONFIDENCE ≠ EXECUTION AUTHORITY
```

---

# 61. Skill Evidence

Cuando una Skill dependa de evidencia, debe conservar cuando corresponda:

```text
source
claim
evidence
confidence
limitations
```

Esto será especialmente importante en Research, Validation y Security.

---

# 62. Skill Source Handling

Cuando una Skill utilice Sources, debe distinguir entre:

```text
SOURCE
CLAIM
EVIDENCE
INTERPRETATION
```

Por tanto:

```text
SOURCE ≠ CLAIM
CLAIM ≠ EVIDENCE
EVIDENCE ≠ INTERPRETATION
```

Esto permite que Robert conserve trazabilidad.

---

# 63. Skill Observability

Una ejecución futura podrá registrar:

```text
skill_id
skill_version
task_id
agent_id
inputs
evidence_requirements
sources_used
models_used
tools_requested
tools_used
permissions
scope
risk
result
limitations
validation
errors
duration
```

---

# 64. Security Invariants

Una Skill nunca puede:

```text
BYPASS ORCHESTRATOR
CREATE PERMISSIONS
OWN PERMISSIONS
EXPAND SCOPE
OWN SCOPE
CREATE AUTONOMY
CREATE EXECUTION AUTHORITY
SELF-APPROVE
ALTER PHASE
ALTER CANONICAL MODEL
HIDE CONFLICTS
ROUTE AGENTS
ROUTE MODELS
ROUTE TOOLS
```

---

# 65. Governance Invariants

```text
USER > SKILL

ROBERT > SKILL

ORCHESTRATOR > SKILL ROUTING

SECURITY > SKILL PROCEDURE

PERMISSION > TOOL REQUIREMENT

SCOPE > SKILL REQUEST

APPROVED DECISION > SKILL OUTPUT

RISK ≠ AUTONOMY

PERMISSION ≠ EXECUTION AUTHORITY

COMPOSITION ≠ ROUTING AUTHORITY
```

---

# 66. Fase 10

Durante Fase 10:

```text
SKILLS = DOCUMENTAL
SKILLS = CONCEPTUAL
SKILLS = MANUAL
SKILLS = SUPERVISED
```

Además:

```text
AUTONOMY_LEVEL = 0
EXECUTION_AUTHORITY = NONE
```

---

# 67. Permitido en Fase 10

Se permite:

* definir Skills;
* crear Skill Manifests conceptuales;
* mantener Skill Registry documental;
* simular Skill Resolver;
* ejecutar procedimientos manualmente;
* comparar resultados entre Models;
* probar Skills en Sandbox;
* revisar reutilización;
* diseñar Validation;
* analizar evidencias y Sources.

---

# 68. No permitido en Fase 10

No se permite:

* Skill execution autónoma;
* Tool invocation automática;
* Memory writes automáticos;
* permisos autoasignados;
* Scope expansion;
* loops autónomos;
* ejecución externa automática;
* self-modification;
* routing autónomo;
* creación autónoma de Agents;
* creación autónoma de Models;
* creación autónoma de Tools.

---

# 69. Sandbox Tests futuros

```text
TEST 1
Correct Skill selected

TEST 2
Wrong Skill rejected

TEST 3
Missing input

TEST 4
Missing precondition

TEST 5
Tool required but unauthorized

TEST 6
Permission missing

TEST 7
Scope exceeded

TEST 8
Skill conflict

TEST 9
Model unavailable

TEST 10
Fallback Skill

TEST 11
Composite Skill

TEST 12
Skill attempts direct Tool access

TEST 13
Skill attempts to create Permission

TEST 14
Skill attempts to create Execution Authority

TEST 15
Composite Skill attempts routing

TEST 16
Skill claims Permission ownership

TEST 17
Skill claims Scope ownership

TEST 18
Missing evidence

TEST 19
Invalid source

TEST 20
Duplicate Skill creation attempt
```

---

# 70. Métricas futuras

```text
skill_selection_accuracy
skill_reuse_rate
task_success_rate
validation_pass_rate
tool_efficiency
input_completeness
evidence_completeness
source_quality
failure_rate
fallback_rate
duplicate_skill_rate
user_correction_rate
```

---

# 71. Relación con Agent Architecture

La relación oficial será:

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
```

Agents no deben implementar procedimientos duplicados cuando exista una Skill reutilizable.

---

# 72. Relación con Model Interface

Las Skills deberán expresar necesidades de capacidad, no dependencia rígida de proveedor.

```text
SKILL
  ↓
MODEL REQUIREMENTS
  ↓
ORCHESTRATOR / MODEL ROUTER
  ↓
MODEL INTERFACE
  ↓
MODEL
```

---

# 73. Relación con Tools

```text
SKILL
  ↓
TOOL REQUIREMENT
  ↓
ORCHESTRATOR
  ↓
PERMISSION / SCOPE
  ↓
TOOL RESOLVER
  ↓
TOOL
```

---

# 74. Relación con Memory

Las Skills pueden requerir Context o Memory.

Pero:

```text
SKILL ≠ MEMORY OWNER
```

El acceso se definirá posteriormente en `ROBERT_MEMORY_ARCHITECTURE`.

---

# 75. Relación con Validation

La futura:

```text
ROBERT_VALIDATION_ARCHITECTURE
```

definirá políticas comunes de validación.

Skill Architecture solo establece requisitos declarativos.

---

# 76. Skill Duplication Rule

Antes de crear una nueva Skill debe verificarse:

```text
DOES EQUIVALENT SKILL EXIST?
```

Si existe:

```text
REUSE
```

Si existe parcialmente:

```text
EXTEND / COMPOSE
```

Crear una nueva Skill debe ser la última opción.

---

# 77. Skill Naming

Los nombres deben describir capacidades.

Preferencia:

```text
architecture_review
source_validation
risk_assessment
```

Evitar:

```text
smart_architect_skill
claude_skill
super_analyzer
skill_v_final_2
```

---

# 78. Skill Granularity

Una Skill debe ser:

```text
specific enough to be predictable
general enough to be reusable
```

Evitar extremos:

```text
TOO BROAD:
solve_problem

TOO NARROW:
review_line_47_of_architecture_doc
```

---

# 79. Catálogo provisional

El catálogo definido en v0.1 es provisional.

Su futura aprobación documental no implica implementación automática.

Antes de v1.0 deberán eliminarse:

* duplicados;
* Skills demasiado amplias;
* Skills demasiado específicas;
* dependencias propietarias innecesarias;
* procedimientos cuya función pertenezca realmente al Orchestrator o Agent.

---

# 80. Decisiones pendientes antes de v1.0

Deben resolverse:

1. catálogo definitivo;
2. Skill Manifest final;
3. tipos oficiales de Skill;
4. Skill Resolver exacto;
5. composición de Skills;
6. políticas de fallback;
7. Model requirements formales;
8. Tool requirements formales;
9. política de versioning;
10. lifecycle técnico;
11. Validation común;
12. Skill Registry técnico o documental definitivo;
13. tests técnicos;
14. formato de Capability Request;
15. políticas definitivas de Evidence;
16. políticas definitivas de Sources.

---

# 81. Estado actual

```text
DOCUMENT: ROBERT_SKILL_ARCHITECTURE
VERSION: 0.1
STATUS: PROPOSED
AUTHORITY: NON-CANONICAL
PHASE: 10
IMPLEMENTATION: NONE
AUTONOMY_LEVEL: 0
EXECUTION_AUTHORITY: NONE
```

---

# 82. Criterios de aprobación

Esta propuesta puede aprobarse cuando:

1. el User la apruebe explícitamente;
2. se registre la Decision correspondiente;
3. se registre el Change correspondiente;
4. se integre como documento arquitectónico;
5. se actualicen referencias mínimas;
6. se confirme que no crea routing paralelo al Orchestrator.

---

# 83. Próximo paso recomendado

Después de aprobar `ROBERT_SKILL_ARCHITECTURE v0.1`, el siguiente documento será:

```text
ROBERT_MODEL_INTERFACE_SPEC v0.1
```

Ese documento definirá cómo Claude, ChatGPT y futuros Models reciben Tasks, Context, Constraints y requisitos de Robert, y cómo devuelven resultados estructurados sin que cada Agent dependa de prompts propietarios distintos.
