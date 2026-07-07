# ROBERT_TECHNICAL_USER_ACTIONS_SPEC

Versión: v0.2 (sin cambio de número — documento ya aprobado)  
Estado: Aprobado — auditoría voluntaria completada sin hallazgos que requieran corrección de contenido  
Fecha de auditoría: 07/07/2026  
Ubicación: 10_MVP  
Fase relacionada: Fase 10 — MVP técnico básico en preparación  
Documento base principal: ROBERT_TECHNICAL_SCREEN_STATE_SPEC v0.2  
Documentos relacionados: ROBERT_TECHNICAL_INTERACTION_FLOW_SPEC v0.2, ROBERT_TECHNICAL_COMPONENTS_SPEC v0.2, ROBERT_TECHNICAL_DATA_MODEL_SPEC v0.1, ROBERT_TECHNICAL_ERROR_AND_BLOCKING_SPEC v0.2, ROBERT_TECHNICAL_PERMISSIONS_AND_SCOPES_SPEC v0.2, ROBERT_TECHNICAL_AUDIT_TRAIL_SPEC v0.2, ROBERT_TECHNICAL_NOTIFICATION_AND_ALERTS_SPEC v0.2, ROBERT_TECHNICAL_SESSION_AND_CONTEXT_SPEC v0.2, ROBERT_TECHNICAL_DATA_CONSISTENCY_AND_CONFLICT_RESOLUTION_SPEC v0.3  
Fuente de verdad actual: ROBERT_CONTEXT_MASTER v0.5  
Decisión relacionada: DECISIÓN #017  
Cambio relacionado: CAMBIO #028  

Tags: #robert/orbita-3 #capa/5 #tipo/tecnico #robert/mvp #robert/user-actions

---

# OBJETIVO

ROBERT_TECHNICAL_USER_ACTIONS_SPEC define qué acciones puede intentar hacer el usuario desde cada pantalla, panel o componente conceptual del MVP técnico básico de Robert.

Su objetivo es responder:

- Qué puede hacer el usuario desde cada vista.
- Qué acciones son permitidas.
- Qué acciones requieren confirmación.
- Qué acciones requieren aprobación formal.
- Qué acciones deben bloquearse.
- Qué componente recibe la acción.
- Qué flujo debe activarse.
- Qué riesgo tiene cada acción.
- Qué pasa después de cada acción.
- Qué acciones son solo informativas.
- Qué acciones son de control.
- Qué acciones son de cambio documental.
- Qué acciones son futuras o no disponibles.
- Qué acciones no deben confundirse con ejecución real.
- Cómo se relacionan las 20 acciones con ApprovalGate.
- Cómo se relacionan las 20 acciones con riesgo, auditoría, notificaciones, permisos y estados.

Este documento no programa la app.

Este documento no crea botones reales.

Este documento no crea pantallas reales.

Este documento no crea código.

Este documento no conecta herramientas externas.

Este documento no ejecuta acciones reales.

---

# ESTADO DEL DOCUMENTO

Este documento queda como:

**Aprobado — auditoría voluntaria completada sin hallazgos que requieran corrección de contenido**

Este documento ya estaba aprobado e integrado mediante:

```text
DECISIÓN #017
CAMBIO #028
```

La auditoría voluntaria no reabre su estado de aprobación.

La auditoría voluntaria no convierte este documento en borrador.

La auditoría voluntaria no lo convierte en propuesta corregida.

La auditoría voluntaria no requiere nueva decisión formal.

La auditoría voluntaria no requiere nuevo cambio formal porque no hubo corrección sustantiva de contenido.

No autoriza programación.

No autoriza prototipo funcional.

No autoriza base de datos real.

No autoriza conexiones externas.

No autoriza automatizaciones.

No autoriza agentes autónomos.

No autoriza ejecución real.

No autoriza avanzar a Fase 11.

---

# AUDITORÍA VOLUNTARIA DE v0.2

Esta sección documenta una revisión voluntaria de ROBERT_TECHNICAL_USER_ACTIONS_SPEC v0.2, ya aprobado e integrado mediante:

```text
DECISIÓN #017
CAMBIO #028
```

Motivo de la auditoría:

```text
El usuario solicitó volver a verificar este documento, sin que existiera 
un conflicto de aprobación real ni un hueco de trazabilidad pendiente.
```

Resultado de la auditoría:

```text
No se encontraron errores de contenido.
La lista canónica de 20 acciones es correcta y completa.
Los 10 componentes usados son los canónicos: AppShell incluido, MainCanvas ausente.
Se corrigió un detalle menor en la TABLA DE MAPEO CON APPROVAL GATE: ACCIÓN 12.
```

Clasificación:

```text
No aplica ningún TIPO de conflicto de DATA_CONSISTENCY_AND_CONFLICT_RESOLUTION_SPEC v0.3.
Esta auditoría no reabre el estado de aprobación del documento.
```

Regla aplicada:

```text
Según DOCUMENT_LIFECYCLE_SPEC v0.2, un documento aprobado que recibe un ajuste menor 
permanece en estado "Aprobado" — no regresa a "Borrador" ni a "Propuesta corregida".
```

Uso previsto de esta auditoría:

```text
Servir como referencia canónica confirmada para corregir 
ROBERT_TECHNICAL_APPROVAL_AND_AUTHORIZATION_GATE_SPEC v0.3, 
que sí tiene dos errores reales pendientes: uso de MainCanvas en vez de AppShell, 
y numeración incorrecta en 13 de las 20 acciones de su tabla de correspondencia.
```

---

# FUENTE CANÓNICA DE ESTA VERSIÓN

La lista canónica de acciones se mantiene con 20 acciones:

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

Regla:

```text
Esta numeración debe mantenerse igual en documentos posteriores.
```

---

# REGLA CENTRAL

El usuario manda.

Robert no ejecuta acciones importantes sin permiso.

Toda acción del usuario debe pasar por control de alcance, riesgo y autorización cuando aplique.

Regla principal:

**Intentar una acción no significa ejecutarla.**

---

# ESTADO ACTUAL DE ROBERT

Robert se encuentra en:

**Fase 10 — MVP técnico básico en preparación**

Estado operativo actual:

- MVP manual validado.
- Sandbox manual validado.
- GitHub configurado como respaldo documental privado y manual.
- Obsidian usado como cerebro documental manual.
- ROBERT_CONTEXT_MASTER v0.5 reanclado.
- ROBERT_PHASES v0.5 reconciliado.
- ROBERT_COMMANDS v0.4 aprobado e integrado.
- Escala de riesgo y autonomía unificada.
- ROBERT_TECHNICAL_MVP_PLAN aprobado.
- ROBERT_TECHNICAL_MVP_WIREFRAME v0.3 aprobado.
- ROBERT_TECHNICAL_COMPONENTS_SPEC v0.2 aprobado.
- ROBERT_TECHNICAL_DATA_MODEL_SPEC v0.1 aprobado e integrado.
- ROBERT_TECHNICAL_INTERACTION_FLOW_SPEC v0.2 aprobado e integrado.
- ROBERT_TECHNICAL_SCREEN_STATE_SPEC v0.2 aprobado e integrado.
- ROBERT_TECHNICAL_USER_ACTIONS_SPEC v0.2 aprobado e integrado, auditado sin cambios de fondo.
- ROBERT_TECHNICAL_ERROR_AND_BLOCKING_SPEC v0.2 aprobado.
- ROBERT_TECHNICAL_PERMISSIONS_AND_SCOPES_SPEC v0.2 aprobado.
- ROBERT_TECHNICAL_AUDIT_TRAIL_SPEC v0.2 aprobado.
- ROBERT_TECHNICAL_NOTIFICATION_AND_ALERTS_SPEC v0.2 aprobado.
- ROBERT_TECHNICAL_SESSION_AND_CONTEXT_SPEC v0.2 aprobado.
- ROBERT_TECHNICAL_DOCUMENT_LIFECYCLE_SPEC v0.2 aprobado.
- ROBERT_TECHNICAL_VERSIONING_AND_CHANGE_POLICY_SPEC v0.2 aprobado.
- ROBERT_TECHNICAL_DATA_CONSISTENCY_AND_CONFLICT_RESOLUTION_SPEC v0.3 aprobado.
- ROBERT_TECHNICAL_APPROVAL_AND_AUTHORIZATION_GATE_SPEC v0.2 pendiente de corrección, v0.3 por preparar.
- ROBERT_HOME v0.8 aprobado e integrado.
- Sin programación autorizada.
- Sin código real.
- Sin pantallas reales.
- Sin base de datos real.
- Sin conexiones externas.
- Sin automatizaciones reales.
- Sin agentes autónomos activos.
- Sin Fase 11 autorizada.

---

# ALCANCE AUTORIZADO

Este documento autoriza únicamente:

- Definir acciones conceptuales del usuario.
- Relacionar acciones con pantallas y componentes.
- Clasificar acciones por riesgo.
- Definir cuándo una acción requiere confirmación.
- Definir cuándo una acción requiere aprobación.
- Definir cuándo una acción debe bloquearse.
- Definir qué ocurre después de una acción.
- Definir la lista canónica de 20 acciones.
- Mantener alineación con SCREEN_STATE_SPEC v0.2.
- Mantener alineación con INTERACTION_FLOW_SPEC v0.2.
- Mantener alineación con COMPONENTS_SPEC v0.2.
- Mantener alineación con DATA_MODEL_SPEC v0.1.
- Mantener a Robert en modo documental, manual y supervisado.
- Servir como referencia canónica para corregir APPROVAL_AND_AUTHORIZATION_GATE_SPEC v0.3.

---

# ALCANCE NO AUTORIZADO

Este documento no autoriza:

- Programar la app.
- Crear código real.
- Crear botones reales.
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

# PRINCIPIO GENERAL DE ACCIÓN

Cada acción del usuario debe responder cinco preguntas:

1. ¿Qué quiere hacer el usuario?
2. ¿Desde qué pantalla o componente lo intenta?
3. ¿Qué documento, módulo o estado afecta?
4. ¿Qué nivel de riesgo tiene?
5. ¿Puede continuar, requiere aprobación o debe bloquearse?

Regla:

**Toda acción importante debe dejar claro su alcance antes de avanzar.**

---

# TIPOS DE ACCIONES

Las acciones del usuario se clasifican en:

1. Acción informativa.
2. Acción de navegación.
3. Acción de consulta.
4. Acción de creación documental.
5. Acción de corrección documental.
6. Acción de aprobación documental.
7. Acción de cambio de modo.
8. Acción de sandbox.
9. Acción de respaldo manual.
10. Acción de control.
11. Acción bloqueada por fase.
12. Acción prohibida.
13. Acción futura no disponible.

---

# NIVELES DE RIESGO APLICABLES

Robert usa la escala oficial:

```text
Nivel 0 — Informativo
Nivel 1 — Bajo
Nivel 2 — Medio
Nivel 3 — Alto
Nivel 4 — Crítico
```

Regla:

```text
No existe Nivel 5 como riesgo.
Nivel 5 solo puede existir como autonomía, no como riesgo.
```

Acciones de control:

```text
DETENTE
PAUSA
NO_AVANCES
BLOQUEA
CANCELA
NO EJECUTES
```

Regla:

```text
Las acciones de control están fuera de la escala de riesgo cuando funcionan como protección del usuario.
La acción bloqueada sí puede tener Nivel 3 o Nivel 4.
```

---

# COMPONENTES BASE

