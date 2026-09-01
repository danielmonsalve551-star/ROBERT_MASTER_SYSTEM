# ROBERT_HOME

Versión: 0.13
Estado: APROBADO E INTEGRADO
Fecha: 31/08/2026
Ubicación: 00_HOME
Función: Punto central de navegación, estado, núcleo visual y control del sistema Robert
Fase actual: Fase 10 — MVP técnico básico en preparación
Última decisión arquitectónica registrada: DECISIÓN #036
Último cambio arquitectónico registrado: CAMBIO #061
Estado operativo: Documental / conceptual / manual / supervisado
Autonomía operativa: 0
Execution Authority: NONE

Tags: #robert/home #robert/nucleo #robert/estado-actual #robert/navegacion #robert/fase-10

---

# OBJETIVO

ROBERT_HOME es la entrada principal del sistema Robert.

Su función es mostrar de forma rápida:

* qué es Robert;
* estado real del proyecto;
* fase actual;
* arquitectura vigente;
* documentos maestros disponibles;
* documentos técnicos disponibles;
* decisiones y cambios recientes;
* prioridades actuales;
* pendientes reales;
* restricciones activas;
* próximo bloque de trabajo.

Este documento funciona como el punto central de navegación del proyecto.

---

# ESTADO MAESTRO ACTUAL

Robert se encuentra en:

```text
FASE 10
MVP TÉCNICO BÁSICO EN PREPARACIÓN
```

Estado operativo:

```text
DOCUMENTAL
CONCEPTUAL
MANUAL
SUPERVISED
```

Se mantiene:

```text
AUTONOMY_LEVEL = 0
EXECUTION_AUTHORITY = NONE
```

No existe todavía autorización para:

```text
PROGRAMMING
REAL TOOL EXECUTION
AUTOMATIC MEMORY
AUTONOMOUS AGENTS
AUTONOMOUS VALIDATION
EXTERNAL EXECUTION
PHASE 11
```

---

# ARQUITECTURA PRINCIPAL APROBADA

La cadena arquitectónica principal vigente es:

```text
ROBERT_CANONICAL_MODEL v0.2
DECISIÓN #030
CAMBIO #053

        ↓

ROBERT_ORCHESTRATOR_SPEC v0.1
DECISIÓN #031
CAMBIO #054

        ↓

ROBERT_AGENT_ARCHITECTURE v0.1
DECISIÓN #032
CAMBIO #055
Corrección: CAMBIO #056

        ↓

ROBERT_SKILL_ARCHITECTURE v0.1
DECISIÓN #033
CAMBIO #057
Corrección: CAMBIO #058

        ↓

ROBERT_MODEL_INTERFACE_SPEC v0.1
DECISIÓN #034
CAMBIO #059

        ↓

ROBERT_MEMORY_ARCHITECTURE v0.1
DECISIÓN #035
CAMBIO #060

        ↓

ROBERT_VALIDATION_ARCHITECTURE v0.1
DECISIÓN #036
CAMBIO #061
```
ROBERT_TOOL_ARCHITECTURE v0.1
DECISIÓN #037
CAMBIO #062

ROBERT_IMPLEMENTATION_CONTRACTS v0.1
DECISIÓN #038
CAMBIO #063

ROBERT_PHASE_10_EXIT_CRITERIA v0.1
DECISIÓN #039
CAMBIO #064

ROBERT_BUILD_ORDER v0.1
DECISIÓN #040
CAMBIO #065
Estado:

```text
CORE ARCHITECTURE = APPROVED
IMPLEMENTATION = NONE
```

---

# DISTINCIONES CANÓNICAS ACTIVAS

Robert mantiene:

```text
ROBERT ≠ MODEL

ROBERT ≠ AGENT

AGENT ≠ SKILL

MODEL ≠ TOOL

SKILL ≠ TOOL

PERMISSION ≠ SCOPE

RISK ≠ PERMISSION

RISK ≠ EXECUTION AUTHORITY

VALIDATION ≠ AUTHORIZATION

VALIDATION ≠ APPROVAL

VALIDATION ≠ EXECUTION AUTHORITY

CONTEXT ≠ MEMORY

MEMORY_TYPE ≠ RETENTION

MEMORY RETRIEVAL SCOPE ≠ AUTHORIZED OPERATIONAL SCOPE
```

---

# ROUTING AUTHORITY

La autoridad de routing pertenece al:

```text
ROBERT_ORCHESTRATOR
```

El Orchestrator puede coordinar conceptualmente:

```text
Intent Router
Context Resolver
Module Router
Agent Router
Skill Resolver
Model Router
Tool Resolver
Memory Resolver
Validation Resolver
Permission / Scope Check
Risk Check
Conflict Check
Approval Gate
```

Las responsabilidades especializadas no crean Orchestrators paralelos.

---

# MEMORY

Arquitectura vigente:

```text
ROBERT_MEMORY_ARCHITECTURE v0.1
STATUS: APPROVED
DECISION: #035
CHANGE: #060
```

Dimensiones canónicas:

```text
RETENTION:
ACTIVE
TEMPORARY
PERSISTENT

MEMORY_TYPE:
CORE
SEMANTIC
EPISODIC
DECISIONAL
PROCEDURAL
```

Se mantiene:

```text
MEMORY CANDIDATE ≠ MEMORY

MODEL OUTPUT ≠ MEMORY WRITE

AGENT OUTPUT ≠ MEMORY WRITE

SKILL OUTPUT ≠ MEMORY WRITE

MEMORY AUTHORITY METADATA ≠ GLOBAL SOURCE PRECEDENCE
```

