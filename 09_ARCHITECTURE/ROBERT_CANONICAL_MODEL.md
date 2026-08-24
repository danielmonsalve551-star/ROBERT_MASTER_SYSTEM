# ROBERT_CANONICAL_MODEL

**Versión:** 0.2
**Estado:** Aprobado e integrado
**Tipo:** Modelo canónico de conceptos
**Ubicación:** `09_ARCHITECTURE/ROBERT_CANONICAL_MODEL.md`
**Fase relacionada:** Fase 10 — MVP técnico básico en preparación
**Dependencia:** `ROBERT_SYSTEM_ARCHITECTURE.md`

---

## 1. Propósito

`ROBERT_CANONICAL_MODEL` define el vocabulario, los límites y las relaciones fundamentales de Robert.

Su función es evitar que distintos documentos, modelos de IA, agentes, skills, tools, módulos o implementaciones utilicen significados incompatibles para los mismos conceptos.

Este documento define conceptos y relaciones, pero **no activa capacidades por sí mismo**.

No autoriza:

* autonomía real;
* ejecución externa;
* acceso automático a nuevas herramientas;
* agentes ejecutivos;
* memoria automática;
* modificaciones automáticas;
* conexiones externas;
* despliegue.

---

## 2. Autoridad y jerarquía

Este documento actúa como modelo conceptual canónico.

```text
ROBERT_CANONICAL_MODEL
        ↓
define significado

ROBERT_SYSTEM_ARCHITECTURE
        ↓
define organización

TECHNICAL SPECS
        ↓
definen representación y comportamiento

IMPLEMENTATION
        ↓
define código e infraestructura
```

Ejemplo:

```text
Decision
    ↓
DecisionRecord
    ↓
schema / código futuro
```

`Decision` es el concepto canónico.

`DecisionRecord` es su representación técnica autorizada.

---

## 3. Regla de canonicalización

Cuando otro documento utilice un concepto definido aquí:

1. debe conservar su significado canónico;
2. puede especializarlo;
3. puede definir su representación técnica;
4. puede definir su máquina de estados;
5. no puede redefinirlo silenciosamente.

Si existe contradicción:

```text
DETECT
  ↓
CLASSIFY
  ↓
REVIEW
  ↓
DECISION
  ↓
CHANGE CONTROL
```

Una propuesta de Claude, ChatGPT, un Agent o cualquier Model no modifica por sí sola el modelo canónico.

---

## 4. Principio fundamental

```text
ROBERT ≠ MODEL
ROBERT ≠ AGENT
ROBERT ≠ SKILL
ROBERT ≠ TOOL
```

Robert es el sistema que coordina:

* identidad;
* autoridad;
* contexto;
* memoria;
* estado;
* gobierno;
* módulos;
* modelos;
* agentes;
* skills;
* tools;
* decisiones;
* cambios;
* seguridad;
* auditoría.

---

# 5. Taxonomía canónica

## 5.1 Robert

**Tipo:** System

Sistema operativo personal de inteligencia artificial definido por el proyecto.

Responsabilidades:

* mantener identidad;
* preservar continuidad;
* gestionar contexto y memoria;
* coordinar capacidades;
* aplicar gobierno;
* controlar permisos;
* registrar decisiones y cambios;
* coordinar Modules, Models, Agents, Skills y Tools;
* respetar la autoridad del User.

Robert no delega su autoridad de gobierno a un Model, Agent, Skill o Tool.

---

## 5.2 User

**Tipo:** Human Authority

Autoridad humana principal del sistema.

Puede:

* aprobar;
* rechazar;
* revocar;
* modificar;
* priorizar;
* autorizar;
* limitar;
* definir objetivos;
* definir alcance.

Los Models y Agents no sustituyen esta autoridad salvo una política futura explícitamente aprobada.

---

## 5.3 Model

**Tipo:** Intelligence Provider

Proveedor de capacidad de razonamiento o generación.

Ejemplos:

```text
Claude
ChatGPT
future_model
```

Un Model puede:

* analizar;
* razonar;
* resumir;
* proponer;
* generar contenido;
* evaluar.

