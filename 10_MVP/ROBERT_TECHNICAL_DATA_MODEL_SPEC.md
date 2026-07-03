# ROBERT_TECHNICAL_DATA_MODEL_SPEC

Versión: 0.1  
Estado: Aprobado  
Fecha: 02/07/2026  
Ubicación: 10_MVP  
Fase relacionada: Fase 10 — MVP técnico básico en preparación  
Documento base relacionado: ROBERT_TECHNICAL_COMPONENTS_SPEC v0.2  
Fuente de verdad actual: ROBERT_CONTEXT_MASTER v0.5  
Decisión relacionada: DECISIÓN #012 — Aprobación de ROBERT_TECHNICAL_DATA_MODEL_SPEC v0.1  
Cambio relacionado: CAMBIO #016 — Creación de ROBERT_TECHNICAL_DATA_MODEL_SPEC v0.1  

Tags: #robert/orbita-2 #robert/mvp #capa/5 #tipo/tecnico

---

# OBJETIVO

ROBERT_TECHNICAL_DATA_MODEL_SPEC define los modelos de datos conceptuales que Robert necesitaría para operar el MVP técnico básico.

Su objetivo es establecer, de forma clara y controlada, qué información debe existir dentro del sistema para que los componentes puedan mostrar estado, decisiones, riesgos, documentos, comandos y cambios.

Este documento responde preguntas como:

- Qué datos necesita Robert para mostrar su estado actual.
- Qué información necesita cada componente del MVP.
- Qué campos deben existir para documentos, decisiones, cambios y riesgos.
- Cómo se relacionan los datos entre sí.
- Qué datos están permitidos en esta etapa.
- Qué datos están prohibidos.
- Qué información sigue siendo manual, documental y supervisada.

Este documento no crea una base de datos real.

Este documento no programa la app.

Este documento no conecta herramientas externas.

Este documento no automatiza acciones.

Este documento solo define una estructura conceptual de información para una futura implementación técnica controlada.

---

# ESTADO DEL DOCUMENTO

Este documento queda aprobado como:

**Especificación técnica documental inicial de modelos de datos conceptuales para el MVP técnico básico de Robert.**

Su aprobación permite usarlo como base para futuras especificaciones técnicas, pero no autoriza construcción, programación ni ejecución real.

Este documento no reemplaza a ningún documento maestro.

Debe mantenerse alineado con:

- ROBERT_CONTEXT_MASTER v0.5
- ROBERT_SECURITY_RULES
- ROBERT_COMMANDS
- ROBERT_DECISIONS_LOG
- ROBERT_CONTROL_DE_CAMBIOS
- ROBERT_PHASES v0.5
- ROBERT_TECHNICAL_COMPONENTS_SPEC v0.2

---

# REGLA CENTRAL

El usuario manda.

Robert no ejecuta acciones importantes sin permiso.

Todo dato que Robert muestre, guarde, procese o relacione debe respetar las reglas de seguridad, autorización y control definidas en los documentos maestros del sistema.

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
- ROBERT_TECHNICAL_DATA_MODEL_SPEC v0.1 aprobado.
- Convención visual de Obsidian validada.
- Sin programación autorizada.
- Sin base de datos real autorizada.
- Sin conexiones externas autorizadas.
- Sin automatizaciones reales autorizadas.
- Sin agentes autónomos activos.

---

# ALCANCE AUTORIZADO

Este documento autoriza únicamente:

- Definir modelos de datos conceptuales.
- Definir campos internos simulados.
- Definir relaciones entre documentos, decisiones, cambios, riesgos y comandos.
- Definir estados permitidos.
- Definir datos permitidos y prohibidos.
- Servir como base documental para futuras especificaciones técnicas.
- Explicar qué datos podrían alimentar los componentes del MVP técnico básico.
- Mantener el proyecto en modo documental, manual y supervisado.

---

# ALCANCE NO AUTORIZADO

Este documento no autoriza:

- Programar la app.
- Crear una base de datos real.
- Crear tablas reales.
- Crear código.
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

# PRINCIPIO GENERAL DEL MODELO DE DATOS

Los datos de Robert deben ser:

- Claros.
- Mínimos.
- Auditables.
- Ordenados.
- Controlados por el usuario.
- Separados por función.
- No sensibles por defecto.
- Simulados en esta etapa.
- Reversibles cuando aplique.
- Alineados con documentos maestros.