Memory automática no está implementada.

---

# VALIDATION

Arquitectura vigente:

```text
ROBERT_VALIDATION_ARCHITECTURE v0.1
STATUS: APPROVED
DECISION: #036
CHANGE: #061
```

Dimensiones principales:

```text
VALIDATION_TYPE
REVIEWER_ROLE
```

Se mantiene:

```text
VALIDATION_TYPE ≠ REVIEWER_ROLE

VALIDATOR ≠ NEW CANONICAL ENTITY TYPE

VALIDATOR ≠ ROUTING AUTHORITY

VALIDATED OUTPUT ≠ AUTHORIZED ACTION

CONSENSUS ≠ TRUTH

CONFIDENCE ≠ TRUTH
```

Validation automática productiva no está implementada.

---

# ESTADO DE IMPLEMENTACIÓN

Actualmente:

```text
CORE ARCHITECTURE: APPROVED

MEMORY STORE: NOT NTED

AUTOMATED VALIDATION ENGINE: NOT IMPLEMENTED

AUTOMATIC TOOL EXECUTION: NOT IMPLEMENTED

AUTONOMOUS AGENTS: NOT ACTIVE

AUTOMATIC MEMORY WRITE: DISABLED

AUTOMATIC MEMORY RETRIEVAL: NOT IMPLEMENTED

EXTERNAL EXECUTION: NONE
```

---

# PENDIENTE REAL ACTUAL

La prioridad ya no es seguir creando arquitectura principal sin revisión.

El bloque actual es:

IMPLEMENTATION_READINESS = IN PROGRESS

CORE_ARCHITECTURE = CLOSED
TOOL_ARCHITECTURE = CLOSED
IMPLEMENTATION_CONTRACTS = CLOSED
PHASE_10_EXIT_CRITERIA = CLOSED
BUILD_ORDER = CLOSED

PHASE_10_EXIT_AUDIT = FAIL

KNOWN_ARCHITECTURAL_BLOCKERS = 0
DOCUMENT_NORMALIZATION_BLOCKERS = 6

READY_FOR_PHASE_10_CLOSURE = NO
READY_FOR_IMPLEMENTATION_AUTHORIZATION = NO
```

Regla:

```text
ARCHITECTURE APPROVED
        ≠
READY FOR CODE
```
DECISIÓN #037 / CAMBIO #062
ROBERT_TOOL_ARCHITECTURE v0.1
APPROVED

DECISIÓN #038 / CAMBIO #063
ROBERT_IMPLEMENTATION_CONTRACTS v0.1
APPROVED

DECISIÓN #039 / CAMBIO #064
ROBERT_PHASE_10_EXIT_CRITERIA v0.1
APPROVED

DECISIÓN #040 / CAMBIO #065
ROBERT_BUILD_ORDER v0.1
APPROVED
---

# TRAZABILIDAD RECIENTE

Últimas aprobaciones arquitectónicas:

```text
DECISIÓN #035
ROBERT_MEMORY_ARCHITECTURE v0.1

DECISIÓN #036
ROBERT_VALIDATION_ARCHITECTURE v0.1
```

Últimos cambios arquitectónicos:

```text
CAMBIO #060
Aprobación e integración de Memory Architecture

CAMBIO #061
Aprobación e integración de Validation Architecture
```

---

# ESTADO DE ROBERT_HOME

`ROBERT_HOME` funciona como resumen vivo del estado del sistema.

Esta versión normaliza el HOME para reflejar la arquitectura vigente hasta:

```text
DECISIÓN #036
CAMBIO #061
```

y elimina del encabezado principal el estado antiguo:

```text
Propuesta corregida — pendiente de revisión
```

La historia detallada de versiones, decisiones y cambios permanece en:

```text
ROBERT_DECISIONS_LOG
ROBERT_CONTROL_DE_CAMBIOS
```

HOME no sustituye esos registros.

---

# DEFINICIÓN DE ROBERT

Robert no es:

* Un chatbot.
* Una app de productividad simple.
* Una automatización aislada.
* Una bóveda de notas.
* Un sistema autónomo sin control del usuario.

Robert es:

**Un sistema operativo personal de inteligencia artificial tipo AI Command Center.**

Su objetivo es transformar:

```text
Ideas
↓
Conversaciones
↓
Documentos
↓
Decisiones
↓
Sistemas
↓
Acciones supervisadas
```

Robert busca funcionar como un centro de mando personal, documental, visual, modular y seguro.

---

# ROBERT_HOME COMO NÚCLEO

ROBERT_HOME funciona como el núcleo de entrada del sistema.

Esto significa que:

* Es el primer punto de navegación.
* Resume el estado real.
* Enlaza documentos principales.
* Muestra restricciones activas.
* Muestra prioridades.
* Muestra documentos técnicos aprobados.
* Muestra documentos pendientes.
* Conecta la parte documental con la visión visual de Robert.
* Funciona como referencia rápida antes de avanzar.

Alineación visual:

```text
ROBERT_HOME = Núcleo documental y visual de entrada
Tag oficial: #robert/nucleo
```

---

# PRINCIPIO CENTRAL

```text
El usuario manda.
Robert no ejecuta acciones importantes sin permiso.
```

---

# ESTADO ACTUAL DEL PROYECTO

Estado real actualizado:

```text
Fase actual:
Fase 10 — MVP técnico básico en preparación

Modo operativo:
Documental, manual y supervisado

