# ROBERT_TECHNICAL_SESSION_AND_CONTEXT_SPEC

Versión: 0.2  
Estado: Propuesta corregida — pendiente de revisión  
Fecha: 06/07/2026  
Ubicación: 10_MVP  
Fase relacionada: Fase 10 — MVP técnico básico en preparación  
Documento base principal: ROBERT_TECHNICAL_NOTIFICATION_AND_ALERTS_SPEC v0.2  
Documentos relacionados: ROBERT_COMMANDS v0.4, ROBERT_TECHNICAL_AUDIT_TRAIL_SPEC v0.2, ROBERT_TECHNICAL_PERMISSIONS_AND_SCOPES_SPEC v0.2, ROBERT_TECHNICAL_ERROR_AND_BLOCKING_SPEC v0.2, ROBERT_TECHNICAL_USER_ACTIONS_SPEC v0.2, ROBERT_TECHNICAL_DATA_MODEL_SPEC v0.1, ROBERT_TECHNICAL_COMPONENTS_SPEC v0.2, ROBERT_TECHNICAL_SCREEN_STATE_SPEC v0.2, ROBERT_TECHNICAL_INTERACTION_FLOW_SPEC v0.2  
Documentos sandbox relacionados: ROBERT_SANDBOX, SANDBOX_RULES, SANDBOX_TESTS, SANDBOX_RESULTS  
Fuente de verdad actual: ROBERT_CONTEXT_MASTER v0.5  

Tags: #robert/orbita-3 #capa/5 #tipo/tecnico #robert/mvp #robert/session-context

---

# OBJETIVO

ROBERT_TECHNICAL_SESSION_AND_CONTEXT_SPEC define cómo Robert debe manejar contexto de sesión, continuidad, pausas, reanudaciones, estado conversacional, memoria documental y recuperación del hilo dentro del MVP técnico básico.

Su objetivo es responder:

- Qué es una sesión de trabajo.
- Qué es contexto activo.
- Qué información debe recordarse durante una sesión.
- Qué información debe recuperarse al reanudar.
- Qué pasa cuando el usuario dice “ya”.
- Qué pasa cuando el usuario pausa.
- Qué pasa cuando el usuario vuelve después de tiempo.
- Qué documentos están activos.
- Qué decisión está pendiente.
- Qué cambio está pendiente.
- Qué bloque está abierto.
- Qué bloque está cerrado.
- Qué siguiente paso está permitido.
- Qué no debe asumirse.
- Qué no debe ejecutarse.
- Qué eventos se conectan con continuidad y pausa.
- Qué componente muestra el contexto activo.
- Qué modelo conceptual representa el estado de sesión.

Este documento no crea memoria real automática.

Este documento no crea base de datos real.

Este documento no crea sistema real de sesiones.

Este documento no crea recuperación automática real.

Este documento no crea sincronización real entre herramientas.

Este documento no programa la app.

Este documento no conecta herramientas externas.

Este documento no ejecuta acciones reales.

---

# ESTADO DEL DOCUMENTO

Este documento queda como:

**Propuesta corregida — pendiente de revisión**

No está aprobado todavía.

No reemplaza a ningún documento maestro.

No autoriza programación.

No autoriza prototipo funcional.

No autoriza pantallas reales.

No autoriza memoria real automática.

No autoriza base de datos real.

No autoriza sistema real de sesiones.

No autoriza conexiones externas.

No autoriza automatizaciones.

No autoriza agentes autónomos.

No autoriza ejecución real.

No autoriza avanzar a Fase 11.

---

# CORRECCIONES APLICADAS EN v0.2

La versión v0.2 corrige los siguientes puntos detectados durante la revisión de v0.1:

1. Se agrega **REGISTRO 2 — Comando** a TIPO 1 — Sesión informativa.
2. Se agrega **REGISTRO 2 — Comando** a TIPO 3 — Sesión de corrección.
3. Se agrega **REGISTRO 11 — Riesgo** a TIPO 13 — Sesión de revisión crítica.
4. Se agrega **REGISTRO 11 — Riesgo** a TIPO 10 — Sesión de bloqueo cuando el bloqueo nace de riesgo detectado.
5. Se aclara que no se crea **TIPO 18 — Sesión de respaldo manual**.
6. Se confirma que el respaldo manual se absorbe dentro de **TIPO 15 — Sesión de cierre de bloque**.
7. Se corrige TIPO 10 para separar riesgo numérico de acción de control fuera de la escala.
8. Se refuerza la relación con AUDIT_TRAIL_SPEC v0.2.
9. Se mantiene que las acciones de control están fuera de la escala de riesgo.
10. Se mantiene que Nivel 0 es únicamente Informativo.

Este documento sigue sin estar aprobado.

---

# REGLA CENTRAL

Robert debe mantener continuidad sin inventar contexto.

Regla principal:

**Robert puede continuar desde el último estado conocido, pero no puede asumir acciones no confirmadas por el usuario.**

---

# REGLA DE ALINEACIÓN DOCUMENTAL

SESSION_AND_CONTEXT_SPEC v0.2 debe mantenerse alineado con:

- ROBERT_COMMANDS v0.4
- ROBERT_TECHNICAL_NOTIFICATION_AND_ALERTS_SPEC v0.2
- ROBERT_TECHNICAL_AUDIT_TRAIL_SPEC v0.2
- ROBERT_TECHNICAL_PERMISSIONS_AND_SCOPES_SPEC v0.2
- ROBERT_TECHNICAL_ERROR_AND_BLOCKING_SPEC v0.2
- ROBERT_TECHNICAL_USER_ACTIONS_SPEC v0.2
- ROBERT_TECHNICAL_DATA_MODEL_SPEC v0.1
- ROBERT_TECHNICAL_COMPONENTS_SPEC v0.2
- ROBERT_TECHNICAL_SCREEN_STATE_SPEC v0.2
- ROBERT_TECHNICAL_INTERACTION_FLOW_SPEC v0.2
- ROBERT_CONTEXT_MASTER v0.5
- ROBERT_SECURITY_RULES
- ROBERT_PHASES
- ROBERT_SANDBOX
- SANDBOX_RULES
- SANDBOX_TESTS
- SANDBOX_RESULTS

Regla:

**SESSION_AND_CONTEXT_SPEC no debe inventar nuevos modelos oficiales, nuevos componentes oficiales, nuevas capacidades activas, nueva memoria autónoma, nueva sincronización real ni nueva lógica de autonomía que no exista en los documentos base.**

Si una función de contexto requiere base de datos real, memoria persistente automática, conexión externa, automatización o agente autónomo, debe bloquearse en Fase 10.

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
- ROBERT_COMMANDS v0.4 aprobado e integrado.
- ROBERT_TECHNICAL_MVP_PLAN aprobado.
- ROBERT_TECHNICAL_MVP_WIREFRAME v0.3 aprobado.
- ROBERT_TECHNICAL_COMPONENTS_SPEC v0.2 aprobado.
- ROBERT_TECHNICAL_DATA_MODEL_SPEC v0.1 aprobado e integrado.
- ROBERT_TECHNICAL_INTERACTION_FLOW_SPEC v0.2 aprobado e integrado.
- ROBERT_TECHNICAL_SCREEN_STATE_SPEC v0.2 aprobado e integrado.
- ROBERT_TECHNICAL_USER_ACTIONS_SPEC v0.2 aprobado e integrado.
- ROBERT_TECHNICAL_ERROR_AND_BLOCKING_SPEC v0.2 aprobado e integrado.
- ROBERT_TECHNICAL_PERMISSIONS_AND_SCOPES_SPEC v0.2 aprobado e integrado.
- ROBERT_TECHNICAL_AUDIT_TRAIL_SPEC v0.2 aprobado e integrado.
- ROBERT_TECHNICAL_NOTIFICATION_AND_ALERTS_SPEC v0.2 aprobado e integrado.
- ROBERT_TECHNICAL_SESSION_AND_CONTEXT_SPEC v0.2 creado como propuesta corregida pendiente de revisión.
- Sin programación autorizada.
- Sin código real.
- Sin botones reales.
- Sin pantallas reales.
- Sin memoria real automática.
- Sin sistema real de sesiones.
- Sin base de datos real.
- Sin conexiones externas.
- Sin automatizaciones reales.
- Sin agentes autónomos activos.