Regla principal:

**Datos mínimos, control máximo.**

Robert no debe guardar información innecesaria solo porque puede hacerlo.

Robert solo debe manejar datos que tengan una función clara dentro del sistema.

---

# CONCEPTOS QUE NO DEBEN MEZCLARSE

Robert debe separar siempre los siguientes conceptos:

- Tipo de cambio.
- Nivel de riesgo.
- Nivel de autonomía.
- Estado documental.
- Estado operativo.
- Modo activo.
- Decisión formal.
- Cambio registrado.

Ejemplo correcto:

- Tipo de cambio: Cambio técnico documental.
- Nivel de riesgo: Nivel 3 — Alto.
- Nivel de autonomía: Nivel 0 — Sin autonomía ejecutiva.
- Estado documental: Aprobado.
- Modo activo: Supervisado.
- Ejecución real: No autorizada.

---

# ESCALA OFICIAL DE RIESGO

La escala oficial de riesgo de Robert es:

- Nivel 0 — Informativo.
- Nivel 1 — Bajo.
- Nivel 2 — Medio.
- Nivel 3 — Alto.
- Nivel 4 — Crítico.

No existe Nivel 5 como riesgo.

Nivel 5 solo puede existir como autonomía si así se define en ROBERT_SECURITY_RULES.

Actualmente Robert no tiene autonomía ejecutiva activa.

---

# MODELOS PRINCIPALES DE DATOS

Esta versión define los modelos conceptuales mínimos para el MVP técnico básico.

Modelos incluidos:

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

SystemState representa el estado general actual de Robert.

Este modelo sirve para que el sistema pueda mostrar en qué fase se encuentra, qué modo está activo, qué documentos están aprobados y qué acciones siguen prohibidas.

Alimenta principalmente:

- TopBar
- CurrentStatePanel
- DocumentStatusMap
- DecisionInbox

## Campos sugeridos

- project_name
- current_phase
- current_phase_status
- active_mode
- execution_status
- last_decision
- last_change
- current_source_of_truth
- github_status
- obsidian_visual_status
- programming_authorized
- database_authorized
- external_connections_authorized
- automations_authorized
- agents_authorized

## Ejemplo conceptual

- project_name: Robert
- current_phase: Fase 10 — MVP técnico básico
- current_phase_status: En preparación
- active_mode: Supervisado
- execution_status: Sin ejecución real autorizada
- last_decision: DECISIÓN #012
- last_change: CAMBIO #016
- current_source_of_truth: ROBERT_CONTEXT_MASTER v0.5
- github_status: Respaldo documental manual
- obsidian_visual_status: Convención visual validada
- programming_authorized: No
- database_authorized: No
- external_connections_authorized: No
- automations_authorized: No
- agents_authorized: No

---

# 2. MODELO — RobertDocument

## Función

RobertDocument representa cualquier documento oficial, borrador, histórico o técnico dentro del sistema Robert.

Permite saber qué documento existe, en qué carpeta está, qué versión tiene, cuál es su estado y con qué decisión o cambio está relacionado.

Alimenta principalmente:

- DocumentStatusMap
- CurrentStatePanel
- DecisionInbox
- LeftSidebar

## Campos sugeridos

- document_id
- document_name
- folder
- version
- document_status
- document_type
- phase_related
- layer_related
- tags
- source_of_truth_level
- decision_related
- change_related
- risk_level
- last_updated
- is_official
- is_draft
- is_historical
- notes

## Estados permitidos

- Borrador
- En revisión
- Pendiente de aprobación
- Aprobado
- Rechazado
- Pausado
- Reemplazado
- Archivado
- Histórico

## Ejemplo conceptual

- document_id: robert_technical_data_model_spec
- document_name: ROBERT_TECHNICAL_DATA_MODEL_SPEC
- folder: 10_MVP
- version: 0.1
- document_status: Aprobado
- document_type: Especificación técnica documental / modelo de datos conceptual
- phase_related: Fase 10
- layer_related: Capa 5
- tags: #robert/orbita-2 #robert/mvp #capa/5 #tipo/tecnico
- decision_related: DECISIÓN #012
- change_related: CAMBIO #016
- risk_level: Nivel 2 — Medio
- is_official: Sí
- is_draft: No
- is_historical: No

---

# 3. MODELO — DecisionRecord

## Función

