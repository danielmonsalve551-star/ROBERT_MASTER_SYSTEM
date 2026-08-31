# ROBERT_TECHNICAL_INTERACTION_FLOW_SPEC

Versión: 0.2  
Estado: APROBADO E INTEGRADO
Fecha: 03/07/2026  
Ubicación: 10_MVP  
Fase relacionada: Fase 10 — MVP técnico básico en preparación  
Documento base relacionado: ROBERT_TECHNICAL_DATA_MODEL_SPEC v0.1  
Documento relacionado: ROBERT_TECHNICAL_COMPONENTS_SPEC v0.2  
Fuente de verdad actual: ROBERT_CONTEXT_MASTER v0.5  
Cambio relacionado previo: CAMBIO #021 — Creación de ROBERT_TECHNICAL_INTERACTION_FLOW_SPEC v0.1  

Tags: #robert/orbita-3 #capa/5 #tipo/tecnico #robert/mvp #robert/interaction-flow

---

# OBJETIVO

ROBERT_TECHNICAL_INTERACTION_FLOW_SPEC define cómo interactúan conceptualmente los componentes del MVP técnico básico de Robert.

Su objetivo es explicar, de forma ordenada, cómo fluye la información entre el usuario, los componentes visuales, los modelos de datos y las reglas de seguridad del sistema.

Este documento define la interacción conceptual entre:

- Usuario
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

Este documento usa como base los modelos definidos en:

**ROBERT_TECHNICAL_DATA_MODEL_SPEC v0.1**

También se relaciona con:

**ROBERT_TECHNICAL_COMPONENTS_SPEC v0.2**

Este documento no programa la app.

Este documento no crea código.

Este documento no crea flujos automáticos reales.

Este documento no conecta herramientas externas.

Este documento no ejecuta acciones reales.

Este documento solo define flujos conceptuales de interacción para una futura implementación técnica controlada.

---

# ESTADO DEL DOCUMENTO

Este documento queda como:

**Propuesta corregida — pendiente de revisión**

No está aprobado todavía.

No reemplaza a ningún documento maestro.

No autoriza programación.

No autoriza base de datos real.

No autoriza conexiones externas.

No autoriza automatizaciones.

No autoriza agentes autónomos.

No autoriza ejecución real.

---

# CAMBIOS DE v0.2 RESPECTO A v0.1

Esta versión corrige puntos detectados durante la revisión de v0.1:

1. Aclara el rol de AppShell como contenedor raíz.
2. Define qué datos reciben TopBar y LeftSidebar.
3. Integra ComponentState dentro de un flujo propio.
4. Integra GitHubBackupStatus y ObsidianGraphStatus dentro de los datos que fluyen.
5. Define mejor qué ocurre con riesgo Nivel 2.
6. Aclara cuándo una respuesta simple actualiza SystemState y cuándo no.
7. Añade FLUJO 13 — Estado de componentes.
8. Añade una sección completa de datos recibidos y enviados por todos los componentes principales.

---

# REGLA CENTRAL

El usuario manda.

Robert no ejecuta acciones importantes sin permiso.

Todo flujo de interacción debe respetar:

- ROBERT_SECURITY_RULES
- ROBERT_CONTEXT_MASTER v0.5
- ROBERT_COMMANDS
- ROBERT_DECISIONS_LOG
- ROBERT_CONTROL_DE_CAMBIOS
- ROBERT_PHASES v0.5
- ROBERT_TECHNICAL_COMPONENTS_SPEC v0.2
- ROBERT_TECHNICAL_DATA_MODEL_SPEC v0.1

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
- ROBERT_TECHNICAL_INTERACTION_FLOW_SPEC v0.1 creado como borrador.
- ROBERT_TECHNICAL_INTERACTION_FLOW_SPEC v0.2 preparado como propuesta corregida.
- Convención visual de Obsidian v0.2 aprobada e integrada.
- Sin programación autorizada.
- Sin base de datos real.
- Sin conexiones externas.
- Sin automatizaciones reales.
- Sin agentes autónomos activos.

---

# ALCANCE AUTORIZADO

Este documento autoriza únicamente:

- Definir flujos conceptuales entre componentes.
- Explicar cómo se mueve la información dentro del MVP.
- Relacionar componentes con modelos de datos.
- Definir cuándo un flujo debe continuar.
- Definir cuándo un flujo debe pausar.
- Definir cuándo un flujo debe pedir aprobación.
- Definir cuándo un flujo debe bloquearse.
- Definir qué datos recibe cada componente.
- Definir qué modelos alimentan cada flujo.
- Preparar base documental para futuras especificaciones técnicas.
- Mantener a Robert en modo documental, manual y supervisado.