---

# ALCANCE AUTORIZADO

Este documento autoriza únicamente:

- Definir sesión conceptual.
- Definir contexto activo conceptual.
- Definir continuidad documental.
- Definir pausa conceptual.
- Definir reanudación conceptual.
- Definir recuperación del hilo.
- Definir interpretación de respuestas cortas como “ya”.
- Definir relación entre sesión y modelos existentes.
- Definir relación entre sesión y componentes visuales conceptuales.
- Definir relación entre sesión, permisos, auditoría, notificaciones, acciones y eventos.
- Mantener a Robert en modo documental, manual y supervisado.

---

# ALCANCE NO AUTORIZADO

Este documento no autoriza:

- Programar la app.
- Crear código real.
- Crear sistema real de sesiones.
- Crear memoria automática real.
- Crear base de datos real.
- Crear tabla real de sesión.
- Crear modelo SessionRecord.
- Crear modelo ContextSnapshot.
- Crear modelo ConversationState.
- Crear componente SessionPanel.
- Crear componente ContextTimeline.
- Crear botones reales.
- Crear pantallas reales.
- Crear prototipo funcional.
- Crear endpoints.
- Conectar Supabase.
- Conectar Firebase.
- Conectar GitHub automáticamente.
- Conectar Obsidian automáticamente.
- Conectar Gmail.
- Conectar Google Calendar.
- Conectar APIs externas.
- Automatizar recuperación de contexto.
- Activar agentes autónomos.
- Ejecutar acciones reales.
- Avanzar automáticamente a Fase 11.

---

# DEFINICIÓN DE SESIÓN

Una sesión es un periodo de trabajo donde el usuario y Robert avanzan sobre un bloque, documento, decisión, prueba o flujo específico.

Una sesión puede incluir:

- Documento activo.
- Bloque activo.
- Estado actual.
- Última acción confirmada.
- Próximo paso pendiente.
- Decisión pendiente.
- Cambio pendiente.
- Restricciones activas.
- Permiso vigente.
- Alcance vigente.
- Evento activo.
- Aviso activo.

---

# DEFINICIÓN DE CONTEXTO ACTIVO

Contexto activo es la información mínima que Robert necesita para continuar correctamente sin perder el hilo.

Incluye:

- Fase actual.
- Documento activo.
- Estado del documento.
- Último cambio registrado.
- Última decisión registrada.
- Siguiente paso esperado.
- Si el usuario ya confirmó una acción.
- Si falta actualizar HOME.
- Si falta actualizar README.
- Si falta registrar DECISIÓN.
- Si falta registrar CAMBIO.
- Si el bloque está abierto o cerrado.
- Si hay pausa o bloqueo activo.

---

# DEFINICIÓN DE CONTINUIDAD

Continuidad significa que Robert puede seguir el flujo correcto después de que el usuario confirma un paso, vuelve más tarde o responde con una palabra corta.

Ejemplo:

```text
Usuario: ya
```

Robert debe interpretar “ya” según el último paso solicitado.

Si el último paso fue:

```text
Cuando termines dime: ya registré CAMBIO 036
```

entonces “ya” significa:

```text
El usuario registró CAMBIO 036.
```

Regla:

**“Ya” solo confirma el último paso indicado por Robert. No confirma pasos futuros.**

---

# DEFINICIÓN DE PAUSA

Pausa significa detener avance hasta que el usuario indique nuevo alcance.

Puede ocurrir por:

- PAUSA.
- DETENTE.
- NO_AVANCES.
- NO_SIGAS.
- NO_EJECUTES.
- Bloqueo manual solicitado.
- Falta de información.
- Contradicción documental.
- Riesgo crítico.
- Fase incorrecta.

Regla:

**Pausa reduce alcance. No aumenta riesgo.**

---

# DEFINICIÓN DE REANUDACIÓN

Reanudación significa continuar desde el último estado confirmado.

Antes de reanudar, Robert debe identificar:

- Último bloque activo.
- Último paso confirmado.
- Documento activo.
- Estado del documento.
- Decisión pendiente.
- Cambio pendiente.
- Próximo paso permitido.
- Restricciones activas.

Regla:

**Robert no debe saltar pasos al reanudar.**

---

# SESSION AND CONTEXT NO ES MODELO NUEVO OFICIAL

En esta versión, los conceptos:

- Session
- Context
- Context Snapshot
- Conversation State

no crean modelos nuevos oficiales.

Son estructuras conceptuales derivadas de modelos ya existentes en DATA_MODEL_SPEC v0.1.

Regla:

**SESSION_AND_CONTEXT_SPEC v0.2 no crea los modelos SessionRecord, ContextSnapshot ni ConversationState.**

Si en el futuro se decide crear modelos oficiales como:

```text
SessionRecord
ContextSnapshot
ConversationState
```

primero deberá corregirse y aprobarse:

```text
ROBERT_TECHNICAL_DATA_MODEL_SPEC
```

---

# SESSION AND CONTEXT NO CREA COMPONENTE NUEVO OFICIAL

En esta versión, Session and Context no crea componentes nuevos.

Regla:

**SESSION_AND_CONTEXT_SPEC v0.2 no crea SessionPanel ni ContextTimeline.**

Si en el futuro se decide crear componentes oficiales como:

```text
SessionPanel
ContextTimeline
```

primero deberá corregirse y aprobarse:

```text
ROBERT_TECHNICAL_COMPONENTS_SPEC
```

---

# RELACIÓN CON DATA_MODEL_SPEC v0.1

Este documento se apoya en los 11 modelos existentes de DATA_MODEL_SPEC v0.1.

Session and Context debe entenderse como una vista conceptual construida con esos modelos.

---

## 1. SystemState

SystemState representa el estado general de la sesión.

Puede reflejar:

- Fase activa.
- Modo activo.
- Estado actual.
- Bloque abierto.
- Bloque cerrado.
- Pausa activa.
- Restricción activa.
- Próximo paso permitido.
- Última acción confirmada.

Uso en este documento:

SystemState es el modelo principal para representar contexto activo.

---

## 2. RobertDocument

RobertDocument identifica el documento activo o relacionado con la sesión.

Puede reflejar:

- Documento en revisión.
- Documento corregido.
- Documento aprobado.
- Documento pendiente.
- Documento actualizado.
- Documento que falta actualizar.
- Documento bloqueado.

Uso en este documento:

Toda sesión documental debe indicar qué RobertDocument está activo.

---

## 3. DecisionRecord

DecisionRecord representa decisiones formales tomadas o pendientes de registrar.

Puede reflejar:

- Última decisión registrada.
- Decisión pendiente.
- Aprobación formal.
- Rechazo.
- Pausa formal.
- Decisión de no avanzar.

Uso en este documento:

Si la sesión gira alrededor de una aprobación o decisión, debe conectarse con DecisionRecord.

---

## 4. ChangeRecord

ChangeRecord representa cambios realizados o pendientes.

Puede reflejar:

- Último cambio registrado.
- Cambio pendiente.
- Corrección aplicada.
- Integración aprobada.
- Actualización de HOME.
- Actualización de README.
- Cambio de estado.

Uso en este documento:

La continuidad debe saber si falta registrar cambio o si el cambio ya fue confirmado.

---

## 5. RiskRecord

RiskRecord representa riesgo activo en la sesión.

Puede reflejar:

- Riesgo inicial.
- Riesgo final.
- Riesgo crítico.
- Riesgo reducido.
- Riesgo por falta de permiso.
- Riesgo por fase incorrecta.
- Riesgo por contradicción.

Uso en este documento:

Si el contexto activo tiene riesgo, Robert debe mantenerlo visible hasta resolverlo.

---

## 6. CommandRequest

CommandRequest representa la última instrucción del usuario.

Puede reflejar:

- Comando actual.
- Comando de control.
- Confirmación corta.
- Solicitud de corrección.
- Solicitud de aprobación.
- Solicitud de crear documento.
- Solicitud de pausar.
- Solicitud de reanudar.

Uso en este documento:

Cada paso de continuidad parte de la última solicitud o confirmación del usuario.

---

## 7. PendingDecision

PendingDecision representa una decisión pendiente en la sesión.

Puede reflejar:

- Documento pendiente de aprobación.
- Confirmación pendiente.
- Falta de información.
- Alcance ambiguo.
- Permiso insuficiente.
- Siguiente paso pendiente.

Uso en este documento:

Si existe PendingDecision, Robert no debe avanzar como si ya estuviera resuelta.

---

## 8. ModeState

ModeState representa el modo operativo de la sesión.

Puede reflejar:

- Manual.
- Supervisado.
- Sandbox.
- Pausado.
- Restringido.
- Modo futuro no disponible.

Uso en este documento:

La continuidad depende del modo activo. Robert no debe asumir autonomía real.

---

## 9. ComponentState

ComponentState representa qué componente muestra el estado de sesión.

Puede reflejar:

- TopBar mostrando fase y modo.
- CurrentStatePanel mostrando contexto activo.
- DecisionInbox mostrando pendiente.
- ApprovalGate mostrando bloqueo.
- RiskBadge mostrando riesgo.
- DocumentStatusMap mostrando documento activo.
- CommandCenter mostrando último comando.

Uso en este documento:

El contexto activo debe poder mostrarse en componentes ya aprobados.

---

## 10. GitHubBackupStatus

GitHubBackupStatus representa respaldo manual relacionado con la sesión.

Puede reflejar:

- Commit sugerido.
- Commit confirmado.
- GitHub actualizado manualmente.
- Respaldo pendiente.
- GitHub no conectado automáticamente.

Uso en este documento:

Cuando el usuario dice “ya”, puede confirmar un respaldo manual si ese era el último paso solicitado.

---

## 11. ObsidianGraphStatus

ObsidianGraphStatus representa estado documental visual en Obsidian.

Puede reflejar:

- Documento en órbita correcta.
- Tag correcto.
- Relación documental visible.
- Documento pendiente de ubicar.
- Grafo actualizado manualmente.
- Estado visual pendiente.

Uso en este documento:

La sesión puede incluir cambios visuales o documentales en Obsidian, pero no automatizarlos.

---

# MAPEO CONCEPTUAL DE SESIÓN Y CONTEXTO A MODELOS EXISTENTES

| Elemento de sesión/contexto | Modelo relacionado | Uso |
|---|---|---|
| Estado actual | SystemState | Refleja fase, modo y bloque activo |
| Documento activo | RobertDocument | Identifica archivo o área actual |
| Último comando | CommandRequest | Captura la instrucción del usuario |
| Confirmación corta | CommandRequest / SystemState | Interpreta “ya” según último paso |
| Decisión pendiente | PendingDecision | Mantiene aprobación o aclaración pendiente |
| Decisión registrada | DecisionRecord | Confirma decisión formal |
| Cambio registrado | ChangeRecord | Confirma cambio formal |
| Riesgo activo | RiskRecord | Mantiene riesgo visible |
| Modo activo | ModeState | Manual, supervisado o sandbox |
| Estado visual | ComponentState | Muestra contexto en interfaz conceptual |
| Respaldo manual | GitHubBackupStatus | Confirma commit o actualización manual |
| Estado Obsidian | ObsidianGraphStatus | Refleja grafo, tags u órbitas |

---

# COMPONENTES PARTICIPANTES

Este documento usa los componentes aprobados en COMPONENTS_SPEC v0.2:

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

# ROL DE CADA COMPONENTE EN SESIÓN Y CONTEXTO

## AppShell

AppShell contiene la vista general de la sesión.

No crea sesión real.

No guarda memoria real.

No ejecuta acciones.

---

## TopBar

TopBar muestra el resumen persistente del contexto.

Puede mostrar:

- Fase activa.
- Modo activo.
- Pausa activa.
- Bloqueo activo.
- Documento activo.
- Respaldo manual pendiente.
- Siguiente paso general.

Ejemplo:

```text
Fase 10 | Modo supervisado | Documento activo: SESSION_AND_CONTEXT_SPEC | Estado: borrador
```

---

## LeftSidebar

LeftSidebar muestra navegación documental dentro del contexto.

Puede mostrar:

- Carpeta activa.
- Documento activo.
- Documento relacionado.
- Documento pendiente.
- Documento aprobado.
- Documento bloqueado.

---

## CommandCenter

CommandCenter recibe la instrucción del usuario.

Puede mostrar:

- Último comando.
- Confirmación corta.
- Solicitud de reanudación.
- Solicitud de pausa.
- Solicitud de corrección.
- Solicitud de aprobación.
- Falta de información.

---

## ModeSelector

ModeSelector muestra el modo operativo del contexto.

Puede mostrar:

- Manual.
- Supervisado.
- Sandbox.
- Pausado.
- Restringido.
- Modo futuro no disponible.

---

## RiskBadge

RiskBadge muestra riesgo activo del contexto.

Puede mostrar:

- Riesgo del documento.
- Riesgo del paso actual.
- Riesgo de avanzar sin permiso.
- Riesgo crítico.
- Riesgo reducido por mantenerlo documental.

---

## ApprovalGate

ApprovalGate valida si la sesión puede avanzar.

Puede mostrar:

- Aprobación requerida.
- Permiso insuficiente.
- Alcance excedido.
- Pausa obligatoria.
- Bloqueo manual.
- Falta de información.
- Decisión pendiente.

---

## DecisionInbox

DecisionInbox muestra decisiones pendientes o resueltas.

Puede mostrar:

- Documento pendiente de aprobación.
- Decisión pendiente.
- Decisión registrada.
- Aprobación pendiente.
- Pausa pendiente.
- Siguiente decisión esperada.

---

## DocumentStatusMap

DocumentStatusMap muestra el estado de documentos dentro de la sesión.

Puede mostrar:

- Documento activo.
- Documento corregido.
- Documento aprobado.
- HOME actualizado.
- README actualizado.
- Cambio registrado.
- Documento pendiente.

---

## CurrentStatePanel

CurrentStatePanel muestra el contexto completo de la sesión.

Debe mostrar:

- Qué estamos haciendo.
- En qué fase estamos.
- Qué documento está activo.
- Qué versión está activa.
- Qué paso se completó.
- Qué paso falta.
- Qué decisión está pendiente.
- Qué cambio está pendiente.
- Qué riesgo existe.
- Qué permiso aplica.
- Qué alcance aplica.
- Qué sigue.

---

# DÓNDE SE MUESTRA CADA ELEMENTO DE CONTEXTO

| Elemento | Componente principal | Componentes relacionados |
|---|---|---|
| Fase activa | TopBar | CurrentStatePanel |
| Modo activo | ModeSelector | TopBar |
| Documento activo | DocumentStatusMap | LeftSidebar |
| Último comando | CommandCenter | CurrentStatePanel |
| Confirmación “ya” | CommandCenter | CurrentStatePanel |
| Decisión pendiente | DecisionInbox | ApprovalGate |
| Cambio pendiente | DocumentStatusMap | CurrentStatePanel |
| Pausa activa | TopBar | ApprovalGate |
| Bloqueo activo | ApprovalGate | RiskBadge |
| Riesgo activo | RiskBadge | CurrentStatePanel |
| Siguiente paso | CurrentStatePanel | CommandCenter |
| Respaldo manual | TopBar | GitHubBackupStatus conceptualmente |
| Estado visual documental | DocumentStatusMap | ObsidianGraphStatus conceptualmente |

---

# TIPOS DE ESTADO DE SESIÓN

Robert puede manejar estos tipos conceptuales:

1. Sesión informativa.
2. Sesión documental activa.
3. Sesión de corrección.
4. Sesión de aprobación.
5. Sesión de integración.
6. Sesión de registro.
7. Sesión de actualización HOME.
8. Sesión de actualización README.
9. Sesión de pausa.
10. Sesión de bloqueo.
11. Sesión de decisión pendiente.
12. Sesión de sandbox manual.
13. Sesión de revisión crítica.
14. Sesión de recuperación de hilo.
15. Sesión de cierre de bloque.
16. Sesión con falta de información.
17. Sesión con capacidad futura no disponible.