DecisionRecord representa una decisión formal tomada por el usuario dentro del proyecto Robert.

Debe alinearse con ROBERT_DECISIONS_LOG.

Sirve para saber qué decidió el usuario, cuándo lo decidió, qué documento afecta, qué alcance autoriza y qué alcance sigue prohibido.

Alimenta principalmente:

- DecisionInbox
- CurrentStatePanel
- DocumentStatusMap
- Historial futuro

## Campos sugeridos

- decision_number
- decision_title
- date
- status
- decision_type
- documents_affected
- decision_summary
- reason
- authorized_scope
- unauthorized_scope
- initial_risk_level
- final_risk_level
- autonomy_level
- active_rule
- closing_note

## Estados permitidos

- Aprobada
- Pendiente
- En revisión
- Rechazada
- Pausada
- Reemplazada
- Archivada

## Ejemplo conceptual

- decision_number: 012
- decision_title: Aprobación de ROBERT_TECHNICAL_DATA_MODEL_SPEC v0.1
- date: 02/07/2026
- status: Aprobada
- decision_type: Aprobación de especificación técnica documental
- documents_affected: ROBERT_TECHNICAL_DATA_MODEL_SPEC
- initial_risk_level: Nivel 3 — Alto
- final_risk_level: Nivel 2 — Medio
- autonomy_level: Nivel 0 — Sin autonomía ejecutiva

---

# 4. MODELO — ChangeRecord

## Función

ChangeRecord representa un cambio registrado dentro de ROBERT_CONTROL_DE_CAMBIOS.

Sirve para mantener historial, trazabilidad y control sobre qué documento cambió, por qué cambió y qué riesgo tuvo ese cambio.

Alimenta principalmente:

- CurrentStatePanel
- DocumentStatusMap
- DecisionInbox
- Historial futuro

## Campos sugeridos

- change_number
- change_title
- date
- status
- document_affected
- change_type
- initial_risk_level
- final_risk_level
- autonomy_level
- reason
- correction_applied
- dependencies
- conflicts
- authorized_scope
- unauthorized_scope
- final_state
- decision_related

## Estados permitidos

- Borrador
- En revisión
- Pendiente de aprobación
- Aprobado
- Actualizado
- Aprobado e integrado
- Pausado
- Rechazado
- Archivado
- Reemplazado

## Ejemplo conceptual

- change_number: 016
- change_title: Creación de ROBERT_TECHNICAL_DATA_MODEL_SPEC v0.1
- status: Borrador creado / pendiente de aprobación inicial
- document_affected: ROBERT_TECHNICAL_DATA_MODEL_SPEC
- change_type: Cambio técnico documental / modelo de datos conceptual
- initial_risk_level: Nivel 3 — Alto
- final_risk_level: Nivel 2 — Medio
- autonomy_level: Nivel 0 — Sin autonomía ejecutiva
- decision_related: DECISIÓN #012

---

# 5. MODELO — RiskRecord

## Función

RiskRecord representa un riesgo detectado dentro de una acción, documento, decisión, cambio o comando.

Sirve para explicar por qué algo requiere aprobación, por qué debe bloquearse o por qué puede continuar solo como borrador.

Alimenta principalmente:

- RiskBadge
- ApprovalGate
- DecisionInbox
- CurrentStatePanel

## Campos sugeridos

- risk_id
- risk_level
- risk_name
- risk_reason
- document_or_module_affected
- mode_active
- requires_approval
- approval_status
- recommended_action
- blocking_required
- related_decision
- related_change

## Niveles permitidos

- Nivel 0 — Informativo
- Nivel 1 — Bajo
- Nivel 2 — Medio
- Nivel 3 — Alto
- Nivel 4 — Crítico

## Ejemplo conceptual

- risk_id: risk_data_model_spec_v01
- risk_level: Nivel 2 — Medio
- risk_name: Modelo de datos conceptual aprobado
- risk_reason: Define datos conceptuales, pero no crea una base de datos real.
- document_or_module_affected: ROBERT_TECHNICAL_DATA_MODEL_SPEC
- mode_active: Supervisado
- requires_approval: Sí
- approval_status: Aprobado por DECISIÓN #012
- recommended_action: Mantener como base documental sin ejecución real.
- blocking_required: No

---

# 6. MODELO — CommandRequest

## Función

CommandRequest representa una solicitud o comando hecho por el usuario dentro de Robert.