---

# ALCANCE NO AUTORIZADO

Este documento no autoriza:

- Programar la app.
- Crear código.
- Crear una base de datos real.
- Crear tablas reales.
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

# PRINCIPIO GENERAL DE INTERACCIÓN

Todo flujo dentro de Robert debe seguir esta lógica:

1. El usuario da una instrucción.
2. Robert interpreta la instrucción.
3. Robert identifica el modo activo.
4. Robert evalúa el nivel de riesgo.
5. Robert determina si necesita aprobación.
6. Robert prepara un resultado, borrador o respuesta.
7. Robert espera autorización si la acción lo requiere.
8. Robert registra decisiones y cambios cuando aplique.
9. Robert actualiza el estado documental cuando exista un cambio real de estado.
10. Robert no ejecuta acciones reales sin permiso.

Regla principal:

**Primero interpretar. Después clasificar. Después evaluar riesgo. Después pedir aprobación si aplica. Después preparar. Nunca ejecutar sin permiso.**

---

# COMPONENTES INVOLUCRADOS

Los componentes principales del MVP técnico básico son:

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

# ACLARACIÓN DE ROLES DE COMPONENTES

## AppShell

AppShell es el contenedor raíz del MVP técnico básico.

Su función es alojar, ordenar y mostrar los componentes principales.

AppShell no toma decisiones.

AppShell no evalúa riesgo.

AppShell no aprueba acciones.

AppShell no ejecuta acciones.

AppShell no modifica documentos.

AppShell solo recibe estado general para organizar la pantalla.

---

## TopBar

TopBar es la barra superior de estado.

Su función es mostrar información resumida del sistema.

TopBar no toma decisiones.

TopBar no ejecuta acciones.

TopBar no modifica documentos.

TopBar solo muestra datos relevantes como fase, modo, estado de ejecución y última actualización.

---

## LeftSidebar

LeftSidebar es la navegación lateral documental.

Su función es permitir moverse entre documentos, áreas, módulos o secciones.

LeftSidebar no toma decisiones.

LeftSidebar no evalúa riesgo.

LeftSidebar no aprueba acciones.

LeftSidebar no ejecuta acciones.

LeftSidebar solo muestra navegación, documentos y estructura.

---

## CommandCenter

CommandCenter es el punto donde el usuario da instrucciones.

Su función es recibir, clasificar y preparar solicitudes.

CommandCenter no ejecuta acciones reales por sí solo.

---

## ModeSelector

ModeSelector identifica el modo activo de Robert.

Su función es limitar o permitir flujos según el modo operativo.

---

## RiskBadge

RiskBadge muestra el nivel de riesgo y la razón del riesgo.

Su función es hacer visible el riesgo antes de avanzar.

---

## ApprovalGate

ApprovalGate decide si una acción requiere autorización, pausa o bloqueo.

No aprueba por sí solo.

Solo aplica las reglas de seguridad.

---

## DecisionInbox

DecisionInbox muestra elementos pendientes de decisión del usuario.

No resuelve decisiones automáticamente.

---

## DocumentStatusMap

DocumentStatusMap muestra estado, versión, fase y relación entre documentos.

No modifica documentos por sí solo.

---

## CurrentStatePanel

CurrentStatePanel muestra el estado general actualizado de Robert.

No ejecuta acciones.

Solo refleja cambios documentales, decisiones, riesgos o modos.

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

# FLUJO GENERAL DEL MVP TÉCNICO BÁSICO

El flujo general del MVP técnico básico es:

Usuario  
↓  
AppShell aloja la interfaz  
↓  
CommandCenter recibe la instrucción  
↓  
ModeSelector identifica modo activo  
↓  
RiskBadge evalúa riesgo  
↓  
ApprovalGate determina si puede continuar  
↓  
DecisionInbox muestra pendientes si aplica  
↓  
Robert prepara respuesta o borrador  
↓  
Usuario aprueba, corrige, pausa o rechaza  
↓  
DecisionRecord si aplica  
↓  
ChangeRecord si aplica  
↓  
RobertDocument se actualiza si aplica  
↓  
SystemState se actualiza si aplica  
↓  
CurrentStatePanel, TopBar, LeftSidebar y DocumentStatusMap muestran estado actualizado  

Este flujo es conceptual.