Todos los tipos deben usar una estructura uniforme.

---

# ESTRUCTURA UNIFORME DE LOS 17 TIPOS

Cada tipo debe incluir:

```text
Qué representa:
Cuándo ocurre:
Riesgo típico:
Modelo principal:
Componente principal:
Evento relacionado:
Notificación relacionada:
Registro de auditoría relacionado:
Acción esperada del usuario:
Restricción:
```

---

# TIPO 1 — SESIÓN INFORMATIVA

## Qué representa

Una sesión donde Robert solo explica, resume o muestra estado.

## Cuándo ocurre

Cuando el usuario pide:

- RESUMEN.
- Estado.
- Explicación.
- Siguiente paso informativo.

## Riesgo típico

Nivel 0 — Informativo.

## Modelo principal

SystemState.

## Componente principal

CurrentStatePanel.

## Evento relacionado

Ninguno obligatorio.

## Notificación relacionada

TIPO 1 — Notificación informativa.

## Registro de auditoría relacionado

REGISTRO 1 — Informativo.

REGISTRO 2 — Comando, cuando la sesión informativa nace de una solicitud directa del usuario, como RESUMEN, estado, explicación o siguiente paso.

## Acción esperada del usuario

Leer o elegir si quiere avanzar.

## Restricción

No modifica documentos.

No registra decisiones.

No registra cambios.

---

# TIPO 2 — SESIÓN DOCUMENTAL ACTIVA

## Qué representa

Una sesión enfocada en un documento activo.

## Cuándo ocurre

Cuando Robert está creando, revisando, corrigiendo o preparando un documento.

## Riesgo típico

Nivel 1 a Nivel 3 según el documento.

## Modelo principal

RobertDocument.

## Componente principal

DocumentStatusMap.

## Evento relacionado

EVENTO 3 si requiere aprobación.

EVENTO 12 si la acción sale del alcance.

## Notificación relacionada

TIPO 2 — Notificación de estado.

## Registro de auditoría relacionado

REGISTRO 4 — Borrador.

REGISTRO 5 — Corrección si aplica.

## Acción esperada del usuario

Confirmar creación, revisión, corrección o pausa.

## Restricción

Documento activo no significa documento aprobado.

---

# TIPO 3 — SESIÓN DE CORRECCIÓN

## Qué representa

Una sesión donde se corrige un documento o sección.

## Cuándo ocurre

Cuando el usuario dice:

- Corrígelo.
- Arregla esto.
- Actualízalo a v0.2.
- Corrige el documento.

## Riesgo típico

Nivel 2 o Nivel 3.

## Modelo principal

ChangeRecord.

## Componente principal

DocumentStatusMap.

## Evento relacionado

EVENTO 3 si requiere aprobación.

EVENTO 10 si corrige contradicción documental.

## Notificación relacionada

TIPO 5 — Advertencia de riesgo.

TIPO 13 — Aviso de cambio registrado.

## Registro de auditoría relacionado

REGISTRO 2 — Comando, porque la corrección nace de una solicitud directa del usuario.

REGISTRO 5 — Corrección.

## Acción esperada del usuario

Aplicar corrección manual y confirmar.

## Restricción

Corregir no significa aprobar.

---

# TIPO 4 — SESIÓN DE APROBACIÓN

## Qué representa

Una sesión donde el usuario aprueba formalmente un documento.

## Cuándo ocurre

Cuando el usuario dice:

- Apruebo.
- Aprobado.
- APRUEBO [documento].

## Riesgo típico

Nivel 3 — Alto.

## Modelo principal

DecisionRecord.

## Componente principal

ApprovalGate.

## Evento relacionado

EVENTO 3 — Aprobación formal requerida.

## Notificación relacionada

TIPO 6 — Confirmación requerida.

TIPO 14 — Aviso de decisión registrada.

## Registro de auditoría relacionado

REGISTRO 8 — Aprobación.

REGISTRO 6 — Decisión.

## Acción esperada del usuario

Registrar decisión formal.

## Restricción

Aprobar documento no autoriza programación.

---

# TIPO 5 — SESIÓN DE INTEGRACIÓN

## Qué representa

Una sesión donde un documento aprobado se integra al estado actual.

## Cuándo ocurre

Después de una aprobación formal y su decisión registrada.

## Riesgo típico

Nivel 3 — Alto.

## Modelo principal

ChangeRecord.

## Componente principal

CurrentStatePanel.

## Evento relacionado

EVENTO 3 si falta aprobación previa.

EVENTO 12 si la integración supera alcance.

## Notificación relacionada

TIPO 13 — Aviso de cambio registrado.

## Registro de auditoría relacionado

REGISTRO 9 — Integración.

## Acción esperada del usuario

Registrar cambio, actualizar HOME y README si aplica.

## Restricción

Integración documental no equivale a implementación técnica real.

---

# TIPO 6 — SESIÓN DE REGISTRO

## Qué representa

Una sesión enfocada en registrar decisiones o cambios.

## Cuándo ocurre

Cuando Robert pide registrar:

- DECISIÓN.
- CAMBIO.
- Actualización HOME.
- Actualización README.

## Riesgo típico

Nivel 2 o Nivel 3.

## Modelo principal

DecisionRecord / ChangeRecord.

## Componente principal

DecisionInbox.

## Evento relacionado

EVENTO 3 si requiere aprobación formal.

## Notificación relacionada

TIPO 13 — Cambio registrado.

TIPO 14 — Decisión registrada.

## Registro de auditoría relacionado

REGISTRO 6 — Decisión.

REGISTRO 7 — Cambio.

## Acción esperada del usuario

Registrar manualmente y confirmar con “ya”.

## Restricción

Robert no debe inventar registros.

---

# TIPO 7 — SESIÓN DE ACTUALIZACIÓN HOME

## Qué representa

Una sesión donde se actualiza ROBERT_HOME.

## Cuándo ocurre

Después de corrección, aprobación o integración relevante.

## Riesgo típico

Nivel 2.

Puede ser Nivel 3 si cambia estado central del sistema.

## Modelo principal

ChangeRecord.

## Componente principal

DocumentStatusMap.

## Evento relacionado

EVENTO 12 si la actualización sale del alcance.

## Notificación relacionada

TIPO 13 — Cambio registrado.

## Registro de auditoría relacionado

REGISTRO 7 — Cambio.

## Acción esperada del usuario

Actualizar HOME manualmente y confirmar.

## Restricción

Actualizar HOME no autoriza siguiente fase.

---

# TIPO 8 — SESIÓN DE ACTUALIZACIÓN README

## Qué representa

Una sesión donde se actualiza README.

## Cuándo ocurre

Después de corrección, aprobación o integración relevante.

## Riesgo típico

Nivel 2.

## Modelo principal

ChangeRecord.

## Componente principal

DocumentStatusMap.

## Evento relacionado

EVENTO 12 si la actualización sale del alcance.

## Notificación relacionada

TIPO 13 — Cambio registrado.

## Registro de auditoría relacionado

REGISTRO 7 — Cambio.

## Acción esperada del usuario

Actualizar README manualmente y confirmar.

## Restricción

README actualizado no significa ejecución real.

---

# TIPO 9 — SESIÓN DE PAUSA

## Qué representa

Una sesión detenida por instrucción del usuario o por necesidad de pausa.

## Cuándo ocurre

Cuando el usuario dice:

- PAUSA.
- DETENTE.
- NO_AVANCES.
- NO_SIGAS.
- NO_EJECUTES.

También ocurre cuando Robert detecta que debe detener avance.

## Riesgo típico

Acción de control fuera de la escala de riesgo.

## Modelo principal

ModeState / SystemState.

## Componente principal

TopBar.

## Evento relacionado

EVENTO 4 — Pausa obligatoria.

## Notificación relacionada

TIPO 2 — Notificación de estado / pausa.

