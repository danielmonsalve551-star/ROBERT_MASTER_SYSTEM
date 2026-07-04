# ROBERT_TECHNICAL_SCREEN_STATE_SPEC

Versión: 0.1  
Estado: Borrador técnico documental nuevo — pendiente de revisión  
Fecha: 03/07/2026  
Ubicación: 10_MVP  
Fase relacionada: Fase 10 — MVP técnico básico en preparación  
Documento base relacionado: ROBERT_TECHNICAL_INTERACTION_FLOW_SPEC v0.2  
Documentos relacionados: ROBERT_TECHNICAL_COMPONENTS_SPEC v0.2, ROBERT_TECHNICAL_DATA_MODEL_SPEC v0.1  
Fuente de verdad actual: ROBERT_CONTEXT_MASTER v0.5  

Tags: #robert/orbita-3 #capa/5 #tipo/tecnico #robert/mvp #robert/screen-state

---

# OBJETIVO

ROBERT_TECHNICAL_SCREEN_STATE_SPEC define qué información debe aparecer en cada pantalla, panel o vista principal del MVP técnico básico de Robert.

Su objetivo es responder:

- Qué ve el usuario.
- Qué muestra cada panel.
- Qué datos alimentan cada pantalla.
- Qué estados puede tener cada vista.
- Qué debe aparecer cuando hay riesgo.
- Qué debe aparecer cuando falta aprobación.
- Qué debe aparecer cuando una acción está bloqueada.
- Qué debe aparecer cuando Robert está en modo manual, supervisado o sandbox.
- Qué información no debe mostrarse todavía.

Este documento usa como base:

- ROBERT_TECHNICAL_COMPONENTS_SPEC v0.2
- ROBERT_TECHNICAL_DATA_MODEL_SPEC v0.1
- ROBERT_TECHNICAL_INTERACTION_FLOW_SPEC v0.2

Este documento no diseña la interfaz final.

Este documento no programa la app.

Este documento no crea pantallas reales.

Este documento no crea código.

Este documento no conecta herramientas externas.

Este documento no ejecuta acciones reales.

Este documento solo define estados conceptuales de pantalla para una futura implementación controlada.

---

# ESTADO DEL DOCUMENTO

Este documento queda como:

**Borrador técnico documental nuevo — pendiente de revisión**

No está aprobado todavía.

No reemplaza a ningún documento maestro.

No autoriza programación.

No autoriza diseño final.

No autoriza base de datos real.

No autoriza conexiones externas.

No autoriza automatizaciones.

No autoriza agentes autónomos.

No autoriza ejecución real.

---

# REGLA CENTRAL

El usuario manda.

Robert no ejecuta acciones importantes sin permiso.

Toda pantalla, panel o vista debe mostrar el estado real del sistema sin exagerar capacidades que todavía no existen.

Regla principal:

**Mostrar estado real. No inventar ejecución. No simular conexión como si fuera real.**

---

# ESTADO ACTUAL DE ROBERT

Robert se encuentra en:

**Fase 10 — MVP técnico básico en preparación**

Estado operativo actual:

- MVP manual validado.
- Sandbox manual validado.
- GitHub configurado como respaldo documental privado y manual.
- ROBERT_CONTEXT_MASTER v0.5 reanclado.
- ROBERT_PHASES v0.5 reconciliado.
- Escala de riesgo y autonomía unificada.
- ROBERT_TECHNICAL_MVP_PLAN aprobado.
- ROBERT_TECHNICAL_MVP_WIREFRAME v0.3 aprobado.
- ROBERT_TECHNICAL_COMPONENTS_SPEC v0.2 aprobado.
- ROBERT_TECHNICAL_DATA_MODEL_SPEC v0.1 aprobado e integrado.
- ROBERT_TECHNICAL_INTERACTION_FLOW_SPEC v0.2 aprobado e integrado.
- ROBERT_TECHNICAL_SCREEN_STATE_SPEC v0.1 creado como borrador.
- Convención visual de Obsidian v0.2 aprobada e integrada.
- Sin programación autorizada.
- Sin código real.
- Sin base de datos real.
- Sin conexiones externas.
- Sin automatizaciones reales.
- Sin agentes autónomos activos.

