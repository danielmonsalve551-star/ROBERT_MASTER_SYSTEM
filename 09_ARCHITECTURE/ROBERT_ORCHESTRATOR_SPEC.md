# ROBERT_ORCHESTRATOR_SPEC

**Versión:** 0.1
**Estado:** APROBADO
**Tipo:** Especificación arquitectónica de orquestación
**Ubicación propuesta:** `09_ARCHITECTURE/ROBERT_ORCHESTRATOR_SPEC.md`
**Fase relacionada:** Fase 10 — MVP técnico básico en preparación
**Dependencias principales:**

* `ROBERT_CANONICAL_MODEL v0.2`
* `ROBERT_SYSTEM_ARCHITECTURE`
* `ROBERT_CONTEXT_MASTER`
* `ROBERT_COMMANDS`
* `ROBERT_SECURITY_RULES`
* `ROBERT_MODULES`
* `ROBERT_TECHNICAL_PERMISSIONS_AND_SCOPES_SPEC`
* `ROBERT_TECHNICAL_DATA_CONSISTENCY_AND_CONFLICT_RESOLUTION_SPEC`
* `ROBERT_TECHNICAL_APPROVAL_AND_AUTHORIZATION_GATE_SPEC`
* `ROBERT_TECHNICAL_AUDIT_TRAIL_SPEC`
* ROBERT_SKILL_ARCHITECTURE v0.1

---

# 1. Propósito

`ROBERT_ORCHESTRATOR_SPEC` define cómo Robert coordina una solicitud desde que entra al sistema hasta que produce una respuesta, propuesta o acción autorizada.

Su función es formalizar la evolución de:

```text
CAPA 2 — CONTROL
```

y del:

```text
PROTOCOLO CANÓNICO DE CONTROL
```

ya existentes en `ROBERT_SYSTEM_ARCHITECTURE`.

El Orchestrator no sustituye la Capa 2.

La especializa.

```text
CAPA 2 — CONTROL
        ↓
ROBERT_ORCHESTRATOR
        ↓
formaliza routing, validación y coordinación
```

---

# 2. Principio fundamental

El Orchestrator no es Robert.

```text
ROBERT ≠ ORCHESTRATOR
```

Robert conserva:

* identidad;
* autoridad;
* gobierno;
* memoria;
* contexto maestro;
* seguridad;
* decisiones;
* fases.

El Orchestrator es el componente lógico encargado de decidir **cómo procesar una tarea**.

---

# 3. Responsabilidad principal

Ante una solicitud, el Orchestrator debe determinar:

```text
¿QUÉ QUIERE EL USER?
        ↓
¿QUÉ CONTEXTO ES NECESARIO?
        ↓
¿QUÉ MODULE PARTICIPA?
        ↓
¿REQUIERE AGENT?
        ↓
¿REQUIERE SKILL?
        ↓
¿QUÉ MODEL ES ADECUADO?
        ↓
¿REQUIERE TOOL?
        ↓
¿EXISTEN PERMISSIONS?
        ↓
¿CUÁL ES EL SCOPE?
        ↓
¿CUÁL ES EL RISK?
        ↓
¿EXISTEN CONFLICTS?
        ↓
¿REQUIERE APPROVAL?
        ↓
¿CÓMO SE VALIDA?
        ↓
¿QUÉ SE REGISTRA?
```

---

# 4. Lo que el Orchestrator NO es

El Orchestrator:

* no es un Model;
* no es un Agent;
* no es una Skill;
* no es una Tool;
* no sustituye al User;
* no modifica Security Rules;
* no crea permisos;
* no aumenta scopes;
* no aprueba sus propias acciones de alto riesgo;
* no activa autonomía por sí mismo.

```text
ORCHESTRATOR ≠ AUTHORITY
```

---

# 5. Posición arquitectónica

```text
USER
  ↓
INPUT
  ↓
ROBERT
  ↓
CAPA 2 — CONTROL
  ↓
ROBERT_ORCHESTRATOR
  │
  ├── Intent Router
  ├── Context Resolver
  ├── Module Router
  ├── Agent Router
  ├── Skill Resolver
  ├── Model Router
  ├── Tool Resolver
  ├── Permission / Scope Check
  ├── Risk Check
  ├── Conflict Check
  ├── Approval Gate
  ├── Validator
  └── Audit Output
```

---

# 6. Flujo canónico de orquestación

