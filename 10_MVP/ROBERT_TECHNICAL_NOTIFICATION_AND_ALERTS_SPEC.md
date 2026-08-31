# ROBERT_TECHNICAL_NOTIFICATION_AND_ALERTS_SPEC

Versión: 0.2  
Estado: APROBADO E INTEGRADO 
Fecha: 06/07/2026  
Ubicación: 10_MVP  
Fase relacionada: Fase 10 — MVP técnico básico en preparación  
Documento base principal: ROBERT_TECHNICAL_AUDIT_TRAIL_SPEC v0.2  
Documentos relacionados: ROBERT_COMMANDS v0.4, ROBERT_TECHNICAL_PERMISSIONS_AND_SCOPES_SPEC v0.2, ROBERT_TECHNICAL_ERROR_AND_BLOCKING_SPEC v0.2, ROBERT_TECHNICAL_USER_ACTIONS_SPEC v0.2, ROBERT_TECHNICAL_DATA_MODEL_SPEC v0.1, ROBERT_TECHNICAL_COMPONENTS_SPEC v0.2, ROBERT_TECHNICAL_SCREEN_STATE_SPEC v0.2, ROBERT_TECHNICAL_INTERACTION_FLOW_SPEC v0.2  
Documentos sandbox relacionados: ROBERT_SANDBOX, SANDBOX_RULES, SANDBOX_TESTS, SANDBOX_RESULTS  
Fuente de verdad actual: ROBERT_CONTEXT_MASTER v0.5  

Tags: #robert/orbita-3 #capa/5 #tipo/tecnico #robert/mvp #robert/notifications-alerts

---

# OBJETIVO

ROBERT_TECHNICAL_NOTIFICATION_AND_ALERTS_SPEC define cómo Robert debe mostrar avisos, alertas, advertencias, confirmaciones, mensajes de bloqueo y notificaciones internas conceptuales dentro del MVP técnico básico.

Su objetivo es responder:

- Qué debe avisar Robert.
- Cuándo debe mostrar una alerta.
- Cuándo debe pedir confirmación.
- Cuándo debe mostrar advertencia.
- Cuándo debe mostrar bloqueo.
- Qué mensaje debe aparecer ante riesgo.
- Qué mensaje debe aparecer ante falta de permiso.
- Qué mensaje debe aparecer ante contradicción documental.
- Qué mensaje debe aparecer ante acción fuera de alcance.
- Qué mensaje debe aparecer ante pausa obligatoria.
- Qué mensaje debe aparecer ante bloqueo manual solicitado.
- Qué mensaje debe aparecer ante acción futura no disponible.
- Qué componente muestra cada tipo de aviso.
- Qué modelo conceptual representa cada aviso.
- Qué acciones requieren notificación.
- Qué eventos generan alerta.
- Qué no debe notificarse todavía.
- Qué queda prohibido en Fase 10.

Este documento no crea sistema real de notificaciones.

Este documento no crea notificaciones push.

Este documento no crea emails.

Este documento no crea pop-ups reales.

Este documento no crea pantallas reales.

Este documento no crea componentes nuevos oficiales.

Este documento no crea modelos nuevos oficiales.

Este documento no programa la app.

Este documento no conecta herramientas externas.

Este documento no ejecuta acciones reales.

---

# ESTADO DEL DOCUMENTO

Este documento queda como:

**APROBADO E INTEGRADO — v0.2**

Trazabilidad formal:

```text
DECISIÓN #021
CAMBIO #035 — Corrección
CAMBIO #036 — Aprobación e integración
```

Estado operativo:

```text
STATUS: APPROVED / INTEGRATED
PHASE: 10
IMPLEMENTATION: NONE
AUTONOMY_LEVEL: 0
EXECUTION_AUTHORITY: NONE
```

No activa notificaciones reales, servicios externos ni automatización.

---


# CORRECCIONES DE LA VERSIÓN v0.2

Esta versión corrige los huecos detectados en v0.1.

Correcciones principales:

1. Se agrega EVENTO 8 — Acción futura no disponible.
2. Se conecta TIPO 12 — Alerta de capacidad futura no disponible con EVENTO 8 como evento general.
3. Se aclara que TIPO 12 solo usa EVENTOS 15 al 20 cuando el usuario intenta activar la capacidad futura como acción real.
4. Se agrega EVENTO 4 — Pausa obligatoria.
5. Se conecta ACCIÓN 13 — Pausar avance con EVENTO 4.
6. Se agrega EVENTO 6 — Bloqueo manual solicitado.
7. Se conecta ACCIÓN 14 — Solicitar bloqueo manual con EVENTO 6.
8. Se agrega EVENTO 7 — Acción prohibida.
9. Se conecta TIPO 9 — Mensaje de bloqueo con EVENTO 7.
10. Se agrega EVENTO 9 — Falta de información.
11. Se conecta TIPO 4 — Alerta de comando ambiguo con EVENTO 9.
12. Se agrega EVENTO 11 — Riesgo crítico.
13. Se conecta TIPO 5 — Advertencia de riesgo con EVENTO 11.
14. Se agrega EVENTO 13 — Sandbox requerido.
15. Se agrega EVENTO 14 — Sandbox excedido.
16. Se conecta TIPO 16 — Aviso de sandbox manual con EVENTOS 13 y 14.
17. Se actualiza la lista de eventos relevantes.
18. Se actualiza la tabla de relación entre tipos y eventos.
19. Se actualiza la correspondencia con USER_ACTIONS_SPEC v0.2.
20. Se mantiene que las acciones de control están fuera de la escala de riesgo.
21. Se mantiene alineación con ERROR_AND_BLOCKING_SPEC v0.2.

---

# REGLA CENTRAL

Robert debe avisar antes de actuar cuando exista riesgo, duda, permiso insuficiente, alcance ambiguo, contradicción, pausa obligatoria o bloqueo.

Regla principal:

**El usuario debe entender qué pasa, por qué pasa y qué opciones tiene antes de continuar.**

---

# REGLA DE ALINEACIÓN DOCUMENTAL

NOTIFICATION_AND_ALERTS_SPEC v0.2 debe mantenerse alineado con:

- ROBERT_COMMANDS v0.4
- ROBERT_TECHNICAL_AUDIT_TRAIL_SPEC v0.2
- ROBERT_TECHNICAL_PERMISSIONS_AND_SCOPES_SPEC v0.2
- ROBERT_TECHNICAL_ERROR_AND_BLOCKING_SPEC v0.2
- ROBERT_TECHNICAL_USER_ACTIONS_SPEC v0.2
- ROBERT_TECHNICAL_DATA_MODEL_SPEC v0.1
- ROBERT_TECHNICAL_COMPONENTS_SPEC v0.2
- ROBERT_TECHNICAL_SCREEN_STATE_SPEC v0.2
- ROBERT_TECHNICAL_INTERACTION_FLOW_SPEC v0.2
- ROBERT_SECURITY_RULES
- ROBERT_PHASES
- ROBERT_SANDBOX
- SANDBOX_RULES
- SANDBOX_TESTS
- SANDBOX_RESULTS

Regla:

**NOTIFICATION_AND_ALERTS_SPEC no debe inventar nuevos modelos oficiales, nuevos componentes oficiales, nuevas capacidades activas, nuevos permisos ejecutivos, nuevos eventos reales ni nueva lógica de autonomía que no exista en los documentos base.**

Si una notificación requiere sistema real, conexión externa, email, push notification, base de datos, automatización o agente autónomo, debe bloquearse en Fase 10.

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
- ROBERT_TECHNICAL_NOTIFICATION_AND_ALERTS_SPEC v0.2 como propuesta corregida pendiente de revisión.
- Sin programación autorizada.
- Sin código real.
- Sin botones reales.
- Sin pantallas reales.
- Sin notificaciones reales.
- Sin emails.
- Sin push notifications.
- Sin base de datos real.
- Sin conexiones externas.
- Sin automatizaciones reales.
- Sin agentes autónomos activos.