---

# ALCANCE AUTORIZADO

Este documento autoriza únicamente:

- Definir estados conceptuales de pantalla.
- Definir qué información debe aparecer en cada panel.
- Relacionar pantallas con modelos de datos.
- Relacionar pantallas con componentes.
- Definir estados visuales permitidos.
- Definir estados visuales prohibidos.
- Definir cuándo una pantalla debe mostrar advertencia, pausa o bloqueo.
- Preparar base documental para futuras especificaciones técnicas.
- Mantener a Robert en modo documental, manual y supervisado.

---

# ALCANCE NO AUTORIZADO

Este documento no autoriza:

- Programar la app.
- Crear código.
- Crear pantallas reales.
- Crear prototipo funcional.
- Crear base de datos real.
- Crear endpoints.
- Conectar Supabase.
- Conectar Firebase.
- Conectar GitHub automáticamente.
- Conectar Gmail.
- Conectar Google Calendar.
- Conectar APIs externas.
- Automatizar acciones.
- Activar agentes autónomos.
- Ejecutar acciones reales.
- Avanzar automáticamente a Fase 11.

---

# PRINCIPIO GENERAL DE PANTALLA

Cada pantalla debe responder tres preguntas:

1. ¿Dónde estoy dentro de Robert?
2. ¿Qué está pasando ahora?
3. ¿Qué puedo hacer sin romper las reglas?

Regla visual principal:

**La pantalla debe mostrar control, no ilusión de autonomía.**

---

# COMPONENTES BASE

Las pantallas del MVP técnico básico se componen de:

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

---

# MODELOS DE DATOS UTILIZADOS

Este documento se apoya en los modelos definidos en DATA_MODEL_SPEC v0.1:

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

# VISTA 1 — APP SHELL / CONTENEDOR PRINCIPAL

## Función

AppShell es el contenedor raíz del MVP técnico básico.

Organiza la pantalla principal y aloja los componentes.

No toma decisiones.

No ejecuta acciones.

No evalúa riesgo.

No aprueba nada.

## Debe mostrar

- TopBar.
- LeftSidebar.
- Área principal de trabajo.
- CommandCenter.
- CurrentStatePanel.
- DocumentStatusMap si aplica.
- DecisionInbox si existen pendientes.
- RiskBadge si hay riesgo relevante.
- ApprovalGate si se requiere autorización.

## Datos que recibe

- SystemState.
- ComponentState.
- ModeState.
- RobertDocument activo.
- PendingDecision si existe.
- RiskRecord si existe.

## Estados posibles

- Estado normal.
- Estado con documento activo.
- Estado con decisión pendiente.
- Estado con riesgo visible.
- Estado con acción bloqueada.
- Estado sandbox.
- Estado sin programación autorizada.
- Estado de solo lectura documental.

## Restricción

AppShell no debe mostrar botones o estados que sugieran ejecución real si esa ejecución no está autorizada.

---

# VISTA 2 — TOPBAR / BARRA SUPERIOR

## Función

TopBar muestra el estado resumido de Robert.

Debe permitir entender rápidamente en qué fase, modo y estado está el sistema.

## Debe mostrar

- Nombre del sistema: Robert.
- Fase actual.
- Modo activo.
- Estado de ejecución.
- Última decisión registrada.
- Último cambio registrado.
- Estado de programación.
- Estado de conexiones externas.
- Estado de automatizaciones.
- Estado de agentes.
- Indicador de riesgo si existe.
- Indicador de decisiones pendientes.

## Datos que recibe

- current_phase.
- active_mode.
- execution_status.
- last_decision.
- last_change.
- risk_summary.
- pending_decision_count.
- programming_authorized.
- database_authorized.
- external_connections_authorized.
- automations_authorized.
- agents_authorized.