```text
INPUT
  ↓
1. NORMALIZE
  ↓
2. INTENT CLASSIFICATION
  ↓
3. TASK DEFINITION
  ↓
4. CONTEXT RESOLUTION
  ↓
5. MODULE ROUTING
  ↓
6. CAPABILITY PLANNING
  ↓
7. AGENT ROUTING
  ↓
8. SKILL RESOLUTION
  ↓
9. MODEL ROUTING
  ↓
10. TOOL RESOLUTION
  ↓
11. PERMISSION / SCOPE CHECK
  ↓
12. RISK CHECK
  ↓
13. CONFLICT CHECK
  ↓
14. APPROVAL CHECK
  ↓
15. EXECUTION / GENERATION
  ↓
16. VALIDATION
  ↓
17. AUDIT
  ↓
18. STATE / MEMORY UPDATE WHEN AUTHORIZED
  ↓
OUTPUT
```

No todas las tareas deben utilizar todos los pasos.

---
## 6.1 Relación con el Protocolo Canónico de Control

El flujo de orquestación definido en este documento NO reemplaza ni crea un protocolo de control paralelo.

Los 18 pasos del Orchestrator son una descomposición técnica de los 14 pasos del Protocolo Canónico de Control existente en `ROBERT_SYSTEM_ARCHITECTURE`.

La relación conceptual es:

| Protocolo Canónico de Control | Orchestrator |
|---|---|
| 1. Capturar intención | Normalize / Intent Classification |
| 2. Detectar tipo de solicitud | Intent Classification |
| 3. Clasificar intención | Intent Classification / Task Definition |
| 4. Identificar documento relacionado | Context Resolution |
| 5. Identificar capa activa | Context Resolution / Module Routing |
| 6. Identificar módulo relacionado | Module Routing |
| 7. Evaluar nivel de riesgo | Risk Check |
| 8. Revisar Security Rules | Permission / Scope / Risk / Conflict Checks |
| 9. Revisar autonomía activa | Permission / Scope Check |
| 10. Revisar alcance autorizado | Permission / Scope Check |
| 11. Decidir respuesta / propuesta / ejecución / bloqueo | Capability Planning / Agent / Skill / Model / Tool Routing / Approval Check |
| 12. Entregar salida | Execution / Generation / Output |
| 13. Registrar si aplica | Audit / State / Memory Update |
| 14. Pedir aprobación cuando corresponda | Approval Check |

Regla:

`ORCHESTRATOR FLOW = TECHNICAL DECOMPOSITION OF CANONICAL CONTROL PROTOCOL`

Nunca debe interpretarse como un protocolo alternativo.

# 7. Orchestration Request

Cada tarea procesada por el Orchestrator deberá poder representarse conceptualmente como:

```text
OrchestrationRequest
```

Campos conceptuales:

```text
request_id
user_intent
raw_input
task
context_requirements
constraints
requested_output
requested_action
module_candidates
risk_hint
session_id
timestamp
```

Esta definición es conceptual.

No autoriza crear todavía un nuevo modelo técnico en `DATA_MODEL`.

---

# 8. Intent Router

## 8.1 Propósito

Determina qué intenta conseguir el User.

Debe distinguir entre categorías como:

```text
ASK
CREATE
ANALYZE
COMPARE
RESEARCH
MODIFY
EXECUTE
PLAN
REVIEW
DEBUG
MONITOR
DECIDE
```

La taxonomía exacta podrá evolucionar.

---

## 8.2 Salida

Ejemplo conceptual:

```text
intent:
  primary: MODIFY
  secondary: REVIEW

target:
  ROBERT_SYSTEM_ARCHITECTURE

execution_required:
  false
```

---

## 8.3 Regla

El Intent Router no decide por sí mismo si algo está permitido.

Solo identifica la intención.

```text
INTENT ≠ AUTHORIZATION
```

---

# 9. Task Definition

Después de clasificar la intención, el Orchestrator debe convertirla en una tarea explícita.

Ejemplo:

```text
User:
"Mejora la memoria de Robert."
```

puede convertirse en:

```text
TASK:
Review current Robert memory architecture and produce an
architectural proposal without implementing persistent memory.
```

La definición de Task debe conservar:

* objetivo;
* restricciones;
* alcance;
* resultado esperado.

---

# 10. Context Resolver

## 10.1 Propósito

Determina qué información necesita la tarea.