---

# ALCANCE AUTORIZADO

Este documento autoriza únicamente:

- Definir notificaciones conceptuales.
- Definir avisos conceptuales.
- Definir alertas conceptuales.
- Definir advertencias conceptuales.
- Definir confirmaciones conceptuales.
- Definir mensajes de bloqueo conceptuales.
- Definir mensajes internos de estado.
- Definir relación entre notificaciones y modelos existentes.
- Definir relación entre notificaciones y componentes visuales conceptuales.
- Definir relación entre notificaciones, permisos, riesgos, acciones, eventos y auditoría.
- Definir avisos para pausa obligatoria.
- Definir avisos para bloqueo manual solicitado.
- Definir avisos para acción futura no disponible.
- Mantener a Robert en modo documental, manual y supervisado.

---

# ALCANCE NO AUTORIZADO

Este documento no autoriza:

- Programar la app.
- Crear código real.
- Crear sistema real de notificaciones.
- Crear notificaciones push.
- Enviar emails.
- Crear pop-ups reales.
- Crear banners reales.
- Crear base de datos real.
- Crear tabla real de notificaciones.
- Crear modelo NotificationRecord.
- Crear modelo AlertRecord.
- Crear componente NotificationCenter.
- Crear componente AlertPanel.
- Crear botones reales.
- Crear pantallas reales.
- Crear prototipo funcional.
- Crear endpoints.
- Conectar Supabase.
- Conectar Firebase.
- Conectar GitHub automáticamente.
- Conectar Gmail.
- Conectar Google Calendar.
- Conectar APIs externas.
- Automatizar avisos.
- Activar agentes autónomos.
- Ejecutar acciones reales.
- Avanzar automáticamente a Fase 11.

---

# DEFINICIÓN DE NOTIFICACIÓN

Una notificación es un mensaje conceptual que informa al usuario sobre un estado, acción, riesgo, cambio, permiso, decisión, bloqueo o siguiente paso.

En Robert, una notificación puede servir para:

- Informar.
- Confirmar.
- Advertir.
- Pedir aprobación.
- Pedir aclaración.
- Mostrar bloqueo.
- Mostrar riesgo.
- Mostrar estado.
- Mostrar resultado.
- Mostrar siguiente paso permitido.

---

# DEFINICIÓN DE ALERTA

Una alerta es una notificación de mayor importancia que aparece cuando existe riesgo, contradicción, permiso insuficiente, acción fuera de alcance, falta de información o posible bloqueo.

Una alerta debe explicar:

- Qué ocurrió.
- Por qué importa.
- Qué riesgo tiene.
- Qué permiso falta.
- Qué información falta.
- Qué acción está bloqueada.
- Qué puede hacer el usuario después.

---

# DEFINICIÓN DE ADVERTENCIA

Una advertencia es un mensaje preventivo antes de que algo se convierta en bloqueo.

Ejemplo:

```text
Esta acción puede afectar un documento aprobado. Necesita confirmación antes de continuar.
```

Una advertencia no siempre bloquea, pero sí debe pausar si falta permiso, información o alcance claro.

---

# DEFINICIÓN DE CONFIRMACIÓN

Una confirmación es un mensaje que pide al usuario validar una acción antes de continuar.

Ejemplo:

```text
¿Apruebas formalmente este documento?
```

Una confirmación debe usarse cuando:

- La acción cambia estado.
- La acción registra decisión.
- La acción registra cambio.
- La acción aprueba documento.
- La acción integra documento.
- La acción modifica alcance.
- La acción puede generar riesgo Nivel 3 o Nivel 4.

---

# DEFINICIÓN DE MENSAJE DE BLOQUEO

Un mensaje de bloqueo informa que Robert no puede avanzar con la acción solicitada.

Debe incluir:

- Motivo.
- Evento relacionado.
- Riesgo.
- Permiso faltante.
- Alcance excedido.
- Restricción de Fase 10.
- Próximo paso permitido.

Ejemplo:

```text
Bloqueado. Esta acción intenta conectar una herramienta externa, lo cual no está autorizado en Fase 10. Se puede documentar como capacidad futura, pero no activarla.
```

---

# NOTIFICATION AND ALERTS NO ES MODELO NUEVO OFICIAL

En esta versión, el concepto:

- Notification
- Alert

no crea modelos nuevos oficiales.

Son estructuras conceptuales derivadas de modelos ya existentes en DATA_MODEL_SPEC v0.1.

Regla:

**NOTIFICATION_AND_ALERTS_SPEC v0.2 no crea los modelos NotificationRecord ni AlertRecord.**

Si en el futuro se decide crear modelos oficiales como:

```text
NotificationRecord
AlertRecord
```

primero deberá corregirse y aprobarse:

```text
ROBERT_TECHNICAL_DATA_MODEL_SPEC
```

---

# NOTIFICATION AND ALERTS NO CREA COMPONENTE NUEVO OFICIAL

En esta versión, Notification and Alerts no crea componentes nuevos.

Regla:

**NOTIFICATION_AND_ALERTS_SPEC v0.2 no crea NotificationCenter ni AlertPanel.**

Si en el futuro se decide crear componentes oficiales como:

```text
NotificationCenter
AlertPanel
```

primero deberá corregirse y aprobarse:

```text
ROBERT_TECHNICAL_COMPONENTS_SPEC
```

---

# RELACIÓN CON DATA_MODEL_SPEC v0.1

Este documento se apoya en los 11 modelos existentes de DATA_MODEL_SPEC v0.1.

Notification and Alerts debe entenderse como una vista conceptual construida con esos modelos.

---

## 1. SystemState

SystemState refleja el estado general que puede generar avisos.

Puede activar conceptualmente:

- Aviso de modo activo.
- Aviso de fase activa.
- Aviso de estado pendiente.
- Aviso de restricción activa.
- Aviso de bloqueo.
- Aviso de próximo paso.
- Aviso de pausa obligatoria.
- Aviso de control aplicado.

Uso en este documento:

SystemState permite mostrar avisos de estado general.

---

## 2. RobertDocument

RobertDocument identifica documentos que pueden generar notificaciones.

Puede activar conceptualmente:

- Documento pendiente de revisión.
- Documento aprobado.
- Documento bloqueado.
- Documento fuera de alcance.
- Documento actualizado.
- Documento con contradicción.

Uso en este documento:

Toda alerta documental debe indicar qué RobertDocument está afectado.

---

## 3. DecisionRecord

DecisionRecord se relaciona con notificaciones de decisión.

Puede activar conceptualmente:

- Decisión pendiente.
- Decisión aprobada.
- Decisión rechazada.
- Decisión registrada.
- Decisión requerida.

Uso en este documento:

Cuando una acción necesita decisión formal, debe mostrarse confirmación o alerta.

---

## 4. ChangeRecord

ChangeRecord se relaciona con notificaciones de cambio.

Puede activar conceptualmente:

- Cambio registrado.
- Cambio pendiente.
- Cambio aprobado.
- Cambio no autorizado.
- Cambio que requiere actualización de HOME.
- Cambio que requiere actualización de README.

Uso en este documento:

Toda modificación documental relevante debe poder generar aviso de cambio.

---

## 5. RiskRecord

RiskRecord se relaciona directamente con alertas y advertencias.

Puede activar conceptualmente:

- Riesgo Nivel 0.
- Riesgo Nivel 1.
- Riesgo Nivel 2.
- Riesgo Nivel 3.
- Riesgo Nivel 4.
- Riesgo mayor al permitido.
- Riesgo reducido.
- Riesgo bloqueado.
- Riesgo crítico.