No implica programación ni ejecución real en esta etapa.

---

# FLUJO 1 — INSTRUCCIÓN DEL USUARIO

## Objetivo

Definir qué pasa cuando el usuario escribe una instrucción dentro de Robert.

## Flujo conceptual

1. El usuario escribe una instrucción.
2. AppShell mantiene visible la interfaz general.
3. CommandCenter recibe la instrucción.
4. CommandCenter crea un CommandRequest.
5. ModeSelector identifica el modo activo.
6. RiskBadge evalúa el nivel de riesgo.
7. ApprovalGate determina si se necesita autorización.
8. Si no requiere aprobación, Robert puede preparar una respuesta.
9. Si requiere aprobación, se crea una PendingDecision.
10. DecisionInbox muestra la decisión pendiente.
11. Robert espera instrucción del usuario cuando el flujo requiera autorización.

## Componentes involucrados

- AppShell
- CommandCenter
- ModeSelector
- RiskBadge
- ApprovalGate
- DecisionInbox
- CurrentStatePanel
- TopBar

## Modelos utilizados

- CommandRequest
- ModeState
- RiskRecord
- PendingDecision
- SystemState

## Regla de actualización de estado

Una instrucción simple no siempre actualiza SystemState.

Solo actualiza SystemState o CurrentStatePanel si cambia alguno de estos elementos:

- Documento activo.
- Modo activo.
- Riesgo relevante.
- Decisión pendiente.
- Cambio documental.
- Decisión formal.
- Estado de ejecución.
- Estado de respaldo.
- Estado visual del grafo.

Si la respuesta es solo explicativa y no cambia nada, no se registra como cambio formal.

## Regla de seguridad

Si la instrucción implica riesgo medio, alto o crítico, Robert debe aplicar las reglas de riesgo definidas en este documento.

---

# FLUJO 2 — COMANDO DOCUMENTAL SIMPLE

## Objetivo

Definir qué pasa cuando el usuario pide crear, revisar o actualizar un documento sin ejecución real.

## Ejemplo de instrucción

crea un documento técnico

## Flujo conceptual

1. CommandCenter recibe la instrucción.
2. Robert clasifica la intención como cambio documental.
3. ModeSelector confirma que el modo activo permite preparación documental.
4. RiskBadge asigna nivel de riesgo.
5. ApprovalGate revisa si el cambio requiere aprobación.
6. Robert prepara el documento como borrador.
7. El documento queda representado como RobertDocument.
8. Si el usuario confirma que lo creó, se registra ChangeRecord.
9. CurrentStatePanel actualiza el estado.
10. DocumentStatusMap refleja el nuevo documento.
11. TopBar puede mostrar última actualización.
12. LeftSidebar puede mostrar el nuevo documento si ya existe.

## Componentes involucrados

- CommandCenter
- ModeSelector
- RiskBadge
- ApprovalGate
- CurrentStatePanel
- DocumentStatusMap
- TopBar
- LeftSidebar

## Modelos utilizados

- CommandRequest
- RiskRecord
- RobertDocument
- ChangeRecord
- SystemState

## Regla de seguridad

Crear un documento no significa aprobarlo.

Preparar un documento no significa integrarlo.

Integrar un documento no significa ejecutar acciones reales.

---

# FLUJO 3 — APROBACIÓN FORMAL DE DOCUMENTO

## Objetivo

Definir qué pasa cuando el usuario aprueba formalmente un documento.

## Ejemplo de instrucción

la apruebo

## Flujo conceptual

1. CommandCenter recibe la aprobación del usuario.
2. Robert identifica qué documento está siendo aprobado.
3. RiskBadge evalúa el riesgo de aprobación.
4. ApprovalGate confirma que la aprobación viene del usuario.
5. Robert prepara una DecisionRecord.
6. El usuario registra la decisión en ROBERT_DECISIONS_LOG.
7. Robert prepara un ChangeRecord de aprobación e integración.
8. El usuario registra el cambio en ROBERT_CONTROL_DE_CAMBIOS.
9. Robert actualiza el estado del documento como aprobado.
10. SystemState actualiza última decisión y último cambio.
11. CurrentStatePanel y DocumentStatusMap reflejan el nuevo estado.
12. TopBar puede mostrar última decisión.
13. LeftSidebar puede mantener visible el documento aprobado.

## Componentes involucrados

- CommandCenter
- RiskBadge
- ApprovalGate
- DecisionInbox
- CurrentStatePanel
- DocumentStatusMap
- TopBar
- LeftSidebar

