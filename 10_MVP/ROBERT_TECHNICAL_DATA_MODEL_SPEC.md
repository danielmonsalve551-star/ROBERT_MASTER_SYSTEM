# ROBERT_TECHNICAL_DATA_MODEL_SPEC

Versión: 0.1
Estado: Borrador técnico documental nuevo — pendiente de revisión
Fecha: 02/07/2026
Ubicación: 10_MVP
Documento base relacionado: ROBERT_TECHNICAL_COMPONENTS_SPEC v0.2
Fuente de verdad actual: ROBERT_CONTEXT_MASTER v0.5
Fase relacionada: Fase 10 — MVP técnico básico en preparación

Tags: #robert/orbita-2 #capa/5 #tipo/tecnico #robert/mvp-tecnico

---

# OBJETIVO

Este documento define los datos internos simulados que Robert necesitaría para operar el MVP técnico básico.

Su función es responder:

* Qué información necesita mostrar Robert.
* Qué datos necesita cada componente.
* Qué campos deben existir.
* Qué relaciones existen entre documentos, decisiones, riesgos, cambios y comandos.
* Qué datos son permitidos.
* Qué datos están prohibidos.
* Qué información sigue siendo manual y documental.

Este documento no crea una base de datos real.

Este documento no programa la app.

Este documento no conecta herramientas reales.

Este documento no automatiza acciones.

Este documento solo define modelos de datos conceptuales para una futura implementación controlada.

---

# ESTADO DE ESTE DOCUMENTO

Este documento queda como:

**Borrador técnico documental nuevo — pendiente de revisión**

No está aprobado todavía.

No reemplaza a ningún documento maestro.

No autoriza programación.

No autoriza base de datos real.

No autoriza conexiones externas.

No autoriza automatizaciones.

No autoriza agentes autónomos.

No autoriza ejecución real.

---

# REGLA CENTRAL

El usuario manda.

Robert no ejecuta acciones importantes sin permiso.

Todo dato mostrado, guardado o procesado por Robert debe respetar:

* ROBERT_SECURITY_RULES
* ROBERT_CONTEXT_MASTER v0.5
* ROBERT_DECISIONS_LOG
* ROBERT_CONTROL_DE_CAMBIOS
* ROBERT_PHASES v0.5
* ROBERT_TECHNICAL_COMPONENTS_SPEC v0.2

---

# FUENTE DE VERDAD

La fuente de verdad principal para el estado general del proyecto es:

**ROBERT_CONTEXT_MASTER v0.5**

Este documento debe alinearse con:

* ROBERT_SECURITY_RULES
* ROBERT_CONTEXT_MASTER v0.5
* ROBERT_COMMANDS
* ROBERT_DECISIONS_LOG
* ROBERT_PHASES v0.5
* ROBERT_HOME
* ROBERT_CONTROL_DE_CAMBIOS
* ROBERT_TECHNICAL_MVP_PLAN
* ROBERT_TECHNICAL_MVP_WIREFRAME v0.3
* ROBERT_TECHNICAL_COMPONENTS_SPEC v0.2

---

# ESTADO ACTUAL DEL PROYECTO

Robert se encuentra en:

**Fase 10 — MVP técnico básico en preparación**

Estado operativo:

* MVP manual validado
* Sandbox manual validado
* GitHub configurado como respaldo documental privado y manual
* ROBERT_CONTEXT_MASTER v0.5 reanclado
* ROBERT_PHASES v0.5 reconciliado
* Escala de riesgo y autonomía unificada
* ROBERT_TECHNICAL_MVP_PLAN aprobado
* ROBERT_TECHNICAL_MVP_WIREFRAME v0.3 aprobado
* ROBERT_TECHNICAL_COMPONENTS_SPEC v0.2 aprobado
* Convención visual de Obsidian validada
* ROBERT_TECHNICAL_DATA_MODEL_SPEC v0.1 creado como borrador nuevo
* Sin programación autorizada todavía
* Sin conexiones reales
* Sin automatizaciones reales
* Sin agentes autónomos activos