## Ejemplo de estado mostrado

- Fase: Fase 10 — MVP técnico básico en preparación.
- Modo: Supervisado.
- Ejecución: No autorizada.
- Programación: No autorizada.
- Conexiones: No activas.
- Automatizaciones: No activas.
- Agentes: No activos.

## Estados posibles

- Normal.
- Advertencia.
- Pendiente de aprobación.
- Bloqueado.
- Sandbox.
- Solo documental.

## Restricción

TopBar solo muestra estado.

No debe permitir ejecutar acciones reales.

---

# VISTA 3 — LEFTSIDEBAR / NAVEGACIÓN DOCUMENTAL

## Función

LeftSidebar permite navegar entre documentos, carpetas, módulos y áreas de Robert.

No toma decisiones.

No aprueba documentos.

No ejecuta acciones.

## Debe mostrar

- Documentos principales.
- Carpetas del sistema.
- Documentos técnicos.
- Documentos maestros.
- Sandbox.
- Visual.
- Módulos.
- Estado básico del documento si aplica.
- Documento activo.

## Estructura recomendada

- 00_HOME
- 01_CONTEXT
- 02_COMMANDS
- 03_DECISIONS
- 04_SECURITY
- 05_PHASES
- 06_MODULES
- 07_VISUAL
- 08_PROMPTS
- 09_ARCHITECTURE
- 10_MVP
- 15_SANDBOX

## Datos que recibe

- document_list.
- folder_structure.
- active_document.
- document_status.
- document_type.
- orbit_tag.
- module_list.

## Datos que puede enviar

- selected_document.
- navigation_target.

## Estados posibles

- Navegación normal.
- Documento activo.
- Documento pendiente de revisión.
- Documento aprobado.
- Documento histórico.
- Documento sin clasificación.
- Documento temporal.

## Restricción

LeftSidebar solo navega.

No modifica documentos por sí sola.

---

# VISTA 4 — COMMANDCENTER

## Función

CommandCenter es el punto donde el usuario da instrucciones a Robert.

Recibe comandos, solicitudes y texto del usuario.

No ejecuta acciones reales por sí solo.

## Debe mostrar

- Campo de entrada.
- Comando detectado.
- Modo activo.
- Intención clasificada.
- Documento afectado si aplica.
- Riesgo preliminar si aplica.
- Siguiente paso sugerido.
- Confirmación requerida si aplica.

## Datos que recibe

- user_input.
- active_mode.
- current_context.
- active_document.
- restricted_actions.
- allowed_actions.

## Datos que envía

- CommandRequest.
- recognized_command.
- classified_intent.
- document_affected.
- module_affected.
- risk_level_preliminar.

## Estados posibles

- Esperando instrucción.
- Interpretando instrucción.
- Comando reconocido.
- Comando ambiguo.
- Requiere confirmación.
- Borrador preparado.
- Acción bloqueada.
- Respuesta entregada.

## Restricción

CommandCenter no debe saltarse RiskBadge ni ApprovalGate cuando la instrucción tiene riesgo.

---

# VISTA 5 — MODESELECTOR

## Función

ModeSelector muestra y controla conceptualmente el modo operativo actual de Robert.

En esta fase no activa autonomía real.

Solo representa modos permitidos documentalmente.

## Debe mostrar

Modos permitidos en esta etapa:

- Manual.
- Supervisado.
- Sandbox.

Modos no activos todavía:

- Autónomo limitado.
- Ejecución limitada.
- Modo crítico.

## Datos que recibe

- ModeState.
- active_mode.
- restricted_modes.
- security_rules.
- user_confirmation_if_required.

## Datos que envía

- active_mode.
- execution_allowed.
- automation_allowed.
- external_actions_allowed.
- agent_autonomy_allowed.

## Estados posibles

- Manual activo.
- Supervisado activo.
- Sandbox activo.
- Modo restringido.
- Modo no disponible.
- Cambio de modo pendiente de aprobación.