## Modelos utilizados

- CommandRequest
- RiskRecord
- DecisionRecord
- ChangeRecord
- RobertDocument
- SystemState

## Regla de seguridad

Aprobar un documento técnico no autoriza programación.

Aprobar un documento técnico no autoriza conexiones.

Aprobar un documento técnico no autoriza automatizaciones.

---

# FLUJO 4 — DETECCIÓN DE RIESGO

## Objetivo

Definir qué pasa cuando Robert detecta riesgo en una instrucción.

## Flujo conceptual

1. CommandCenter recibe una instrucción.
2. RiskBadge analiza el tipo de acción.
3. RiskBadge asigna un nivel de riesgo.
4. Si el riesgo es Nivel 0 o Nivel 1, Robert puede responder o preparar borrador.
5. Si el riesgo es Nivel 2, Robert debe mostrar advertencia y confirmar alcance.
6. Si el riesgo es Nivel 3, Robert debe pedir autorización explícita.
7. Si el riesgo es Nivel 4, Robert debe bloquear o pausar.
8. ApprovalGate decide si el flujo puede continuar.
9. DecisionInbox muestra lo pendiente si hay decisión requerida.
10. CurrentStatePanel puede reflejar el riesgo si afecta estado relevante.

## Componentes involucrados

- CommandCenter
- RiskBadge
- ApprovalGate
- DecisionInbox
- CurrentStatePanel
- TopBar

## Modelos utilizados

- CommandRequest
- RiskRecord
- PendingDecision
- ModeState
- SystemState

## Escala aplicada

- Nivel 0 — Informativo
- Nivel 1 — Bajo
- Nivel 2 — Medio
- Nivel 3 — Alto
- Nivel 4 — Crítico

## Regla específica para Nivel 2

Nivel 2 significa riesgo medio.

Por defecto, Nivel 2 genera:

- Advertencia visible.
- Confirmación de alcance.
- Revisión antes de continuar.

Nivel 2 no siempre genera una PendingDecision formal.

Nivel 2 sí debe generar PendingDecision cuando afecta cualquiera de estos elementos:

- Documento maestro.
- Seguridad.
- Fuente de verdad.
- Fases.
- Control de cambios.
- Decisión formal.
- Datos sensibles.
- Acción externa.
- Preparación de conexión real.
- Avance hacia programación.
- Avance hacia Fase 11.

Si Nivel 2 no afecta esos elementos, puede manejarse como confirmación inline sin registro formal.

## Regla de seguridad

No existe Nivel 5 como riesgo.

Nivel 5 solo puede existir como autonomía si está definido en SECURITY_RULES.

---

# FLUJO 5 — BLOQUEO POR ACCIÓN NO AUTORIZADA

## Objetivo

Definir qué pasa cuando el usuario o el sistema intenta avanzar a una acción no autorizada.

## Ejemplos de acciones no autorizadas

- Programar la app.
- Crear base de datos real.
- Conectar Gmail.
- Conectar Google Calendar.
- Conectar GitHub automáticamente.
- Activar agentes.
- Ejecutar acciones externas.
- Automatizar decisiones.
- Avanzar a Fase 11 sin aprobación formal.

## Flujo conceptual

1. CommandCenter recibe la instrucción.
2. ModeSelector identifica que el modo actual no permite ejecución real.
3. RiskBadge marca riesgo alto o crítico.
4. ApprovalGate bloquea la acción.
5. Robert explica el motivo del bloqueo.
6. DecisionInbox puede crear una decisión pendiente si aplica.
7. CurrentStatePanel mantiene el estado sin cambios ejecutivos.
8. TopBar puede mostrar estado bloqueado si el bloqueo es relevante.
9. SystemState no cambia a ejecución real.

## Componentes involucrados

- CommandCenter
- ModeSelector
- RiskBadge
- ApprovalGate
- DecisionInbox
- CurrentStatePanel
- TopBar

## Modelos utilizados

- CommandRequest
- ModeState
- RiskRecord
- PendingDecision
- SystemState

## Regla de seguridad

Robert puede explicar, preparar o simular.

Robert no debe ejecutar.

---

# FLUJO 6 — ACTUALIZACIÓN DEL ESTADO GENERAL

## Objetivo

Definir cómo Robert actualiza su estado después de una decisión o cambio documental.

## Flujo conceptual