Uso en este documento:

Toda alerta de riesgo debe conectarse con RiskRecord.

---

## 6. CommandRequest

CommandRequest representa la solicitud que puede generar una notificación.

Puede activar conceptualmente:

- Comando reconocido.
- Comando ambiguo.
- Comando fuera de alcance.
- Comando con información insuficiente.
- Comando de control.
- Comando que requiere aprobación.
- Comando prohibido en Fase 10.

Uso en este documento:

Toda notificación nace de una solicitud, estado o evento.

---

## 7. PendingDecision

PendingDecision se relaciona con avisos de decisión pendiente.

Puede activar conceptualmente:

- Confirmación requerida.
- Aprobación pendiente.
- Alcance ambiguo.
- Permiso insuficiente.
- Información faltante.
- Siguiente paso pendiente.

Uso en este documento:

Cuando el sistema no puede avanzar sin usuario, debe existir aviso de decisión pendiente.

---

## 8. ModeState

ModeState se relaciona con avisos de modo operativo.

Puede activar conceptualmente:

- Modo manual.
- Modo supervisado.
- Modo sandbox.
- Modo restringido.
- Modo no disponible.
- Intento de autonomía bloqueado.
- Sandbox requerido.
- Sandbox excedido.

Uso en este documento:

Robert debe mostrar avisos si el usuario intenta usar un modo no disponible o si se requiere sandbox.

---

## 9. ComponentState

ComponentState indica qué componente muestra la notificación.

Puede indicar:

- TopBar mostrando estado.
- RiskBadge mostrando riesgo.
- ApprovalGate mostrando confirmación o bloqueo.
- DecisionInbox mostrando pendiente.
- CurrentStatePanel mostrando detalle.
- DocumentStatusMap mostrando documento afectado.
- CommandCenter mostrando aclaración.

Uso en este documento:

Toda notificación conceptual debe poder asociarse a un componente existente.

---

## 10. GitHubBackupStatus

GitHubBackupStatus se relaciona con avisos de respaldo manual.

Puede activar conceptualmente:

- Commit sugerido.
- Commit confirmado.
- Respaldo pendiente.
- GitHub actualizado manualmente.
- GitHub no conectado automáticamente.

Uso en este documento:

Robert puede avisar sobre respaldo manual, pero no afirmar actualización automática.

---

## 11. ObsidianGraphStatus

ObsidianGraphStatus se relaciona con avisos visuales/documentales.

Puede activar conceptualmente:

- Documento fuera de órbita.
- Tag pendiente.
- Grafo actualizado manualmente.
- Relación documental faltante.
- Documento no visible en mapa.

Uso en este documento:

Robert puede avisar sobre estado visual/documental, pero no automatizar Obsidian.

---

# MAPEO CONCEPTUAL DE NOTIFICACIONES A MODELOS EXISTENTES

| Elemento de notificación | Modelo relacionado | Uso |
|---|---|---|
| Estado general | SystemState | Aviso de fase, modo o restricción |
| Documento afectado | RobertDocument | Alerta documental |
| Decisión requerida | PendingDecision / DecisionRecord | Confirmación o decisión pendiente |
| Cambio registrado | ChangeRecord | Aviso de cambio |
| Riesgo detectado | RiskRecord | Advertencia o alerta |
| Comando recibido | CommandRequest | Mensaje de comando reconocido o ambiguo |
| Modo activo | ModeState | Aviso de modo |
| Componente visible | ComponentState | Dónde aparece el aviso |
| Respaldo manual | GitHubBackupStatus | Aviso de commit manual |
| Estado visual documental | ObsidianGraphStatus | Aviso de grafo, órbita o tag |

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

# ROL DE CADA COMPONENTE EN NOTIFICACIONES Y ALERTAS

## AppShell

AppShell contiene el marco general donde viven los avisos conceptuales.

No genera notificaciones reales.

No ejecuta acciones.

No decide.

---

## TopBar

TopBar muestra avisos resumidos y persistentes.

Puede mostrar:

- Modo activo.
- Fase activa.
- Restricción activa.
- Estado de respaldo manual.
- Decisión pendiente.
- Bloqueo activo.
- Pausa activa.
- Alerta crítica resumida.

Ejemplo:

```text
Fase 10 | Modo supervisado | Bloqueo activo: conexión no autorizada
```

---

## LeftSidebar

LeftSidebar puede mostrar estado documental básico.

Puede mostrar:

- Documento activo.
- Documento pendiente.
- Documento aprobado.
- Documento bloqueado.
- Documento fuera de alcance.

---

## CommandCenter

CommandCenter muestra mensajes relacionados con comandos.

Puede mostrar:

- Comando reconocido.
- Comando ambiguo.
- Comando con falta de información.
- Comando fuera de alcance.
- Confirmación requerida.
- Solicitud de aclaración.
- Comando de control aplicado.

---

## ModeSelector

ModeSelector muestra avisos relacionados con modo operativo.

Puede mostrar:

- Modo actual.
- Cambio de modo pendiente.
- Modo no disponible.
- Autonomía no autorizada.
- Sandbox manual activo conceptualmente.
- Sandbox requerido.
- Sandbox excedido.

---

## RiskBadge

RiskBadge muestra alertas de riesgo.

Puede mostrar:

- Nivel de riesgo.
- Motivo del riesgo.
- Riesgo inicial.
- Riesgo final.
- Riesgo crítico.
- Riesgo bloqueado.
- Riesgo mayor al autorizado.

---

## ApprovalGate

ApprovalGate muestra confirmaciones, advertencias y bloqueos.

Puede mostrar:

- Aprobación requerida.
- Permiso insuficiente.
- Acción fuera de alcance.
- Acción prohibida.
- Acción bloqueada.
- Confirmación pendiente.
- Falta de información.
- Siguiente paso permitido.

---

## DecisionInbox

DecisionInbox muestra avisos de decisiones pendientes.

Puede mostrar:

- Documento pendiente de aprobación.
- Decisión requerida.
- Decisión aprobada.
- Decisión rechazada.
- Pausa solicitada.
- Opciones disponibles.

---

## DocumentStatusMap

DocumentStatusMap muestra alertas documentales.

Puede mostrar:

- Documento afectado.
- Documento relacionado.
- Documento bloqueado.
- Contradicción documental.
- Cambio asociado.
- Decisión asociada.
- Estado de versión.

---

## CurrentStatePanel

CurrentStatePanel muestra el detalle completo del aviso o alerta.

Debe mostrar:

- Qué ocurrió.
- Por qué importa.
- Qué documento afecta.
- Qué permiso aplica.
- Qué riesgo tiene.
- Qué evento se activó.
- Qué registro de auditoría corresponde.
- Qué acción está permitida.
- Qué acción está prohibida.
- Qué sigue.

---

# DÓNDE SE MUESTRA CADA TIPO DE AVISO

| Tipo de aviso | Componente principal | Componentes relacionados |
|---|---|---|
| Aviso informativo | CurrentStatePanel | TopBar |
| Aviso de modo o pausa | ModeSelector / TopBar | CurrentStatePanel |
| Aviso de documento | DocumentStatusMap | LeftSidebar |
| Aviso de comando | CommandCenter | CurrentStatePanel |
| Advertencia de riesgo | RiskBadge | ApprovalGate |
| Confirmación requerida | ApprovalGate | DecisionInbox |
| Decisión pendiente | DecisionInbox | ApprovalGate |
| Bloqueo | ApprovalGate | RiskBadge, TopBar |
| Bloqueo manual | ApprovalGate | TopBar, CurrentStatePanel |
| Contradicción documental | DocumentStatusMap | ApprovalGate, RiskBadge |
| Respaldo manual | TopBar | CurrentStatePanel |
| Sandbox | ModeSelector | ApprovalGate, CurrentStatePanel |
| Siguiente paso | CurrentStatePanel | CommandCenter |