---

# ALCANCE AUTORIZADO

Este documento autoriza únicamente:

* Definir modelos de datos conceptuales.
* Definir campos internos simulados.
* Definir relaciones entre datos.
* Definir estados permitidos.
* Definir datos prohibidos.
* Preparar base documental para una futura especificación técnica.
* Mantener la fase en modo documental y supervisado.

---

# ALCANCE NO AUTORIZADO

Este documento no autoriza:

* Programar la app.
* Crear una base de datos real.
* Crear tablas reales.
* Crear código.
* Conectar Supabase.
* Conectar Firebase.
* Conectar GitHub automáticamente.
* Conectar Gmail.
* Conectar Google Calendar.
* Conectar APIs reales.
* Automatizar acciones.
* Activar agentes autónomos.
* Ejecutar acciones reales.
* Avanzar automáticamente a Fase 11.

---

# PRINCIPIO DE DISEÑO DE DATOS

Los datos de Robert deben ser:

* Claros.
* Auditables.
* Mínimos.
* Reversibles cuando aplique.
* Separados por función.
* No sensibles por defecto.
* Simulados en esta etapa.
* Controlados por el usuario.
* Alineados con documentos maestros.

Regla principal:

**Datos mínimos, control máximo.**

---

# CONCEPTOS QUE NO DEBEN MEZCLARSE

Robert debe separar siempre:

```text
Tipo de cambio
Nivel de riesgo
Nivel de autonomía
Estado documental
Estado operativo
Modo activo
Decisión formal
Cambio registrado
```

Ejemplo correcto:

```text
Tipo de cambio: Cambio técnico documental
Nivel de riesgo: Nivel 3 — Alto
Nivel de autonomía: Nivel 0 — Sin autonomía ejecutiva
Estado documental: En revisión
Modo activo: Supervisado
```

---

# ESCALA OFICIAL DE RIESGO

La escala oficial de riesgo es:

```text
Nivel 0 — Informativo
Nivel 1 — Bajo
Nivel 2 — Medio
Nivel 3 — Alto
Nivel 4 — Crítico
```

No existe Nivel 5 como riesgo.

Nivel 5 solo puede existir como autonomía, si aplica en ROBERT_SECURITY_RULES.

Actualmente Robert no tiene autonomía ejecutiva activa.

---

# MODELOS PRINCIPALES DE DATOS

Esta versión define los modelos conceptuales mínimos para el MVP técnico básico.

Modelos principales:

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

---

# 1. MODELO — SystemState

## Función

Representa el estado general actual de Robert.

Este modelo alimenta principalmente:

* TopBar
* CurrentStatePanel
* DocumentStatusMap
* DecisionInbox

## Campos sugeridos

```text
project_name
current_phase
current_phase_status
active_mode
execution_status
last_decision
last_change
current_source_of_truth
github_status
obsidian_visual_status
programming_authorized
external_connections_authorized
automations_authorized
agents_authorized
```

## Ejemplo conceptual

```text
project_name: Robert
current_phase: Fase 10 — MVP técnico básico
current_phase_status: En preparación
active_mode: Supervisado
execution_status: Sin ejecución real autorizada
last_decision: DECISIÓN #011
last_change: CAMBIO #015
current_source_of_truth: ROBERT_CONTEXT_MASTER v0.5
github_status: Respaldo documental manual
obsidian_visual_status: Convención visual validada
programming_authorized: No
external_connections_authorized: No
automations_authorized: No
agents_authorized: No
```

---

# 2. MODELO — RobertDocument

## Función

Representa un documento dentro del sistema Robert.

Este modelo alimenta principalmente:

* DocumentStatusMap
* CurrentStatePanel
* DecisionInbox
* LeftSidebar

## Campos sugeridos

```text
document_id
document_name
folder
version
document_status
document_type
phase_related
layer_related
tags
source_of_truth_level
decision_related
change_related
risk_level
last_updated
is_official
is_draft
is_historical
notes
```