Un Model:

* no es automáticamente un Agent;
* no es una Tool;
* no obtiene permisos de ejecución por existir.

### Compatibilidad histórica

La documentación anterior clasificaba Claude y ChatGPT dentro de `TOOLS`.

La v0.2 separa formalmente:

```text
MODEL ≠ TOOL
```

Este cambio queda aprobado mediante:

```text
DECISIÓN #030
CAMBIO #053
```

---

## 5.4 Agent

**Tipo:** Specialized Operator

Un Agent es un especialista lógico que puede operar dentro de uno o más Modules para cumplir un objetivo definido.

Esto conserva la definición previa de `ROBERT_MODULES`.

Puede:

* recibir tareas;
* operar dentro de Modules;
* usar Skills autorizadas;
* solicitar Models;
* solicitar Tools;
* producir análisis;
* producir Proposals;
* detectar Risks;
* detectar Conflicts;
* solicitar Actions.

Un Agent no obtiene ejecución automática ni acceso universal a Tools.

---

## 5.5 Skill

**Tipo:** Procedural Capability

Una Skill define **cómo realizar una clase reutilizable de trabajo**.

Ejemplos:

```text
architecture_review
code_review
contradiction_detection
web_research
memory_extraction
decision_analysis
```

Una Skill:

* no representa identidad;
* no representa autoridad;
* puede ser usada por distintos Agents;
* puede trabajar con distintos Models;
* puede requerir Tools.

---

## 5.6 Tool

**Tipo:** External or Technical Capability

Una Tool permite interactuar con un recurso, entorno o servicio.

Ejemplos:

```text
filesystem
GitHub
web
database
terminal
Gmail
Calendar
```

Una Tool:

* no es un Model;
* no es un Agent;
* no es una Skill.

Su acceso depende de:

* Permission;
* Scope;
* Risk;
* Security;
* Phase;
* Approval cuando corresponda.

---

# 6. Capability Providers

```text
CAPABILITY PROVIDERS
│
├── MODELS
│   ├── Claude
│   ├── ChatGPT
│   └── futuros modelos
│
└── TOOLS
    ├── filesystem
    ├── GitHub
    ├── web
    ├── database
    └── otros servicios
```

Models y Tools pueden colaborar, pero conservan naturalezas distintas.

---

# 7. Command

**Tipo:** Operational Request

Solicitud estructurada de una operación reconocida por Robert.

Un Command no puede saltarse:

* Security;
* Permissions;
* Scopes;
* Risk;
* Phase;
* Approval Gates.

---

# 8. Module

**Tipo:** Functional Domain

Agrupa capacidades o responsabilidades relacionadas.

Puede contener o relacionarse con:

* Agents;
* Skills;
* Tools;
* Models;
* Commands.

```text
MODULE ≠ AGENT
```

---

# 9. Context

**Tipo:** Operational Information

Información utilizada para interpretar correctamente una tarea en un momento determinado.

Puede incluir:

* estado;
* sesión;
* documentos relevantes;
* decisiones vigentes;
* restricciones;
* resultados anteriores;
* objetivo actual.

```text
CONTEXT ≠ MEMORY
```

---

# 10. Session

**Tipo:** Temporal Interaction Unit

Una Session representa un periodo de interacción o trabajo.

Puede contener:

* mensajes;
* tareas;
* contexto activo;
* eventos;
* resultados;
* propuestas;
* decisiones pendientes;
* acciones.

Cerrar una Session no implica almacenar permanentemente todo su contenido.

---

# 11. State

**Tipo:** Canonical Abstraction

State representa la condición conocida de una entidad o del sistema.

No sustituye modelos técnicos existentes.

```text
State
├── SystemState
├── ModeState
├── ComponentState
└── otros estados especializados
```

Las especificaciones técnicas determinan los campos y valores de cada especialización.

---

# 12. Event

**Tipo:** Recorded Occurrence

Un Event representa algo que ocurrió y resulta relevante para el sistema.

```text
EVENT ≠ DECISION
EVENT ≠ ACTION
```