MVP manual:
Validado

Sandbox manual:
Validado

GitHub:
Configurado como respaldo documental privado y manual

Obsidian:
Cerebro documental manual

Programación:
No autorizada

Código real:
No autorizado

Pantallas reales:
No autorizadas

Base de datos real:
No autorizada

Conexiones externas:
No autorizadas

Automatizaciones reales:
No autorizadas

Agentes autónomos:
No autorizados

Fase 11:
No autorizada
```

---

# ESTADO OPERATIVO ACTUAL

Robert se encuentra en:

```text
Fase 10 — MVP técnico básico en preparación
```

Estado consolidado:

```text
MVP manual validado
Sandbox manual validado
GitHub configurado como respaldo documental privado/manual
Obsidian usado como cerebro documental manual
CONTEXT_MASTER v0.5 reanclado
PHASES v0.5 reconciliado
COMMANDS v0.4 aprobado e integrado
Escala de riesgo y autonomía unificada
DOCUMENT_LIFECYCLE_SPEC v0.2 aprobado
VERSIONING_AND_CHANGE_POLICY_SPEC v0.2 aprobado
DATA_CONSISTENCY_AND_CONFLICT_RESOLUTION_SPEC v0.3 aprobado
ROBERT_HOME v0.11 aprobado e integrado
ROBERT_HOME v0.12 en propuesta corregida pendiente de revisión
USER_ACTIONS_SPEC v0.2 aprobado, integrado y auditado voluntariamente
CAMBIO #047 reconocido como antecedente de trazabilidad de USER_ACTIONS_SPEC v0.2
APPROVAL_GATE v0.3 aprobado e integrado
DECISIÓN #027 registrada
CAMBIO #049 registrado
ROBERT_HOME v0.11 aprobado e integrado mediante DECISIÓN #028 / CAMBIO #050
ROBERT_VISUAL_REFERENCE reconocido como documento visual correcto
Wireframe v0.3 aprobado e integrado
Fuente física del wireframe v0.3 normalizada mediante CAMBIO #051
```

Restricciones activas:

```text
Sin programación autorizada
Sin código real
Sin base de datos real
Sin gate real
Sin sistema real de autorización
Sin sistema real de consistencia documental
Sin sistema real de control de versiones
Sin motor real de resolución de conflictos
Sin conexiones externas
Sin automatizaciones reales
Sin agentes autónomos activos
Sin avance a Fase 11
```

---

# DOCUMENTOS MAESTROS DEL SISTEMA

## 00_HOME

```text
ROBERT_HOME.md
Versión actual propuesta: v0.12
Estado: Propuesta corregida — pendiente de revisión
Cambio relacionado: CAMBIO #051
Función: Punto central de navegación, estado, núcleo visual y control del sistema
Tag clave: #robert/nucleo
```

Estado previo aprobado:

```text
ROBERT_HOME v0.11
Estado: Aprobado e integrado
Decisión relacionada: DECISIÓN #028
Cambio de integración: CAMBIO #050
```

---

## 01_CONTEXT

```text
ROBERT_CONTEXT_MASTER.md
Versión actual: v0.5
Estado: Reanclado
Función: Fuente central de verdad contextual
```

---

## 02_COMMANDS

```text
ROBERT_COMMANDS.md
Versión actual: v0.4
Estado: Aprobado e integrado
Función: Comandos, acciones de control e interpretación operativa
```

---

## 03_DECISIONS

```text
ROBERT_DECISIONS_LOG.md
Estado: Activo
Función: Registro formal de decisiones aprobadas por el usuario
Última decisión relevante: DECISIÓN #028
```

---

## 04_SECURITY

```text
ROBERT_SECURITY_RULES.md
Estado: Aprobado
Función: Seguridad, límites, permisos y control del usuario
```

```text
ROBERT_CONTROL_DE_CAMBIOS.md
Estado: Activo
Función: Registro formal de cambios, correcciones e integraciones
Nota: Documento maestro operativo de trazabilidad
Último cambio relevante: CAMBIO #051
```

---

## 05_PHASES

```text
ROBERT_PHASES.md
Versión actual: v0.5
Estado: Reconciliado
Función: Mapa de fases del proyecto Robert
```

---

## 06_MODULES

```text
ROBERT_MODULES.md
Estado: Estructura inicial aprobada
Función: Módulos funcionales del sistema Robert
```

---

## 07_VISUAL

```text
ROBERT_VISUAL_REFERENCE.md
Estado: En desarrollo conceptual
Función: Dirección visual, núcleo, galaxias, paneles y experiencia visual
Nota: HOME funciona como núcleo documental y visual de entrada
```

Regla de nomenclatura visual:

```text
El documento visual correcto es ROBERT_VISUAL_REFERENCE.
No usar ROBERT_VISUAL como documento oficial si la fuente vigente confirmada es ROBERT_VISUAL_REFERENCE.
```

---

## 08_PROMPTS

```text
ROBERT_PROMPTS.md
Estado: Activo / en evolución
Función: Prompts base para trabajar con ChatGPT, Claude y otros modelos
```

---

## 09_ARCHITECTURE

```text
ROBERT_SYSTEM_ARCHITECTURE.md
Estado: Activo
Función: Arquitectura conceptual por capas
```

---

## 10_MVP

```text
ROBERT_MVP_PLAN.md
Estado: Aprobado
Función: Plan del MVP manual y técnico
```

---

## 15_SANDBOX

```text
ROBERT_SANDBOX.md
Estado: Validado
Función: Área de pruebas manuales y simulaciones controladas
```

```text
SANDBOX_RULES.md
Estado: Activo
Función: Reglas del sandbox manual
```

```text
SANDBOX_TESTS.md
Estado: Activo
Función: Pruebas manuales del sistema
```

```text
SANDBOX_RESULTS.md
Estado: Activo
Función: Resultados de pruebas del sandbox
```

---

# DOCUMENTOS TÉCNICOS DE FASE 10

## Wireframe oficial vigente

```text
ROBERT_TECHNICAL_MVP_WIREFRAME.md
Versión vigente: v0.3
Estado: Aprobado e integrado
Fuente física oficial vigente: Sí
Normalización física: Completada mediante CAMBIO #051
```

Regla de fuente vigente:

```text
No existen dos wireframes oficiales vigentes en paralelo.
El wireframe vigente conceptual y físico es ROBERT_TECHNICAL_MVP_WIREFRAME.md v0.3.
Cualquier versión anterior queda como histórica/reemplazada o no vigente.
```

Archivo propuesta:

```text
ROBERT_TECHNICAL_MVP_WIREFRAME_v0.3_PROPUESTA.md
Estado: Eliminado previamente / no vigente / no fuente oficial / no requerido
```

Regla:

```text
No recrear la propuesta.
No restaurar el archivo eliminado.
No mantener dos fuentes físicas paralelas.
```

---

## Documentos aprobados e integrados

```text
ROBERT_TECHNICAL_MVP_PLAN.md
Estado: Aprobado
```

```text
ROBERT_TECHNICAL_MVP_WIREFRAME.md
Versión vigente: v0.3
Estado: Aprobado e integrado
Fuente física oficial vigente: Sí
Cambio de normalización: CAMBIO #051
Nota: La pendiente de normalización física quedó cerrada.
```

```text
ROBERT_TECHNICAL_COMPONENTS_SPEC.md
Versión: v0.2
Estado: Aprobado
```

```text
ROBERT_TECHNICAL_DATA_MODEL_SPEC.md
Versión: v0.1
Estado: Aprobado
```

```text
ROBERT_TECHNICAL_INTERACTION_FLOW_SPEC.md
Versión: v0.2
Estado: Aprobado
```

```text
ROBERT_TECHNICAL_SCREEN_STATE_SPEC.md
Versión: v0.2
Estado: Aprobado
```

```text
ROBERT_TECHNICAL_USER_ACTIONS_SPEC.md
Versión: v0.2
Estado: Aprobado e integrado — auditoría voluntaria completada sin cambios de fondo
Decisión relacionada: DECISIÓN #017
Cambio relacionado: CAMBIO #028
Antecedente de trazabilidad: CAMBIO #047
Nota: Fuente canónica usada para APPROVAL_GATE v0.3
```

```text
ROBERT_TECHNICAL_ERROR_AND_BLOCKING_SPEC.md
Versión: v0.2
Estado: Aprobado
```

```text
ROBERT_TECHNICAL_PERMISSIONS_AND_SCOPES_SPEC.md
Versión: v0.2
Estado: Aprobado
```

```text
ROBERT_TECHNICAL_AUDIT_TRAIL_SPEC.md
Versión: v0.2
Estado: Aprobado
```

```text
ROBERT_TECHNICAL_NOTIFICATION_AND_ALERTS_SPEC.md
Versión: v0.2
Estado: Aprobado
```

```text
ROBERT_TECHNICAL_SESSION_AND_CONTEXT_SPEC.md
Versión: v0.2
Estado: Aprobado
```

```text
ROBERT_TECHNICAL_DOCUMENT_LIFECYCLE_SPEC.md
Versión: v0.2
Estado: Aprobado
```

```text
ROBERT_TECHNICAL_VERSIONING_AND_CHANGE_POLICY_SPEC.md
Versión: v0.2
Estado: Aprobado
```

```text
ROBERT_TECHNICAL_DATA_CONSISTENCY_AND_CONFLICT_RESOLUTION_SPEC.md
Versión: v0.3
Estado: Aprobado
```

```text
ROBERT_TECHNICAL_APPROVAL_AND_AUTHORIZATION_GATE_SPEC.md
Versión: v0.3
Estado: Aprobado e integrado
Decisión relacionada: DECISIÓN #027
Cambio relacionado: CAMBIO #049
Cambio de corrección previo: CAMBIO #048
Nota: Especificación conceptual del ApprovalGate. No crea gate real.
```

---

# ESTADO DE WIREFRAME v0.3

Documento:

```text
ROBERT_TECHNICAL_MVP_WIREFRAME.md
```

Versión:

```text
v0.3
```

Estado:

```text
Aprobado e integrado
Fuente física oficial vigente
Normalización física completada
```

Relación formal:

```text
DECISIÓN #010 — Aprobación de ROBERT_TECHNICAL_MVP_WIREFRAME v0.3
CAMBIO #010 — Actualización del wireframe técnico a v0.3
CAMBIO #051 — Normalización de fuente física vigente de ROBERT_TECHNICAL_MVP_WIREFRAME v0.3
```

Archivo propuesta:

```text
ROBERT_TECHNICAL_MVP_WIREFRAME_v0.3_PROPUESTA.md
Estado: Eliminado previamente / no vigente / no fuente oficial / no requerido
```

Regla:

```text
La fuente conceptual y física vigente es ROBERT_TECHNICAL_MVP_WIREFRAME.md.
La propuesta eliminada no debe recrearse.
```

---

# ESTADO DE APPROVAL_GATE v0.3

Documento:

```text
ROBERT_TECHNICAL_APPROVAL_AND_AUTHORIZATION_GATE_SPEC.md
```

Versión:

```text
v0.3
```

Estado:

```text
Aprobado e integrado
```

Relación formal:

```text
DECISIÓN #027 — Aprobación de ROBERT_TECHNICAL_APPROVAL_AND_AUTHORIZATION_GATE_SPEC v0.3
CAMBIO #049 — Aprobación e integración de ROBERT_TECHNICAL_APPROVAL_AND_AUTHORIZATION_GATE_SPEC v0.3
CAMBIO #048 — Corrección de ROBERT_TECHNICAL_APPROVAL_AND_AUTHORIZATION_GATE_SPEC v0.3
```

Función:

```text
Definir conceptualmente cómo Robert debe decidir si una acción del usuario puede continuar, requiere confirmación, requiere aprobación formal, debe pausarse o debe bloquearse.
```

Regla:

```text
APPROVAL_GATE v0.3 está aprobado e integrado como documento técnico conceptual.
APPROVAL_GATE v0.3 no crea gate real.
APPROVAL_GATE v0.3 no autoriza programación.
APPROVAL_GATE v0.3 no autoriza ejecución real.
APPROVAL_GATE v0.3 no autoriza Fase 11.
```

---

# FUENTE CANÓNICA USADA PARA APPROVAL_GATE v0.3

La fuente canónica usada para APPROVAL_GATE v0.3 es:

```text
ROBERT_TECHNICAL_USER_ACTIONS_SPEC v0.2
Estado: Aprobado e integrado
DECISIÓN #017
CAMBIO #028
Antecedente de trazabilidad: CAMBIO #047
Auditoría voluntaria: completada sin cambios de fondo
```

La auditoría voluntaria confirmó:

```text
1. Lista canónica de 20 acciones.
2. Numeración correcta de las 20 acciones.
3. Uso de los 10 componentes canónicos.
4. Inclusión de AppShell como componente oficial.
5. Exclusión de MainCanvas como componente oficial.
6. ACCIÓN 12 mapeada correctamente como Gate 2 / Gate 7.
7. Uso como referencia canónica para corregir APPROVAL_GATE v0.3.
```

Lista canónica de 20 acciones:

```text
ACCIÓN 1 — ESCRIBIR COMANDO
ACCIÓN 2 — SELECCIONAR DOCUMENTO
ACCIÓN 3 — REVISAR ESTADO GENERAL
ACCIÓN 4 — CREAR DOCUMENTO TÉCNICO
ACCIÓN 5 — CORREGIR DOCUMENTO TÉCNICO
ACCIÓN 6 — APROBAR DOCUMENTO
ACCIÓN 7 — REGISTRAR DECISIÓN
ACCIÓN 8 — REGISTRAR CAMBIO
ACCIÓN 9 — ACTUALIZAR HOME
ACCIÓN 10 — ACTUALIZAR README
ACCIÓN 11 — CAMBIAR MODO
ACCIÓN 12 — ACTIVAR SANDBOX MANUAL
ACCIÓN 13 — PAUSAR AVANCE
ACCIÓN 14 — BLOQUEAR ACCIÓN
ACCIÓN 15 — VER DECISIONES PENDIENTES
ACCIÓN 16 — RESOLVER DECISIÓN PENDIENTE
ACCIÓN 17 — VER MAPA DOCUMENTAL
ACCIÓN 18 — MARCAR RESPALDO MANUAL EN GITHUB
ACCIÓN 19 — SOLICITAR REVISIÓN CRÍTICA
ACCIÓN 20 — PEDIR SIGUIENTE PASO
```

Componentes canónicos confirmados:

```text
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
```

Regla:

```text
MainCanvas no forma parte de la lista canónica de componentes aprobados.
MainCanvas no debe usarse como componente oficial.
```

---

# ENLACES CENTRALES DEL SISTEMA

## Documentos base

```text
[[ROBERT_HOME]]
[[ROBERT_CONTEXT_MASTER]]
[[ROBERT_COMMANDS]]
[[ROBERT_DECISIONS_LOG]]
[[ROBERT_CONTROL_DE_CAMBIOS]]
[[ROBERT_SECURITY_RULES]]
[[ROBERT_PHASES]]
[[ROBERT_MODULES]]
[[ROBERT_VISUAL_REFERENCE]]
[[ROBERT_PROMPTS]]
[[ROBERT_SYSTEM_ARCHITECTURE]]
[[ROBERT_MVP_PLAN]]
```

---

## MVP técnico

```text
[[ROBERT_TECHNICAL_MVP_PLAN]]
[[ROBERT_TECHNICAL_MVP_WIREFRAME]]
[[ROBERT_TECHNICAL_COMPONENTS_SPEC]]
[[ROBERT_TECHNICAL_DATA_MODEL_SPEC]]
[[ROBERT_TECHNICAL_INTERACTION_FLOW_SPEC]]
[[ROBERT_TECHNICAL_SCREEN_STATE_SPEC]]
[[ROBERT_TECHNICAL_USER_ACTIONS_SPEC]]
[[ROBERT_TECHNICAL_ERROR_AND_BLOCKING_SPEC]]
[[ROBERT_TECHNICAL_PERMISSIONS_AND_SCOPES_SPEC]]
[[ROBERT_TECHNICAL_AUDIT_TRAIL_SPEC]]
[[ROBERT_TECHNICAL_NOTIFICATION_AND_ALERTS_SPEC]]
[[ROBERT_TECHNICAL_SESSION_AND_CONTEXT_SPEC]]
[[ROBERT_TECHNICAL_DOCUMENT_LIFECYCLE_SPEC]]
[[ROBERT_TECHNICAL_VERSIONING_AND_CHANGE_POLICY_SPEC]]
[[ROBERT_TECHNICAL_DATA_CONSISTENCY_AND_CONFLICT_RESOLUTION_SPEC]]
[[ROBERT_TECHNICAL_APPROVAL_AND_AUTHORIZATION_GATE_SPEC]]
```

---

## Sandbox

```text
[[ROBERT_SANDBOX]]
[[SANDBOX_RULES]]
[[SANDBOX_TESTS]]
[[SANDBOX_RESULTS]]
```

---

# PRIORIDAD ACTUAL

Prioridad actual real:

```text
1. Reemplazar ROBERT_HOME con v0.12 como propuesta corregida pendiente de revisión.
2. Revisar ROBERT_HOME v0.12 completo.
3. Confirmar que HOME v0.12 elimina la pendiente de normalización física del wireframe.
4. Confirmar que HOME v0.12 reconoce CAMBIO #051.
5. Confirmar que HOME v0.12 mantiene ROBERT_TECHNICAL_MVP_WIREFRAME.md como fuente física oficial vigente.
6. Confirmar que HOME v0.12 no recrea la propuesta eliminada.
7. Actualizar README después de HOME v0.12 si se acepta la corrección.
8. Mantener APPROVAL_GATE v0.3 como aprobado e integrado.
9. Mantener ROBERT_VISUAL_REFERENCE como documento visual correcto.
10. Mantener Fase 10 sin programación.
11. Mantener GitHub y Obsidian manuales.
12. Definir el siguiente documento técnico solo con autorización del usuario.
13. No avanzar a programación.
14. No avanzar a Fase 11.
```

---

# PRÓXIMOS PASOS

Próximos pasos recomendados:

```text
Paso 1:
Reemplazar ROBERT_HOME con v0.12.