## Registro de auditoría relacionado

REGISTRO 10 — Bloqueo si detiene acción relevante.

REGISTRO 13 — Alcance.

## Acción esperada del usuario

Indicar nuevo alcance o reanudar.

## Restricción

Robert no debe continuar automáticamente después de pausa.

---

# TIPO 10 — SESIÓN DE BLOQUEO

## Qué representa

Una sesión donde una acción queda bloqueada.

## Cuándo ocurre

Cuando existe:

- Bloqueo automático.
- Bloqueo manual solicitado.
- Acción prohibida.
- Fase incorrecta.
- Permiso insuficiente.
- Alcance excedido.

## Riesgo típico

Nivel 2 a Nivel 4, según el tipo de bloqueo.

## Nota de control

Si el bloqueo es solicitado manualmente por el usuario, la acción de control queda fuera de la escala de riesgo.

Ejemplo:

```text
BLOQUEA
DETENTE
NO_EJECUTES
NO_AVANCES
```

Estas instrucciones no deben clasificarse como Nivel 0, Nivel 1, Nivel 2, Nivel 3 o Nivel 4.

Son acciones de control.

## Modelo principal

RiskRecord.

## Componente principal

ApprovalGate.

## Evento relacionado

EVENTO 5 — Bloqueo automático.

EVENTO 6 — Bloqueo manual solicitado.

EVENTO 7 — Acción prohibida.

EVENTO 12 — Fuera de alcance.

EVENTOS 15 al 20 si aplica.

## Notificación relacionada

TIPO 9 — Mensaje de bloqueo.

## Registro de auditoría relacionado

REGISTRO 10 — Bloqueo.

REGISTRO 11 — Riesgo, cuando el bloqueo nace de riesgo detectado, riesgo crítico, permiso insuficiente, alcance excedido o fase incorrecta.

## Acción esperada del usuario

Corregir solicitud, pausar o convertirlo en documentación futura.

## Restricción

Bloqueo no debe ofrecer ejecución real como alternativa.

---

# TIPO 11 — SESIÓN DE DECISIÓN PENDIENTE

## Qué representa

Una sesión donde falta decisión del usuario.

## Cuándo ocurre

Cuando hay:

- Aprobación pendiente.
- Alcance ambiguo.
- Permiso insuficiente.
- Decisión formal necesaria.
- Falta confirmación.

## Riesgo típico

Nivel 2 o Nivel 3.

Puede ser Nivel 4 si intenta autorizar algo prohibido.

## Modelo principal

PendingDecision.

## Componente principal

DecisionInbox.

## Evento relacionado

EVENTO 3 — Aprobación formal requerida.

EVENTO 9 — Falta de información si aplica.

## Notificación relacionada

TIPO 6 — Confirmación requerida.

TIPO 4 — Falta de información si aplica.

## Registro de auditoría relacionado

REGISTRO 6 — Decisión.

REGISTRO 12 — Permiso.

## Acción esperada del usuario

Aprobar, rechazar, corregir o pausar.

## Restricción

Robert no debe resolver decisiones por el usuario.

---

# TIPO 12 — SESIÓN DE SANDBOX MANUAL

## Qué representa

Una sesión de simulación o prueba manual.

## Cuándo ocurre

Cuando el usuario activa o revisa sandbox manual.

## Riesgo típico

Nivel 2 o Nivel 3.

Nivel 4 si intenta convertirse en ejecución real.

## Modelo principal

ModeState.

## Componente principal

ModeSelector.

## Evento relacionado

EVENTO 13 — Sandbox requerido.

EVENTO 14 — Sandbox excedido.

EVENTOS 15 al 20 si intenta ejecución real.

## Notificación relacionada

TIPO 16 — Aviso de sandbox manual.

## Registro de auditoría relacionado

REGISTRO 14 — Sandbox.

## Acción esperada del usuario

Registrar prueba, resultado o cierre.

## Restricción

Sandbox manual no ejecuta acciones reales.

---

# TIPO 13 — SESIÓN DE REVISIÓN CRÍTICA

## Qué representa

Una sesión donde se buscan inconsistencias, riesgos o huecos documentales.

## Cuándo ocurre

Cuando el usuario revisa críticamente un documento o detecta problemas.

## Riesgo típico

Nivel 1 a Nivel 3.

Nivel 4 si la inconsistencia permitiría ejecución real.

## Modelo principal

RiskRecord.

## Componente principal

RiskBadge.

## Evento relacionado

EVENTO 10 — Contradicción documental si aplica.

EVENTO 11 — Riesgo crítico si aplica.

EVENTO 9 — Falta de información si aplica.

## Notificación relacionada

TIPO 5 — Advertencia de riesgo.

TIPO 10 — Contradicción documental.

## Registro de auditoría relacionado

REGISTRO 3 — Revisión.

REGISTRO 11 — Riesgo, cuando la revisión crítica detecta riesgo, riesgo crítico, riesgo operativo, riesgo documental o riesgo de ejecución no autorizada.

REGISTRO 16 — Contradicción documental.

## Acción esperada del usuario

Decidir si corregir, aprobar, pausar o revisar otra vez.

## Restricción

Revisar no corrige automáticamente.

---

# TIPO 14 — SESIÓN DE RECUPERACIÓN DE HILO

## Qué representa

Una sesión donde Robert debe reconstruir el estado anterior antes de continuar.

## Cuándo ocurre

Cuando el usuario vuelve después de tiempo, dice “continuemos”, “dónde íbamos” o responde con una confirmación corta después de una pausa.

## Riesgo típico

Nivel 1 o Nivel 2.

Puede subir si se intenta reanudar una acción de riesgo sin confirmación.

## Modelo principal

SystemState.

## Componente principal

CurrentStatePanel.

## Evento relacionado

EVENTO 9 — Falta de información si el estado no es claro.

EVENTO 4 — Pausa obligatoria si no puede reanudar con seguridad.

## Notificación relacionada

TIPO 17 — Aviso de siguiente paso.

TIPO 4 — Falta de información si aplica.

## Registro de auditoría relacionado

REGISTRO 1 — Informativo.

REGISTRO 13 — Alcance.

## Acción esperada del usuario

Confirmar último estado o elegir siguiente paso.

## Restricción

Robert no debe inventar continuidad.

---

# TIPO 15 — SESIÓN DE CIERRE DE BLOQUE

## Qué representa

Una sesión donde se confirma que un bloque completo quedó cerrado.

## Cuándo ocurre

Cuando se registraron decisión, cambio, HOME, README y respaldo manual relacionados.

## Riesgo típico

Nivel 1 o Nivel 2.

Puede ser Nivel 3 si cierra documento técnico aprobado.

## Modelo principal

SystemState / ChangeRecord.

## Componente principal

CurrentStatePanel.

## Evento relacionado

Ninguno obligatorio.

EVENTO 3 si falta aprobación antes de cerrar.

## Notificación relacionada

TIPO 17 — Aviso de siguiente paso.

TIPO 15 — Aviso de respaldo manual.

## Registro de auditoría relacionado

REGISTRO 9 — Integración.

REGISTRO 15 — Respaldo manual.

## Acción esperada del usuario

Elegir siguiente documento, revisar o pausar.

## Restricción

Cerrar bloque no autoriza avanzar de fase.

---

# TIPO 16 — SESIÓN CON FALTA DE INFORMACIÓN

## Qué representa

Una sesión donde Robert no tiene información suficiente para actuar.

## Cuándo ocurre

Cuando falta:

- Documento exacto.
- Alcance.
- Versión.
- Estado.
- Permiso.
- Confirmación.
- Último paso claro.

## Riesgo típico

Nivel 1 a Nivel 3.

Puede ser Nivel 4 si la falta de información puede causar ejecución incorrecta.

## Modelo principal

PendingDecision.

## Componente principal

ApprovalGate.

## Evento relacionado

EVENTO 9 — Falta de información.

## Notificación relacionada

TIPO 4 — Alerta de comando ambiguo o falta de información.

## Registro de auditoría relacionado

REGISTRO 3 — Revisión.

REGISTRO 12 — Permiso.