Un Event puede ser consecuencia de una Decision o Action.

---

# 13. Memory

Memory es información retenida por Robert más allá del uso inmediato cuando existe una razón válida para conservarla.

No toda información debe convertirse en Memory.

La arquitectura utiliza dos dimensiones independientes.

## 13.1 Retention

```text
RETENTION
├── ACTIVE
├── TEMPORARY
└── PERSISTENT
```

### ACTIVE

Información utilizada directamente en el trabajo actual.

### TEMPORARY

Información retenida durante un periodo limitado.

### PERSISTENT

Información que permanece disponible más allá de sesiones individuales.

---

## 13.2 Memory Type

```text
MEMORY_TYPE
├── CORE
├── SEMANTIC
├── EPISODIC
├── DECISIONAL
└── PROCEDURAL
```

### CORE

Identidad, principios y reglas fundamentales.

### SEMANTIC

Conocimiento estructurado sobre Robert, el proyecto o dominios relevantes.

### EPISODIC

Registro de hechos o episodios ocurridos.

### DECISIONAL

Decisiones adoptadas y su razonamiento asociado.

### PROCEDURAL

Métodos, procedimientos y formas autorizadas de realizar tareas.

Ejemplo:

```text
memory_type: DECISIONAL
retention: PERSISTENT
source: USER
authority: HIGH
status: ACTIVE
```

---

# 14. Decision

**Tipo:** Approved Determination

Una Decision representa una determinación formalmente adoptada.

```text
PROPOSAL ≠ DECISION
```

Debe poder relacionarse con:

* motivo;
* autoridad;
* fecha;
* alcance;
* estado;
* decisiones anteriores.

---

# 15. Proposal

**Tipo:** Non-Adopted Recommendation

Una Proposal es una recomendación, diseño, cambio o acción que todavía no constituye una Decision oficial.

Puede provenir de:

* User;
* Model;
* Agent;
* Module;
* análisis interno.

---

# 16. Action

**Tipo:** Executable Operation

Una Action representa una operación solicitada, autorizada, ejecutada o bloqueada.

La propuesta de una Action no implica permiso para ejecutarla.

---

# 17. Permission

**Tipo:** Capability Authorization

Permission define si una entidad puede realizar o solicitar una capacidad.

Puede aplicarse a:

* User;
* Agent;
* Model;
* Tool;
* Module;
* Action.

---

# 18. Scope

**Tipo:** Authorization Boundary

Scope delimita dónde, cuándo o sobre qué recursos es válido un Permission.

Ejemplos:

```text
read_only
single_repository
specific_module
single_session
no_external_execution
```

```text
PERMISSION ≠ SCOPE
```

---

# 19. Risk

**Tipo:** Risk Assessment

Risk representa el riesgo asociado a:

* Action;
* Proposal;
* Tool;
* Change;
* capability;
* integración.

La escala técnica vigente definida por Robert prevalece sobre cualquier escala genérica descrita aquí.

---

# 20. Conflict

**Tipo:** Detected Incompatibility

Conflict representa una incompatibilidad entre dos o más elementos.

Puede involucrar:

* documentos;
* estados;
* decisiones;
* versiones;
* permisos;
* scopes;
* fases;
* seguridad;
* acciones;
* modelos;
* componentes.

La taxonomía y resolución oficial continúa definida en:

```text
ROBERT_TECHNICAL_DATA_CONSISTENCY_AND_CONFLICT_RESOLUTION_SPEC
```

Este documento no sustituye los tipos de conflicto ya definidos.

---

# 21. AuditRecord

**Tipo:** Conceptual Audit Abstraction

AuditRecord representa conceptualmente la información necesaria para reconstruir un hecho relevante.

Puede incluir:

* qué ocurrió;
* cuándo;
* quién lo originó;
* qué objeto fue afectado;
* autorización;
* resultado.

### Restricción

La definición de `AuditRecord` aquí **no autoriza crear un nuevo modelo técnico de datos**.

