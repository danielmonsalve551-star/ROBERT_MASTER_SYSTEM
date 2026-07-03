# ROBERT_TECHNICAL_INTERACTION_FLOW_SPEC

Versión: 0.1  
Estado: Borrador técnico documental nuevo — pendiente de revisión  
Fecha: 02/07/2026  
Ubicación: 10_MVP  
Fase relacionada: Fase 10 — MVP técnico básico en preparación  
Documento base relacionado: ROBERT_TECHNICAL_DATA_MODEL_SPEC v0.1  
Documento relacionado: ROBERT_TECHNICAL_COMPONENTS_SPEC v0.2  
Fuente de verdad actual: ROBERT_CONTEXT_MASTER v0.5  

---

Tags: #robert/orbita-3 #capa/5 #tipo/tecnico #robert/mvp #robert/interaction-flow

[[ROBERT_HOME]]
[[ROBERT_TECHNICAL_COMPONENTS_SPEC]]
[[ROBERT_TECHNICAL_DATA_MODEL_SPEC]]
[[ROBERT_TECHNICAL_MVP_WIREFRAME]]
[[ROBERT_SECURITY_RULES]]

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
- Convención visual de Obsidian validada.
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
9. Robert actualiza el estado documental.
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
CommandCenter  
↓  
ModeSelector  
↓  
RiskBadge  
↓  
ApprovalGate  
↓  
DecisionInbox si aplica  
↓  
Robert prepara respuesta o borrador  
↓  
Usuario aprueba, corrige, pausa o rechaza  
↓  
DecisionRecord si aplica  
↓  
ChangeRecord si aplica  
↓  
RobertDocument se actualiza  
↓  
SystemState se actualiza  
↓  
CurrentStatePanel y DocumentStatusMap muestran el estado actualizado  

Este flujo es conceptual.

No implica programación ni ejecución real en esta etapa.

---

# FLUJO 1 — INSTRUCCIÓN DEL USUARIO

## Objetivo

Definir qué pasa cuando el usuario escribe una instrucción dentro de Robert.

## Flujo conceptual

1. El usuario escribe una instrucción.
2. CommandCenter recibe la instrucción.
3. CommandCenter crea un CommandRequest.
4. ModeSelector identifica el modo activo.
5. RiskBadge evalúa el nivel de riesgo.
6. ApprovalGate determina si se necesita autorización.
7. Si no requiere aprobación, Robert puede preparar una respuesta.
8. Si requiere aprobación, se crea una PendingDecision.
9. DecisionInbox muestra la decisión pendiente.
10. Robert espera instrucción del usuario.

## Componentes involucrados

- CommandCenter
- ModeSelector
- RiskBadge
- ApprovalGate
- DecisionInbox
- CurrentStatePanel

## Modelos utilizados

- CommandRequest
- ModeState
- RiskRecord
- PendingDecision
- SystemState

## Regla de seguridad

Si la instrucción implica riesgo medio, alto o crítico, Robert debe pausar y pedir autorización.

---

# FLUJO 2 — COMANDO DOCUMENTAL SIMPLE

## Objetivo

Definir qué pasa cuando el usuario pide crear, revisar o actualizar un documento sin ejecución real.

## Ejemplo de instrucción

crea un documento técnico

## Flujo conceptual

1. CommandCenter recibe la instrucción.
2. Robert clasifica la intención como cambio documental.
3. RiskBadge asigna nivel de riesgo.
4. ApprovalGate revisa si el cambio requiere aprobación.
5. Robert prepara el documento como borrador.
6. El documento queda representado como RobertDocument.
7. Si el usuario confirma que lo creó, se registra ChangeRecord.
8. CurrentStatePanel actualiza el estado.
9. DocumentStatusMap refleja el nuevo documento.

## Componentes involucrados

- CommandCenter
- RiskBadge
- ApprovalGate
- CurrentStatePanel
- DocumentStatusMap

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
10. CurrentStatePanel y DocumentStatusMap reflejan el nuevo estado.

## Componentes involucrados