## Estados permitidos

```text
Borrador
En revisión
Pendiente de aprobación
Aprobado
Rechazado
Pausado
Reemplazado
Archivado
Histórico
```

## Ejemplo conceptual

```text
document_id: robert_technical_components_spec
document_name: ROBERT_TECHNICAL_COMPONENTS_SPEC
folder: 10_MVP
version: 0.2
document_status: Aprobado
document_type: Especificación técnica documental
phase_related: Fase 10
layer_related: Capa 5
tags: #robert/orbita-2 #capa/5 #tipo/tecnico
decision_related: DECISIÓN #011
change_related: CAMBIO #015
risk_level: Nivel 2 — Medio
is_official: Sí
is_draft: No
is_historical: No
```

---

# 3. MODELO — DecisionRecord

## Función

Representa una decisión formal registrada por el usuario.

Debe alinearse con ROBERT_DECISIONS_LOG.

Este modelo alimenta principalmente:

* DecisionInbox
* CurrentStatePanel
* HistoryLog futuro
* DocumentStatusMap

## Campos sugeridos

```text
decision_number
decision_title
date
status
decision_type
documents_affected
decision_summary
reason
authorized_scope
unauthorized_scope
initial_risk_level
final_risk_level
autonomy_level
active_rule
closing_note
```

## Estados permitidos

```text
Aprobada
Pendiente
En revisión
Rechazada
Pausada
Reemplazada
Archivada
```

## Ejemplo conceptual

```text
decision_number: 011
decision_title: Aprobación de ROBERT_TECHNICAL_COMPONENTS_SPEC v0.2
date: 30/06/2026
status: Aprobada
decision_type: Aprobación de especificación técnica documental
documents_affected: ROBERT_TECHNICAL_COMPONENTS_SPEC
initial_risk_level: Nivel 3 — Alto
final_risk_level: Nivel 2 — Medio
autonomy_level: Nivel 0 — Sin autonomía ejecutiva
```

---

# 4. MODELO — ChangeRecord

## Función

Representa un cambio registrado en ROBERT_CONTROL_DE_CAMBIOS.

Este modelo alimenta principalmente:

* CurrentStatePanel
* DocumentStatusMap
* DecisionInbox
* HistoryLog futuro

## Campos sugeridos

```text
change_number
change_title
date
status
document_affected
change_type
initial_risk_level
final_risk_level
autonomy_level
reason
correction_applied
dependencies
conflicts
authorized_scope
unauthorized_scope
final_state
decision_related
```

## Estados permitidos

```text
Borrador
En revisión
Pendiente de aprobación
Aprobado
Actualizado
Aprobado e integrado
Pausado
Rechazado
Archivado
Reemplazado
```

## Ejemplo conceptual

```text
change_number: 015
change_title: Aprobación e integración de ROBERT_TECHNICAL_COMPONENTS_SPEC v0.2
status: Aprobado e integrado
document_affected: ROBERT_TECHNICAL_COMPONENTS_SPEC
change_type: Cambio técnico documental / especificación técnica
initial_risk_level: Nivel 3 — Alto
final_risk_level: Nivel 2 — Medio
autonomy_level: Nivel 0 — Sin autonomía ejecutiva
decision_related: DECISIÓN #011
```

---

# 5. MODELO — RiskRecord

## Función

Representa un riesgo detectado en una acción, documento, cambio o decisión.

Este modelo alimenta principalmente:

* RiskBadge
* ApprovalGate
* DecisionInbox
* CurrentStatePanel

## Campos sugeridos

```text
risk_id
risk_level
risk_name
risk_reason
document_or_module_affected
mode_active
requires_approval
approval_status
recommended_action
blocking_required
related_decision
related_change
```

## Niveles permitidos

```text
Nivel 0 — Informativo
Nivel 1 — Bajo
Nivel 2 — Medio
Nivel 3 — Alto
Nivel 4 — Crítico
```