Mientras `ROBERT_TECHNICAL_DATA_MODEL_SPEC` no defina un modelo `AuditRecord`, debe utilizarse la infraestructura de auditoría ya autorizada.

---

# 22. Change

**Tipo:** Controlled Modification

Change representa una modificación propuesta, aprobada o realizada sobre:

* arquitectura;
* documentación;
* configuración;
* sistema;
* código futuro.

```text
DECISION = qué se decide
CHANGE   = qué se modifica
```

Una Decision puede autorizar un Change.

---

# 23. Phase

**Tipo:** Project Evolution State

Phase representa una etapa formal del desarrollo de Robert.

Una Phase determina qué capacidades están:

* permitidas;
* prohibidas;
* documentadas;
* pendientes;
* implementadas;
* activas.

Describir una capacidad futura no la convierte en activa.

---

# 24. Distinciones obligatorias

```text
Robert     ≠ Model
Model      ≠ Agent
Model      ≠ Tool
Agent      ≠ Skill
Agent      ≠ Module
Skill      ≠ Tool

Proposal   ≠ Decision
Decision   ≠ Change
Change     ≠ Action
Event      ≠ Decision
Event      ≠ Action

Context    ≠ Memory
Permission ≠ Scope
Risk       ≠ Conflict
```

---

# 25. State Machines y Lifecycle

No existe una máquina de estados universal para todos los objetos.

Cada entidad utiliza exclusivamente la máquina de estados definida en su especificación autorizada.

Ejemplos:

```text
Document
    → Document Lifecycle Spec

Decision
    → Decisions / Data Model

Action
    → User Actions / Approval specs

Command
    → Command specifications
```

Robert puede utilizar vocabulario general como:

```text
DRAFT
PROPOSED
PENDING
APPROVED
AUTHORIZED
ACTIVE
COMPLETED
BLOCKED
REJECTED
REVOKED
SUPERSEDED
HISTORICAL
ARCHIVED
```

pero la existencia de un término aquí no significa que sea válido para todos los objetos.

---

# 26. Source, Authority y Confidence

Cuando resulte relevante, una pieza de información deberá poder conservar:

```text
source
source_type
authority
confidence
created_at
updated_at
status
```

Ejemplo:

```text
source: USER
source_type: PRIMARY
authority: CANONICAL
confidence: 1.00
status: ACTIVE
```

Frente a:

```text
source: CLAUDE
source_type: MODEL_PROPOSAL
authority: NON_CANONICAL
confidence: 0.74
status: PROPOSED
```

La confianza declarada por un Model no convierte automáticamente su salida en verdad canónica.

---

# 27. Orchestration y Capa 2 — Control

La arquitectura de orquestación **no crea un segundo sistema de control paralelo**.

`ROBERT_SYSTEM_ARCHITECTURE.md` ya define:

```text
CAPA 2 — CONTROL
```

y un:

```text
PROTOCOLO CANÓNICO DE CONTROL
```

La futura:

```text
ROBERT_ORCHESTRATOR_SPEC
```

deberá ser una **especialización y evolución técnica** de esa Capa 2.

Podrá formalizar:

```text
Intent Router
Context Resolver
Module Router
Agent Router
Skill Resolver
Model Router
Tool Resolver
Risk Check
Permission / Scope Check
Conflict Check
Approval Gate
Validator
Audit Output
```

Todos deben respetar el Protocolo Canónico de Control existente.

---

# 28. Flujo conceptual de ejecución

```text
USER
  ↓
INPUT / COMMAND
  ↓
ROBERT
  ↓
CAPA 2 — CONTROL / ORCHESTRATION
  ↓
CONTEXT RESOLUTION
  ↓
MODULE
  ↓
AGENT
  ↓
SKILL
  ↓
MODEL
  ↓
TOOL
  ↓
VALIDATION
  ↓
RISK / SECURITY / PERMISSION / SCOPE
  ↓
APPROVAL WHEN REQUIRED
  ↓
ACTION
  ↓
AUDIT
  ↓
STATE / MEMORY UPDATE WHEN AUTHORIZED
```

No todas las tareas requieren todos los pasos.

---

# 29. Model Interface