1. Se registra una DecisionRecord o ChangeRecord.
2. RobertDocument actualiza el estado del documento afectado.
3. SystemState actualiza la última decisión y el último cambio.
4. CurrentStatePanel muestra el estado actualizado.
5. DocumentStatusMap refleja el cambio visualmente.
6. TopBar muestra la fase, modo y última actualización.
7. LeftSidebar mantiene navegación documental.
8. AppShell mantiene la estructura visual general.

## Componentes involucrados

- AppShell
- CurrentStatePanel
- DocumentStatusMap
- TopBar
- LeftSidebar

## Modelos utilizados

- SystemState
- RobertDocument
- DecisionRecord
- ChangeRecord
- ComponentState

## Regla de seguridad

Actualizar estado documental no significa ejecutar acciones reales.

---

# FLUJO 7 — DECISIONES PENDIENTES

## Objetivo

Definir cómo Robert maneja elementos que requieren aprobación del usuario.

## Flujo conceptual

1. Una instrucción genera una acción pendiente.
2. ApprovalGate determina que no debe avanzar sin autorización.
3. Se crea una PendingDecision.
4. DecisionInbox muestra la decisión pendiente.
5. El usuario puede aprobar, rechazar, corregir, pausar o archivar.
6. Robert actúa únicamente dentro del alcance autorizado.
7. Si se aprueba, se registra DecisionRecord.
8. Si genera cambio documental, se registra ChangeRecord.
9. CurrentStatePanel actualiza el estado pendiente o resuelto.
10. TopBar puede mostrar que existe una decisión pendiente.

## Componentes involucrados

- ApprovalGate
- DecisionInbox
- CommandCenter
- CurrentStatePanel
- TopBar

## Modelos utilizados

- PendingDecision
- DecisionRecord
- ChangeRecord
- RiskRecord
- SystemState

## Regla de seguridad

Una decisión pendiente no debe resolverse automáticamente.

---

# FLUJO 8 — MAPA DE DOCUMENTOS

## Objetivo

Definir cómo Robert muestra el estado de sus documentos.

## Flujo conceptual

1. RobertDocument contiene información de cada documento.
2. DocumentStatusMap lee estado, versión, fase, tags y riesgo.
3. CurrentStatePanel resume documentos principales.
4. LeftSidebar permite navegación por áreas.
5. TopBar muestra el estado general de la fase.
6. AppShell mantiene visible la estructura general.

## Componentes involucrados

- AppShell
- DocumentStatusMap
- CurrentStatePanel
- LeftSidebar
- TopBar

## Modelos utilizados

- RobertDocument
- SystemState
- ChangeRecord
- DecisionRecord
- ObsidianGraphStatus

## Estados posibles

- Borrador
- En revisión
- Pendiente de aprobación
- Aprobado
- Rechazado
- Pausado
- Reemplazado
- Archivado
- Histórico

---

# FLUJO 9 — MODO ACTIVO

## Objetivo

Definir cómo Robert interpreta el modo operativo actual.

## Modos permitidos en esta etapa

- Manual
- Supervisado
- Sandbox

## Flujo conceptual

1. ModeSelector identifica el modo activo.
2. CommandCenter interpreta la instrucción dentro de ese modo.
3. RiskBadge ajusta el nivel de riesgo según el modo.
4. ApprovalGate bloquea acciones que el modo no permita.
5. CurrentStatePanel muestra el modo actual.
6. TopBar muestra el modo activo.
7. AppShell mantiene la interfaz dentro de los límites del modo.

## Componentes involucrados

- AppShell
- ModeSelector
- CommandCenter
- RiskBadge
- ApprovalGate
- CurrentStatePanel
- TopBar

## Modelos utilizados

- ModeState
- CommandRequest
- RiskRecord
- SystemState

## Regla de seguridad

El modo activo nunca debe permitir más autonomía de la autorizada por SECURITY_RULES.

---

# FLUJO 10 — RESPUESTA DE ROBERT

## Objetivo

Definir cómo Robert responde después de interpretar una instrucción.

## Tipos de respuesta permitidos

- Explicación.
- Resumen.
- Borrador.
- Documento para copiar.
- Revisión.
- Corrección.
- Clasificación.
- Simulación.
- Recomendación.
- Solicitud de aprobación.
- Bloqueo justificado.

## Flujo conceptual

1. CommandCenter interpreta la solicitud.
2. RiskBadge evalúa el riesgo.
3. ApprovalGate define si puede responder.
4. Robert prepara la respuesta dentro del alcance permitido.
5. Si requiere aprobación, Robert se detiene.
6. Si no requiere aprobación, Robert entrega el resultado.
7. Si la respuesta no cambia estado documental, no se registra ChangeRecord.
8. Si la respuesta cambia estado documental, se actualiza SystemState.
9. Robert no ejecuta acciones externas.