Paso 2:
Revisar ROBERT_HOME v0.12 completo.

Paso 3:
Si ROBERT_HOME v0.12 queda correcto, actualizar README para reflejar:

- ROBERT_HOME v0.12 como propuesta corregida pendiente de revisión.
- CAMBIO #051 registrado.
- Fuente física del wireframe v0.3 normalizada.
- ROBERT_TECHNICAL_MVP_WIREFRAME.md como fuente física oficial vigente.
- Archivo propuesta eliminado previamente / no vigente / no requerido.
- APPROVAL_GATE v0.3 aprobado e integrado.
- ROBERT_HOME v0.11 aprobado e integrado.
- Sin programación.
- Sin conexiones.
- Sin automatizaciones.
- Sin agentes.
- Sin Fase 11.

Paso 4:
No aprobar HOME automáticamente.

Paso 5:
Si el usuario decide aprobar HOME v0.12, deberá escribir:

APRUEBO ROBERT_HOME v0.12

Paso 6:
Solo después de esa aprobación explícita:

- Registrar decisión formal.
- Registrar cambio de aprobación e integración.
- Actualizar README si aplica.

Paso 7:
No avanzar a programación.
No activar conexiones.
No activar automatizaciones.
No activar agentes.
No avanzar a Fase 11.
```

---

# REGLAS PRINCIPALES ACTIVAS

```text
El usuario manda.
Robert no ejecuta acciones importantes sin permiso.
Primero orden. Después poder.
Simular no es ejecutar.
Preparar no es enviar.
Diseñar no es activar.
Proponer no es decidir.
Aprobar no es ejecutar.
Documento técnico no es sistema real.
ApprovalGate conceptual no es gate real.
Fase 10 no autoriza programación.
Fase 10 no autoriza conexiones externas.
Fase 10 no autoriza automatizaciones reales.
Fase 10 no autoriza agentes autónomos.
```

---

# ACCIONES DE CONTROL

Las acciones de control están fuera de la escala de riesgo.

Comandos de control:

```text
DETENTE
PAUSA
NO_AVANCES
NO SIGAS
CANCELA
BLOQUEA
NO EJECUTES
SOLO BORRADOR
REVOCA_AUTONOMIA
VOLVER_A_MANUAL
```

Regla:

```text
Si el usuario usa una acción de control, Robert debe obedecer inmediatamente.
```

---

# ESCALA DE RIESGO ACTUAL

```text
Nivel 0 — Informativo
Nivel 1 — Bajo
Nivel 2 — Medio
Nivel 3 — Alto
Nivel 4 — Crítico
```

Regla corregida:

```text
Nivel 0 = Informativo
Acciones de control = fuera de la escala de riesgo
```

---

# AUTONOMÍA ACTUAL

Nivel de autonomía actual:

```text
Nivel 0 — Sin autonomía ejecutiva
```

Robert puede:

```text
Explicar
Resumir
Ordenar
Proponer
Redactar documentos
Corregir documentos
Detectar contradicciones
Sugerir siguientes pasos
Preparar bloques para copiar/pegar
```

Robert no puede:

```text
Ejecutar acciones reales
Programar
Crear sistemas reales
Conectar apps
Automatizar flujos
Modificar GitHub automáticamente
Modificar Obsidian automáticamente
Enviar correos
Crear bases de datos
Activar agentes autónomos
Avanzar de fase por su cuenta
```

---

# ESTADO DE GITHUB

Repositorio:

```text
ROBERT_MASTER_SYSTEM
```

Uso autorizado:

```text
Respaldo documental privado
Control de versiones manual
Historial manual de cambios
Base documental para futura fase técnica
```

No autorizado:

```text
Commits automáticos
Sincronización automática
Agentes modificando archivos
Conexiones automáticas
Automatización de GitHub
```

Últimas acciones manuales relevantes:

```text
DECISIÓN #028 registrada manualmente
CAMBIO #050 registrado manualmente
ROBERT_HOME v0.11 aprobado e integrado
CAMBIO #051 registrado manualmente
Fuente física del wireframe v0.3 normalizada
ROBERT_HOME v0.12 preparado como propuesta corregida pendiente de revisión
```

---

# ESTADO DE OBSIDIAN

Uso actual:

```text
Cerebro documental manual
Organización por carpetas
Grafo visual conceptual
Lectura y navegación de documentos
```

No autorizado:

```text
Sincronización automática
Automatización de notas
Agentes modificando archivos
Conexiones automáticas
```

Documento visual correcto:

```text
ROBERT_VISUAL_REFERENCE
```

---

# FASES DEL PROYECTO

Estado resumido:

```text
Fase 1 — Identidad y visión: completada
Fase 2 — Documentos maestros: completada
Fase 3 — Fuente central de verdad: completada
Fase 4 — Comandos: completada
Fase 5 — Módulos: completada
Fase 6 — Arquitectura conceptual: completada
Fase 7 — Diseño visual/UX: en evolución conceptual
Fase 8 — MVP manual: validado
Fase 9 — Sandbox manual: validado
Fase 10 — MVP técnico básico: en preparación
Fase 11 — Conexión de herramientas: no autorizada
Fase 12 — Automatizaciones controladas: no autorizada
Fase 13 — Voz/multimodal: futura
Fase 14 — Agentes especializados: futura
Fase 15 — Business Builder avanzado: futura
Fase 16 — Seguridad avanzada/pruebas: futura
Fase 17 — Iteraciones: futura
```

Fase activa:

```text
Fase 10 — MVP técnico básico en preparación
```

---

# CONTROL DE VERSIONES DE ROBERT_HOME

| Versión | Estado                                      | Descripción                                                                                                                                                                        |
| ------- | ------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| v0.1    | Inicial                                     | Primer documento HOME del sistema                                                                                                                                                  |
| v0.2    | Actualización                               | Se integró dirección general del proyecto Robert                                                                                                                                   |
| v0.3    | Base actualizada                            | Se organizaron documentos maestros y navegación inicial                                                                                                                            |
| v0.4    | Parcial / inconsistente                     | Se agregaron múltiples logs de avances, pero la parte superior quedó desactualizada                                                                                                |
| v0.5    | Propuesta corregida no cerrada              | Se reconcilió HOME con Fase 10, pero quedaron huecos de wireframe, trazabilidad y tag de núcleo                                                                                    |
| v0.6    | Propuesta corregida no cerrada              | Se corrigió fuente vigente del wireframe, trazabilidad pendiente de APPROVAL_GATE y tag #robert/nucleo, pero faltó tarea operativa para normalizar el archivo físico del wireframe |
| v0.7    | Propuesta corregida no cerrada              | Se agregó tarea manual para resolver la fuente física vigente del wireframe v0.3, pero aún faltaba trazabilidad formal del propio HOME                                             |
| v0.8    | Aprobado e integrado                        | Se cita CAMBIO #045 para cerrar trazabilidad acumulada de HOME v0.5–v0.7 y se integra mediante DECISIÓN #026 / CAMBIO #046                                                         |
| v0.9    | Propuesta corregida pendiente de revisión   | Actualizó HOME después de CAMBIO #048 y reconoció APPROVAL_GATE v0.3 como propuesta corregida pendiente de revisión                                                                |
| v0.10   | Propuesta corregida con conflicto detectado | Actualizó HOME después de DECISIÓN #027 / CAMBIO #049, pero omitió CAMBIO #047 y mantuvo ROBERT_VISUAL en lugar de ROBERT_VISUAL_REFERENCE                                         |
| v0.11   | Aprobado e integrado                        | Corrigió trazabilidad de CAMBIO #047 y reemplazó ROBERT_VISUAL por ROBERT_VISUAL_REFERENCE                                                                                         |
| v0.12   | Propuesta corregida pendiente de revisión   | Actualiza HOME después de CAMBIO #051 y cierra la pendiente de normalización física del wireframe v0.3                                                                             |

---

# MOTIVO DE v0.12

ROBERT_HOME v0.12 existe para corregir:

```text
1. La pendiente de normalización física del wireframe v0.3.
2. La referencia a posible duplicidad entre ROBERT_TECHNICAL_MVP_WIREFRAME.md y ROBERT_TECHNICAL_MVP_WIREFRAME_v0.3_PROPUESTA.md.
3. La necesidad de reflejar CAMBIO #051.
4. La necesidad de reconocer que ROBERT_TECHNICAL_MVP_WIREFRAME.md es la fuente física oficial vigente.
5. La necesidad de registrar que la propuesta v0.3 ya fue eliminada previamente y no debe recrearse.
```

---

# ESTADO DE DOCUMENTOS Y CAMBIOS RECIENTES

## Aprobaciones recientes

```text
DECISIÓN #027 — Aprobación de ROBERT_TECHNICAL_APPROVAL_AND_AUTHORIZATION_GATE_SPEC v0.3
CAMBIO #049 — Aprobación e integración de ROBERT_TECHNICAL_APPROVAL_AND_AUTHORIZATION_GATE_SPEC v0.3