Puede recuperar:

* Context activo;
* Context Master;
* Canonical Model;
* Decisions;
* Phase;
* Security Rules;
* Module information;
* Technical Specs;
* resultados previos;
* Memory autorizada.

---

## 10.2 Context mínimo necesario

Principio:

```text
MINIMUM SUFFICIENT CONTEXT
```

Robert no debe cargar todo el sistema para cada tarea si no es necesario.

Debe buscar el contexto mínimo suficiente para responder correctamente.

---

## 10.3 Prioridad conceptual de fuentes

Orden orientativo:

```text
1. USER explicit instruction
2. SECURITY / GOVERNANCE
3. CANONICAL MODEL
4. ACTIVE DECISIONS
5. CURRENT PHASE
6. SYSTEM ARCHITECTURE
7. TECHNICAL SPECS
8. CONTEXT MASTER
9. SESSION CONTEXT
10. MEMORY
11. MODEL-GENERATED INFERENCE
```

Esta prioridad no sustituye reglas específicas de autoridad existentes.

---

# 11. Module Router

Determina qué Module o Modules deben participar.

Ejemplo conceptual:

```text
TASK:
Diseñar memoria episódica

MODULE ROUTING:
- MEMORY
- ARCHITECTURE
- SECURITY
```

Puede existir:

```text
primary_module
supporting_modules[]
```
### Model Interface vigente

La interfaz arquitectónica vigente para Models es:

`ROBERT_MODEL_INTERFACE_SPEC v0.1`

Aprobada mediante:

- DECISIÓN #034
- CAMBIO #059

El Model Router deberá utilizar la Model Interface como contrato común para Models actuales y futuros.

La separación vigente es:

```text
ORCHESTRATOR
  ↓
MODEL ROUTER
  ↓
MODEL INTERFACE
  ↓
MODEL ADAPTER
  ↓
MODEL

---

# 12. Capability Planning

Antes de elegir Agent, Skill, Model o Tool, el Orchestrator debe determinar qué capacidades necesita.

Ejemplo:

```text
required_capabilities:
- architecture_analysis
- contradiction_detection
- memory_design
- security_review
```

Esto evita seleccionar un Model o Agent por costumbre.

Primero se determina la necesidad.

Después se asigna el proveedor.

---

# 13. Agent Router

## 13.1 Propósito

Selecciona un Agent cuando la tarea se beneficie de un especialista.

Ejemplos futuros:

```text
ROBERT_ARCHITECT
ROBERT_CRITIC
ROBERT_SECURITY
ROBERT_RESEARCHER
ROBERT_MEMORY
ROBERT_CODER
ROBERT_TESTER
```

---

## 13.2 Regla

Una tarea simple puede ejecutarse sin Agent dedicado.

```text
TASK
  ↓
AGENT_REQUIRED?
  ├── NO → continuar
  └── YES → seleccionar
```

---

## 13.3 Selección

Debe considerar:

```text
domain_match
capability_match
permissions
risk
module
task_complexity
availability
```

---

# 14. Skill Resolver

### Skill Architecture vigente

La arquitectura documental vigente de Skills es:

`ROBERT_SKILL_ARCHITECTURE v0.1`

Aprobada mediante:

- DECISIÓN #033
- CAMBIO #057

El Skill Resolver deberá respetar:

- Skill Contract;
- Skill Reuse;
- Skill Registry;
- Skill Composition;
- Model Requirements;
- Tool Requirements;
- Permission Requirements;
- Scope Requirements;
- Evidence Requirements;
- Source Requirements;
- Validation Requirements.

Una Skill declara requisitos, pero no posee autorización.

```text
SKILL REQUIREMENT ≠ PERMISSION
SKILL REQUIREMENT ≠ SCOPE
COMPOSITION ≠ ROUTING AUTHORITY

## 14.1 Propósito

Determina qué procedimiento reutilizable necesita la tarea.

Ejemplos futuros:

```text
architecture_review
contradiction_detection
code_review
research
decision_analysis
memory_extraction
risk_review
```

---

## 14.2 Relación

```text
AGENT
  ↓ uses
SKILL
  ↓ may request
MODEL / TOOL
```

Un Agent puede usar varias Skills.

Una Skill puede ser compartida por varios Agents.

---

# 15. Model Router

## 15.1 Propósito

Selecciona el Model más adecuado.

Ejemplos actuales:

```text
Claude
ChatGPT
```

Futuros Models pueden integrarse sin redefinir la arquitectura.

---

## 15.2 Criterios de selección

El Model Router podrá considerar:

```text
task_type
context_size
reasoning_requirement
tool_access
latency
cost
quality
specialization
availability
privacy
risk
```

No todos estos criterios estarán activos en Fase 10.

---

## 15.3 Regla fundamental

```text
BEST MODEL FOR TASK
≠
DEFAULT MODEL FOR EVERYTHING
```

---

## 15.4 Ejemplo conceptual

```text
Task:
Review 40 architecture documents.

Candidate:
Claude

Reason:
Large context + long-form architecture review.
```

Otro ejemplo:

```text
Task:
Current web research + validation.

Candidate:
ChatGPT

Reason:
Tool access + web retrieval + independent validation.
```

Esto es orientación conceptual.

No constituye routing automático todavía.

---

# 16. Multi-Model Routing

El Orchestrator podrá permitir en fases futuras:

```text
MODEL A
  ↓
produces proposal

MODEL B
  ↓
reviews proposal

VALIDATOR
  ↓
synthesizes
```

Ejemplo:

```text
Claude
  ↓
Architecture Proposal
  ↓
ChatGPT
  ↓
Adversarial Review
```

o al revés.

---

## 16.1 Regla

Dos Models no deben considerarse automáticamente más correctos por coincidir.

```text
MODEL CONSENSUS ≠ TRUTH
```

La validación sigue siendo necesaria.

---

# 17. Tool Resolver

## 17.1 Propósito

Determina si una tarea necesita una Tool.

Ejemplos:

```text
web
GitHub
filesystem
database
terminal
Gmail
Calendar
```

---

## 17.2 Regla

El Orchestrator debe preferir:

```text
NO TOOL
```

cuando la tarea puede completarse correctamente sin acceso externo.

Esto reduce:

* riesgo;
* complejidad;
* costo;
* exposición.

---

# 18. Permission Check

Antes de solicitar o utilizar una Tool, Agent capability o Action:

```text
CHECK PERMISSION
```

Debe verificar:

```text
actor
capability
resource
permission
```

Si no existe Permission:

```text
BLOCK / REQUEST APPROVAL
```

según las reglas vigentes.

---

# 19. Scope Check

Permission no es suficiente.

Debe comprobarse también Scope.

Ejemplo:

```text
Permission:
GitHub write

Scope:
repository X only
```

No implica acceso de escritura universal.

```text
PERMISSION ≠ UNIVERSAL ACCESS
```

---

# 20. Risk Check

Toda tarea que pueda producir una Action o Change debe evaluar Risk.

Factores potenciales:

```text
external_effect
data_sensitivity
irreversibility
financial_impact
security_impact
system_impact
user_impact
uncertainty
```

La escala oficial vigente de Robert sigue teniendo autoridad.

---

# 21. Conflict Check

Antes de producir una decisión operacional importante, el Orchestrator debe comprobar posibles conflictos.

Ejemplos:

```text
Proposal vs Security
Proposal vs Phase
Proposal vs Decision
Action vs Permission
State vs Document
Model output vs Canonical Model
```

Debe utilizar la taxonomía de conflictos ya existente.

---

# 22. Approval Gate

Si una tarea requiere aprobación:

```text
STOP
  ↓
PRESENT PROPOSAL
  ↓
REQUEST USER APPROVAL
```

No ejecutar antes.

Ejemplo:

```text
Agent proposes:
Delete obsolete architecture file.

Risk:
medium

Approval:
required

Result:
PENDING USER
```

---

# 23. Execution / Generation

El Orchestrator puede llegar a dos tipos principales de resultado.

## 23.1 Cognitive Output

No produce cambio externo.

Ejemplos:

* análisis;
* recomendación;
* documento;
* comparación;
* plan;
* revisión.

## 23.2 Executable Action

Produce o intenta producir un efecto externo.

Ejemplos:

* editar archivo;
* enviar mensaje;
* modificar base de datos;
* hacer commit;
* ejecutar comando.

Las Actions externas requieren las autorizaciones correspondientes.

---

# 24. Validator

## 24.1 Propósito

Revisar el resultado antes de entregarlo o ejecutarlo.

Puede comprobar:

```text
task_alignment
canonical_compliance
security
permissions
scope
risk
conflicts
completeness
internal_consistency
evidence
```