REGISTRO 13 — Alcance.

## Acción esperada del usuario

Aclarar información faltante.

## Restricción

Robert debe pausar antes de actuar.

---

# TIPO 17 — SESIÓN CON CAPACIDAD FUTURA NO DISPONIBLE

## Qué representa

Una sesión donde el usuario pide algo que todavía no existe o no está autorizado.

## Cuándo ocurre

Cuando se solicita:

- Memoria real automática.
- Base de datos real.
- Sincronización real.
- App funcional.
- Conexiones externas.
- Automatizaciones.
- Agentes autónomos.
- Ejecución real.

## Riesgo típico

Nivel 2 o Nivel 3 si se documenta.

Nivel 4 si se intenta activar.

## Modelo principal

PendingDecision / ModeState.

## Componente principal

ApprovalGate.

## Evento relacionado

EVENTO 8 — Acción futura no disponible.

EVENTOS 15 al 20 si intenta activarse.

## Notificación relacionada

TIPO 12 — Capacidad futura no disponible.

## Registro de auditoría relacionado

REGISTRO 17 — Capacidad futura no disponible.

## Acción esperada del usuario

Documentar como capacidad futura o cancelar.

## Restricción

Puede diseñarse conceptualmente, no activarse en Fase 10.

---

# ACLARACIÓN SOBRE RESPALDO MANUAL Y NO CREACIÓN DE TIPO 18

SESSION_AND_CONTEXT_SPEC v0.2 no crea un tipo separado llamado:

```text
TIPO 18 — Sesión de respaldo manual
```

Motivo:

El respaldo manual no se considera una sesión completa independiente dentro de esta versión.

El respaldo manual normalmente ocurre como parte del cierre de un bloque documental, después de registrar decisión, registrar cambio, actualizar HOME y actualizar README.

Por eso, en v0.2 el respaldo manual queda absorbido dentro de:

```text
TIPO 15 — Sesión de cierre de bloque
```

Relación con NOTIFICATION_AND_ALERTS_SPEC v0.2:

NOTIFICATION_AND_ALERTS_SPEC sí tiene:

```text
TIPO 15 — Aviso de respaldo manual
```

Eso no obliga a SESSION_AND_CONTEXT_SPEC a crear un tipo equivalente, porque una notificación puede ser más específica que una sesión.

Regla:

**Una sesión puede contener varios avisos, pero no todo aviso necesita convertirse en un tipo de sesión independiente.**

Por lo tanto:

- Se mantiene la paridad funcional.
- No se mantiene paridad numérica exacta.
- No se crea TIPO 18.
- No se crean modelos nuevos.
- No se crean componentes nuevos.
- No se autoriza sistema real de respaldo.
- No se automatiza GitHub.
- No se automatiza Obsidian.

---

# REGLA PARA INTERPRETAR “YA”

Cuando el usuario dice:

```text
ya
```

Robert debe interpretarlo como confirmación del último paso solicitado explícitamente.

Ejemplos:

| Última instrucción de Robert | Significado de “ya” |
|---|---|
| “Cuando termines dime: ya registré DECISIÓN 021” | El usuario registró DECISIÓN 021 |
| “Cuando termines dime: ya registré CAMBIO 036” | El usuario registró CAMBIO 036 |
| “Cuando termines dime: ya actualicé HOME…” | El usuario actualizó HOME |
| “Cuando termines dime: ya actualicé README…” | El usuario actualizó README |
| “Cuando termines dime: ya creé el documento…” | El usuario creó el documento |
| “Cuando termines dime: ya corregí…” | El usuario corrigió el documento |

Regla:

**“Ya” no aprueba documentos, no registra decisiones futuras y no autoriza pasos nuevos salvo que ese fuera el último paso solicitado.**

---

# REGLA PARA REANUDAR DESPUÉS DE PAUSA

Al reanudar, Robert debe decir:

1. Último bloque activo.
2. Último paso confirmado.
3. Estado actual.
4. Próximo paso permitido.
5. Restricciones activas.

Ejemplo:

```text
Último bloque activo: NOTIFICATION_AND_ALERTS_SPEC v0.2 aprobado.
Último paso confirmado: README actualizado.
Estado: bloque cerrado.
Próximo paso permitido: crear SESSION_AND_CONTEXT_SPEC.
Restricción: sin programación ni Fase 11.
```

---

# REGLA PARA BLOQUE ABIERTO

Un bloque está abierto cuando falta al menos uno de estos pasos:

- Documento creado.
- Corrección registrada.
- HOME actualizado.
- README actualizado.
- Decisión registrada.
- Cambio registrado.
- Aprobación confirmada.
- Integración confirmada.
- Cierre confirmado.

Regla:

**Robert no debe recomendar un documento nuevo si el bloque anterior sigue abierto, salvo que el usuario lo autorice explícitamente.**

---

# REGLA PARA BLOQUE CERRADO

Un bloque queda cerrado cuando:

- Documento aprobado o corregido según correspondía.
- DECISIÓN registrada si hubo aprobación.
- CAMBIO registrado.
- HOME actualizado.
- README actualizado.
- Restricciones confirmadas.
- No queda decisión pendiente inmediata.
- Usuario confirmó el último paso.

Regla:

**Cerrar bloque no autoriza avanzar de fase. Solo permite recomendar siguiente documento o pausar.**

---

# RELACIÓN CON USER_ACTIONS_SPEC v0.2

| Acción | Tipo de sesión/contexto esperado | Evento relacionado si aplica |
|---|---|---|
| ACCIÓN 1 — Escribir comando | TIPO 1, 3, 9, 14 o 16 según comando | EVENTO 9 si falta información |
| ACCIÓN 2 — Seleccionar documento | TIPO 2 — Sesión documental activa | Ninguno obligatorio |
| ACCIÓN 3 — Revisar estado general | TIPO 1 — Sesión informativa | Ninguno obligatorio |
| ACCIÓN 4 — Crear documento técnico | TIPO 2 — Sesión documental activa | EVENTO 3 si requiere aprobación |
| ACCIÓN 5 — Corregir documento técnico | TIPO 3 — Sesión de corrección | EVENTO 10 si corrige contradicción |
| ACCIÓN 6 — Aprobar documento | TIPO 4 — Sesión de aprobación | EVENTO 3 |
| ACCIÓN 7 — Registrar decisión | TIPO 6 — Sesión de registro | EVENTO 3 si aplica |
| ACCIÓN 8 — Registrar cambio | TIPO 6 — Sesión de registro | Ninguno obligatorio |
| ACCIÓN 9 — Actualizar HOME | TIPO 7 — Actualización HOME | Ninguno obligatorio |
| ACCIÓN 10 — Actualizar README | TIPO 8 — Actualización README | Ninguno obligatorio |
| ACCIÓN 11 — Cambiar modo | TIPO 9, 12 o 17 según caso | EVENTO 20 si fase incorrecta |
| ACCIÓN 12 — Solicitar sandbox manual | TIPO 12 — Sandbox manual | EVENTO 13 o 14 si aplica |
| ACCIÓN 13 — Pausar avance | TIPO 9 — Pausa | EVENTO 4 |
| ACCIÓN 14 — Solicitar bloqueo manual | TIPO 10 — Bloqueo | EVENTO 6 |
| ACCIÓN 15 — Ver decisiones pendientes | TIPO 11 — Decisión pendiente | EVENTO 3 si requiere aprobación |
| ACCIÓN 16 — Resolver decisión pendiente | TIPO 11 — Decisión pendiente | EVENTO 3 |
| ACCIÓN 17 — Ver mapa documental | TIPO 2 — Sesión documental activa | Ninguno obligatorio |
| ACCIÓN 18 — Marcar respaldo manual en GitHub | TIPO 15 — Cierre de bloque / respaldo | Ninguno obligatorio |
| ACCIÓN 19 — Solicitar revisión crítica | TIPO 13 — Revisión crítica | EVENTO 10 o 11 si aplica |
| ACCIÓN 20 — Pedir siguiente paso | TIPO 14 o TIPO 17 según estado | EVENTO 9 si falta información |