## Ejemplo conceptual

```text
risk_id: risk_components_spec_v02
risk_level: Nivel 2 — Medio
risk_name: Cambio técnico documental aprobado
risk_reason: Define componentes técnicos, pero no autoriza programación.
document_or_module_affected: ROBERT_TECHNICAL_COMPONENTS_SPEC
mode_active: Supervisado
requires_approval: Sí
approval_status: Aprobado por DECISIÓN #011
recommended_action: Registrar cambio y mantener sin ejecución real.
blocking_required: No
```

---

# 6. MODELO — CommandRequest

## Función

Representa una solicitud o comando del usuario dentro de Robert.

Este modelo alimenta principalmente:

* CommandCenter
* ModeSelector
* RiskBadge
* ApprovalGate
* DecisionInbox

## Campos sugeridos

```text
command_id
user_input
recognized_command
mode_requested
active_mode
document_affected
module_affected
classified_intent
change_type
risk_level
autonomy_level
requires_approval
status
prepared_output
result
timestamp
```

## Estados permitidos

```text
Recibido
Clasificado
En revisión
Borrador preparado
Requiere aprobación
Aprobado
Pausado
Bloqueado
No permitido
Completado
```

## Ejemplo conceptual

```text
command_id: cmd_001
user_input: crea ROBERT_TECHNICAL_DATA_MODEL_SPEC
recognized_command: CREA
active_mode: Supervisado
document_affected: ROBERT_TECHNICAL_DATA_MODEL_SPEC
classified_intent: Crear documento técnico documental
change_type: Cambio técnico documental
risk_level: Nivel 3 — Alto
autonomy_level: Nivel 0 — Sin autonomía ejecutiva
requires_approval: Sí
status: Borrador preparado
```

---

# 7. MODELO — PendingDecision

## Función

Representa un elemento que necesita decisión del usuario.

Este modelo alimenta principalmente:

* DecisionInbox
* ApprovalGate
* CurrentStatePanel

## Campos sugeridos

```text
pending_id
title
reason
document_affected
change_type
risk_level
autonomy_level
current_status
options_available
recommended_option
created_date
decision_required
blocking_status
```

## Opciones permitidas

```text
Aprobar
Rechazar
Pausar
Corregir
Enviar a revisión
Enviar a sandbox
Archivar
```

## Ejemplo conceptual

```text
pending_id: pending_data_model_spec
title: Revisar ROBERT_TECHNICAL_DATA_MODEL_SPEC v0.1
reason: Nuevo documento técnico documental
document_affected: ROBERT_TECHNICAL_DATA_MODEL_SPEC
risk_level: Nivel 3 — Alto
autonomy_level: Nivel 0 — Sin autonomía ejecutiva
current_status: Borrador pendiente de revisión
recommended_option: Revisar antes de aprobar
decision_required: Sí
blocking_status: No bloquea fase, pero no debe aprobarse automáticamente
```

---

# 8. MODELO — ModeState

## Función

Representa el modo operativo actual de Robert.

Este modelo alimenta principalmente:

* ModeSelector
* TopBar
* CurrentStatePanel
* CommandCenter

## Campos sugeridos

```text
active_mode
available_modes
restricted_modes
execution_allowed
external_actions_allowed
automation_allowed
agent_autonomy_allowed
reason_for_restriction
```

## Modos activos permitidos en MVP básico

```text
Manual
Supervisado
Sandbox
```

## Modos no activos todavía

```text
Autónomo limitado
Ejecución limitada
Modo crítico
```

## Ejemplo conceptual

```text
active_mode: Supervisado
available_modes: Manual, Supervisado, Sandbox
restricted_modes: Autónomo limitado, Ejecución limitada, Modo crítico
execution_allowed: No
external_actions_allowed: No
automation_allowed: No
agent_autonomy_allowed: No
reason_for_restriction: Fase 10 documental, sin programación autorizada
```

---

# 9. MODELO — ComponentState

## Función

Representa el estado de un componente del MVP técnico básico.