## Restricción

ModeSelector no puede activar modos con mayor autonomía sin aprobación formal.

---

# VISTA 6 — RISKBADGE

## Función

RiskBadge muestra el nivel de riesgo de una instrucción, documento, cambio o decisión.

Debe hacer visible el riesgo antes de avanzar.

## Debe mostrar

- Nivel de riesgo.
- Motivo del riesgo.
- Acción recomendada.
- Si requiere aprobación.
- Si requiere pausa.
- Si requiere bloqueo.
- Si afecta documento maestro.
- Si afecta seguridad.
- Si afecta fase.
- Si afecta fuente de verdad.

## Datos que recibe

- CommandRequest.
- RiskRecord.
- active_mode.
- action_type.
- document_affected.
- security_rules.

## Datos que envía

- risk_level.
- risk_reason.
- recommended_action.
- blocking_required.
- approval_recommended.

## Estados posibles

- Nivel 0 — Informativo.
- Nivel 1 — Bajo.
- Nivel 2 — Medio.
- Nivel 3 — Alto.
- Nivel 4 — Crítico.

## Regla específica para Nivel 2

Nivel 2 debe mostrar advertencia visible.

Si afecta documentos maestros, seguridad, fases o fuente de verdad, debe activar ApprovalGate y PendingDecision.

Si no afecta esos elementos, puede manejarse como confirmación inline.

## Restricción

No existe Nivel 5 como riesgo.

---

# VISTA 7 — APPROVALGATE

## Función

ApprovalGate determina si una instrucción puede continuar, debe pausarse o debe bloquearse.

No aprueba por sí solo.

Solo aplica reglas de autorización.

## Debe mostrar

- Si la acción requiere aprobación.
- Qué se quiere aprobar.
- Por qué se requiere aprobación.
- Qué alcance se autoriza.
- Qué alcance sigue prohibido.
- Opciones disponibles.
- Estado de aprobación.

## Datos que recibe

- RiskRecord.
- CommandRequest.
- ModeState.
- user_approval_if_available.
- security_rules.

## Datos que envía

- approval_required.
- approval_status.
- blocked_reason.
- next_allowed_action.
- pending_decision_required.

## Estados posibles

- No requiere aprobación.
- Requiere confirmación inline.
- Requiere aprobación formal.
- Aprobación pendiente.
- Aprobado por usuario.
- Rechazado por usuario.
- Pausado.
- Bloqueado.

## Restricción

ApprovalGate no puede convertir una aprobación documental en autorización de ejecución real.

---

# VISTA 8 — DECISIONINBOX

## Función

DecisionInbox muestra decisiones pendientes del usuario.

Sirve para evitar que Robert avance sin autorización.

## Debe mostrar

- Lista de decisiones pendientes.
- Documento afectado.
- Motivo de la decisión.
- Nivel de riesgo.
- Opciones disponibles.
- Recomendación.
- Estado actual.
- Fecha de creación.
- Si bloquea avance o no.

## Datos que recibe

- PendingDecision.
- RiskRecord.
- ApprovalGate result.
- related_document.
- related_change.

## Datos que envía

- pending_id.
- title.
- options_available.
- recommended_option.
- current_status.
- decision_required.

## Opciones posibles

- Aprobar.
- Rechazar.
- Pausar.
- Corregir.
- Enviar a revisión.
- Enviar a sandbox.
- Archivar.

## Estados posibles

- Sin pendientes.
- Pendiente activa.
- Pendiente bloqueante.
- Pendiente no bloqueante.
- Pendiente aprobada.
- Pendiente rechazada.
- Pendiente pausada.

## Restricción

DecisionInbox no resuelve decisiones automáticamente.

---

# VISTA 9 — DOCUMENTSTATUSMAP

## Función

DocumentStatusMap muestra el estado documental del sistema Robert.

Debe permitir ver qué documentos existen, en qué estado están y cómo se relacionan.

## Debe mostrar