---

# RELACIÓN CON ERROR_AND_BLOCKING_SPEC

Eventos relevantes para sesión y contexto:

- EVENTO 3 — Aprobación formal requerida.
- EVENTO 4 — Pausa obligatoria.
- EVENTO 5 — Bloqueo automático.
- EVENTO 6 — Bloqueo manual solicitado.
- EVENTO 7 — Acción prohibida.
- EVENTO 8 — Acción futura no disponible.
- EVENTO 9 — Falta de información.
- EVENTO 10 — Contradicción documental.
- EVENTO 11 — Riesgo crítico.
- EVENTO 12 — Fuera de alcance.
- EVENTO 13 — Sandbox requerido.
- EVENTO 14 — Sandbox excedido.
- EVENTO 15 — Ejecución no autorizada.
- EVENTO 16 — Conexión no autorizada.
- EVENTO 17 — Automatización no autorizada.
- EVENTO 18 — Agente no autorizado.
- EVENTO 19 — Dato sensible detectado.
- EVENTO 20 — Fase incorrecta.

Regla:

**Si el contexto no es suficiente para continuar, debe activarse EVENTO 9 — Falta de información o EVENTO 4 — Pausa obligatoria según corresponda.**

---

# RELACIÓN CON NOTIFICATION_AND_ALERTS_SPEC

NOTIFICATION_AND_ALERTS_SPEC define qué se muestra.

SESSION_AND_CONTEXT_SPEC define qué estado se recuerda conceptualmente para saber qué mostrar.

Ejemplos:

- Si hay pausa activa, se muestra aviso de pausa.
- Si falta información, se muestra alerta de falta de información.
- Si hay decisión pendiente, se muestra confirmación requerida.
- Si el bloque cerró, se muestra siguiente paso.

---

# RELACIÓN CON AUDIT_TRAIL_SPEC

AUDIT_TRAIL_SPEC define qué rastro queda.

SESSION_AND_CONTEXT_SPEC define qué parte del rastro se usa para continuar.

Ejemplo:

```text
Última decisión: DECISIÓN #021
Último cambio: CAMBIO #036
Último documento aprobado: NOTIFICATION_AND_ALERTS_SPEC v0.2
Siguiente documento recomendado: SESSION_AND_CONTEXT_SPEC
```

Regla:

**La continuidad debe poder apoyarse en la trazabilidad documental.**

## Registros de auditoría especialmente relevantes para sesión y contexto

SESSION_AND_CONTEXT_SPEC v0.2 debe tomar en cuenta especialmente:

- REGISTRO 1 — Informativo.
- REGISTRO 2 — Comando.
- REGISTRO 3 — Revisión.
- REGISTRO 5 — Corrección.
- REGISTRO 6 — Decisión.
- REGISTRO 7 — Cambio.
- REGISTRO 8 — Aprobación.
- REGISTRO 9 — Integración.
- REGISTRO 10 — Bloqueo.
- REGISTRO 11 — Riesgo.
- REGISTRO 12 — Permiso.
- REGISTRO 13 — Alcance.
- REGISTRO 14 — Sandbox.
- REGISTRO 15 — Respaldo manual.
- REGISTRO 16 — Contradicción documental.
- REGISTRO 17 — Capacidad futura no disponible.

Corrección aplicada en v0.2:

- REGISTRO 2 — Comando queda referenciado en TIPO 1 y TIPO 3.
- REGISTRO 11 — Riesgo queda referenciado en TIPO 10 y TIPO 13.

Regla:

**Una sesión debe poder reconstruirse desde comandos, revisiones, decisiones, cambios, riesgos, bloqueos, permisos y respaldos manuales registrados.**

---

# RELACIÓN CON PERMISSIONS_AND_SCOPES_SPEC

PERMISSIONS_AND_SCOPES_SPEC define qué permiso existe.

SESSION_AND_CONTEXT_SPEC define si ese permiso sigue vigente, expiró o fue revocado dentro de la sesión.

Regla:

**Un permiso no dura para siempre salvo autorización explícita.**

---

# RELACIÓN CON ROBERT_COMMANDS

ROBERT_COMMANDS v0.4 define comandos.

SESSION_AND_CONTEXT_SPEC define cómo afectan la continuidad.

Ejemplos:

- `RESUMEN` genera sesión informativa.
- `PAUSA` activa sesión de pausa.
- `NO_AVANCES` detiene avance.
- `SOLO_BORRADOR` limita alcance.
- `APRUEBO` activa sesión de aprobación.
- `ACTUALIZA` puede activar sesión de corrección o registro.
- `MODO_SANDBOX` activa sesión de sandbox manual.
- `REVOCA_AUTONOMIA` reduce alcance.
- `INFORME_ACCIONES` genera sesión informativa/auditoría.

---

# RELACIÓN CON SCREEN_STATE_SPEC

SCREEN_STATE_SPEC define qué se ve.

SESSION_AND_CONTEXT_SPEC define qué estado de sesión debe verse.

Ejemplo:

- TopBar muestra fase, modo y pausa.
- CurrentStatePanel muestra estado completo.
- DecisionInbox muestra pendiente.
- DocumentStatusMap muestra documento activo.
- ApprovalGate muestra si puede avanzar.
- RiskBadge muestra riesgo activo.

---

# RELACIÓN CON INTERACTION_FLOW_SPEC

INTERACTION_FLOW_SPEC define cómo se mueve la información.

SESSION_AND_CONTEXT_SPEC no debe crear flujos nuevos.

Si se necesita un flujo nuevo para recuperar contexto, primero debe corregirse INTERACTION_FLOW_SPEC.

---

# RELACIÓN CON COMPONENTS_SPEC

COMPONENTS_SPEC define componentes.

SESSION_AND_CONTEXT_SPEC solo usa componentes ya existentes.

No crea componentes nuevos.

Si en el futuro se requiere:

```text
SessionPanel
ContextTimeline
```

primero deberá corregirse y aprobarse:

```text
ROBERT_TECHNICAL_COMPONENTS_SPEC
```

---

# RELACIÓN CON SANDBOX

SESSION_AND_CONTEXT_SPEC no redefine sandbox.

La lógica de sandbox vive en:

- ROBERT_SANDBOX
- SANDBOX_RULES
- SANDBOX_TESTS
- SANDBOX_RESULTS

Este documento solo define cómo se mantiene el contexto de una simulación sandbox manual.

Regla:

**Reanudar sandbox no significa ejecutar acciones reales.**

---

# REGLAS DE BLOQUEO POR SESIÓN Y CONTEXTO

Robert debe bloquear o pausar cuando:

- No sabe cuál fue el último paso.
- No sabe qué documento está activo.
- No sabe qué significa “ya”.
- Falta información para continuar.
- Existe contradicción documental.
- Hay decisión pendiente.
- Hay permiso insuficiente.
- Hay alcance vencido.
- Se intenta reanudar una acción prohibida.
- Se intenta asumir que algo fue registrado sin confirmación.
- Se intenta decir que GitHub fue actualizado automáticamente.
- Se intenta recuperar contexto desde herramienta externa no conectada.
- Se intenta usar memoria real automática no autorizada.
- Se intenta avanzar a Fase 11 automáticamente.

---

# MATRIZ DE CONTINUIDAD

| Situación | Interpretación correcta | Acción de Robert |
|---|---|---|
| Usuario dice “ya” después de pedir registrar decisión | Decisión registrada | Continuar con cambio relacionado |
| Usuario dice “ya” después de pedir registrar cambio | Cambio registrado | Actualizar HOME o README según flujo |
| Usuario dice “ya” después de pedir actualizar HOME | HOME actualizado | Pedir actualizar README |
| Usuario dice “ya” después de pedir actualizar README | README actualizado | Cerrar bloque |
| Usuario dice “pausa” | Avance detenido | No continuar hasta nueva instrucción |
| Usuario vuelve después de tiempo | Reanudar desde último estado conocido | Mostrar estado y siguiente paso |
| Falta documento activo | Contexto insuficiente | Preguntar o pausar |
| Hay decisión pendiente | No avanzar | Pedir decisión |
| Hay contradicción | No avanzar | Corregir o pedir decisión |
| Se pide capacidad futura | No activar | Documentar como futura |
| Se pide ejecución real | Bloquear | Mantener Fase 10 |