---

# TIPOS DE NOTIFICACIONES Y ALERTAS

Robert puede manejar estos tipos conceptuales:

1. Notificación informativa.
2. Notificación de estado.
3. Notificación de comando reconocido.
4. Alerta de comando ambiguo o falta de información.
5. Advertencia de riesgo.
6. Confirmación requerida.
7. Alerta de permiso insuficiente.
8. Alerta de alcance excedido.
9. Mensaje de bloqueo.
10. Alerta de contradicción documental.
11. Alerta de fase incorrecta.
12. Alerta de capacidad futura no disponible.
13. Aviso de cambio registrado.
14. Aviso de decisión registrada.
15. Aviso de respaldo manual.
16. Aviso de sandbox manual.
17. Aviso de siguiente paso.

Todos los tipos deben usar una estructura uniforme.

---

# ESTRUCTURA UNIFORME DE LOS 17 TIPOS

Cada tipo debe incluir:

```text
Qué muestra:
Cuándo aparece:
Riesgo típico:
Modelo principal:
Componente principal:
Evento relacionado:
Registro de auditoría relacionado:
Acción esperada del usuario:
Restricción:
```

---

# TIPO 1 — NOTIFICACIÓN INFORMATIVA

## Qué muestra

Información general sin modificación documental.

## Cuándo aparece

Cuando el usuario pide estado, resumen, explicación o siguiente paso informativo.

## Riesgo típico

Nivel 0 — Informativo.

## Modelo principal

SystemState.

## Componente principal

CurrentStatePanel.

## Evento relacionado

Ninguno obligatorio.

EVENTO 1 y EVENTO 2 pueden quedar cubiertos aquí si en ERROR_AND_BLOCKING_SPEC funcionan como advertencia o confirmación genérica.

## Registro de auditoría relacionado

REGISTRO 1 — Informativo.

## Acción esperada del usuario

Leer o decidir si quiere avanzar.

## Restricción

No modifica documentos.

No aprueba.

No registra cambio formal.

---

# TIPO 2 — NOTIFICACIÓN DE ESTADO

## Qué muestra

Estado actual del sistema, fase, modo, documento activo, restricción activa o pausa aplicada.

## Cuándo aparece

Cuando cambia o se consulta el estado actual.

También aparece cuando el usuario usa una acción de control como:

- PAUSA.
- DETENTE.
- NO_AVANCES.

## Riesgo típico

Nivel 0 o Nivel 1 cuando solo informa.

Acciones de control fuera de la escala de riesgo cuando detiene, pausa o reduce alcance.

## Modelo principal

SystemState.

## Componente principal

TopBar.

## Evento relacionado

EVENTO 4 — Pausa obligatoria cuando el sistema debe detener avance.

EVENTO 20 — Fase incorrecta si detecta estado o fase incompatible.

## Registro de auditoría relacionado

REGISTRO 1 — Informativo.

REGISTRO 13 — Alcance.

REGISTRO 10 — Bloqueo si la pausa detiene una acción relevante.

## Acción esperada del usuario

Confirmar, continuar, pausar o indicar siguiente paso.

## Restricción

No debe presentar estado falso.

No debe afirmar capacidades no activas.

Una pausa no aumenta riesgo; reduce alcance.

---

# TIPO 3 — NOTIFICACIÓN DE COMANDO RECONOCIDO

## Qué muestra

Que Robert entendió un comando o instrucción del usuario.

## Cuándo aparece

Cuando el usuario escribe comandos como:

- Hazlo.
- Corrígelo.
- Apruebo.
- Pausa.
- MODO_SANDBOX.

## Riesgo típico

Depende del comando.

Puede ser Nivel 0 a Nivel 4.

## Modelo principal

CommandRequest.

## Componente principal

CommandCenter.

## Evento relacionado

Puede relacionarse con EVENTO 3 si requiere aprobación.

Puede relacionarse con EVENTO 12 si supera alcance.

Puede relacionarse con EVENTO 4 si el comando es de pausa o control.

## Registro de auditoría relacionado

REGISTRO 2 — Comando.

## Acción esperada del usuario

Confirmar o seguir el siguiente paso indicado.

## Restricción

Comando reconocido no significa permiso ilimitado.

---

# TIPO 4 — ALERTA DE COMANDO AMBIGUO O FALTA DE INFORMACIÓN

## Qué muestra

Que la instrucción no tiene alcance suficiente o que falta información para actuar.

## Cuándo aparece

Cuando el usuario dice algo como:

```text
Haz todo.
Arréglalo.
Sigue.
Actívalo.
```

sin definir alcance claro.

También aparece cuando falta información necesaria para decidir, corregir o registrar.

## Riesgo típico

Nivel 1 a Nivel 3.

Puede ser Nivel 4 si intenta activar acción real.

## Modelo principal

CommandRequest / PendingDecision.

## Componente principal

ApprovalGate.

## Evento relacionado

EVENTO 9 — Falta de información.

EVENTO 12 — Fuera de alcance.

## Registro de auditoría relacionado

REGISTRO 12 — Permiso.

REGISTRO 13 — Alcance.

REGISTRO 3 — Revisión si la falta de información aparece durante revisión.

## Acción esperada del usuario

Definir alcance, proporcionar información faltante o confirmar acción específica.

## Restricción

Robert debe pausar antes de actuar.

No debe inventar información faltante.

---

# TIPO 5 — ADVERTENCIA DE RIESGO

## Qué muestra

Que una acción tiene riesgo y puede requerir aprobación o bloqueo.

## Cuándo aparece

Cuando una acción tiene riesgo Nivel 2, Nivel 3 o Nivel 4.

## Riesgo típico

Nivel 2 a Nivel 4.

## Modelo principal

RiskRecord.

## Componente principal

RiskBadge.

## Evento relacionado

EVENTO 11 — Riesgo crítico cuando el riesgo sea Nivel 4.

Puede relacionarse con EVENTO 3, EVENTO 5, EVENTO 7, EVENTO 12 o EVENTOS 15 al 20 según aplique.

## Registro de auditoría relacionado

REGISTRO 11 — Riesgo.

## Acción esperada del usuario

Aprobar, corregir, pausar o cancelar.

## Restricción

Robert no debe ocultar riesgo.

Si el riesgo es Nivel 4, debe bloquear o pedir decisión formal según corresponda.

---

# TIPO 6 — CONFIRMACIÓN REQUERIDA

## Qué muestra

Que Robert necesita aprobación explícita antes de continuar.

## Cuándo aparece

Cuando se intenta:

- Aprobar documento.
- Integrar documento.
- Registrar decisión.
- Registrar cambio.
- Cambiar modo.
- Modificar documento oficial.
- Resolver pendiente.

## Riesgo típico

Nivel 2 o Nivel 3.

Puede ser Nivel 4 si la confirmación intenta autorizar algo prohibido.

## Modelo principal

PendingDecision / DecisionRecord.

## Componente principal

ApprovalGate.

## Evento relacionado

EVENTO 3 — Aprobación formal requerida.

## Registro de auditoría relacionado

REGISTRO 6 — Decisión.

REGISTRO 8 — Aprobación.

## Acción esperada del usuario

Responder con aprobación, rechazo, corrección o pausa.

## Restricción

Sin aprobación explícita, Robert no avanza.

---

# TIPO 7 — ALERTA DE PERMISO INSUFICIENTE

## Qué muestra

Que la acción solicitada supera el permiso autorizado.

## Cuándo aparece