## Componentes involucrados

- CommandCenter
- RiskBadge
- ApprovalGate
- CurrentStatePanel
- TopBar

## Modelos utilizados

- CommandRequest
- RiskRecord
- ModeState
- SystemState

## Regla de actualización

Una respuesta simple no genera cambio formal.

Una respuesta genera actualización formal solo si:

- Crea documento.
- Modifica documento.
- Cambia estado.
- Registra decisión.
- Registra cambio.
- Cambia modo.
- Crea decisión pendiente.
- Bloquea una acción relevante.

---

# FLUJO 11 — RESPALDO MANUAL EN GITHUB

## Objetivo

Definir cómo Robert interpreta el estado del respaldo documental manual en GitHub.

## Flujo conceptual

1. El usuario actualiza un documento en Obsidian.
2. El usuario actualiza manualmente GitHub.
3. GitHubBackupStatus refleja que el respaldo sigue siendo manual.
4. CurrentStatePanel puede mostrar el estado de respaldo.
5. DocumentStatusMap puede mostrar qué documentos están actualizados.
6. TopBar puede mostrar última actualización manual si aplica.
7. Robert no sincroniza automáticamente.

## Componentes involucrados

- CurrentStatePanel
- DocumentStatusMap
- TopBar

## Modelos utilizados

- GitHubBackupStatus
- RobertDocument
- SystemState

## Regla de seguridad

GitHub funciona solo como respaldo documental manual.

No hay sincronización automática autorizada.

---

# FLUJO 12 — GRAFO VISUAL DE OBSIDIAN

## Objetivo

Definir cómo Robert interpreta la organización visual de Obsidian.

## Flujo conceptual

1. ObsidianGraphStatus guarda la convención visual.
2. ROBERT_HOME funciona como centro visual.
3. ROBERT_CONTEXT_MASTER funciona como centro conceptual.
4. Las órbitas representan función arquitectónica.
5. Los colores representan capa o función visual.
6. DocumentStatusMap puede usar esta lógica como referencia visual.
7. CurrentStatePanel puede mostrar si la convención visual está actualizada.
8. Robert no depende del grafo para ejecutar acciones.

## Componentes involucrados

- DocumentStatusMap
- CurrentStatePanel
- LeftSidebar
- TopBar

## Modelos utilizados

- ObsidianGraphStatus
- RobertDocument
- SystemState

## Regla de seguridad

Obsidian Graph View funciona como navegación documental.

No es el HUD final de Robert.

No ejecuta acciones.

---

# FLUJO 13 — ESTADO DE COMPONENTES

## Objetivo

Definir cómo Robert representa el estado de sus componentes principales.

Este flujo corrige la ausencia de uso explícito del modelo ComponentState.

## Flujo conceptual

1. ComponentState representa cada componente del MVP técnico básico.
2. AppShell recibe la lista de componentes disponibles.
3. AppShell organiza visualmente los componentes.
4. CurrentStatePanel muestra qué componentes están definidos documentalmente.
5. DocumentStatusMap relaciona componentes con documentos técnicos.
6. TopBar puede mostrar si el MVP técnico sigue en preparación.
7. Robert no activa componentes reales porque no hay programación autorizada.

## Componentes involucrados

- AppShell
- CurrentStatePanel
- DocumentStatusMap
- TopBar
- LeftSidebar

## Modelos utilizados

- ComponentState
- SystemState
- RobertDocument

## Componentes representados

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

## Estados posibles de componente

- Definido documentalmente.
- Pendiente de diseño.
- Pendiente de revisión.
- Pendiente de aprobación.
- Aprobado documentalmente.
- No implementado.
- Bloqueado.
- Futuro.

## Regla de seguridad

Que un componente esté definido documentalmente no significa que exista técnicamente.

Definir un componente no autoriza programarlo.

---

# DATOS QUE FLUYEN ENTRE COMPONENTES

## AppShell recibe

- system_state
- component_list
- active_mode
- current_phase
- active_document
- layout_status

## AppShell envía

- No envía datos operativos.
- No toma decisiones.
- No ejecuta acciones.
- Solo aloja y organiza componentes.

---

## TopBar recibe

- current_phase
- active_mode
- execution_status
- risk_summary
- last_decision
- last_change
- last_update
- backup_status
- pending_decision_count