Este documento usa los 10 componentes aprobados:

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
No debe usarse como componente oficial en este documento.
```

---

# MODELOS RELACIONADOS

Este documento se apoya en los modelos definidos en DATA_MODEL_SPEC v0.1:

```text
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
```

Este documento no crea un modelo de datos nuevo oficial.

Las acciones del usuario se entienden conceptualmente como instrucciones, solicitudes o intentos de operación que pueden convertirse en:

- CommandRequest.
- PendingDecision.
- RiskRecord.
- DecisionRecord.
- ChangeRecord.
- ModeState.
- GitHubBackupStatus.
- ObsidianGraphStatus.

---

# ESTRUCTURA UNIFORME DE LAS 20 ACCIONES

Cada acción debe poder mostrar:

```text
Dónde ocurre:
Qué intenta hacer el usuario:
Ejemplos:
Componente principal:
Componentes relacionados:
Modelo principal:
Flujo activado:
Riesgo:
Resultado permitido:
Requiere aprobación:
Restricción:
Gate probable:
Evento relacionado:
Registro de auditoría relacionado:
Notificación relacionada:
```

---

# ACCIÓN 1 — ESCRIBIR COMANDO

## Dónde ocurre

CommandCenter.

## Qué intenta hacer el usuario

El usuario escribe una instrucción, comando, pregunta o solicitud.

## Ejemplos

- Crear un documento.
- Revisar una especificación.
- Corregir un texto.
- Clasificar una idea.
- Pedir un resumen.
- Pedir una recomendación.
- Aprobar un documento.
- Pausar el avance.

## Componente principal

CommandCenter.

## Componentes relacionados

- AppShell.
- RiskBadge.
- ApprovalGate.
- DecisionInbox.
- CurrentStatePanel.

## Modelo principal

CommandRequest.

## Flujo activado

- Clasificación de intención.
- Evaluación preliminar de riesgo.
- RiskBadge si aplica.
- ApprovalGate si aplica.
- PendingDecision si aplica.

## Riesgo

Variable.

Puede ser:

- Nivel 0 si solo pregunta algo.
- Nivel 1 si pide una explicación simple.
- Nivel 2 si afecta documento no crítico.
- Nivel 3 si afecta documento técnico, maestro o decisión formal.
- Nivel 4 si intenta ejecutar acción real, conectar herramientas o saltarse seguridad.

## Resultado permitido

Robert puede:

- Responder.
- Preparar borrador.
- Pedir confirmación.
- Marcar riesgo.
- Bloquear acción.
- Crear decisión pendiente.
- Sugerir siguiente paso.

## Requiere aprobación

Solo si la acción implica aprobación formal, integración, cambio maestro, fase, seguridad o decisión relevante.

## Restricción

CommandCenter no ejecuta acciones reales.

## Gate probable

Gate 0, Gate 1, Gate 2, Gate 3, Gate 5 o Gate 7 según intención.

## Evento relacionado

EVENTO 9 — Falta de información, si la instrucción es ambigua.  
EVENTO 15 — Ejecución no autorizada, si intenta ejecución real.

## Registro de auditoría relacionado

REGISTRO 3 — Revisión.  
REGISTRO 6 — Decisión, si se convierte en aprobación.

## Notificación relacionada

TIPO 1 — Informativa.  
TIPO 6 — Confirmación requerida.  
TIPO 9 — Bloqueo, si aplica.

---

# ACCIÓN 2 — SELECCIONAR DOCUMENTO

## Dónde ocurre

LeftSidebar o DocumentStatusMap.

## Qué intenta hacer el usuario

El usuario selecciona un documento para verlo, revisarlo o continuar trabajándolo.

## Ejemplos

- Abrir ROBERT_HOME.
- Abrir ROBERT_CONTEXT_MASTER.
- Abrir ROBERT_TECHNICAL_SCREEN_STATE_SPEC.
- Revisar CONTROL_DE_CAMBIOS.
- Ver documentos de 10_MVP.

## Componente principal

LeftSidebar.

## Componentes relacionados

- DocumentStatusMap.
- CurrentStatePanel.
- TopBar.
- AppShell.

## Modelo principal

RobertDocument.

## Flujo activado

- Selección de documento.
- Visualización de estado.
- Confirmación de documento activo.

## Riesgo

Nivel 0 — Informativo.

## Resultado permitido

Robert puede mostrar:

- Documento activo.
- Estado del documento.
- Versión.
- Carpeta.
- Relación con decisiones y cambios.
- Riesgo si aplica.

## Requiere aprobación

No.

## Restricción

Seleccionar un documento no lo modifica.

## Gate probable

Gate 0 o Gate 1.

## Evento relacionado

Ninguno obligatorio.

## Registro de auditoría relacionado

REGISTRO 3 — Revisión, si forma parte de una auditoría documental.

## Notificación relacionada

TIPO 1 — Informativa.

---

# ACCIÓN 3 — REVISAR ESTADO GENERAL

## Dónde ocurre

CurrentStatePanel o TopBar.

## Qué intenta hacer el usuario

El usuario quiere saber en qué estado está Robert.

## Ejemplos

- Ver fase actual.
- Ver último cambio.
- Ver última decisión.
- Ver si hay programación autorizada.
- Ver si hay conexiones activas.
- Ver si hay decisiones pendientes.

## Componente principal

CurrentStatePanel.

## Componentes relacionados

- TopBar.
- DecisionInbox.
- DocumentStatusMap.
- AppShell.

## Modelo principal

SystemState.

## Flujo activado

- Lectura de estado.
- Consulta de fase.
- Consulta de restricciones.
- Consulta de pendientes.

## Riesgo

Nivel 0 — Informativo.

## Resultado permitido

Robert puede mostrar estado actual.

## Requiere aprobación

No.

## Restricción

Ver estado no autoriza avanzar.

## Gate probable

Gate 0.

## Evento relacionado

Ninguno obligatorio.

## Registro de auditoría relacionado

REGISTRO 3 — Revisión, si forma parte de auditoría.

## Notificación relacionada

TIPO 1 — Informativa.

---

# ACCIÓN 4 — CREAR DOCUMENTO TÉCNICO

## Dónde ocurre

CommandCenter.

## Qué intenta hacer el usuario

El usuario pide crear un nuevo documento técnico dentro de Robert.

## Ejemplos

- Crear USER_ACTIONS_SPEC.
- Crear una nueva especificación técnica.
- Crear un documento de arquitectura.
- Crear un documento de reglas.

## Componente principal

CommandCenter.

## Componentes relacionados

- RiskBadge.
- ApprovalGate.
- DocumentStatusMap.
- CurrentStatePanel.
- AppShell.

## Modelo principal

RobertDocument.

## Flujo activado

- Crear borrador.
- Clasificar riesgo.
- Marcar documento como borrador o propuesta.
- Preparar bloque para copiar.

## Riesgo

Nivel 3 — Alto.

## Resultado permitido

Robert puede crear:

- Borrador documental.
- Propuesta pendiente de revisión.
- Texto para copiar y pegar.
- Commit sugerido.

## Requiere aprobación

No siempre para crear borrador.

Sí para aprobar formalmente.

## Restricción

Crear documento técnico no autoriza programación.

## Gate probable

Gate 2 — Autorización documental.

## Evento relacionado

EVENTO 3 — Aprobación formal requerida, si el usuario intenta aprobar.  
EVENTO 12 — Fuera de alcance, si excede documentación.

## Registro de auditoría relacionado

REGISTRO 5 — Corrección, si es una versión corregida.  
REGISTRO 7 — Cambio, si se registra formalmente.

## Notificación relacionada

TIPO 6 — Confirmación requerida.

---

# ACCIÓN 5 — CORREGIR DOCUMENTO TÉCNICO

## Dónde ocurre

CommandCenter.

## Qué intenta hacer el usuario

El usuario detecta errores, contradicciones o inconsistencias y pide corregir un documento.

## Ejemplos

- Corregir SCREEN_STATE_SPEC.
- Corregir INTERACTION_FLOW_SPEC.
- Alinear datos entre documentos.
- Eliminar contradicciones.
- Cambiar estado de borrador a propuesta corregida.

## Componente principal

CommandCenter.

## Componentes relacionados

- RiskBadge.
- ApprovalGate.
- DocumentStatusMap.
- CurrentStatePanel.
- AppShell.

## Modelo principal

ChangeRecord.

## Flujo activado

- Detectar conflicto.
- Proponer corrección.
- Crear versión corregida.
- Mantener pendiente de revisión.
- Preparar cambio si aplica.

## Riesgo

Nivel 3 — Alto al inicio.

Puede bajar a Nivel 2 si queda limitado a corrección documental.

## Resultado permitido

Robert puede:

- Corregir el documento.
- Marcarlo como propuesta corregida.
- Mantenerlo pendiente de revisión.
- Preparar cambio para CONTROL_DE_CAMBIOS.
- Preparar actualización de HOME y README.

## Requiere aprobación

No para preparar propuesta corregida.

Sí para aprobar e integrar.

## Restricción

Corregir no significa aprobar.

## Gate probable

Gate 2 — Autorización documental.

## Evento relacionado

EVENTO 10 — Contradicción documental.  
EVENTO 9 — Falta de información, si falta fuente.

## Registro de auditoría relacionado

REGISTRO 5 — Corrección.  
REGISTRO 16 — Contradicción documental, si aplica.

## Notificación relacionada

TIPO 10 — Alerta de contradicción documental.

---

# ACCIÓN 6 — APROBAR DOCUMENTO

## Dónde ocurre

CommandCenter o DecisionInbox.

## Qué intenta hacer el usuario

El usuario aprueba formalmente un documento.

## Ejemplos

- APRUEBO SCREEN_STATE_SPEC v0.2.
- APRUEBO INTERACTION_FLOW_SPEC v0.2.
- Aprobar un documento técnico.
- Aprobar integración documental.

## Componente principal

DecisionInbox.

## Componentes relacionados

- ApprovalGate.
- RiskBadge.
- DocumentStatusMap.
- CurrentStatePanel.
- AppShell.

## Modelo principal

DecisionRecord.

## Flujo activado

- Validar aprobación explícita.
- Validar documento y versión.
- Registrar decisión.
- Preparar cambio de integración.

## Riesgo

Nivel 3 — Alto.

## Resultado permitido

Robert puede preparar:

- Registro de decisión.
- Registro de cambio.
- Actualización de HOME.
- Actualización de README.
- Estado aprobado e integrado.

## Requiere aprobación

Sí.

Debe existir instrucción clara del usuario.

## Restricción

Aprobar documento no autoriza ejecución real.

## Gate probable

Gate 3 — Aprobación formal.

## Evento relacionado

EVENTO 3 — Aprobación formal requerida.  
EVENTO 9 — Falta de información, si falta versión.

## Registro de auditoría relacionado

REGISTRO 6 — Decisión.  
REGISTRO 8 — Aprobación.

## Notificación relacionada

TIPO 6 — Confirmación requerida.

---

# ACCIÓN 7 — REGISTRAR DECISIÓN

## Dónde ocurre

CommandCenter.

## Qué intenta hacer el usuario

El usuario registra una decisión formal en ROBERT_DECISIONS_LOG.

## Ejemplos

- Registrar DECISIÓN #015.
- Registrar aprobación de documento.
- Registrar cambio de estado.
- Registrar decisión de no avanzar.

## Componente principal

CommandCenter.

## Componentes relacionados

- DecisionInbox.
- DocumentStatusMap.
- CurrentStatePanel.
- AppShell.

## Modelo principal

DecisionRecord.

## Flujo activado

- Crear bloque para DECISIONS_LOG.
- Relacionar decisión con documento.
- Relacionar decisión con versión.
- Preparar siguiente cambio si aplica.

## Riesgo

Nivel 2 o Nivel 3.

Nivel 3 si afecta documento técnico, maestro, seguridad o fases.

## Resultado permitido

Robert puede preparar bloque para pegar en DECISIONS_LOG.

## Requiere aprobación

Sí, cuando representa una decisión formal.

## Restricción

La decisión debe representar una aprobación real del usuario.

Robert no debe inventar aprobaciones.

## Gate probable

Gate 3 — Aprobación formal.

## Evento relacionado

EVENTO 3 — Aprobación formal requerida.

## Registro de auditoría relacionado

REGISTRO 6 — Decisión.

## Notificación relacionada

TIPO 1 — Informativa.  
TIPO 6 — Confirmación requerida, si falta claridad.

---

# ACCIÓN 8 — REGISTRAR CAMBIO

## Dónde ocurre

CommandCenter.

## Qué intenta hacer el usuario

El usuario registra un cambio en ROBERT_CONTROL_DE_CAMBIOS.

## Ejemplos

- Registrar CAMBIO #025.
- Registrar corrección documental.
- Registrar integración.
- Registrar actualización de HOME o README.

## Componente principal

CommandCenter.

## Componentes relacionados

- DocumentStatusMap.
- CurrentStatePanel.
- TopBar.
- AppShell.

## Modelo principal

ChangeRecord.

## Flujo activado

- Crear bloque para CONTROL_DE_CAMBIOS.
- Relacionar cambio con decisión.
- Relacionar cambio con documento.
- Relacionar cambio con versión.

## Riesgo

Nivel 2 o Nivel 3.

Nivel 3 si el cambio afecta documentos técnicos, maestros, seguridad o fases.

## Resultado permitido

Robert puede preparar bloque de cambio para pegar.

## Requiere aprobación

Depende del cambio.

Si integra documento aprobado, debe existir decisión previa.

## Restricción

Registrar cambio no autoriza acciones externas.

## Gate probable

Gate 4 — Integración documental.

## Evento relacionado

EVENTO 3 — Aprobación formal requerida, si falta decisión.  
EVENTO 10 — Contradicción documental, si el cambio no coincide.

## Registro de auditoría relacionado

REGISTRO 7 — Cambio.  
REGISTRO 9 — Integración, si aplica.

## Notificación relacionada

TIPO 1 — Informativa.  
TIPO 10 — Contradicción documental, si aplica.

---

# ACCIÓN 9 — ACTUALIZAR HOME

## Dónde ocurre

CommandCenter.

## Qué intenta hacer el usuario

El usuario actualiza ROBERT_HOME con el nuevo estado del sistema.

## Ejemplos

- Actualizar HOME con una decisión.
- Actualizar HOME con un cambio.
- Actualizar HOME con documento aprobado.
- Corregir estado desactualizado.

## Componente principal

CommandCenter.

## Componentes relacionados

- CurrentStatePanel.
- DocumentStatusMap.
- TopBar.
- AppShell.

## Modelo principal

RobertDocument.

## Flujo activado

- Preparar bloque de actualización.
- Verificar estado real.
- Verificar decisión/cambio relacionado.
- Evitar contradicción interna.

## Riesgo

Nivel 2 — Medio.

Puede subir a Nivel 3 si corrige estado central del sistema.

## Resultado permitido

Robert puede preparar bloque para ROBERT_HOME.

## Requiere aprobación

Sí si cambia estado central, versión, fase, aprobación o integración.

## Restricción

HOME debe reflejar estado real, no capacidades futuras como si estuvieran activas.

## Gate probable

Gate 4 — Integración documental.

## Evento relacionado

EVENTO 10 — Contradicción documental.  
EVENTO 9 — Falta de información, si falta trazabilidad.

## Registro de auditoría relacionado

REGISTRO 7 — Cambio.  
REGISTRO 9 — Integración.

## Notificación relacionada

TIPO 10 — Alerta de contradicción documental.

---

# ACCIÓN 10 — ACTUALIZAR README

## Dónde ocurre

CommandCenter.

## Qué intenta hacer el usuario

El usuario actualiza README.md con el estado general del repositorio.

## Ejemplos

- Actualizar README con documento aprobado.
- Actualizar README con estado de Fase 10.
- Actualizar README con bloque de cierre.
- Actualizar README con restricciones activas.

## Componente principal

CommandCenter.

## Componentes relacionados

- DocumentStatusMap.
- TopBar.
- CurrentStatePanel.
- AppShell.

## Modelo principal

GitHubBackupStatus.

## Flujo activado

- Preparar bloque para README.
- Verificar que el texto coincida con HOME.
- Mantener respaldo manual.

## Riesgo

Nivel 2 — Medio.

## Resultado permitido

Robert puede preparar bloque para README.

## Requiere aprobación

Puede requerir confirmación si actualiza estado oficial.

## Restricción

README no debe decir que hay app funcional si todavía no existe.

## Gate probable

Gate 4 — Integración documental.

## Evento relacionado

EVENTO 10 — Contradicción documental, si README no coincide.  
EVENTO 16 — Conexión no autorizada, si se intenta automatizar GitHub.

## Registro de auditoría relacionado

REGISTRO 7 — Cambio.  
REGISTRO 12 — Permiso, si se relaciona con GitHub.

## Notificación relacionada

TIPO 1 — Informativa.  
TIPO 9 — Bloqueo, si se intenta automatizar.

---

# ACCIÓN 11 — CAMBIAR MODO

## Dónde ocurre

ModeSelector o CommandCenter.

## Qué intenta hacer el usuario

El usuario pide cambiar el modo operativo.

## Modos permitidos actualmente

- Manual.
- Supervisado.
- Sandbox.

## Modos no disponibles todavía

- Autónomo limitado.
- Ejecución limitada.
- Modo crítico.
- Agentes autónomos.
- Automatización real.

## Componente principal

ModeSelector.

## Componentes relacionados

- ApprovalGate.
- RiskBadge.
- CurrentStatePanel.
- TopBar.
- AppShell.

## Modelo principal

ModeState.

## Flujo activado

- Evaluar modo solicitado.
- Confirmar si el modo está permitido.
- Bloquear modo futuro o no autorizado.

## Riesgo

Nivel 2 si cambia entre modos permitidos.

Nivel 3 si afecta documentos, pruebas o sandbox.

Nivel 4 si intenta activar autonomía real, automatización o ejecución externa.

## Resultado permitido

Robert puede:

- Cambiar estado conceptual del modo.
- Pedir confirmación.
- Bloquear modo no autorizado.
- Mostrar modo activo.

## Requiere aprobación

Sí si el modo cambia alcance o riesgo.

## Restricción

Cambiar modo no activa autonomía real.

## Gate probable

Gate 2, Gate 5 o Gate 6.

## Evento relacionado

EVENTO 8 — Acción futura no disponible.  
EVENTO 18 — Agente no autorizado, si aplica.  
EVENTO 20 — Fase incorrecta, si aplica.

## Registro de auditoría relacionado

REGISTRO 12 — Permiso.  
REGISTRO 17 — Capacidad futura no disponible.

## Notificación relacionada

TIPO 11 — Fase incorrecta.  
TIPO 12 — Capacidad futura no disponible.

---

# ACCIÓN 12 — ACTIVAR SANDBOX MANUAL

## Dónde ocurre

ModeSelector o CommandCenter.

## Qué intenta hacer el usuario

El usuario quiere entrar en modo de prueba controlada.

## Ejemplos

- Activar sandbox manual.
- Probar idea en simulación.
- Ejecutar prueba documental.
- Revisar comportamiento de Business Builder.

## Componente principal

ModeSelector.

## Componentes relacionados

- RiskBadge.
- ApprovalGate.
- CurrentStatePanel.
- DocumentStatusMap.
- AppShell.

## Modelo principal

ModeState.

## Flujo activado

- Cambiar a modo sandbox conceptual.
- Mantener simulación documental.
- Verificar que no haya ejecución real.

## Riesgo

Nivel 2 o Nivel 3.

## Resultado permitido

Robert puede operar en simulación documental.

## Requiere aprobación

Sí, si la prueba afecta documentos, seguridad o decisiones.

## Restricción

Sandbox manual no ejecuta acciones reales.

## Gate probable

Gate 2 o Gate 7 si el usuario pausa.

## Evento relacionado

EVENTO 12 — Fuera de alcance, si intenta ejecución real.  
EVENTO 15 — Ejecución no autorizada, si aplica.

## Registro de auditoría relacionado

REGISTRO 3 — Revisión.  
REGISTRO 11 — Riesgo, si aplica.

## Notificación relacionada

TIPO 5 — Advertencia de riesgo, si aplica.

---

# ACCIÓN 13 — PAUSAR AVANCE

## Dónde ocurre

CommandCenter, DecisionInbox o ApprovalGate.

## Qué intenta hacer el usuario

El usuario ordena detener temporalmente el avance.

## Comandos relacionados

- PAUSA.
- DETENTE.
- NO_AVANCES.
- NO SIGAS.
- CANCELA.
- SOLO BORRADOR.

## Componente principal

ApprovalGate.

## Componentes relacionados

- CommandCenter.
- CurrentStatePanel.
- DecisionInbox.
- TopBar.
- AppShell.

## Modelo principal

ModeState.

## Flujo activado

- Pausa inmediata.
- Bloqueo temporal de siguiente paso.
- Esperar nueva autorización.

## Riesgo

Acción de control fuera de escala de riesgo.

## Resultado permitido

Robert debe detener el avance.

## Requiere aprobación

No.

## Restricción

Robert no debe continuar al siguiente paso hasta nueva autorización.

## Gate probable

Gate 7 — Revocación o control manual.

## Evento relacionado

EVENTO 4 — Pausa obligatoria.

## Registro de auditoría relacionado

REGISTRO 3 — Revisión.

## Notificación relacionada

TIPO 1 — Informativa.

---

# ACCIÓN 14 — BLOQUEAR ACCIÓN

## Dónde ocurre

ApprovalGate o RiskBadge.

## Qué intenta hacer el usuario

El usuario o las reglas de seguridad bloquean una acción.

## Ejemplos

- No conectar Gmail.
- No programar todavía.
- No avanzar a Fase 11.
- No activar agentes.
- No crear base de datos real.

## Componente principal

ApprovalGate.

## Componentes relacionados

- RiskBadge.
- CurrentStatePanel.
- DecisionInbox.
- TopBar.
- AppShell.

## Modelo principal

RiskRecord.

## Flujo activado

- Bloqueo.
- Mostrar motivo.
- Detener avance.
- Mantener restricción activa.

## Riesgo

Acción de control fuera de escala de riesgo.

La acción bloqueada puede tener Nivel 3 o Nivel 4.

## Resultado permitido

Robert debe mostrar motivo del bloqueo.

## Requiere aprobación

No, si el bloqueo protege seguridad o respeta instrucción del usuario.

## Restricción

Robert no debe buscar rutas alternas para ejecutar lo bloqueado.

## Gate probable

Gate 5 o Gate 7.

## Evento relacionado

EVENTO 6 — Bloqueo manual solicitado.  
EVENTO 7 — Acción prohibida.  
EVENTO 15 — Ejecución no autorizada, si aplica.

## Registro de auditoría relacionado

REGISTRO 10 — Bloqueo.  
REGISTRO 11 — Riesgo.

## Notificación relacionada

TIPO 9 — Mensaje de bloqueo.

---

# ACCIÓN 15 — VER DECISIONES PENDIENTES

## Dónde ocurre

DecisionInbox.

## Qué intenta hacer el usuario

El usuario quiere revisar qué decisiones siguen pendientes.

## Ejemplos

- Ver qué falta aprobar.
- Ver decisiones abiertas.
- Ver documentos pendientes.
- Ver riesgos pendientes.

## Componente principal

DecisionInbox.

## Componentes relacionados

- CurrentStatePanel.
- DocumentStatusMap.
- AppShell.

## Modelo principal

PendingDecision.

## Flujo activado

- Mostrar decisiones pendientes.
- Mostrar documento afectado.
- Mostrar riesgo y opciones.

## Riesgo

Nivel 0 — Informativo.

## Resultado permitido

Robert puede mostrar:

- Decisiones pendientes.
- Motivo.
- Riesgo.
- Documento afectado.
- Opciones disponibles.

## Requiere aprobación

No.

## Restricción

Ver pendientes no resuelve decisiones.

## Gate probable

Gate 0.

## Evento relacionado

Ninguno obligatorio.

## Registro de auditoría relacionado

REGISTRO 3 — Revisión.

## Notificación relacionada

TIPO 1 — Informativa.

---

# ACCIÓN 16 — RESOLVER DECISIÓN PENDIENTE

## Dónde ocurre

DecisionInbox o CommandCenter.

## Qué intenta hacer el usuario

El usuario elige qué hacer con una decisión pendiente.

## Opciones permitidas

- Aprobar.
- Rechazar.
- Pausar.
- Corregir.
- Revisar otra vez.
- Mandar a sandbox.
- Archivar.

## Componente principal

DecisionInbox.

## Componentes relacionados

- ApprovalGate.
- RiskBadge.
- CurrentStatePanel.
- AppShell.

## Modelo principal

PendingDecision.

## Flujo activado

- Elegir resolución.
- Registrar decisión si aplica.
- Registrar cambio si aplica.
- Mantener pendiente si falta información.

## Riesgo

Nivel 2 o Nivel 3.

## Resultado permitido

Robert puede preparar el registro correspondiente.

## Requiere aprobación

Sí si resuelve una decisión formal o aprueba un documento.

## Restricción

Robert no resuelve decisiones sin instrucción del usuario.

## Gate probable

Gate 3 o Gate 4.

## Evento relacionado

EVENTO 3 — Aprobación formal requerida.  
EVENTO 9 — Falta de información, si falta claridad.

## Registro de auditoría relacionado

REGISTRO 6 — Decisión.  
REGISTRO 7 — Cambio, si aplica.

## Notificación relacionada

TIPO 6 — Confirmación requerida.

---

# ACCIÓN 17 — VER MAPA DOCUMENTAL

## Dónde ocurre

DocumentStatusMap.

## Qué intenta hacer el usuario

El usuario quiere ver los documentos, estados y relaciones del sistema.

## Ejemplos

- Ver documentos por carpeta.
- Ver documentos aprobados.
- Ver documentos pendientes.
- Ver relación entre decisiones y cambios.
- Ver mapa de órbitas.

## Componente principal

DocumentStatusMap.

## Componentes relacionados

- LeftSidebar.
- CurrentStatePanel.
- AppShell.

## Modelo principal

RobertDocument.

## Flujo activado

- Mostrar mapa documental.
- Mostrar estado por documento.
- Mostrar versión y relación.

## Riesgo

Nivel 0 — Informativo.

## Resultado permitido

Robert puede mostrar:

- Documento.
- Estado.
- Versión.
- Órbita.
- Capa.
- Decisión relacionada.
- Cambio relacionado.
- Respaldo manual.
- Estado visual de Obsidian Graph.

## Requiere aprobación

No.

## Restricción

Ver el mapa no modifica documentos.

## Gate probable

Gate 0.

## Evento relacionado

Ninguno obligatorio.

## Registro de auditoría relacionado

REGISTRO 3 — Revisión.

## Notificación relacionada

TIPO 1 — Informativa.

---

# ACCIÓN 18 — MARCAR RESPALDO MANUAL EN GITHUB

## Dónde ocurre

CommandCenter, TopBar o CurrentStatePanel.

## Qué intenta hacer el usuario

El usuario indica que ya actualizó GitHub manualmente.

## Ejemplos

- ya
- ya actualicé README
- ya registré CAMBIO
- ya hice commit
- ya subí el cambio

## Componente principal

CurrentStatePanel.

## Componentes relacionados

- TopBar.
- DocumentStatusMap.
- CommandCenter.
- AppShell.

## Modelo principal

GitHubBackupStatus.

## Flujo activado

- Interpretar confirmación del usuario.
- Actualizar estado conversacional.
- Preparar siguiente paso documental.
- No conectar GitHub automáticamente.

## Riesgo

Nivel 1 o Nivel 2.

Puede subir si el respaldo confirma un cambio técnico o maestro.

## Resultado permitido

Robert puede actualizar el estado documental de la conversación y preparar el siguiente paso.

## Requiere aprobación

No si solo confirma respaldo manual.

Sí si implica cambio de estado documental oficial.

## Restricción

Robert no debe asumir que puede conectarse a GitHub automáticamente.

## Gate probable

Gate 1 o Gate 4.

## Evento relacionado

EVENTO 16 — Conexión no autorizada, si intenta automatizar GitHub.

## Registro de auditoría relacionado

REGISTRO 12 — Permiso.  
REGISTRO 7 — Cambio, si el respaldo confirma cambio.

## Notificación relacionada

TIPO 1 — Informativa.  
TIPO 9 — Bloqueo, si se intenta automatizar.

---

# ACCIÓN 19 — SOLICITAR REVISIÓN CRÍTICA

## Dónde ocurre

CommandCenter.

## Qué intenta hacer el usuario

El usuario pide revisar un documento para detectar contradicciones.

## Ejemplos

- Revisar un documento técnico.
- Detectar conflictos.
- Comparar con la serie.
- Revisar si hay huecos.
- Auditar consistencia.

## Componente principal

CommandCenter.

## Componentes relacionados

- RiskBadge.
- DocumentStatusMap.
- CurrentStatePanel.
- AppShell.

## Modelo principal

RiskRecord.

## Flujo activado

- Revisar documento.
- Detectar conflictos.
- Clasificar conflicto.
- Proponer corrección.
- Mantener pendiente de aprobación.

## Riesgo

Nivel 2.

Puede subir a Nivel 3 si la revisión afecta documento maestro o técnico aprobado.

## Resultado permitido

Robert puede:

- Señalar inconsistencias.
- Recomendar correcciones.
- Proponer v0.2 o nueva versión.
- Mantener pendiente de aprobación.

## Requiere aprobación

No para revisar.

Sí para corregir, aprobar o integrar.

## Restricción

Revisar no aprueba ni modifica por sí solo.

## Gate probable

Gate 0 o Gate 2.

## Evento relacionado

EVENTO 10 — Contradicción documental.  
EVENTO 9 — Falta de información, si falta fuente.

## Registro de auditoría relacionado

REGISTRO 3 — Revisión.  
REGISTRO 16 — Contradicción documental.

## Notificación relacionada

TIPO 10 — Alerta de contradicción documental.

---

# ACCIÓN 20 — PEDIR SIGUIENTE PASO

## Dónde ocurre

CommandCenter.

## Qué intenta hacer el usuario

El usuario pregunta qué sigue.

## Ejemplos

- ¿Qué sigue?
- Dame el siguiente paso.
- ¿Ahora qué hago?
- Continúa.
- Siguiente documento.

## Componente principal

CommandCenter.

## Componentes relacionados

- CurrentStatePanel.
- DecisionInbox.
- DocumentStatusMap.
- AppShell.

## Modelo principal

SystemState.

## Flujo activado

- Revisar estado actual.
- Detectar pendientes.
- Recomendar siguiente paso.
- No ejecutar sin permiso.

## Riesgo

Nivel 0 o Nivel 1.

Puede subir si el siguiente paso afecta documentos, decisiones o integraciones.

## Resultado permitido

Robert puede recomendar siguiente paso.

## Requiere aprobación

No para recomendar.

Sí para ejecutar/corregir/aprobar/integrar.

## Restricción

Recomendar no significa avanzar sin autorización.

## Gate probable

Gate 0 o Gate 1.

## Evento relacionado

Ninguno obligatorio.

EVENTO 9 — Falta de información, si no hay contexto suficiente.

## Registro de auditoría relacionado

REGISTRO 3 — Revisión.

## Notificación relacionada

TIPO 1 — Informativa.

---

# TABLA RESUMEN DE ACCIONES

| Acción | Nombre | Componente principal | Riesgo típico | Resultado permitido |
|---:|---|---|---:|---|
| 1 | Escribir comando | CommandCenter | Variable | Clasificar, responder o pedir aprobación |
| 2 | Seleccionar documento | LeftSidebar | 0 | Mostrar documento |
| 3 | Revisar estado general | CurrentStatePanel | 0 | Mostrar estado |
| 4 | Crear documento técnico | CommandCenter | 3 | Borrador pendiente |
| 5 | Corregir documento técnico | CommandCenter | 2-3 | Propuesta corregida |
| 6 | Aprobar documento | DecisionInbox | 3 | Decisión y cambio |
| 7 | Registrar decisión | CommandCenter | 2-3 | Bloque para DECISIONS_LOG |
| 8 | Registrar cambio | CommandCenter | 2-3 | Bloque para CONTROL_DE_CAMBIOS |
| 9 | Actualizar HOME | CommandCenter | 2-3 | Bloque para HOME |
| 10 | Actualizar README | CommandCenter | 2 | Bloque para README |
| 11 | Cambiar modo | ModeSelector | 2-4 | Cambio conceptual o bloqueo |
| 12 | Activar sandbox manual | ModeSelector | 2-3 | Simulación documental |
| 13 | Pausar avance | ApprovalGate | Control | Detener avance |
| 14 | Bloquear acción | ApprovalGate | Control | Bloqueo visible |
| 15 | Ver decisiones pendientes | DecisionInbox | 0 | Mostrar pendientes |
| 16 | Resolver decisión pendiente | DecisionInbox | 2-3 | Registro correspondiente |
| 17 | Ver mapa documental | DocumentStatusMap | 0 | Mostrar mapa |
| 18 | Marcar respaldo manual en GitHub | CurrentStatePanel | 1-2 | Actualizar estado conversacional |
| 19 | Solicitar revisión crítica | CommandCenter | 2-3 | Detectar inconsistencias |
| 20 | Pedir siguiente paso | CommandCenter | 0-1 | Recomendar, no ejecutar |

---

# TABLA DE MAPEO CON APPROVAL GATE

| Acción | Nombre | Gate probable |
|---:|---|---|
| 1 | Escribir comando | Gate 0 / 1 / 2 / 3 / 5 / 7 |
| 2 | Seleccionar documento | Gate 0 / 1 |
| 3 | Revisar estado general | Gate 0 |
| 4 | Crear documento técnico | Gate 2 |
| 5 | Corregir documento técnico | Gate 2 |
| 6 | Aprobar documento | Gate 3 |
| 7 | Registrar decisión | Gate 3 |
| 8 | Registrar cambio | Gate 4 |
| 9 | Actualizar HOME | Gate 4 |
| 10 | Actualizar README | Gate 4 |
| 11 | Cambiar modo | Gate 2 / 5 / 6 |
| 12 | Activar sandbox manual | Gate 2 / Gate 7 |
| 13 | Pausar avance | Gate 7 |
| 14 | Bloquear acción | Gate 5 / 7 |
| 15 | Ver decisiones pendientes | Gate 0 |
| 16 | Resolver decisión pendiente | Gate 3 / 4 |
| 17 | Ver mapa documental | Gate 0 |
| 18 | Marcar respaldo manual en GitHub | Gate 1 / 4 |
| 19 | Solicitar revisión crítica | Gate 0 / 2 |
| 20 | Pedir siguiente paso | Gate 0 / 1 |

---

# ACCIONES PROHIBIDAS EN ESTA FASE

Robert debe bloquear acciones como:

- Programar la app.
- Crear código real.
- Crear prototipo funcional.
- Crear pantallas reales.
- Crear base de datos real.
- Crear endpoints.
- Conectar Supabase.
- Conectar Firebase.
- Conectar GitHub automáticamente.
- Conectar Gmail.
- Conectar Google Calendar.
- Conectar APIs externas.
- Activar automatizaciones reales.
- Activar agentes autónomos.
- Ejecutar acciones reales.
- Avanzar automáticamente a Fase 11.

Estas acciones deben mostrarse como:

**Bloqueadas / No autorizadas / Futuras / Pendientes de decisión formal**

---

# ACCIONES FUTURAS NO DISPONIBLES

Estas acciones pueden existir como visión futura, pero no están activas:

- Ejecutar comandos en computadora.
- Operar apps externas.
- Leer Gmail automáticamente.
- Crear eventos en calendario automáticamente.
- Conectar APIs reales.
- Ejecutar workflows.
- Activar agentes especializados.
- Usar voz como control real.
- Sincronizar Obsidian y GitHub automáticamente.
- Tomar decisiones autónomas.

Deben aparecer como:

**Futuro — no disponible en Fase 10**

---

# REGLAS DE CONFIRMACIÓN

Una acción requiere confirmación simple cuando:

- Cambia un documento no maestro.
- Cambia un estado documental menor.
- Actualiza README.
- Actualiza HOME.
- Registra un cambio no crítico.
- Cambia modo entre opciones permitidas.
- Confirma respaldo manual en GitHub.
- Confirma que el usuario terminó un paso.

Una acción requiere aprobación formal cuando:

- Aprueba documento técnico.
- Aprueba documento maestro.
- Cambia reglas de seguridad.
- Cambia fases.
- Cambia fuente de verdad.
- Crea decisión formal.
- Integra documento técnico.
- Modifica arquitectura conceptual.
- Acerca el sistema a programación.
- Acerca el sistema a conexiones externas.

Una acción debe bloquearse cuando:

- Intenta ejecutar algo real.
- Intenta conectar herramientas.
- Intenta automatizar.
- Intenta crear código sin autorización.
- Intenta avanzar a Fase 11 sin decisión formal.
- Intenta saltarse ApprovalGate.
- Intenta ignorar DETENTE, PAUSA o NO_AVANCES.

---

# RELACIÓN CON COMPONENTS_SPEC v0.2

Este documento usa exclusivamente los componentes canónicos aprobados:

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

Regla:

```text
No usar MainCanvas como componente oficial.
```

---

# RELACIÓN CON DATA_MODEL_SPEC v0.1

Este documento no crea modelos nuevos.

Usa modelos ya existentes para interpretar acciones del usuario.

Relación principal:

| Acción | Modelo principal |
|---:|---|
| 1 | CommandRequest |
| 2 | RobertDocument |
| 3 | SystemState |
| 4 | RobertDocument |
| 5 | ChangeRecord |
| 6 | DecisionRecord |
| 7 | DecisionRecord |
| 8 | ChangeRecord |
| 9 | RobertDocument |
| 10 | GitHubBackupStatus |
| 11 | ModeState |
| 12 | ModeState |
| 13 | ModeState |
| 14 | RiskRecord |
| 15 | PendingDecision |
| 16 | PendingDecision |
| 17 | RobertDocument |
| 18 | GitHubBackupStatus |
| 19 | RiskRecord |
| 20 | SystemState |

---

# RELACIÓN CON APPROVAL_AND_AUTHORIZATION_GATE_SPEC

USER_ACTIONS_SPEC define qué intenta hacer el usuario.

APPROVAL_AND_AUTHORIZATION_GATE_SPEC define si la acción puede pasar, requiere confirmación, requiere aprobación o debe bloquearse.

Regla:

```text
Toda acción importante debe pasar por ApprovalGate antes de cambiar estado documental.
```

---

# RELACIÓN CON DATA_CONSISTENCY_AND_CONFLICT_RESOLUTION_SPEC v0.3

Si una acción produce conflicto entre documentos, debe clasificarse según DATA_CONSISTENCY_AND_CONFLICT_RESOLUTION_SPEC.

Ejemplos:

```text
Acción con versión incorrecta:
TIPO 3 — Conflicto de versión