Sirve para clasificar la intención del usuario, detectar riesgo, determinar si requiere aprobación y decidir si Robert puede preparar una respuesta, pausar o bloquear.

Alimenta principalmente:

- CommandCenter
- ModeSelector
- RiskBadge
- ApprovalGate
- DecisionInbox

## Campos sugeridos

- command_id
- user_input
- recognized_command
- mode_requested
- active_mode
- document_affected
- module_affected
- classified_intent
- change_type
- risk_level
- autonomy_level
- requires_approval
- status
- prepared_output
- result
- timestamp

## Estados permitidos

- Recibido
- Clasificado
- En revisión
- Borrador preparado
- Requiere aprobación
- Aprobado
- Pausado
- Bloqueado
- No permitido
- Completado

## Ejemplo conceptual

- command_id: cmd_001
- user_input: crea ROBERT_TECHNICAL_DATA_MODEL_SPEC
- recognized_command: CREA
- active_mode: Supervisado
- document_affected: ROBERT_TECHNICAL_DATA_MODEL_SPEC
- classified_intent: Crear documento técnico documental
- change_type: Cambio técnico documental
- risk_level: Nivel 3 — Alto
- autonomy_level: Nivel 0 — Sin autonomía ejecutiva
- requires_approval: Sí
- status: Completado documentalmente

---

# 7. MODELO — PendingDecision

## Función

PendingDecision representa una decisión pendiente que requiere intervención del usuario.

Sirve para que Robert no avance automáticamente cuando algo necesita revisión, aprobación, corrección o pausa.

Alimenta principalmente:

- DecisionInbox
- ApprovalGate
- CurrentStatePanel

## Campos sugeridos

- pending_id
- title
- reason
- document_affected
- change_type
- risk_level
- autonomy_level
- current_status
- options_available
- recommended_option
- created_date
- decision_required
- blocking_status

## Opciones permitidas

- Aprobar
- Rechazar
- Pausar
- Corregir
- Enviar a revisión
- Enviar a sandbox
- Archivar

## Ejemplo conceptual

- pending_id: pending_interaction_flow_spec
- title: Decidir si se crea ROBERT_TECHNICAL_INTERACTION_FLOW_SPEC
- reason: DATA_MODEL_SPEC v0.1 ya fue aprobado
- document_affected: ROBERT_TECHNICAL_INTERACTION_FLOW_SPEC
- risk_level: Nivel 3 — Alto
- autonomy_level: Nivel 0 — Sin autonomía ejecutiva
- current_status: Pendiente
- recommended_option: Revisar antes de crear
- decision_required: Sí
- blocking_status: No bloquea, pero requiere autorización

---

# 8. MODELO — ModeState

## Función

ModeState representa el modo operativo actual de Robert.

Sirve para saber si Robert está trabajando en modo manual, supervisado o sandbox, y qué acciones están bloqueadas en ese modo.

Alimenta principalmente:

- ModeSelector
- TopBar
- CurrentStatePanel
- CommandCenter

## Campos sugeridos

- active_mode
- available_modes
- restricted_modes
- execution_allowed
- external_actions_allowed
- automation_allowed
- agent_autonomy_allowed
- reason_for_restriction

## Modos activos permitidos en MVP básico

- Manual
- Supervisado
- Sandbox

## Modos no activos todavía

- Autónomo limitado
- Ejecución limitada
- Modo crítico

## Ejemplo conceptual

- active_mode: Supervisado
- available_modes: Manual, Supervisado, Sandbox
- restricted_modes: Autónomo limitado, Ejecución limitada, Modo crítico
- execution_allowed: No
- external_actions_allowed: No
- automation_allowed: No
- agent_autonomy_allowed: No
- reason_for_restriction: Fase 10 documental, sin programación autorizada

---

# 9. MODELO — ComponentState

## Función

ComponentState representa el estado de cada componente del MVP técnico básico.

Sirve para saber qué componente existe documentalmente, qué datos necesita, qué documento lo define y qué riesgo tiene.

Alimenta principalmente:

- DocumentStatusMap
- CurrentStatePanel
- Futuras vistas técnicas

## Campos sugeridos

- component_id
- component_name
- component_status
- component_priority
- layer_main
- layer_represented
- related_document
- requires_data_model
- requires_approval_gate
- risk_level
- notes

## Componentes prioritarios