DECISIÓN #028 — Aprobación de ROBERT_HOME v0.11
CAMBIO #050 — Aprobación e integración de ROBERT_HOME v0.11
```

---

## Cambios recientes registrados

```text
CAMBIO #047 — Corrección de ROBERT_TECHNICAL_USER_ACTIONS_SPEC v0.2
Estado: Registrado como antecedente de corrección / trazabilidad
Función: Resolver conflicto de versión, fuente vigente y trazabilidad de USER_ACTIONS_SPEC v0.2
```

```text
CAMBIO #048 — Corrección de ROBERT_TECHNICAL_APPROVAL_AND_AUTHORIZATION_GATE_SPEC v0.3
Estado: Registrado
Función: Registrar APPROVAL_GATE v0.3 como propuesta corregida pendiente de revisión antes de su aprobación formal
```

```text
CAMBIO #049 — Aprobación e integración de ROBERT_TECHNICAL_APPROVAL_AND_AUTHORIZATION_GATE_SPEC v0.3
Estado: Aprobado e integrado
Función: Registrar APPROVAL_GATE v0.3 como documento técnico conceptual aprobado e integrado
```

```text
CAMBIO #050 — Aprobación e integración de ROBERT_HOME v0.11
Estado: Aprobado e integrado
Función: Registrar ROBERT_HOME v0.11 como documento maestro aprobado e integrado
```

```text
CAMBIO #051 — Normalización de fuente física vigente de ROBERT_TECHNICAL_MVP_WIREFRAME v0.3
Estado: Registrado
Función: Confirmar ROBERT_TECHNICAL_MVP_WIREFRAME.md como fuente física oficial vigente y aclarar que la propuesta eliminada no debe recrearse
```

---

# NORMALIZACIÓN DEL WIREFRAME

Estado:

```text
Completada mediante CAMBIO #051
```

Fuente física oficial vigente:

```text
ROBERT_TECHNICAL_MVP_WIREFRAME.md
```

Versión:

```text
v0.3
```

Estado:

```text
Aprobado e integrado
```

Archivo propuesta:

```text
ROBERT_TECHNICAL_MVP_WIREFRAME_v0.3_PROPUESTA.md
```

Estado:

```text
Eliminado previamente
No vigente
No fuente oficial
No requerido
No recrear
```

---

# DOCUMENTO TÉCNICO RECIÉN NORMALIZADO

```text
ROBERT_TECHNICAL_MVP_WIREFRAME.md
Estado: Fuente física oficial vigente
Versión: v0.3
Estado documental: Aprobado e integrado
Cambio de normalización: CAMBIO #051
```

Regla:

```text
La normalización no cambia el contenido aprobado del wireframe.
Solo elimina la ambigüedad física entre archivo oficial y archivo propuesta.
```

---

# ESTADO FINAL DE ROBERT_HOME
DOCUMENT: ROBERT_HOME

STATUS: APPROVED / INTEGRATED

PHASE: 10

LATEST_ARCHITECTURAL_DECISION: #040
LATEST_CHANGE: #065

CORE_ARCHITECTURE: CLOSED
TOOL_ARCHITECTURE: CLOSED
IMPLEMENTATION_CONTRACTS: APPROVED
PHASE_10_EXIT_CRITERIA: APPROVED
BUILD_ORDER: APPROVED

PHASE_10_EXIT_AUDIT: FAIL
KNOWN_ARCHITECTURAL_BLOCKERS: 0
DOCUMENT_NORMALIZATION_BLOCKERS: 6

READY_FOR_PHASE_10_CLOSURE: NO
READY_FOR_IMPLEMENTATION_AUTHORIZATION: NO

AUTONOMY_LEVEL: 0
EXECUTION_AUTHORITY: NONE

# PRIORIDAD ACTUAL

```text
NORMALIZE PHYSICAL DOCUMENT STATE
        ↓