- Nombre del documento.
- Carpeta.
- Versión.
- Estado.
- Tipo.
- Órbita.
- Capa.
- Decisión relacionada.
- Cambio relacionado.
- Riesgo si aplica.
- Documento base si aplica.
- Documento dependiente si aplica.

## Datos que recibe

- RobertDocument.
- DecisionRecord.
- ChangeRecord.
- ObsidianGraphStatus.
- GitHubBackupStatus.
- SystemState.

## Datos que envía

- document_name.
- document_status.
- version.
- decision_related.
- change_related.
- orbit_tag.
- document_type.
- risk_level_if_relevant.

## Estados posibles

- Borrador.
- En revisión.
- Pendiente de aprobación.
- Aprobado.
- Aprobado e integrado.
- Rechazado.
- Pausado.
- Reemplazado.
- Archivado.
- Histórico.

## Restricción

DocumentStatusMap no modifica documentos por sí solo.

Solo muestra estado.

---

# VISTA 10 — CURRENTSTATEPANEL

## Función

CurrentStatePanel muestra el estado general actual de Robert.

Debe ser la vista más clara para saber en qué punto se encuentra el proyecto.

## Debe mostrar

- Fase actual.
- Modo activo.
- Estado operativo.
- Última decisión.
- Último cambio.
- Fuente de verdad actual.
- Estado de GitHub.
- Estado de Obsidian Graph.
- Programación autorizada o no.
- Base de datos autorizada o no.
- Conexiones autorizadas o no.
- Automatizaciones autorizadas o no.
- Agentes autorizados o no.
- Próximo punto pendiente.

## Datos que recibe

- SystemState.
- DecisionRecord.
- ChangeRecord.
- RiskRecord.
- PendingDecision.
- GitHubBackupStatus.
- ObsidianGraphStatus.
- ComponentState.

## Datos que envía

- current_phase.
- active_mode.
- last_decision.
- last_change.
- execution_status.
- programming_authorized.
- database_authorized.
- external_connections_authorized.
- automations_authorized.
- agents_authorized.

## Estados posibles

- Estado estable.
- Documento pendiente.
- Decisión pendiente.
- Cambio registrado.
- Riesgo detectado.
- Acción bloqueada.
- Sandbox activo.
- Fase en preparación.

## Restricción

CurrentStatePanel no ejecuta acciones.

Solo refleja el estado.

---

# ESTADOS GLOBALES DE PANTALLA

El MVP técnico básico puede tener estos estados globales:

## 1. Estado normal

Robert está en modo supervisado o manual, sin acciones pendientes.

## 2. Estado de borrador

Robert está preparando un documento, idea, estructura o respuesta.

## 3. Estado de revisión

Un documento o decisión requiere revisión.

## 4. Estado de aprobación pendiente

Una acción requiere aprobación explícita del usuario.

## 5. Estado bloqueado

La acción no está permitida por seguridad o fase.

## 6. Estado sandbox

Robert está simulando o probando sin afectar sistemas reales.

## 7. Estado sin conexión

No hay herramientas externas conectadas.

## 8. Estado documental

Robert solo organiza documentos, decisiones y cambios.

## 9. Estado de riesgo

Existe riesgo visible y debe mostrarse.

## 10. Estado de actualización

Se registró una decisión, cambio o documento nuevo.

---

# PANTALLA PRINCIPAL RECOMENDADA

La pantalla principal del MVP técnico básico debe mostrar:

- TopBar arriba.
- LeftSidebar a la izquierda.
- Área central de trabajo.
- CommandCenter visible.
- CurrentStatePanel visible.
- RiskBadge visible cuando aplique.
- ApprovalGate visible cuando aplique.
- DecisionInbox visible cuando haya pendientes.
- DocumentStatusMap accesible.

Estructura conceptual:

```text
TopBar
────────────────────────
LeftSidebar | MainArea
            | CommandCenter
            | CurrentStatePanel
            | DocumentStatusMap
            | DecisionInbox
            | RiskBadge / ApprovalGate