Cuando el usuario autorizó una cosa, pero la acción intenta hacer otra.

Ejemplo:

- Autorizó corregir, pero se intenta aprobar.
- Autorizó revisar, pero se intenta modificar.
- Autorizó documentar, pero se intenta programar.

## Riesgo típico

Nivel 2 o Nivel 3.

Nivel 4 si implica ejecución real.

## Modelo principal

PendingDecision / RiskRecord.

## Componente principal

ApprovalGate.

## Evento relacionado

EVENTO 12 — Fuera de alcance.

EVENTO 5 — Bloqueo automático si no aplica subtipo específico.

## Registro de auditoría relacionado

REGISTRO 12 — Permiso.

REGISTRO 10 — Bloqueo.

## Acción esperada del usuario

Ampliar permiso, corregir alcance o cancelar.

## Restricción

Permiso parcial no significa permiso total.

---

# TIPO 8 — ALERTA DE ALCANCE EXCEDIDO

## Qué muestra

Que una acción intenta salir del documento, fase, modo o límite autorizado.

## Cuándo aparece

Cuando el alcance activo no cubre la acción solicitada.

## Riesgo típico

Nivel 2 a Nivel 4.

## Modelo principal

SystemState / RiskRecord.

## Componente principal

ApprovalGate.

## Evento relacionado

EVENTO 12 — Fuera de alcance.

## Registro de auditoría relacionado

REGISTRO 13 — Alcance.

REGISTRO 10 — Bloqueo.

## Acción esperada del usuario

Definir nuevo alcance o pausar.

## Restricción

Robert debe detenerse si el alcance no alcanza.

---

# TIPO 9 — MENSAJE DE BLOQUEO

## Qué muestra

Que una acción no puede continuar.

## Cuándo aparece

Cuando una acción está prohibida, no autorizada, fuera de fase o bloqueada manualmente por el usuario.

## Riesgo típico

Nivel 3 o Nivel 4 para bloqueos por riesgo.

Acción de control fuera de la escala de riesgo cuando el bloqueo manual viene del usuario.

## Modelo principal

RiskRecord / PendingDecision.

## Componente principal

ApprovalGate.

## Evento relacionado

EVENTO 5 — Bloqueo automático.

EVENTO 6 — Bloqueo manual solicitado.

EVENTO 7 — Acción prohibida.

EVENTOS 15 al 20 si aplica subtipo específico.

## Registro de auditoría relacionado

REGISTRO 10 — Bloqueo.

## Acción esperada del usuario

Aceptar bloqueo, corregir solicitud, convertirlo en borrador/documentación o indicar nuevo alcance.

## Restricción

Bloqueo no debe ofrecer ejecución real como alternativa.

Bloqueo manual solicitado reduce alcance; no aumenta riesgo.

---

# TIPO 10 — ALERTA DE CONTRADICCIÓN DOCUMENTAL

## Qué muestra

Que dos documentos entran en conflicto.

## Cuándo aparece

Cuando hay contradicción entre:

- COMMANDS.
- USER_ACTIONS.
- SECURITY_RULES.
- PHASES.
- DATA_MODEL_SPEC.
- COMPONENTS_SPEC.
- ERROR_AND_BLOCKING_SPEC.
- PERMISSIONS_AND_SCOPES_SPEC.
- AUDIT_TRAIL_SPEC.

## Riesgo típico

Nivel 2 o Nivel 3.

Nivel 4 si permitiría ejecución real o avance incorrecto de fase.

## Modelo principal

RiskRecord.

## Componente principal

DocumentStatusMap.

## Evento relacionado

EVENTO 10 — Contradicción documental.

## Registro de auditoría relacionado

REGISTRO 16 — Contradicción documental.

## Acción esperada del usuario

Corregir documento, pausar o decidir cuál documento domina.

## Restricción

Robert no debe avanzar si la contradicción afecta seguridad, permisos, fases o ejecución.

---

# TIPO 11 — ALERTA DE FASE INCORRECTA

## Qué muestra

Que la acción pertenece a una fase futura.

## Cuándo aparece

Cuando se intenta:

- Programar.
- Crear app real.
- Crear base de datos.
- Conectar herramientas.
- Automatizar.
- Activar agentes.
- Ejecutar acciones reales.
- Avanzar a Fase 11 sin decisión formal.

## Riesgo típico

Nivel 4 — Crítico.

## Modelo principal

ModeState / RiskRecord.

## Componente principal

ApprovalGate.

## Evento relacionado

EVENTO 20 — Fase incorrecta.

EVENTO 11 — Riesgo crítico si implica riesgo Nivel 4.

## Registro de auditoría relacionado

REGISTRO 17 — Capacidad futura no disponible.

REGISTRO 10 — Bloqueo.

## Acción esperada del usuario

Mantenerlo como documentación futura o pausar.

## Restricción

No puede activarse en Fase 10.

---

# TIPO 12 — ALERTA DE CAPACIDAD FUTURA NO DISPONIBLE

## Qué muestra

Que la capacidad solicitada todavía no existe o no está autorizada.

## Cuándo aparece

Cuando el usuario pide:

- Conectar Gmail.
- Conectar Google Calendar.
- Conectar GitHub automáticamente.
- Activar agentes.
- Crear logs reales.
- Crear notificaciones reales.
- Ejecutar código.
- Automatizar procesos.

## Riesgo típico

Nivel 2 o Nivel 3 si solo se documenta como capacidad futura.

Nivel 4 si intenta activarse como capacidad real.

## Modelo principal

PendingDecision / ModeState.

## Componente principal

ApprovalGate.

## Evento relacionado

EVENTO 8 — Acción futura no disponible.

EVENTOS 15 al 20 si la capacidad futura intenta activarse como acción real.

## Registro de auditoría relacionado

REGISTRO 17 — Capacidad futura no disponible.

## Acción esperada del usuario

Documentar como capacidad futura, convertir en especificación conceptual o cancelar.

## Restricción

Puede diseñarse conceptualmente, no activarse.

---

# TIPO 13 — AVISO DE CAMBIO REGISTRADO

## Qué muestra

Que un cambio fue registrado o debe registrarse.

## Cuándo aparece

Cuando se registra:

- CAMBIO.
- Corrección.
- Integración.
- Actualización de HOME.
- Actualización de README.

## Riesgo típico

Nivel 2 o Nivel 3.

## Modelo principal

ChangeRecord.

## Componente principal

DocumentStatusMap.

## Evento relacionado

Ninguno obligatorio.

Puede relacionarse con EVENTO 3 si requiere aprobación previa.

## Registro de auditoría relacionado

REGISTRO 7 — Cambio.

## Acción esperada del usuario

Confirmar que el cambio fue registrado manualmente.

## Restricción

Robert no debe inventar cambios.

---

# TIPO 14 — AVISO DE DECISIÓN REGISTRADA

## Qué muestra

Que una decisión fue registrada o debe registrarse.

## Cuándo aparece

Cuando el usuario aprueba, rechaza, pausa o decide formalmente.

## Riesgo típico

Nivel 2 o Nivel 3.

## Modelo principal

DecisionRecord.

## Componente principal

DecisionInbox.

## Evento relacionado

EVENTO 3 — Aprobación formal requerida cuando aplique.

EVENTO 4 — Pausa obligatoria cuando la decisión sea pausar.

## Registro de auditoría relacionado

REGISTRO 6 — Decisión.

## Acción esperada del usuario

Confirmar registro manual o pasar al cambio relacionado.

## Restricción

Robert no debe inventar decisiones.

---

# TIPO 15 — AVISO DE RESPALDO MANUAL

## Qué muestra

Estado del respaldo manual en GitHub.

## Cuándo aparece

Cuando el usuario confirma:

- Ya actualicé README.
- Ya actualicé HOME.
- Ya registré CAMBIO.
- Ya hice commit.

## Riesgo típico

Nivel 1 o Nivel 2.

## Modelo principal

GitHubBackupStatus.

## Componente principal

TopBar.

## Evento relacionado

Ninguno obligatorio.

## Registro de auditoría relacionado

REGISTRO 15 — Respaldo manual.

## Acción esperada del usuario

Confirmar si falta otro documento o cierre de bloque.

## Restricción

Robert no debe decir que GitHub fue actualizado automáticamente.

---

# TIPO 16 — AVISO DE SANDBOX MANUAL

## Qué muestra

Estado, requisito, límite o resultado de una simulación sandbox manual.

## Cuándo aparece

Cuando se inicia, revisa o cierra prueba sandbox.

También aparece cuando:

- Una acción requiere sandbox antes de avanzar.
- Una simulación excede los límites del sandbox.
- Una prueba intenta convertirse en ejecución real.

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

EVENTO 5, EVENTO 12 o EVENTOS 15 al 20 según el caso probado.

## Registro de auditoría relacionado

REGISTRO 14 — Sandbox.

## Acción esperada del usuario

Registrar resultado, corregir regla, aprobar cierre o pausar.

## Restricción

Sandbox manual no ejecuta acciones reales.

Sandbox manual no conecta herramientas.

Sandbox manual no activa automatizaciones.

---

# TIPO 17 — AVISO DE SIGUIENTE PASO

## Qué muestra

El próximo paso permitido dentro del alcance actual.

## Cuándo aparece

Al cerrar un bloque, terminar un documento o resolver una decisión.

## Riesgo típico

Nivel 0 o Nivel 1.

Puede subir si el siguiente paso afecta documento técnico, seguridad o fase.

## Modelo principal

SystemState.

## Componente principal

CurrentStatePanel.

## Evento relacionado

Ninguno obligatorio.

Puede relacionarse con EVENTO 3 si el siguiente paso requiere aprobación.

Puede relacionarse con EVENTO 9 si falta información para definir el siguiente paso.

## Registro de auditoría relacionado

REGISTRO 1 — Informativo.

## Acción esperada del usuario

Elegir continuar, revisar, corregir, aprobar o pausar.

## Restricción

Robert puede recomendar, no decidir por el usuario.

---

# CORRESPONDENCIA CON USER_ACTIONS_SPEC v0.2

| Acción | Tipo de notificación esperado | Evento relacionado si aplica |
|---|---|---|
| ACCIÓN 1 — Escribir comando | TIPO 3 — Comando reconocido o TIPO 4 — Comando ambiguo | EVENTO 9 o EVENTO 12 si falta información o alcance |
| ACCIÓN 2 — Seleccionar documento | TIPO 2 — Notificación de estado | Ninguno obligatorio |
| ACCIÓN 3 — Revisar estado general | TIPO 1 — Informativa | Ninguno obligatorio |
| ACCIÓN 4 — Crear documento técnico | TIPO 5 — Advertencia de riesgo si aplica | EVENTO 3 si requiere aprobación |
| ACCIÓN 5 — Corregir documento técnico | TIPO 5 o TIPO 6 | EVENTO 3 si requiere aprobación |
| ACCIÓN 6 — Aprobar documento | TIPO 6 — Confirmación requerida | EVENTO 3 |
| ACCIÓN 7 — Registrar decisión | TIPO 14 — Decisión registrada | EVENTO 3 si requiere aprobación |
| ACCIÓN 8 — Registrar cambio | TIPO 13 — Cambio registrado | EVENTO 3 si depende de aprobación |
| ACCIÓN 9 — Actualizar HOME | TIPO 13 — Cambio registrado | Ninguno obligatorio |
| ACCIÓN 10 — Actualizar README | TIPO 13 — Cambio registrado | Ninguno obligatorio |
| ACCIÓN 11 — Cambiar modo | TIPO 2 o TIPO 11 si no autorizado | EVENTO 20 si fase incorrecta |
| ACCIÓN 12 — Solicitar sandbox manual | TIPO 16 — Sandbox manual | EVENTO 13 o EVENTO 14 si aplica |
| ACCIÓN 13 — Pausar avance | TIPO 2 — Estado / pausa aplicada | EVENTO 4 — Pausa obligatoria |
| ACCIÓN 14 — Solicitar bloqueo manual | TIPO 9 — Mensaje de bloqueo manual | EVENTO 6 — Bloqueo manual solicitado |
| ACCIÓN 15 — Ver decisiones pendientes | TIPO 6 o TIPO 14 | EVENTO 3 si requiere decisión |
| ACCIÓN 16 — Resolver decisión pendiente | TIPO 6 o TIPO 14 | EVENTO 3 |
| ACCIÓN 17 — Ver mapa documental | TIPO 2 — Estado | Ninguno obligatorio |
| ACCIÓN 18 — Marcar respaldo manual en GitHub | TIPO 15 — Respaldo manual | Ninguno obligatorio |
| ACCIÓN 19 — Solicitar revisión crítica | TIPO 5 o TIPO 10 si hay contradicción | EVENTO 10 si hay contradicción |
| ACCIÓN 20 — Pedir siguiente paso | TIPO 17 — Siguiente paso | EVENTO 9 si falta información |

---

# RELACIÓN CON ERROR_AND_BLOCKING_SPEC

Si una acción requiere aprobación, pausa, bloqueo, detecta contradicción, falta información, supera alcance o intenta activar capacidad futura, debe mostrarse una alerta conectada a evento.

Eventos relevantes para notificaciones y alertas:

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

Nota:

EVENTO 1 y EVENTO 2 pueden quedar cubiertos por notificaciones informativas, advertencias o confirmaciones genéricas cuando no requieran tratamiento fuerte.

Regla:

**Toda alerta de bloqueo debe indicar evento, motivo y próximo paso permitido.**

Regla adicional:

**Las acciones de control como PAUSA, DETENTE, NO_AVANCES y bloqueo manual están fuera de la escala de riesgo.**

---

# TABLA DE RELACIÓN ENTRE TIPOS Y EVENTOS

| Tipo de aviso | Evento relacionado | Motivo |
|---|---|---|
| TIPO 2 — Estado / pausa | EVENTO 4 | Cuando el avance debe pausarse |
| TIPO 3 — Comando reconocido | EVENTO 3 | Si el comando requiere aprobación |
| TIPO 3 — Comando reconocido | EVENTO 4 | Si el comando es de pausa/control |
| TIPO 4 — Comando ambiguo o falta de información | EVENTO 9 | Cuando falta información |
| TIPO 4 — Comando ambiguo o falta de información | EVENTO 12 | Cuando no hay alcance suficiente |
| TIPO 5 — Advertencia de riesgo | EVENTO 11 | Cuando el riesgo es crítico |
| TIPO 6 — Confirmación requerida | EVENTO 3 | Acción necesita aprobación explícita |
| TIPO 7 — Permiso insuficiente | EVENTO 12 | La acción supera el permiso |
| TIPO 8 — Alcance excedido | EVENTO 12 | La acción sale del alcance |
| TIPO 9 — Bloqueo | EVENTO 5 | Bloqueo general |
| TIPO 9 — Bloqueo manual | EVENTO 6 | Usuario solicita bloqueo manual |
| TIPO 9 — Acción prohibida | EVENTO 7 | Acción no permitida |
| TIPO 9 — Bloqueo específico | EVENTOS 15 al 20 | Bloqueo específico |
| TIPO 10 — Contradicción documental | EVENTO 10 | Conflicto entre documentos |
| TIPO 11 — Fase incorrecta | EVENTO 20 | Acción pertenece a fase futura |
| TIPO 12 — Capacidad futura no disponible | EVENTO 8 | Capacidad todavía no disponible |
| TIPO 12 — Capacidad futura intentando activarse | EVENTOS 15 al 20 | Depende de la capacidad solicitada |
| TIPO 14 — Decisión registrada / pausa | EVENTO 4 | Cuando la decisión es pausar |
| TIPO 16 — Sandbox manual | EVENTO 13 | Sandbox requerido |
| TIPO 16 — Sandbox manual | EVENTO 14 | Sandbox excedido |
| TIPO 16 — Sandbox manual | EVENTOS 5, 12 o 15 al 20 | Según el caso probado |
| TIPO 17 — Siguiente paso | EVENTO 9 | Si falta información para definirlo |