Este modelo alimenta principalmente:

* DocumentStatusMap
* CurrentStatePanel
* Futuras vistas técnicas

## Campos sugeridos

```text
component_id
component_name
component_status
component_priority
layer_main
layer_represented
related_document
requires_data_model
requires_approval_gate
risk_level
notes
```

## Componentes prioritarios

```text
AppShell
TopBar
LeftSidebar
CommandCenter
ModeSelector
RiskBadge
ApprovalGate
DecisionInbox
DocumentStatusMap
CurrentStatePanel
```

## Ejemplo conceptual

```text
component_id: risk_badge
component_name: RiskBadge
component_status: Definido documentalmente
component_priority: Prioritario
layer_main: Capa 5 — Presentación
layer_represented: Capa 4 — Gobierno / Seguridad
related_document: ROBERT_TECHNICAL_COMPONENTS_SPEC v0.2
requires_data_model: Sí
requires_approval_gate: Sí
risk_level: Nivel 2 — Medio
```

---

# 10. MODELO — GitHubBackupStatus

## Función

Representa el estado del respaldo manual de Robert en GitHub.

Este modelo alimenta principalmente:

* CurrentStatePanel
* TopBar
* DocumentStatusMap

## Campos sugeridos

```text
repository_name
repository_status
backup_mode
last_checkpoint
manual_update_required
automatic_sync_enabled
external_connection_status
risk_level
notes
```

## Ejemplo conceptual

```text
repository_name: ROBERT_MASTER_SYSTEM
repository_status: Privado
backup_mode: Manual
last_checkpoint: Checkpoint documental GitHub completado
manual_update_required: Sí
automatic_sync_enabled: No
external_connection_status: No conectado automáticamente
risk_level: Nivel 2 — Medio
notes: GitHub funciona solo como respaldo documental manual.
```

---

# 11. MODELO — ObsidianGraphStatus

## Función

Representa el estado de la convención visual de Obsidian.

Este modelo alimenta principalmente:

* DocumentStatusMap
* CurrentStatePanel
* Posibles vistas visuales futuras

## Campos sugeridos

```text
graph_status
visual_center
conceptual_center
orbit_rule
color_rule
tags_enabled
wikilinks_enabled
official_convention
related_document
risk_level
notes
```

## Ejemplo conceptual

```text
graph_status: Convención visual validada
visual_center: ROBERT_HOME
conceptual_center: ROBERT_CONTEXT_MASTER
orbit_rule: Órbita = posición / cercanía al núcleo
color_rule: Capa o función = color visual
tags_enabled: Sí
wikilinks_enabled: Sí
official_convention: Sí
related_document: ROBERT_VISUAL
risk_level: Nivel 2 — Medio
notes: Obsidian Graph View es navegación documental, no HUD final.
```

---

# RELACIONES ENTRE MODELOS

## Relación principal

```text
SystemState
↓
usa RobertDocument
↓
usa DecisionRecord
↓
usa ChangeRecord
↓
usa RiskRecord
↓
alimenta CurrentStatePanel, DocumentStatusMap y DecisionInbox
```

---

## Relación documento-decisión-cambio

```text
RobertDocument
↓
puede tener una DecisionRecord relacionada
↓
puede tener un ChangeRecord relacionado
↓
puede tener un RiskRecord relacionado
```

---

## Relación comando-riesgo-aprobación

```text
CommandRequest
↓
genera RiskRecord
↓
puede activar ApprovalGate
↓
puede crear PendingDecision
```

---

## Relación componente-dato

```text
ComponentState
↓
define qué modelo necesita
↓
muestra datos simulados
↓
no ejecuta acciones reales
```

---

# DATOS PROHIBIDOS EN ESTA ETAPA

En esta fase no deben guardarse datos sensibles reales como:

* Contraseñas.
* API keys.
* Tokens.
* Datos bancarios.
* Datos fiscales reales.
* Datos legales confidenciales.
* Correos privados.
* Teléfonos de clientes reales.
* Información personal sensible.
* Listas reales de clientes.
* Credenciales de herramientas.
* Datos médicos.
* Datos financieros operativos.
* Documentos privados de terceros sin autorización.

---

# DATOS PERMITIDOS EN ESTA ETAPA

Se permiten datos documentales y simulados como:

* Nombre del documento.
* Estado del documento.
* Versión.
* Fase relacionada.
* Cambio relacionado.
* Decisión relacionada.
* Riesgo conceptual.
* Modo activo.
* Componente relacionado.
* Estado de GitHub manual.
* Estado de Obsidian Graph.
* Notas de revisión.
* Campos simulados.
* Ejemplos ficticios.
* Datos de prueba no sensibles.

---

# REGLAS DE VALIDACIÓN

Antes de usar un dato en Robert, debe revisarse:

```text
¿Es necesario?
¿Es sensible?
¿Está autorizado?
¿Es real o simulado?
¿Pertenece a un documento oficial?
¿Debe mostrarse en el MVP?
¿Requiere aprobación?
¿Debe bloquearse?
```

---

# CRITERIOS DE ACEPTACIÓN DEL DATA MODEL SPEC

Este documento podrá considerarse listo para revisión si:

* No autoriza base de datos real.
* No autoriza programación.
* No autoriza conexiones externas.
* Define modelos conceptuales claros.
* Se alinea con COMPONENTS_SPEC v0.2.
* Respeta CONTEXT_MASTER v0.5.
* Respeta PHASES v0.5.
* Respeta SECURITY_RULES.
* Usa la escala oficial de riesgo.
* Separa riesgo, autonomía, tipo de cambio y estado.
* Define datos permitidos y prohibidos.
* Mantiene a Robert en Fase 10.

---

# RIESGO DEL DOCUMENTO

Tipo de cambio:

**Cambio técnico documental / modelo de datos conceptual**

Nivel de riesgo inicial:

**Nivel 3 — Alto**

Motivo:

Este documento empieza a definir la estructura de datos que podría alimentar el MVP técnico básico. Aunque no implementa una base de datos, acerca el proyecto a una futura construcción técnica.

Nivel de riesgo final esperado:

**Nivel 2 — Medio**

Motivo de reducción:

El documento es conceptual, no crea base de datos, no programa, no conecta herramientas reales y no autoriza ejecución.

Nivel de autonomía:

**Nivel 0 — Sin autonomía ejecutiva**

---

# DECISIÓN PENDIENTE

Este documento queda como:

**Borrador técnico documental pendiente de revisión**

Para aprobarlo formalmente, el usuario deberá escribir:

```text
APRUEBO ROBERT_TECHNICAL_DATA_MODEL_SPEC v0.1
```

---

# EFECTO DE UNA APROBACIÓN FUTURA

Si se aprueba este documento, se deberá:

1. Registrar decisión formal en ROBERT_DECISIONS_LOG.
2. Registrar cambio en ROBERT_CONTROL_DE_CAMBIOS.
3. Actualizar ROBERT_HOME.
4. Actualizar README si aplica.
5. Mantenerlo como base para futuras especificaciones técnicas.
6. No pasar automáticamente a programación.

---

# PRÓXIMO PASO RECOMENDADO

Después de revisar este documento, el siguiente documento posible sería:

**ROBERT_TECHNICAL_INTERACTION_FLOW_SPEC**

Ese documento definiría cómo interactúan los componentes entre sí usando los modelos de datos conceptuales definidos aquí.

No debe crearse hasta revisar o aprobar DATA_MODEL_SPEC.

---

# CIERRE

ROBERT_TECHNICAL_DATA_MODEL_SPEC v0.1 define los modelos de datos conceptuales iniciales para el MVP técnico básico de Robert.

Este documento prepara la estructura lógica de información, pero no crea una base de datos real.

Robert sigue en modo documental y supervisado.

El usuario mantiene control total.

Robert no ejecuta acciones importantes sin permiso.