Claude y ChatGPT deberán converger progresivamente hacia una interfaz lógica común.

Entrada conceptual:

```text
TASK
CONTEXT
CONSTRAINTS
PERMISSIONS
SCOPE
RISK
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
```

El formato técnico se definirá posteriormente en:

```text
ROBERT_MODEL_INTERFACE_SPEC
```

---

# 30. Relación con Technical Data Model

El Canonical Model no sustituye los modelos técnicos existentes.

Modelos técnicos vigentes identificados:

```text
SystemState
RobertDocument
DecisionRecord
ChangeRecord
RiskRecord
CommandRequest
PendingDecision
ModeState
ComponentState
GitHubBackupStatus
ObsidianGraphStatus
```

Relación:

```text
CANONICAL CONCEPT
      ↓
TECHNICAL MODEL
      ↓
IMPLEMENTATION
```

Ejemplos:

```text
Decision → DecisionRecord
Change   → ChangeRecord
Risk     → RiskRecord
State    → SystemState / ModeState / ComponentState
```

---

# 31. Reglas de modificación

Cualquier cambio que:

* agregue un concepto;
* elimine un concepto;
* cambie una definición;
* cambie una relación;
* cambie autoridad;
* modifique una distinción fundamental;

debe pasar por:

```text
PROPOSAL
  ↓
REVIEW
  ↓
DECISION
  ↓
CHANGE CONTROL
  ↓
UPDATE
  ↓
AUDIT
```

---

# 32. Impacto previsto

La integración de este documento implica revisar progresivamente:

```text
ROBERT_CONTEXT_MASTER
ROBERT_MODULES
ROBERT_PROMPTS
ROBERT_SYSTEM_ARCHITECTURE
ROBERT_TECHNICAL_DATA_MODEL_SPEC
ROBERT_TECHNICAL_AUDIT_TRAIL_SPEC
README
```

Los documentos históricos no deben reescribirse.

---

# 33. Fuera de alcance de v0.2

Esta versión no define todavía:

* lista definitiva de Agents;
* lista definitiva de Skills;
* Agent Router implementado;
* Model Router implementado;
* ejecución autónoma;
* memoria automática;
* embeddings;
* vector database;
* APIs;
* infraestructura;
* comunicación automática Claude ↔ ChatGPT;
* despliegue.

---

# 34. Próximas piezas

```text
ROBERT_CANONICAL_MODEL
        ↓
ROBERT_ORCHESTRATOR_SPEC
        ↓
ROBERT_AGENT_ARCHITECTURE
        ↓
ROBERT_SKILL_ARCHITECTURE
        ↓
ROBERT_MODEL_INTERFACE_SPEC
        ↓
ROBERT_MEMORY_ARCHITECTURE
        ↓
ROBERT_VALIDATION_ARCHITECTURE
```

---

# 35. Criterios de promoción cumplidos

La v0.2 fue promovida de `PROPOSED` a `APPROVED` después de:

1. aprobación explícita del User el 24/08/2026;
2. registro mediante DECISIÓN #030;
3. registro mediante CAMBIO #053;
4. integración en `09_ARCHITECTURE`;
5. preparación de referencias mínimas en documentos relacionados.

---

# 36. Estado actual

```text
VERSION: 0.2
STATUS: APPROVED
AUTHORITY: CANONICAL
DECISION: #030
CHANGE: #053
EXECUTION: NONE
```

Esta versión incorpora:

* separación Model / Tool;
* compatibilidad Agent / Module;
* Memory en dos dimensiones;
* State como abstracción;
* AuditRecord no técnico;
* lifecycles específicos por entidad;
* Orchestration subordinada a Capa 2 — Control.

---

# 37. Registro de aprobación

**Aprobación del usuario:** 24/08/2026
**Decisión:** DECISIÓN #030
**Cambio:** CAMBIO #053
**Estado final:** Aprobado e integrado

La aprobación es documental y arquitectónica.

No autoriza:

* programación;
* autonomía real;
* agentes autónomos;
* conexiones externas;
* avance automático a Fase 11.