---

## 24.2 Tipos de validación

```text
SELF_VALIDATION
CROSS_MODEL_VALIDATION
AGENT_VALIDATION
RULE_VALIDATION
USER_VALIDATION
```

---

## 24.3 Regla

El Validator no puede convertir una operación no autorizada en autorizada.

```text
VALIDATION ≠ AUTHORIZATION
```

---

# 25. Confidence

Cuando resulte útil, el resultado podrá incluir:

```text
confidence
```

Ejemplo:

```text
confidence: 0.82
```

Confidence representa certeza estimada.

No representa autoridad.

```text
CONFIDENCE ≠ AUTHORITY
```

---

# 26. Audit Output

Cada proceso relevante podrá generar un registro conceptual de:

```text
request_id
intent
task
context_used
modules
agents
skills
models
tools
permissions
scope
risk
conflicts
approval
result
validation
timestamp
```

La representación técnica seguirá dependiendo de las specs existentes.

---

# 27. State Update

Después de una operación autorizada, Robert puede necesitar actualizar State.

Ejemplos:

```text
task_status
component_status
decision_status
change_status
phase_status
```

El Orchestrator no puede inventar estados no permitidos por las specs correspondientes.

---

# 28. Memory Update

Un resultado no entra automáticamente en Memory.

Debe existir una decisión de retención.

Ejemplo:

```text
Should store?
  ↓
NO → discard after context
YES
  ↓
Memory Type
  ↓
Retention
  ↓
Source
  ↓
Authority
```

Esto se definirá en detalle en:

```text
ROBERT_MEMORY_ARCHITECTURE
```

---

# 29. Routing Plan

Para cada tarea compleja, el Orchestrator podrá construir conceptualmente:

```text
ROUTING PLAN
```

Ejemplo:

```text
Task:
Design Agent Architecture

Module:
Architecture

Agent:
ROBERT_ARCHITECT

Skills:
- architecture_design
- contradiction_detection

Model:
Claude

Reviewer:
ChatGPT

Tools:
none

Risk:
1

Approval:
required before canonicalization
```

---

# 30. Simple Task Optimization

No toda solicitud necesita un pipeline complejo.

Ejemplo:

```text
User:
¿Qué significa Permission?
```

Ruta:

```text
Intent Router
  ↓
Context Resolver
  ↓
Canonical Model
  ↓
Model
  ↓
Response
```

No necesita:

* Agent;
* Tool;
* Approval;
* multi-model validation.

---

# 31. Complex Task Routing

Ejemplo:

```text
User:
Reestructura la memoria de Robert.
```

Ruta posible:

```text
Intent
  ↓
Architecture Module
  ↓
Memory Module
  ↓
ROBERT_MEMORY_AGENT
  ↓
memory_architecture Skill
  ↓
Claude
  ↓
ROBERT_CRITIC
  ↓
ChatGPT
  ↓
Security Review
  ↓
Proposal
  ↓
User Approval
```

---

# 32. Orchestration Levels

Se propone distinguir niveles de complejidad.

## LEVEL 0 — DIRECT

```text
input → model → response
```

Uso:

* preguntas simples;
* definiciones;
* tareas triviales.

## LEVEL 1 — CONTEXTUAL

```text
input → context → model → validate → response
```

Uso:

* preguntas sobre Robert;
* trabajo documental sencillo.

## LEVEL 2 — SPECIALIZED

```text
input → module → agent → skill → model → validate
```

Uso:

* arquitectura;
* seguridad;
* código;
* memoria.

## LEVEL 3 — MULTI-MODEL

```text
model A
  ↓
model B review
  ↓
validator
```

Uso:

* decisiones importantes;
* arquitectura;
* análisis complejo.

## LEVEL 4 — CONTROLLED ACTION

```text
routing
  ↓
permissions
  ↓
risk
  ↓
approval
  ↓
tool/action
  ↓
audit
```

Uso:

* cambios externos.

En Fase 10 estos niveles son principalmente conceptuales y documentales.

---

# 33. Failure Handling

Si una etapa falla:

```text
FAIL
  ↓
CLASSIFY ERROR
  ↓
CAN RETRY?
  ├── YES → retry within limits
  └── NO
       ↓
BLOCK / ESCALATE
```

Casos:

```text
MODEL_FAILURE
TOOL_FAILURE
CONTEXT_MISSING
PERMISSION_DENIED
SCOPE_VIOLATION
RISK_TOO_HIGH
CONFLICT_UNRESOLVED
VALIDATION_FAILED
```

La gestión técnica detallada sigue dependiendo de `ERROR_AND_BLOCKING_SPEC`.

---

# 34. Fallback Model

En fases futuras podrá definirse:

```text
PRIMARY MODEL
    ↓ fail
FALLBACK MODEL
```

Ejemplo:

```text
Claude unavailable
        ↓
ChatGPT
```

Pero un fallback debe conservar:

* Task;
* Context;
* Constraints;
* Permissions;
* Scope;
* Risk.

---

# 35. Model Independence

Robert debe evitar dependencia excesiva de un único proveedor.

La arquitectura debe permitir:

```text
MODEL INTERFACE
        ↓
Claude Adapter
ChatGPT Adapter
Future Adapter
```

Esto se formalizará en:

```text
ROBERT_MODEL_INTERFACE_SPEC
```

---
### Estado de dependencias técnicas

Algunas Technical Specs relacionadas pueden encontrarse todavía en estado de propuesta o pendiente de revisión.

Mientras no hayan sido aprobadas formalmente:

- pueden utilizarse como referencia de diseño;
- no adquieren autoridad canónica por ser citadas aquí;
- no pueden sobreescribir Security Rules, Decisions, Canonical Model o documentos maestros aprobados;
- cualquier contradicción deberá escalarse mediante el sistema vigente de conflictos y Change Control.

  
# 36. Agent Independence

Los Agents no deben escribirse exclusivamente para un único Model salvo necesidad explícita.

Preferencia:

```text
AGENT
  ↓
SKILLS
  ↓
MODEL INTERFACE
```

en lugar de:

```text
AGENT
  ↓
CLAUDE ONLY
```
### Agent Architecture vigente

La arquitectura documental vigente de Agents es:

`ROBERT_AGENT_ARCHITECTURE v0.1`

Aprobada mediante:

- DECISIÓN #032
- CAMBIO #055

El Agent Router deberá respetar las reglas de:

- Primary / Supporting ownership;
- Capability Request;
- Permission;
- Scope;
- Risk limits;
- Approval requirements;
- Handoff;
- Structured Context Transfer;
- Validation;
- Escalation.

Los Agents permanecen documentales, conceptuales, manuales y supervisados durante Fase 10.

---

# 37. Skill Independence

Una Skill debe describir un procedimiento reutilizable, no un prompt específico de un proveedor.

Ejemplo correcto:

```text
contradiction_detection
```

Ejemplo menos deseable:

```text
claude_contradiction_prompt_v7
```

Los prompts específicos podrán existir como adaptadores.

---

# 38. Model Response Contract

El Orchestrator deberá esperar conceptualmente respuestas estructurables como:

```text
ANALYSIS
PROPOSAL
RISKS
CONFLICTS
CONFIDENCE
RECOMMENDATION
```

No todos los campos son obligatorios para todas las tareas.

Esto se formalizará en Model Interface.

---

# 39. Security Invariants

El Orchestrator nunca deberá:

```text
BYPASS SECURITY
BYPASS PERMISSIONS
EXPAND SCOPE SILENTLY
SELF-APPROVE HIGH-RISK ACTIONS
ALTER CANONICAL RULES
HIDE CONFLICTS
CONVERT PROPOSAL INTO DECISION
```

---

# 40. Governance Invariants

Siempre debe preservarse:

```text
USER > MODEL
USER > AGENT

SECURITY > CONVENIENCE

APPROVED DECISION > MODEL PROPOSAL

CANONICAL MODEL > MODEL INTERPRETATION

AUTHORIZED SCOPE > AGENT INTENT
```

---

# 41. Fase 10

En Fase 10, `ROBERT_ORCHESTRATOR_SPEC v0.1` será exclusivamente:

```text
DOCUMENTAL
CONCEPTUAL
MANUAL
SUPERVISED
```

No se activa:

* routing automático real;
* ejecución autónoma;
* Agents reales;
* Skills ejecutables;
* Model Router automático;
* Tool Router automático;
* memoria automática.

---

# 42. Qué sí permite v0.1

Permite:

* definir la arquitectura;
* diseñar Agents;
* diseñar Skills;
* definir contratos de routing;
* diseñar el Model Interface;
* preparar tests de Sandbox;
* simular routing manual;
* comparar Claude y ChatGPT.