---

# RELACIÓN CON PERMISSIONS_AND_SCOPES_SPEC

PERMISSIONS_AND_SCOPES_SPEC define si existe permiso suficiente.

NOTIFICATION_AND_ALERTS_SPEC define qué mensaje aparece cuando:

- El permiso alcanza.
- El permiso no alcanza.
- El permiso es ambiguo.
- El permiso expiró.
- El permiso fue revocado.
- El permiso intenta activar algo prohibido.
- El permiso intenta activar una capacidad futura no disponible.

Regla:

**Toda alerta de permiso debe mostrar el alcance autorizado y el alcance excedido.**

---

# RELACIÓN CON AUDIT_TRAIL_SPEC

AUDIT_TRAIL_SPEC define qué rastro queda.

NOTIFICATION_AND_ALERTS_SPEC define qué se le muestra al usuario.

Regla:

**No toda notificación genera registro formal, pero toda alerta importante debe poder conectarse a un registro de auditoría.**

---

# RELACIÓN CON ROBERT_COMMANDS

ROBERT_COMMANDS v0.4 define comandos.

NOTIFICATION_AND_ALERTS_SPEC define qué mensaje conceptual debe responder Robert ante comandos.

Ejemplos:

- `APRUEBO` genera confirmación de aprobación y registro pendiente.
- `DETENTE` genera aviso de pausa/control.
- `PAUSA` genera aviso de pausa obligatoria.
- `NO_AVANCES` genera aviso de alcance detenido.
- `SOLO_BORRADOR` genera aviso de restricción.
- `MODO_SANDBOX` genera aviso de sandbox manual.
- `REVOCA_AUTONOMIA` genera aviso de reducción de alcance.
- `BLOQUEA` genera aviso de bloqueo manual solicitado.

Regla:

**Los comandos de control deben producir aviso claro de estado, aunque estén fuera de la escala de riesgo.**

---

# RELACIÓN CON SCREEN_STATE_SPEC

SCREEN_STATE_SPEC define qué se ve.

NOTIFICATION_AND_ALERTS_SPEC define qué mensajes deben aparecer dentro de esas zonas.

Ejemplo:

- TopBar muestra estado resumido.
- CurrentStatePanel muestra detalle.
- RiskBadge muestra riesgo.
- ApprovalGate muestra confirmación o bloqueo.
- DecisionInbox muestra pendientes.
- DocumentStatusMap muestra documentos afectados.
- ModeSelector muestra modo, sandbox o restricción.

---

# RELACIÓN CON INTERACTION_FLOW_SPEC

INTERACTION_FLOW_SPEC define cómo se mueve la información.

NOTIFICATION_AND_ALERTS_SPEC no debe crear flujos nuevos.

Si una notificación requiere flujo nuevo, primero debe corregirse INTERACTION_FLOW_SPEC.

---

# RELACIÓN CON COMPONENTS_SPEC

COMPONENTS_SPEC define los componentes.

NOTIFICATION_AND_ALERTS_SPEC solo asigna mensajes a componentes ya existentes.

No crea componentes nuevos.

Si en el futuro se requiere un componente llamado:

```text
NotificationCenter
AlertPanel
```

primero deberá corregirse y aprobarse:

```text
ROBERT_TECHNICAL_COMPONENTS_SPEC
```

---

# RELACIÓN CON SANDBOX

NOTIFICATION_AND_ALERTS_SPEC no redefine sandbox.

La lógica de sandbox vive en:

- ROBERT_SANDBOX
- SANDBOX_RULES
- SANDBOX_TESTS
- SANDBOX_RESULTS

Este documento solo define qué aviso debe mostrarse durante simulaciones sandbox manuales.

Regla:

**Sandbox manual debe avisar claramente que es simulación y no ejecución real.**

---

# REGLAS DE BLOQUEO POR NOTIFICACIONES

Robert debe bloquear o pausar cuando:

- Se intenta enviar notificación real.
- Se intenta enviar email real.
- Se intenta activar push notification.
- Se intenta crear sistema real de alertas.
- Se intenta crear NotificationRecord sin actualizar DATA_MODEL_SPEC.
- Se intenta crear AlertRecord sin actualizar DATA_MODEL_SPEC.
- Se intenta crear NotificationCenter sin actualizar COMPONENTS_SPEC.
- Se intenta crear AlertPanel sin actualizar COMPONENTS_SPEC.
- Se intenta decir que una alerta fue enviada externamente.
- Se intenta conectar Gmail, Calendar, GitHub o APIs para notificar.
- Se intenta automatizar avisos.
- Se intenta avanzar a Fase 11 automáticamente.

---

# MATRIZ DE NOTIFICACIONES

| Situación | Aviso esperado | Componente principal |
|---|---|---|
| Estado consultado | Informativo | CurrentStatePanel |
| Comando ambiguo | Alerta de ambigüedad | ApprovalGate |
| Falta información | Alerta de información faltante | ApprovalGate |
| Riesgo detectado | Advertencia de riesgo | RiskBadge |
| Riesgo crítico | Alerta crítica | RiskBadge |
| Aprobación requerida | Confirmación | ApprovalGate |
| Pausa obligatoria | Aviso de pausa | TopBar / CurrentStatePanel |
| Permiso insuficiente | Alerta de permiso | ApprovalGate |
| Alcance excedido | Alerta de alcance | ApprovalGate |
| Bloqueo automático | Mensaje de bloqueo | ApprovalGate |
| Bloqueo manual solicitado | Mensaje de bloqueo manual | ApprovalGate |
| Acción prohibida | Mensaje de bloqueo | ApprovalGate |
| Acción futura no disponible | Alerta de capacidad futura | ApprovalGate |
| Contradicción documental | Alerta documental | DocumentStatusMap |
| Sandbox requerido | Aviso de sandbox | ModeSelector |
| Sandbox excedido | Alerta de sandbox | ModeSelector / ApprovalGate |
| Fase incorrecta | Alerta crítica | ApprovalGate |
| Capacidad futura intentando activarse | Alerta de no disponible / bloqueo | ApprovalGate |
| Cambio registrado | Aviso de cambio | DocumentStatusMap |
| Decisión registrada | Aviso de decisión | DecisionInbox |
| Respaldo manual | Aviso de respaldo | TopBar |
| Sandbox manual | Aviso de sandbox | ModeSelector |
| Siguiente paso | Aviso de siguiente paso | CurrentStatePanel |

---

# FORMATO MÍNIMO DE MENSAJE

Todo aviso importante debe poder mostrar:

```text
Tipo de aviso:
Qué ocurrió:
Documento afectado:
Riesgo:
Permiso:
Alcance:
Evento relacionado:
Registro de auditoría relacionado:
Acción permitida:
Acción no permitida:
Siguiente paso:
```

---

# EJEMPLO — CONFIRMACIÓN REQUERIDA