RESOLVE ARCHITECTURE GAPS
        ↓
DEFINE IMPLEMENTATION READINESS
        ↓
DECIDE PHASE 10 EXIT
        ↓
ONLY THEN CONSIDER CODE
```

---

# RESTRICCIONES ACTIVAS

No autorizado actualmente:

```text
REAL PROGRAMMING
REAL DATABASE
REAL MEMORY STORE
AUTONOMOUS MEMORY
AUTONOMOUS VALIDATION
REAL TOOL EXECUTION
AUTONOMOUS AGENTS
EXTERNAL AUTOMATION
AUTOMATIC PHASE TRANSITION
```

---

# SIGUIENTE PASO

El siguiente documento a normalizar es:

```text
README.md
```

Después:

```text
ROBERT_TECHNICAL_DATA_CONSISTENCY_AND_CONFLICT_RESOLUTION_SPEC
```

y:

```text
ROBERT_TECHNICAL_VERSIONING_AND_CHANGE_POLICY_SPEC
```

---

# CIERRE

Robert mantiene una arquitectura principal formalmente aprobada hasta Validation Architecture.

El sistema continúa en Fase 10.

La prioridad actual es asegurar que los archivos físicos, estados documentales, referencias cruzadas y contratos de implementación coincidan con la gobernanza ya aprobada.

```text
ARCHITECTURE CORE = CLOSED

DOCUMENT NORMALIZATION = IN PROGRESS

READY FOR CODE = NO
```

El usuario mantiene control total.

Robert no ejecuta acciones importantes sin permiso.