- AppShell
- TopBar
- LeftSidebar
- CommandCenter
- ModeSelector
- RiskBadge
- ApprovalGate
- DecisionInbox
- DocumentStatusMap
- CurrentStatePanel

## Ejemplo conceptual

- component_id: risk_badge
- component_name: RiskBadge
- component_status: Definido documentalmente
- component_priority: Prioritario
- layer_main: Capa 5 — Presentación
- layer_represented: Capa 4 — Gobierno / Seguridad
- related_document: ROBERT_TECHNICAL_COMPONENTS_SPEC v0.2
- requires_data_model: Sí
- requires_approval_gate: Sí
- risk_level: Nivel 2 — Medio

---

# 10. MODELO — GitHubBackupStatus

## Función

GitHubBackupStatus representa el estado del respaldo manual de Robert en GitHub.

Sirve para mostrar si el repositorio existe, si es privado, si el respaldo es manual y si hay sincronización automática activa.

Alimenta principalmente:

- CurrentStatePanel
- TopBar
- DocumentStatusMap

## Campos sugeridos

- repository_name
- repository_status
- backup_mode
- last_checkpoint
- manual_update_required
- automatic_sync_enabled
- external_connection_status
- risk_level
- notes

## Ejemplo conceptual

- repository_name: ROBERT_MASTER_SYSTEM
- repository_status: Privado
- backup_mode: Manual
- last_checkpoint: Checkpoint documental GitHub completado
- manual_update_required: Sí
- automatic_sync_enabled: No
- external_connection_status: No conectado automáticamente
- risk_level: Nivel 2 — Medio
- notes: GitHub funciona solo como respaldo documental manual.

---

# 11. MODELO — ObsidianGraphStatus

## Función

ObsidianGraphStatus representa el estado de la convención visual de Obsidian.

Sirve para mostrar si el grafo documental está organizado, qué nodo funciona como centro visual, qué nodo funciona como centro conceptual y qué reglas de color se están usando.

Alimenta principalmente:

- DocumentStatusMap
- CurrentStatePanel
- Futuras vistas visuales

## Campos sugeridos

- graph_status
- visual_center
- conceptual_center
- orbit_rule
- color_rule
- tags_enabled
- wikilinks_enabled
- official_convention
- related_document
- risk_level
- notes

## Ejemplo conceptual

- graph_status: Convención visual validada
- visual_center: ROBERT_HOME
- conceptual_center: ROBERT_CONTEXT_MASTER
- orbit_rule: Órbita = posición / cercanía al núcleo
- color_rule: Capa o función = color visual
- tags_enabled: Sí
- wikilinks_enabled: Sí
- official_convention: Sí
- related_document: ROBERT_VISUAL
- risk_level: Nivel 2 — Medio
- notes: Obsidian Graph View funciona como navegación documental, no como HUD final.

---

# RELACIONES ENTRE MODELOS

Los modelos se relacionan de la siguiente manera:

SystemState muestra el estado general del sistema.

RobertDocument representa los documentos que forman parte del sistema.

DecisionRecord registra las decisiones formales tomadas por el usuario.

ChangeRecord registra los cambios documentales realizados.

RiskRecord explica los riesgos asociados a documentos, comandos, cambios o decisiones.

CommandRequest interpreta solicitudes del usuario y puede generar riesgos o decisiones pendientes.

PendingDecision guarda elementos que no deben avanzar sin aprobación.

ModeState define el modo operativo actual de Robert.

ComponentState indica qué componentes existen documentalmente y qué datos necesitan.

GitHubBackupStatus muestra el estado del respaldo manual en GitHub.

ObsidianGraphStatus muestra el estado de la organización visual en Obsidian.

---

# FLUJO CONCEPTUAL DE DATOS

El flujo conceptual de información del MVP técnico básico es:

1. El usuario da una instrucción.
2. Robert la interpreta como CommandRequest.
3. Robert identifica el modo activo mediante ModeState.
4. Robert evalúa el riesgo mediante RiskRecord.
5. Si la instrucción requiere aprobación, se crea una PendingDecision.
6. Si el usuario aprueba, se registra una DecisionRecord.
7. Si la aprobación genera cambios, se registra un ChangeRecord.
8. Los documentos afectados se actualizan como RobertDocument.
9. SystemState refleja el nuevo estado general.
10. CurrentStatePanel y DocumentStatusMap muestran el estado actualizado.

Este flujo es conceptual.