```text
Tipo de aviso: Confirmación requerida
Qué ocurrió: Se solicita aprobar AUDIT_TRAIL_SPEC v0.2
Documento afectado: ROBERT_TECHNICAL_AUDIT_TRAIL_SPEC
Riesgo: Nivel 3 — Alto
Permiso: Aprobación documental explícita requerida
Alcance: Aprobar documento técnico, no programar
Evento relacionado: EVENTO 3 — Aprobación formal requerida
Registro de auditoría relacionado: REGISTRO 8 — Aprobación
Acción permitida: Aprobar, corregir, revisar o pausar
Acción no permitida: Programar, conectar herramientas, avanzar a Fase 11
Siguiente paso: Esperar respuesta del usuario
```

---

# EJEMPLO — BLOQUEO POR FASE INCORRECTA

```text
Tipo de aviso: Bloqueo
Qué ocurrió: Se intentó activar conexión externa
Documento afectado: Ninguno todavía
Riesgo: Nivel 4 — Crítico
Permiso: No autorizado
Alcance: Fase 10 documental
Evento relacionado: EVENTO 20 — Fase incorrecta
Registro de auditoría relacionado: REGISTRO 17 — Capacidad futura no disponible
Acción permitida: Documentar como capacidad futura
Acción no permitida: Conectar herramienta externa
Siguiente paso: Mantenerlo como especificación futura o pausar
```

---

# EJEMPLO — ACCIÓN FUTURA NO DISPONIBLE

```text
Tipo de aviso: Capacidad futura no disponible
Qué ocurrió: El usuario solicita una capacidad que todavía no existe en Fase 10
Documento afectado: Ninguno todavía
Riesgo: Nivel 2 o Nivel 3 si solo se documenta
Permiso: Diseño conceptual permitido
Alcance: Documentar como capacidad futura
Evento relacionado: EVENTO 8 — Acción futura no disponible
Registro de auditoría relacionado: REGISTRO 17 — Capacidad futura no disponible
Acción permitida: Documentar o diseñar conceptualmente
Acción no permitida: Activar, conectar, automatizar o ejecutar
Siguiente paso: Crear especificación futura o pausar
```

---

# EJEMPLO — PAUSA OBLIGATORIA

```text
Tipo de aviso: Pausa obligatoria
Qué ocurrió: El usuario pidió PAUSA o NO_AVANCES
Documento afectado: Depende del contexto activo
Riesgo: Acción de control fuera de la escala de riesgo
Permiso: Revocación o reducción de alcance
Alcance: Avance detenido
Evento relacionado: EVENTO 4 — Pausa obligatoria
Registro de auditoría relacionado: REGISTRO 10 — Bloqueo si detiene acción relevante
Acción permitida: Esperar nueva instrucción del usuario
Acción no permitida: Continuar automáticamente
Siguiente paso: Pausar aquí
```

---

# EJEMPLO — BLOQUEO MANUAL SOLICITADO

```text
Tipo de aviso: Bloqueo manual solicitado
Qué ocurrió: El usuario pidió bloquear la acción o detener el avance
Documento afectado: Depende del contexto activo
Riesgo: Acción de control fuera de la escala de riesgo
Permiso: Bloqueo manual autorizado por el usuario
Alcance: Acción detenida
Evento relacionado: EVENTO 6 — Bloqueo manual solicitado
Registro de auditoría relacionado: REGISTRO 10 — Bloqueo
Acción permitida: Mantener bloqueo o pedir nuevo alcance
Acción no permitida: Continuar con la acción bloqueada
Siguiente paso: Esperar instrucción del usuario
```

---

# CRITERIOS DE ACEPTACIÓN

Este documento podrá considerarse listo para aprobación si:

- Define notificaciones conceptuales.
- Define alertas conceptuales.
- Define advertencias conceptuales.
- Define confirmaciones conceptuales.
- Define mensajes de bloqueo conceptuales.
- Aclara que no crea NotificationRecord.
- Aclara que no crea AlertRecord.
- Aclara que no crea NotificationCenter.
- Aclara que no crea AlertPanel.
- Conecta notificaciones con los 11 modelos de DATA_MODEL_SPEC v0.1.
- Define componentes participantes.
- Define dónde aparece cada tipo de aviso.
- Uniforma los 17 tipos de notificación.
- Conecta acciones de USER_ACTIONS_SPEC v0.2 con avisos.
- Conecta ACCIÓN 13 — Pausar avance con EVENTO 4.
- Conecta ACCIÓN 14 — Solicitar bloqueo manual con EVENTO 6.
- Conecta eventos de ERROR_AND_BLOCKING_SPEC v0.2 con alertas.
- Incluye EVENTO 3 — Aprobación formal requerida.
- Incluye EVENTO 4 — Pausa obligatoria.
- Incluye EVENTO 5 — Bloqueo automático.
- Incluye EVENTO 6 — Bloqueo manual solicitado.
- Incluye EVENTO 7 — Acción prohibida.
- Incluye EVENTO 8 — Acción futura no disponible.
- Incluye EVENTO 9 — Falta de información.
- Incluye EVENTO 10 — Contradicción documental.
- Incluye EVENTO 11 — Riesgo crítico.
- Incluye EVENTO 12 — Fuera de alcance.
- Incluye EVENTO 13 — Sandbox requerido.
- Incluye EVENTO 14 — Sandbox excedido.
- Incluye EVENTOS 15 al 20 como eventos de bloqueo específico.
- Conecta permisos con avisos.
- Conecta audit trail con avisos.
- Mantiene Nivel 0 únicamente como Informativo.
- Mantiene acciones de control fuera de la escala de riesgo.
- No crea modelos nuevos oficiales.
- No crea componentes nuevos oficiales.
- No autoriza programación.
- No autoriza código real.
- No autoriza pantallas reales.
- No autoriza notificaciones reales.
- No autoriza emails.
- No autoriza push notifications.
- No autoriza base de datos real.
- No autoriza conexiones externas.
- No autoriza automatizaciones.
- No autoriza agentes autónomos.
- Mantiene a Robert en Fase 10.
- Mantiene control total del usuario.

---

# RIESGO DEL DOCUMENTO

Tipo de cambio:

**Cambio técnico documental / notificaciones y alertas conceptuales**

Nivel de riesgo inicial:

**Nivel 3 — Alto**

Motivo:

Este documento define cómo Robert comunica riesgos, bloqueos, permisos, confirmaciones, advertencias y estados al usuario. Aunque sigue siendo conceptual, influye en seguridad, claridad operativa y control futuro.

Nivel de riesgo final esperado:

**Nivel 2 — Medio**

Motivo de reducción:

El documento es documental. No crea notificaciones reales, no crea sistema real de alertas, no crea base de datos real, no crea modelos nuevos oficiales, no crea componentes nuevos oficiales, no programa, no conecta herramientas externas y no ejecuta acciones.

Nivel de autonomía:

**Nivel 0 — Sin autonomía ejecutiva**

---

# ESTADO DE APROBACIÓN

Este documento está formalmente:

```text
APPROVED
INTEGRATED
```

La trazabilidad correspondiente se encuentra registrada en:

```text
ROBERT_DECISIONS_LOG
ROBERT_CONTROL_DE_CAMBIOS
```

No requiere nueva aprobación para reconocer su estado vigente.

---

# RESTRICCIONES

La aprobación documental no autoriza:

```text
PROGRAMMING
AUTOMATIC EXECUTION
EXTERNAL CONNECTIONS
AUTONOMOUS AGENTS
AUTOMATIC PHASE TRANSITION
PHASE 11
```

Se mantiene:

```text
AUTONOMY_LEVEL = 0
EXECUTION_AUTHORITY = NONE
```

---

# CIERRE

El documento permanece como especificación técnica documental aprobada dentro de Fase 10.

Su aprobación no implica implementación técnica productiva.

El usuario mantiene control total.