---

# FORMATO MÍNIMO DE ESTADO DE SESIÓN

Todo estado de sesión importante debe poder mostrar:

```text
Fase actual:
Modo actual:
Documento activo:
Versión activa:
Bloque activo:
Última acción confirmada:
Última decisión:
Último cambio:
Estado de HOME:
Estado de README:
Permiso activo:
Alcance activo:
Riesgo activo:
Evento activo:
Notificación activa:
Registro de auditoría relacionado:
Próximo paso permitido:
Restricciones:
```

---

# EJEMPLO — ESTADO DESPUÉS DE CERRAR BLOQUE

```text
Fase actual: Fase 10 — MVP técnico básico en preparación
Modo actual: Manual / supervisado
Documento activo: ROBERT_TECHNICAL_NOTIFICATION_AND_ALERTS_SPEC v0.2
Bloque activo: Cerrado
Última acción confirmada: README actualizado
Última decisión: DECISIÓN #021
Último cambio: CAMBIO #036
Estado de HOME: Actualizado
Estado de README: Actualizado
Permiso activo: Ninguno pendiente
Alcance activo: Bloque cerrado
Riesgo activo: Nivel 2 documental
Evento activo: Ninguno
Notificación activa: Siguiente paso recomendado
Registro de auditoría relacionado: Aprobación e integración documental
Próximo paso permitido: Crear SESSION_AND_CONTEXT_SPEC
Restricciones: Sin programación, sin Fase 11
```

---

# EJEMPLO — REANUDACIÓN SEGURA

```text
Último estado conocido:
NOTIFICATION_AND_ALERTS_SPEC v0.2 aprobado e integrado.
DECISIÓN #021 registrada.
CAMBIO #036 registrado.
HOME actualizado.
README actualizado.

Estado:
Bloque cerrado.

Próximo paso permitido:
Crear SESSION_AND_CONTEXT_SPEC como borrador técnico documental.

Restricción:
Sin programación, sin código real, sin conexiones, sin automatizaciones, sin Fase 11.
```

---

# EJEMPLO — “YA” AMBIGUO

Si el usuario dice “ya” pero no existe último paso claro:

```text
No tengo suficiente contexto para saber qué confirmaste con “ya”.
¿Te refieres a que actualizaste HOME, README, registraste decisión o registraste cambio?
```

Evento relacionado:

```text
EVENTO 9 — Falta de información
```

---

# CRITERIOS DE ACEPTACIÓN

Este documento podrá considerarse listo para aprobación si:

- Define sesión conceptual.
- Define contexto activo.
- Define continuidad.
- Define pausa.
- Define reanudación.
- Define recuperación de hilo.
- Define interpretación de “ya”.
- Define bloque abierto.
- Define bloque cerrado.
- Aclara que no crea SessionRecord.
- Aclara que no crea ContextSnapshot.
- Aclara que no crea ConversationState.
- Aclara que no crea SessionPanel.
- Aclara que no crea ContextTimeline.
- Conecta sesión y contexto con los 11 modelos de DATA_MODEL_SPEC v0.1.
- Define componentes participantes.
- Define dónde se muestra cada elemento de contexto.
- Uniforma los 17 tipos de estado de sesión.
- Conecta acciones de USER_ACTIONS_SPEC v0.2 con estados de sesión.
- Conecta eventos de ERROR_AND_BLOCKING_SPEC v0.2 con continuidad.
- Conecta notificaciones con estados de sesión.
- Conecta auditoría con continuidad.
- Conecta permisos con vigencia de sesión.
- Referencia REGISTRO 2 — Comando en TIPO 1 — Sesión informativa.
- Referencia REGISTRO 2 — Comando en TIPO 3 — Sesión de corrección.
- Referencia REGISTRO 11 — Riesgo en TIPO 10 — Sesión de bloqueo cuando aplica.
- Referencia REGISTRO 11 — Riesgo en TIPO 13 — Sesión de revisión crítica.
- Aclara que no se crea TIPO 18 — Sesión de respaldo manual.
- Aclara que el respaldo manual se absorbe dentro de TIPO 15 — Sesión de cierre de bloque.
- Aclara que una notificación específica no siempre requiere un tipo de sesión independiente.
- Separa riesgo típico de acción de control fuera de escala.
- Mantiene Nivel 0 únicamente como Informativo.
- Mantiene acciones de control fuera de la escala de riesgo.
- No crea modelos nuevos oficiales.
- No crea componentes nuevos oficiales.
- No autoriza programación.
- No autoriza código real.
- No autoriza pantallas reales.
- No autoriza memoria real automática.
- No autoriza base de datos real.
- No autoriza conexiones externas.
- No autoriza automatizaciones.
- No autoriza agentes autónomos.
- Mantiene a Robert en Fase 10.
- Mantiene control total del usuario.

---

# RIESGO DEL DOCUMENTO

Tipo de cambio:

**Cambio técnico documental / sesión, contexto y continuidad conceptual**

Nivel de riesgo inicial:

**Nivel 3 — Alto**

Motivo:

Este documento define cómo Robert mantiene continuidad, interpreta confirmaciones, reanuda trabajo y evita perder el hilo. Aunque sigue siendo conceptual, influye en seguridad operativa, trazabilidad y control del usuario.

Nivel de riesgo final esperado:

**Nivel 2 — Medio**

Motivo de reducción:

El documento es documental. No crea memoria real automática, no crea sistema real de sesiones, no crea base de datos real, no crea modelos nuevos oficiales, no crea componentes nuevos oficiales, no programa, no conecta herramientas externas y no ejecuta acciones.

Nivel de autonomía:

**Nivel 0 — Sin autonomía ejecutiva**

---

# DECISIÓN PENDIENTE

Este documento queda como:

**Propuesta corregida pendiente de revisión**

Para aprobarlo formalmente, el usuario deberá escribir:

**APRUEBO ROBERT_TECHNICAL_SESSION_AND_CONTEXT_SPEC v0.2**

---

# EFECTO DE UNA APROBACIÓN FUTURA

Si se aprueba este documento, se deberá:

1. Registrar decisión formal en ROBERT_DECISIONS_LOG.
2. Registrar cambio en ROBERT_CONTROL_DE_CAMBIOS.
3. Actualizar ROBERT_HOME.
4. Actualizar README si aplica.
5. Mantenerlo como base para futuras especificaciones técnicas.
6. No crear memoria real automática.
7. No crear sistema real de sesiones.
8. No crear base de datos real.
9. No pasar automáticamente a programación.
10. No avanzar automáticamente a Fase 11.

---

# PRÓXIMO PASO RECOMENDADO

Después de revisar este documento, el siguiente documento posible sería:

**ROBERT_TECHNICAL_DOCUMENT_LIFECYCLE_SPEC**

Ese documento definiría el ciclo de vida de documentos: borrador, propuesta, corrección, revisión, aprobación, integración, actualización, depreciación y reemplazo.

No debe crearse hasta revisar o aprobar SESSION_AND_CONTEXT_SPEC.

---

# CIERRE

ROBERT_TECHNICAL_SESSION_AND_CONTEXT_SPEC v0.2 define sesión, contexto activo, continuidad, pausa, reanudación, interpretación de confirmaciones cortas, recuperación del hilo y cierre de bloques dentro del MVP técnico básico de Robert.

Este documento conecta sesión y contexto con DATA_MODEL_SPEC v0.1, COMPONENTS_SPEC v0.2, USER_ACTIONS_SPEC v0.2, ERROR_AND_BLOCKING_SPEC v0.2, PERMISSIONS_AND_SCOPES_SPEC v0.2, AUDIT_TRAIL_SPEC v0.2 y NOTIFICATION_AND_ALERTS_SPEC v0.2.

Este documento mantiene a Robert en modo documental, manual y supervisado.

El usuario mantiene control total.

Robert no ejecuta acciones importantes sin permiso.