- CommandCenter
- RiskBadge
- ApprovalGate
- DecisionInbox
- CurrentStatePanel
- DocumentStatusMap

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

## Componentes involucrados

- CommandCenter
- RiskBadge
- ApprovalGate
- DecisionInbox

## Modelos utilizados

- CommandRequest
- RiskRecord
- PendingDecision
- ModeState

## Escala aplicada

- Nivel 0 — Informativo
- Nivel 1 — Bajo
- Nivel 2 — Medio
- Nivel 3 — Alto
- Nivel 4 — Crítico

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

## Componentes involucrados

- CommandCenter
- ModeSelector
- RiskBadge
- ApprovalGate
- DecisionInbox
- CurrentStatePanel

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
6. TopBar puede mostrar la fase y modo actual.
7. LeftSidebar mantiene navegación documental.

## Componentes involucrados

- CurrentStatePanel
- DocumentStatusMap
- TopBar
- LeftSidebar

## Modelos utilizados

- SystemState
- RobertDocument
- DecisionRecord
- ChangeRecord

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

## Componentes involucrados

- ApprovalGate
- DecisionInbox
- CommandCenter
- CurrentStatePanel

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

## Componentes involucrados

- DocumentStatusMap
- CurrentStatePanel
- LeftSidebar
- TopBar

## Modelos utilizados

- RobertDocument
- SystemState
- ChangeRecord
- DecisionRecord

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

## Componentes involucrados

- ModeSelector
- CommandCenter
- RiskBadge
- ApprovalGate
- CurrentStatePanel

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
7. Robert no ejecuta acciones externas.

## Componentes involucrados

- CommandCenter
- RiskBadge
- ApprovalGate
- CurrentStatePanel

## Modelos utilizados

- CommandRequest
- RiskRecord
- ModeState
- SystemState

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
6. Robert no sincroniza automáticamente.

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
4. Las órbitas representan cercanía al núcleo.
5. Los colores representan capa o función.
6. DocumentStatusMap puede usar esta lógica como referencia visual.
7. Robert no depende del grafo para ejecutar acciones.

## Componentes involucrados

- DocumentStatusMap
- CurrentStatePanel
- LeftSidebar

## Modelos utilizados

- ObsidianGraphStatus
- RobertDocument
- SystemState

## Regla de seguridad

Obsidian Graph View funciona como navegación documental.

No es el HUD final de Robert.

No ejecuta acciones.

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

---

# DATOS QUE FLUYEN ENTRE COMPONENTES

## CommandCenter envía

- user_input
- recognized_command
- classified_intent
- document_affected
- risk_level preliminar

## ModeSelector envía

- active_mode
- restricted_modes
- execution_allowed
- automation_allowed
- external_actions_allowed

## RiskBadge envía

- risk_level
- risk_reason
- recommended_action
- blocking_required

## ApprovalGate envía

- approval_required
- approval_status
- blocked_reason
- next_allowed_action

## DecisionInbox envía

- pending_id
- title
- options_available
- recommended_option
- current_status

## DocumentStatusMap envía

- document_name
- document_status
- version
- decision_related
- change_related

## CurrentStatePanel envía

- current_phase
- active_mode
- last_decision
- last_change
- execution_status

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

# CRITERIOS DE ACEPTACIÓN

Este documento podrá considerarse listo para revisión si:

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

**Borrador técnico documental pendiente de revisión**

Para aprobarlo formalmente, el usuario deberá escribir:

**APRUEBO ROBERT_TECHNICAL_INTERACTION_FLOW_SPEC v0.1**

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

ROBERT_TECHNICAL_INTERACTION_FLOW_SPEC v0.1 define los flujos conceptuales de interacción entre los componentes principales del MVP técnico básico de Robert.

Este documento explica cómo Robert recibiría instrucciones, evaluaría riesgo, pediría aprobación, registraría decisiones, actualizaría documentos y mostraría estado.

Robert sigue en modo documental, manual y supervisado.

El usuario mantiene control total.

Robert no ejecuta acciones importantes sin permiso.