No implica programación ni ejecución real en esta etapa.

---

# DATOS PROHIBIDOS EN ESTA ETAPA

En esta fase no deben guardarse datos sensibles reales como:

- Contraseñas.
- API keys.
- Tokens.
- Datos bancarios.
- Datos fiscales reales.
- Datos legales confidenciales.
- Correos privados.
- Teléfonos de clientes reales.
- Información personal sensible.
- Listas reales de clientes.
- Credenciales de herramientas.
- Datos médicos.
- Datos financieros operativos.
- Documentos privados de terceros sin autorización.

---

# DATOS PERMITIDOS EN ESTA ETAPA

Se permiten datos documentales y simulados como:

- Nombre del documento.
- Estado del documento.
- Versión.
- Fase relacionada.
- Cambio relacionado.
- Decisión relacionada.
- Riesgo conceptual.
- Modo activo.
- Componente relacionado.
- Estado de GitHub manual.
- Estado de Obsidian Graph.
- Notas de revisión.
- Campos simulados.
- Ejemplos ficticios.
- Datos de prueba no sensibles.

---

# REGLAS DE VALIDACIÓN

Antes de usar un dato dentro de Robert, debe revisarse:

- ¿Este dato es necesario?
- ¿Este dato es sensible?
- ¿Este dato está autorizado?
- ¿Este dato es real o simulado?
- ¿Este dato pertenece a un documento oficial?
- ¿Este dato debe mostrarse en el MVP?
- ¿Este dato requiere aprobación?
- ¿Este dato debe bloquearse?

Si existe duda, Robert debe pausar y pedir autorización.

---

# CRITERIOS DE ACEPTACIÓN

Este documento se considera aprobado porque:

- No autoriza programación.
- No autoriza base de datos real.
- No autoriza conexiones externas.
- No autoriza automatizaciones.
- No autoriza agentes autónomos.
- Define modelos conceptuales claros.
- Se alinea con COMPONENTS_SPEC v0.2.
- Respeta CONTEXT_MASTER v0.5.
- Respeta PHASES v0.5.
- Respeta SECURITY_RULES.
- Usa la escala oficial de riesgo.
- Separa riesgo, autonomía, tipo de cambio y estado.
- Define datos permitidos y prohibidos.
- Mantiene a Robert en Fase 10.

---

# RIESGO DEL DOCUMENTO

Tipo de cambio:

**Aprobación técnica documental / modelo de datos conceptual**

Nivel de riesgo inicial:

**Nivel 3 — Alto**

Motivo:

Este documento define la estructura conceptual de datos que podría alimentar el MVP técnico básico. Aunque no implementa nada, acerca el proyecto a una futura construcción técnica.

Nivel de riesgo final:

**Nivel 2 — Medio**

Motivo de reducción:

El documento es conceptual, no crea una base de datos real, no programa, no conecta herramientas externas y no autoriza ejecución.

Nivel de autonomía:

**Nivel 0 — Sin autonomía ejecutiva**

---

# EFECTO DE LA APROBACIÓN

Con esta aprobación:

- ROBERT_TECHNICAL_DATA_MODEL_SPEC v0.1 queda aprobado.
- Puede usarse como base para futuras especificaciones técnicas.
- Puede relacionarse con COMPONENTS_SPEC v0.2.
- Puede ayudar a definir qué datos necesitarán los componentes del MVP.
- No autoriza programación.
- No autoriza base de datos real.
- No autoriza conexiones externas.
- No autoriza automatizaciones.
- No autoriza agentes autónomos.
- No autoriza ejecución real.

---

# PRÓXIMO PASO RECOMENDADO

Después de este documento, el siguiente documento posible es:

**ROBERT_TECHNICAL_INTERACTION_FLOW_SPEC**

Ese documento definiría cómo interactúan los componentes entre sí usando los modelos de datos conceptuales aprobados aquí.

No debe crearse sin autorización del usuario.

---

# CIERRE

ROBERT_TECHNICAL_DATA_MODEL_SPEC v0.1 define los modelos de datos conceptuales iniciales para el MVP técnico básico de Robert.

Este documento organiza la información que Robert necesitaría para mostrar estado, documentos, decisiones, cambios, riesgos, comandos y componentes.

Robert sigue en modo documental y supervisado.

El usuario mantiene control total.

Robert no ejecuta acciones importantes sin permiso.