Acción con fuente vigente incorrecta:
TIPO 16 — Conflicto de fuente vigente

Acción sin trazabilidad:
TIPO 17 — Conflicto de trazabilidad insuficiente

Acción que intenta ejecución real:
TIPO 15 — Conflicto de ejecución no autorizada
```

---

# CRITERIOS DE ACEPTACIÓN

Este documento se mantiene aceptado si:

- Define qué acciones puede intentar el usuario.
- Mantiene la lista canónica de 20 acciones.
- Mantiene la numeración correcta de las 20 acciones.
- Relaciona acciones con componentes.
- Usa AppShell como componente canónico.
- No usa MainCanvas como componente oficial.
- Clasifica acciones por riesgo.
- Define resultados permitidos.
- Define restricciones.
- Define acciones prohibidas.
- Define acciones futuras no disponibles.
- Define relación con ApprovalGate.
- Define relación con DATA_CONSISTENCY.
- Respeta SCREEN_STATE_SPEC v0.2.
- Respeta INTERACTION_FLOW_SPEC v0.2.
- Respeta COMPONENTS_SPEC v0.2.
- Respeta DATA_MODEL_SPEC v0.1.
- No autoriza programación.
- No autoriza código real.
- No autoriza pantallas reales.
- No autoriza base de datos real.
- No autoriza conexiones externas.
- No autoriza automatizaciones.
- No autoriza agentes autónomos.
- Mantiene a Robert en Fase 10.
- Mantiene control total del usuario.

---

# RIESGO DEL DOCUMENTO

Tipo de cambio:

**Auditoría voluntaria / acciones conceptuales del usuario**

Nivel de riesgo inicial de la auditoría:

**Nivel 1 — Bajo**

Motivo:

La auditoría revisa un documento ya aprobado e integrado, sin reabrir su aprobación ni modificar contenido sustantivo.

Nivel de riesgo final:

**Nivel 0 — Informativo**

Motivo de reducción:

No se encontraron errores de contenido. El único ajuste aplicado fue menor: corrección de la fila ACCIÓN 12 en la TABLA DE MAPEO CON APPROVAL GATE.

Nivel de autonomía:

**Nivel 0 — Sin autonomía ejecutiva**

---

# ESTADO DE APROBACIÓN

ROBERT_TECHNICAL_USER_ACTIONS_SPEC v0.2 se mantiene como:

```text
Aprobado e integrado
DECISIÓN #017
CAMBIO #028
```

Esta auditoría no requiere nueva decisión formal.

Esta auditoría no requiere nuevo cambio formal porque no hubo corrección sustantiva de contenido.

---

# USO COMO REFERENCIA CANÓNICA

Este documento debe usarse como referencia confirmada para corregir:

```text
ROBERT_TECHNICAL_APPROVAL_AND_AUTHORIZATION_GATE_SPEC v0.3
```

La corrección de APPROVAL_GATE v0.3 deberá:

```text
1. Reemplazar MainCanvas por AppShell.
2. Usar la lista canónica de 20 acciones de este documento.
3. Corregir la numeración de las acciones en su tabla de correspondencia.
4. Mantener Fase 10 sin programación ni ejecución real.
```

---

# CIERRE DE AUDITORÍA

ROBERT_TECHNICAL_USER_ACTIONS_SPEC v0.2 se mantiene aprobado e integrado, sin cambios de fondo tras esta auditoría voluntaria.

Único ajuste aplicado:

```text
Corrección de la fila ACCIÓN 12 en TABLA DE MAPEO CON APPROVAL GATE.
```

Este documento sirve como referencia confirmada para corregir:

```text
APPROVAL_AND_AUTHORIZATION_GATE_SPEC v0.3
```

No se requiere nueva DECISIÓN ni CAMBIO formal, ya que no hubo corrección sustantiva de contenido.

Robert continúa en modo documental, manual y supervisado.

El usuario mantiene control total.

Robert no ejecuta acciones importantes sin permiso.