## TopBar envía

- No envía decisiones.
- No ejecuta acciones.
- Solo muestra estado resumido.

---

## LeftSidebar recibe

- document_list
- folder_structure
- active_document
- document_status
- document_type
- orbit_tag
- module_list

## LeftSidebar envía

- selected_document
- navigation_target

## Regla

LeftSidebar solo navega.

No aprueba, no bloquea y no ejecuta.

---

## CommandCenter envía

- user_input
- recognized_command
- classified_intent
- document_affected
- module_affected
- risk_level_preliminar

## CommandCenter recibe

- active_mode
- allowed_actions
- restricted_actions
- current_context
- active_document

---

## ModeSelector envía

- active_mode
- restricted_modes
- execution_allowed
- automation_allowed
- external_actions_allowed
- agent_autonomy_allowed

## ModeSelector recibe

- mode_request
- current_security_rules
- user_confirmation_if_required

---

## RiskBadge envía

- risk_level
- risk_reason
- recommended_action
- blocking_required
- approval_recommended

## RiskBadge recibe

- command_request
- active_mode
- document_affected
- action_type
- security_rules

---

## ApprovalGate envía

- approval_required
- approval_status
- blocked_reason
- next_allowed_action
- pending_decision_required

## ApprovalGate recibe

- risk_record
- command_request
- mode_state
- user_approval_if_available

---

## DecisionInbox envía

- pending_id
- title
- options_available
- recommended_option
- current_status
- decision_required

## DecisionInbox recibe

- pending_decision
- risk_record
- approval_gate_result
- related_document
- related_change

---

## DocumentStatusMap envía

- document_name
- document_status
- version
- decision_related
- change_related
- orbit_tag
- document_type
- risk_level_if_relevant

## DocumentStatusMap recibe

- robert_document
- decision_record
- change_record
- obsidian_graph_status
- github_backup_status

---

## CurrentStatePanel envía

- current_phase
- active_mode
- last_decision
- last_change
- execution_status
- programming_authorized
- database_authorized
- external_connections_authorized
- automations_authorized
- agents_authorized

## CurrentStatePanel recibe

- system_state
- decision_record
- change_record
- risk_record
- pending_decision
- github_backup_status
- obsidian_graph_status
- component_state

---

## GitHubBackupStatus envía

- repository_name
- repository_status
- backup_mode
- last_checkpoint
- manual_update_required
- automatic_sync_enabled
- external_connection_status
- backup_risk_level

## GitHubBackupStatus recibe

- manual_update_confirmation
- document_updated
- checkpoint_note

## Regla

GitHubBackupStatus solo representa respaldo manual.

No sincroniza automáticamente.

---

## ObsidianGraphStatus envía

- graph_status
- visual_center
- conceptual_center
- orbit_rule
- color_rule
- tags_enabled
- wikilinks_enabled
- official_convention

## ObsidianGraphStatus recibe

- visual_convention_update
- tag_cleanup_status
- graph_review_note

## Regla

ObsidianGraphStatus representa navegación documental.

No ejecuta acciones.

---

## ComponentState envía

- component_id
- component_name
- component_status
- component_priority
- layer_main
- related_document
- requires_data_model
- requires_approval_gate
- risk_level_if_relevant

## ComponentState recibe

- component_definition
- related_spec_document
- approval_status
- review_status

## Regla

ComponentState representa componentes conceptuales.

No significa que el componente ya exista como código.

---

# DATOS PROHIBIDOS EN LOS FLUJOS

En esta etapa, ningún flujo debe mover, guardar o procesar:

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

# DATOS PERMITIDOS EN LOS FLUJOS

Los flujos pueden usar únicamente datos documentales y simulados como:

- Nombre de documento.
- Estado de documento.
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
- Datos ficticios.
- Datos de prueba no sensibles.

---

# REGLAS DE PAUSA

Robert debe pausar cuando:

- Falte información importante.
- Exista ambigüedad de alcance.
- El usuario pida una acción real.
- El usuario pida conectar herramientas.
- El usuario pida automatizar.
- El usuario pida programar sin aprobación formal.
- El riesgo sea Nivel 3 o Nivel 4.
- Nivel 2 afecte documento maestro, seguridad, fuente de verdad o fase.
- La instrucción pueda afectar documentos maestros.
- La instrucción contradiga SECURITY_RULES.
- La instrucción pueda avanzar de fase sin aprobación.

---

# REGLAS DE BLOQUEO

Robert debe bloquear cuando:

- Se intente ejecutar una acción externa sin permiso.
- Se pidan credenciales, tokens o contraseñas.
- Se intente conectar apps reales sin fase autorizada.
- Se intente activar agentes autónomos.
- Se intente automatizar decisiones importantes.
- Se intente modificar documentos maestros sin autorización.
- Se intente avanzar a Fase 11 sin aprobación formal.
- Se intente usar datos sensibles reales sin control.

---

# REGLAS DE APROBACIÓN

Robert debe pedir aprobación explícita cuando:

- Se crea un documento técnico nuevo.
- Se aprueba un documento.
- Se integra un documento al estado oficial.
- Se modifica una regla de seguridad.
- Se modifica la fuente de verdad.
- Se registra una decisión formal.
- Se registra un cambio relevante.
- Se cambia de fase.
- Se prepara una futura conexión real.
- Se acerca el proyecto a programación o ejecución.
- Un riesgo Nivel 2 afecta documentos maestros, seguridad, fases o fuente de verdad.

---

# CRITERIOS DE ACEPTACIÓN

Este documento podrá considerarse listo para aprobación si:

- Define flujos claros entre componentes.
- Usa los modelos de DATA_MODEL_SPEC v0.1.
- Respeta COMPONENTS_SPEC v0.2.
- Respeta SECURITY_RULES.
- Respeta CONTEXT_MASTER v0.5.
- Respeta PHASES v0.5.
- Mantiene a Robert en Fase 10.
- No autoriza programación.
- No autoriza base de datos real.
- No autoriza conexiones externas.
- No autoriza automatizaciones.
- No autoriza agentes autónomos.
- Incluye reglas de pausa, bloqueo y aprobación.
- Aclara el rol de AppShell.
- Declara qué reciben TopBar y LeftSidebar.
- Usa ComponentState en un flujo explícito.
- Integra GitHubBackupStatus y ObsidianGraphStatus en datos que fluyen.
- Define cómo manejar riesgo Nivel 2.
- Define cuándo SystemState debe actualizarse.
- Mantiene control total del usuario.

---

# RIESGO DEL DOCUMENTO

Tipo de cambio:

**Cambio técnico documental / flujo conceptual de interacción**

Nivel de riesgo inicial:

**Nivel 3 — Alto**

Motivo:

Este documento define cómo interactuarían conceptualmente los componentes del MVP técnico básico. Aunque no programa nada, acerca el proyecto a una futura implementación técnica.

Nivel de riesgo final esperado:

**Nivel 2 — Medio**

Motivo de reducción:

El documento es conceptual, no crea código, no conecta herramientas externas, no automatiza acciones y no ejecuta nada.

Nivel de autonomía:

**Nivel 0 — Sin autonomía ejecutiva**

---

# DECISIÓN PENDIENTE

Este documento queda como:

**Propuesta corregida pendiente de revisión**

Para aprobarlo formalmente, el usuario deberá escribir:

**APRUEBO ROBERT_TECHNICAL_INTERACTION_FLOW_SPEC v0.2**

---

# EFECTO DE UNA APROBACIÓN FUTURA

Si se aprueba este documento, se deberá:

1. Registrar decisión formal en ROBERT_DECISIONS_LOG.
2. Registrar cambio en ROBERT_CONTROL_DE_CAMBIOS.
3. Actualizar ROBERT_HOME.
4. Actualizar README si aplica.
5. Mantenerlo como base para futuras especificaciones técnicas.
6. No pasar automáticamente a programación.
7. No avanzar automáticamente a Fase 11.

---

# PRÓXIMO PASO RECOMENDADO

Después de revisar este documento, el siguiente documento posible sería:

**ROBERT_TECHNICAL_SCREEN_STATE_SPEC**

Ese documento definiría qué información aparece en cada pantalla o panel del MVP técnico básico.

No debe crearse hasta revisar o aprobar INTERACTION_FLOW_SPEC.

---

# CIERRE

ROBERT_TECHNICAL_INTERACTION_FLOW_SPEC v0.2 corrige la versión v0.1 y define con más precisión los flujos conceptuales de interacción entre los componentes principales del MVP técnico básico de Robert.

Este documento aclara cómo Robert recibiría instrucciones, evaluaría riesgo, pediría aprobación, registraría decisiones, actualizaría documentos, mostraría estado y representaría componentes.

Robert sigue en modo documental, manual y supervisado.

El usuario mantiene control total.

Robert no ejecuta acciones importantes sin permiso.