---

# 43. Qué no permite v0.1

No permite:

* código de producción;
* ejecución automática;
* conexiones no autorizadas;
* modificación automática del repositorio;
* autonomía;
* autoaprobación;
* acceso universal a Tools.

---

# 44. Tests futuros

El Sandbox deberá poder probar casos como:

```text
TEST 1
Simple question → Level 0

TEST 2
Architecture analysis → Level 2

TEST 3
High-impact architecture decision → Level 3

TEST 4
GitHub modification → Level 4

TEST 5
Permission denied

TEST 6
Scope conflict

TEST 7
Security conflict

TEST 8
Model disagreement

TEST 9
Tool unavailable

TEST 10
Missing context
```

---

# 45. Métricas futuras

El Orchestrator podrá medirse por:

```text
routing_accuracy
task_success
validation_pass_rate
conflict_detection
unnecessary_tool_usage
context_efficiency
model_cost
latency
user_corrections
unsafe_action_blocks
```

Estas métricas no se implementan todavía.

---

# 46. Arquitectura resumida

```text
                       USER
                         │
                         ▼
                       ROBERT
                         │
                         ▼
                CAPA 2 — CONTROL
                         │
                         ▼
                 ORCHESTRATOR
                         │
       ┌─────────────────┼─────────────────┐
       ▼                 ▼                 ▼
   CONTEXT            ROUTING          GOVERNANCE
       │                 │                 │
       │          ┌──────┼──────┐          │
       │          ▼      ▼      ▼          │
       │       MODULE  AGENT   SKILL        │
       │                   │                │
       │                   ▼                │
       │                 MODEL              │
       │                   │                │
       │                 TOOL               │
       │                   │                │
       └───────────────────┼────────────────┘
                           ▼
                     VALIDATION
                           │
                           ▼
                       APPROVAL
                           │
                           ▼
                    OUTPUT / ACTION
                           │
                           ▼
                         AUDIT
```

---

# 47. Dependencias futuras

Una vez aprobado este documento, deberán diseñarse:

```text
ROBERT_AGENT_ARCHITECTURE
ROBERT_SKILL_ARCHITECTURE
ROBERT_MODEL_INTERFACE_SPEC
ROBERT_MEMORY_ARCHITECTURE
ROBERT_VALIDATION_ARCHITECTURE
ROBERT_AGENT_ARCHITECTURE v0.1
```

Orden recomendado:

```text
ORCHESTRATOR
     ↓
AGENTS
     ↓
SKILLS
     ↓
MODEL INTERFACE
     ↓
MEMORY
     ↓
VALIDATION
```

---

# 48. Decisiones pendientes antes de v1.0

Todavía deben decidirse:

1. lista oficial de tipos de Intent;
2. niveles exactos de Orchestration;
3. catálogo inicial de Agents;
4. catálogo inicial de Skills;
5. criterios cuantitativos del Model Router;
6. reglas de fallback entre Models;
7. estructura técnica de Routing Plan;
8. política de multi-model validation;
9. relación precisa entre Orchestrator y Memory Gate;
10. implementación técnica futura.

---

# 49. Criterios de aprobación

Esta propuesta puede pasar a `APPROVED` cuando:

1. el User la revise y apruebe;
2. se verifique compatibilidad con Capa 2 — Control;
3. se registre la Decision correspondiente;
4. se registre el Change correspondiente;
5. se añada a `09_ARCHITECTURE`;
6. se actualicen las referencias mínimas necesarias.

---

# 50. Estado actual

```text
DOCUMENT: ROBERT_ORCHESTRATOR_SPEC
VERSION: 0.1
STATUS: PROPOSED
AUTHORITY: NON-CANONICAL
PHASE: 10
EXECUTION: NONE
AUTONOMY: NONE
```

---

# 51. Siguiente paso recomendado

Después de aprobar `ROBERT_ORCHESTRATOR_SPEC v0.1`:

```text
ROBERT_AGENT_ARCHITECTURE v0.1
```

deberá definir formalmente:

* qué es un Agent en Robert;
* catálogo inicial;
* roles;
* responsabilidades;
* inputs;
* outputs;
* permisos;
* scopes;
* acceso a Skills;
* acceso a Models;
* acceso a Tools;
* lifecycle;
* límites;
* interacción entre Agents.
