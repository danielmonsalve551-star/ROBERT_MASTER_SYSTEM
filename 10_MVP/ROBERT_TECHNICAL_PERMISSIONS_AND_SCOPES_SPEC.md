# ROBERT_TECHNICAL_PERMISSIONS_AND_SCOPES_SPEC

Versión: 0.2  
Estado: Propuesta corregida — pendiente de revisión  
Fecha: 04/07/2026  
Ubicación: 10_MVP  
Fase relacionada: Fase 10 — MVP técnico básico en preparación  
Documento base principal: ROBERT_TECHNICAL_ERROR_AND_BLOCKING_SPEC v0.2  
Documentos relacionados: ROBERT_COMMANDS v0.4, ROBERT_TECHNICAL_USER_ACTIONS_SPEC v0.2, ROBERT_TECHNICAL_SCREEN_STATE_SPEC v0.2, ROBERT_TECHNICAL_INTERACTION_FLOW_SPEC v0.2, ROBERT_TECHNICAL_COMPONENTS_SPEC v0.2, ROBERT_TECHNICAL_DATA_MODEL_SPEC v0.1  
Documentos sandbox relacionados: ROBERT_SANDBOX, SANDBOX_RULES, SANDBOX_TESTS, SANDBOX_RESULTS  
Fuente de verdad actual: ROBERT_CONTEXT_MASTER v0.5  

Tags: #robert/orbita-3 #capa/5 #tipo/tecnico #robert/mvp #robert/permissions-scopes

---

# OBJETIVO

ROBERT_TECHNICAL_PERMISSIONS_AND_SCOPES_SPEC define cómo Robert debe entender permisos, alcances, límites, duración de autorizaciones y acciones permitidas dentro del MVP técnico básico.

Su objetivo es responder:

- Qué significa que el usuario autorice algo.
- Qué puede hacer Robert dentro de un alcance autorizado.
- Qué no puede hacer aunque exista autorización parcial.
- Cuánto dura una autorización.
- Qué documentos o áreas cubre una autorización.
- Qué nivel de riesgo máximo permite una autorización.
- Qué pasa cuando una acción supera el alcance.
- Cómo se revoca una autorización.
- Qué componente muestra el permiso activo.
- Qué componente valida si el permiso alcanza.
- Qué modelo conceptual representa la solicitud.
- Qué debe registrarse.
- Qué debe bloquearse.
- Qué permisos no existen todavía.

Este documento no programa la app.

Este documento no crea permisos reales.

Este documento no crea sistema de usuarios.

Este documento no crea roles reales.

Este documento no crea base de datos real.

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

No autoriza base de datos real.

No autoriza conexiones externas.

No autoriza automatizaciones.

No autoriza agentes autónomos.

No autoriza ejecución real.

No autoriza avanzar a Fase 11.

---

# CORRECCIONES DE LA VERSIÓN v0.2

Esta versión corrige los problemas estructurales detectados en v0.1.

Correcciones principales:

1. Se agrega relación explícita con los 11 modelos de DATA_MODEL_SPEC v0.1.
2. Se aclara que Permiso y Alcance no son modelos nuevos oficiales en esta versión.
3. Se define que Permiso y Alcance son estructuras conceptuales derivadas.
4. Se establece que, si en el futuro se necesita un modelo nuevo llamado PermissionScope, primero deberá actualizarse DATA_MODEL_SPEC.
5. Se agrega sección de componentes participantes.
6. Se define qué componente muestra permiso activo, alcance, duración, expiración y revocación.
7. Se agrega tabla de correspondencia entre los 13 permisos y las 20 acciones de USER_ACTIONS_SPEC v0.2.
8. Se agrega EVENTO 5 — Bloqueo automático como categoría general de respaldo en la relación con ERROR_AND_BLOCKING_SPEC.
9. Se mantiene alineación con ROBERT_COMMANDS v0.4, USER_ACTIONS_SPEC v0.2 y ERROR_AND_BLOCKING_SPEC v0.2.

---

# REGLA CENTRAL

El usuario manda.

Robert no ejecuta acciones importantes sin permiso.

Una autorización debe ser clara, limitada, trazable y revocable.

Regla principal:

**Permiso parcial no significa permiso total.**

---

# REGLA DE ALINEACIÓN DOCUMENTAL

PERMISSIONS_AND_SCOPES_SPEC v0.2 debe mantenerse alineado con:

- ROBERT_COMMANDS v0.4
- ROBERT_TECHNICAL_ERROR_AND_BLOCKING_SPEC v0.2
- ROBERT_TECHNICAL_USER_ACTIONS_SPEC v0.2
- ROBERT_TECHNICAL_SCREEN_STATE_SPEC v0.2
- ROBERT_TECHNICAL_INTERACTION_FLOW_SPEC v0.2
- ROBERT_TECHNICAL_COMPONENTS_SPEC v0.2
- ROBERT_TECHNICAL_DATA_MODEL_SPEC v0.1
- ROBERT_SECURITY_RULES
- ROBERT_PHASES
- ROBERT_SANDBOX
- SANDBOX_RULES
- SANDBOX_TESTS
- SANDBOX_RESULTS

Regla:

**PERMISSIONS_AND_SCOPES_SPEC no debe inventar nuevos niveles de riesgo, nuevas capacidades activas, nuevos permisos ejecutivos, nuevos modelos oficiales ni nueva lógica de autonomía que no exista en los documentos base.**

Si un permiso requiere capacidad real, conexión externa, base de datos, automatización o agente autónomo, debe bloquearse en Fase 10.

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
- ROBERT_TECHNICAL_PERMISSIONS_AND_SCOPES_SPEC v0.2 como propuesta corregida pendiente de revisión.
- Sin programación autorizada.
- Sin código real.
- Sin botones reales.
- Sin pantallas reales.
- Sin base de datos real.
- Sin conexiones externas.
- Sin automatizaciones reales.
- Sin agentes autónomos activos.

---

# ALCANCE AUTORIZADO

Este documento autoriza únicamente:

- Definir permisos conceptuales.
- Definir alcances conceptuales.
- Definir límites de autorización.
- Definir duración de permisos.
- Definir revocación de permisos.
- Definir cómo se relacionan permisos con modelos existentes.
- Definir qué componentes muestran o validan permisos.
- Definir cuándo pedir confirmación.
- Definir cuándo pedir aprobación formal.
- Definir cuándo bloquear.
- Definir permisos documentales.
- Definir permisos de sandbox manual.
- Definir permisos futuros no disponibles.
- Mantener a Robert en modo documental, manual y supervisado.

---

# ALCANCE NO AUTORIZADO

Este documento no autoriza:

- Programar la app.
- Crear código real.
- Crear sistema real de permisos.
- Crear usuarios reales.
- Crear roles reales.
- Crear botones reales.
- Crear pantallas reales.
- Crear prototipo funcional.
- Crear base de datos real.
- Crear endpoints.
- Crear modelo nuevo oficial sin actualizar DATA_MODEL_SPEC.
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

# DEFINICIÓN DE PERMISO

Un permiso es una autorización explícita del usuario para que Robert pueda realizar una acción dentro de un alcance específico.

Un permiso debe tener:

1. Acción permitida.
2. Documento o área afectada.
3. Límite de riesgo.
4. Modo operativo.
5. Duración.
6. Restricciones.
7. Forma de revocación.
8. Necesidad de registro o no.

Ejemplo:

```text
Autorizo corregir USER_ACTIONS_SPEC v0.2 como propuesta documental.
No apruebes automáticamente.
No programes.
No avances a Fase 11.
```

---

# DEFINICIÓN DE ALCANCE

Un alcance define los límites exactos donde Robert puede actuar.

Un alcance debe responder:

- Qué puede hacer.
- Qué no puede hacer.
- En qué documento.
- En qué fase.
- Con qué nivel máximo de riesgo.
- Durante cuánto tiempo.
- Bajo qué modo.
- Qué necesita para continuar.

Ejemplo de alcance claro:

```text
Puedes corregir solo la sección de eventos del documento ERROR_AND_BLOCKING_SPEC.
Mantén el documento como propuesta pendiente de revisión.
No apruebes.
No actualices otros documentos todavía.
```

Ejemplo de alcance ambiguo:

```text
Hazlo todo.
```

Cuando el alcance es ambiguo, Robert debe pedir aclaración.

---

# PERMISO Y ALCANCE NO SON MODELOS NUEVOS OFICIALES

En esta versión, los conceptos:

- Permiso
- Alcance

no crean modelos nuevos oficiales.

Son estructuras conceptuales derivadas de modelos ya existentes en DATA_MODEL_SPEC v0.1.

Regla:

**PERMISSIONS_AND_SCOPES_SPEC v0.2 no crea el modelo PermissionScope.**

Si en el futuro se decide crear un modelo oficial como:

```text
PermissionScope
```

primero deberá corregirse y aprobarse:

```text
ROBERT_TECHNICAL_DATA_MODEL_SPEC
```

---

# RELACIÓN CON DATA_MODEL_SPEC v0.1

Este documento se apoya en los 11 modelos existentes de DATA_MODEL_SPEC v0.1.

Permiso y Alcance deben entenderse como combinaciones conceptuales de estos modelos.

---

## 1. SystemState

SystemState refleja el estado general del sistema.

Puede mostrar:

- Permiso activo.
- Alcance activo.
- Modo activo.
- Fase actual.
- Estado de autorización.
- Restricciones activas.
- Si existe permiso vigente o no.
- Si el permiso expiró.

Uso en este documento:

SystemState no crea el permiso, pero refleja su estado dentro del sistema.

---

## 2. RobertDocument

RobertDocument identifica qué documento está afectado por un permiso o alcance.

Puede indicar:

- Documento autorizado.
- Documento restringido.
- Documento pendiente de revisión.
- Documento aprobado.
- Documento bloqueado.
- Documento relacionado con una autorización.

Uso en este documento:

Un permiso debe indicar si afecta a un RobertDocument específico.

---

## 3. DecisionRecord

DecisionRecord registra aprobaciones formales del usuario.

Puede registrar:

- Aprobación documental.
- Aprobación de alcance.
- Aprobación de integración.
- Aprobación de cambio de modo.
- Aprobación de sandbox.
- Aprobación de una decisión formal.

Uso en este documento:

Cuando un permiso se vuelve formal y afecta documentos oficiales, debe registrarse como DecisionRecord.

---

## 4. ChangeRecord

ChangeRecord registra cambios derivados de un permiso autorizado.

Puede registrar:

- Cambio documental.
- Corrección aplicada.
- Integración aprobada.
- Actualización de HOME.
- Actualización de README.
- Corrección de alcance.
- Cambio de estado.

Uso en este documento:

Si el permiso genera un cambio real dentro del sistema documental, debe existir ChangeRecord.

---

## 5. RiskRecord

RiskRecord evalúa el riesgo de la acción autorizada o solicitada.

Puede indicar:

- Nivel de riesgo.
- Motivo del riesgo.
- Si requiere aprobación.
- Si debe bloquearse.
- Si supera el alcance.
- Si implica acción futura no disponible.

Uso en este documento:

Todo permiso relevante debe poder conectarse con un RiskRecord.

---

## 6. CommandRequest

CommandRequest representa la solicitud del usuario.

Puede contener:

- Comando usado.
- Acción solicitada.
- Documento afectado.
- Intención.
- Alcance solicitado.
- Modo solicitado.
- Resultado esperado.

Uso en este documento:

Todo permiso comienza como una solicitud o comando del usuario, por lo tanto inicia como CommandRequest.

---

## 7. PendingDecision

PendingDecision representa una decisión pendiente cuando el permiso solicitado no puede resolverse automáticamente.

Puede aparecer cuando:

- Falta aprobación formal.
- El permiso es ambiguo.
- El alcance supera lo autorizado.
- La acción afecta documentos maestros.
- La acción afecta seguridad.
- La acción afecta fases.
- La acción puede acercarse a ejecución real.

Uso en este documento:

Si el permiso requiere decisión del usuario antes de continuar, debe convertirse en PendingDecision.

---

## 8. ModeState

ModeState indica el modo operativo actual.

Puede mostrar:

- Manual.
- Supervisado.
- Sandbox.
- Modo no disponible.
- Cambio de modo pendiente.
- Autonomía no autorizada.

Uso en este documento:

Todo permiso debe interpretarse dentro de un modo activo.

---

## 9. ComponentState

ComponentState muestra el estado visual o funcional de componentes relacionados con permisos.

Puede indicar:

- ApprovalGate activo.
- RiskBadge visible.
- DecisionInbox con pendientes.
- CurrentStatePanel mostrando alcance activo.
- TopBar mostrando modo o permiso activo.
- CommandCenter esperando aclaración.

Uso en este documento:

Permisos y alcances deben poder mostrarse mediante estados de componentes.

---

## 10. GitHubBackupStatus

GitHubBackupStatus refleja respaldo manual en GitHub.

Puede indicar:

- Respaldo manual actualizado.
- Commit sugerido.
- Commit confirmado por el usuario.
- Respaldo pendiente.
- GitHub no conectado automáticamente.

Uso en este documento:

Un permiso puede permitir confirmar respaldo manual, pero no conectar GitHub automáticamente.

---

## 11. ObsidianGraphStatus

ObsidianGraphStatus refleja estado visual/documental en Obsidian.

Puede indicar:

- Órbita actual.
- Documento visible.
- Tag corregido.
- Estado de grafo.
- Relación documental.
- Documento fuera de órbita esperada.

Uso en este documento:

Un permiso puede permitir revisar o corregir estado visual/documental, pero no automatizar Obsidian.

---

# MAPEO CONCEPTUAL DE PERMISO Y ALCANCE A MODELOS EXISTENTES

| Concepto de este documento | Modelo relacionado | Uso |
|---|---|---|
| Solicitud de permiso | CommandRequest | Captura lo que pide el usuario |
| Acción permitida | CommandRequest / RiskRecord | Define acción y riesgo |
| Documento afectado | RobertDocument | Identifica documento o área |
| Límite de riesgo | RiskRecord | Define riesgo máximo permitido |
| Modo operativo | ModeState | Indica si es manual, supervisado o sandbox |
| Duración | SystemState / PendingDecision | Refleja vigencia o pendiente |
| Restricciones | RiskRecord / ApprovalGate conceptualmente | Define límites |
| Revocación | CommandRequest / ModeState / SystemState | Reduce alcance o vuelve a manual |
| Aprobación formal | DecisionRecord | Registra autorización formal |
| Cambio derivado | ChangeRecord | Registra modificación documental |
| Estado visual | ComponentState | Muestra permiso activo |
| Respaldo manual | GitHubBackupStatus | Refleja commit manual |
| Estado visual documental | ObsidianGraphStatus | Refleja grafo/tags/órbitas |

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

# ROL DE CADA COMPONENTE EN PERMISOS Y ALCANCES

## AppShell

AppShell aloja los componentes que muestran permisos, alcances, bloqueos y estado general.

No decide permisos.

No aprueba permisos.

No evalúa riesgo.

---

## TopBar

TopBar debe mostrar el estado resumido del permiso o alcance activo cuando sea relevante.

Puede mostrar:

- Modo activo.
- Permiso activo.
- Alcance resumido.
- Estado de ejecución no autorizada.
- Estado de conexiones no autorizadas.
- Estado de automatizaciones no activas.
- Respaldo manual si aplica.

Ejemplo:

```text
Modo: Supervisado | Alcance: corrección documental | Ejecución: no autorizada
```

---

## LeftSidebar

LeftSidebar permite navegar a documentos afectados por permisos.

Puede mostrar:

- Documento activo.
- Carpeta.
- Estado documental.
- Documento dentro o fuera del alcance actual.

No modifica permisos.

---

## CommandCenter

CommandCenter recibe la solicitud de permiso del usuario.

Puede recibir:

- Autorización.
- Revocación.
- Cambio de alcance.
- Solicitud de aprobación.
- Solicitud de sandbox.
- Comando de control.

CommandCenter convierte la solicitud en CommandRequest.

---

## ModeSelector

ModeSelector muestra y representa el modo operativo relacionado con el permiso.

Puede mostrar:

- Manual.
- Supervisado.
- Sandbox.
- Modo restringido.
- Modo no disponible.

No activa autonomía real en Fase 10.

---

## RiskBadge

RiskBadge muestra el riesgo asociado al permiso solicitado.

Puede mostrar:

- Nivel de riesgo.
- Motivo.
- Si supera alcance.
- Si requiere aprobación.
- Si debe bloquearse.

---

## ApprovalGate

ApprovalGate valida si el permiso alcanza para continuar.

Puede mostrar:

- Permiso suficiente.
- Permiso insuficiente.
- Aprobación requerida.
- Acción fuera de alcance.
- Acción bloqueada.
- Confirmación requerida.

---

## DecisionInbox

DecisionInbox muestra permisos pendientes de aprobación formal.

Puede mostrar:

- Permiso pendiente.
- Documento afectado.
- Riesgo.
- Opciones: aprobar, rechazar, corregir, pausar.
- Si bloquea avance o no.

---

## DocumentStatusMap

DocumentStatusMap muestra documentos afectados por permisos.

Puede mostrar:

- Documento dentro del alcance.
- Documento fuera del alcance.
- Documento aprobado.
- Documento pendiente.
- Documento bloqueado.
- Cambio relacionado.
- Decisión relacionada.

---

## CurrentStatePanel

CurrentStatePanel debe mostrar el detalle más claro del permiso o alcance activo.

Debe mostrar:

- Permiso activo.
- Alcance activo.
- Documento autorizado.
- Modo activo.
- Duración.
- Riesgo máximo permitido.
- Acciones permitidas.
- Acciones prohibidas.
- Forma de revocación.
- Próximo paso permitido.
- Si el permiso expiró.

---

# DÓNDE SE MUESTRA CADA ELEMENTO DEL PERMISO

| Elemento | Componente principal | Componentes relacionados |
|---|---|---|
| Permiso activo | CurrentStatePanel | TopBar |
| Alcance activo | CurrentStatePanel | TopBar, DocumentStatusMap |
| Duración | CurrentStatePanel | ApprovalGate |
| Expiración | CurrentStatePanel | ApprovalGate |
| Riesgo máximo permitido | RiskBadge | CurrentStatePanel |
| Acción permitida | CommandCenter | ApprovalGate |
| Acción prohibida | ApprovalGate | RiskBadge |
| Documento afectado | DocumentStatusMap | LeftSidebar |
| Decisión pendiente | DecisionInbox | ApprovalGate |
| Revocación | CommandCenter | ModeSelector, CurrentStatePanel |
| Respaldo manual | TopBar | CurrentStatePanel, DocumentStatusMap |

---

# PRINCIPIO DE MÍNIMO PERMISO

Robert debe usar siempre el permiso mínimo necesario.

Regla:

**Si el usuario autoriza revisar, Robert no debe corregir.  
Si autoriza corregir, Robert no debe aprobar.  
Si autoriza aprobar, Robert no debe ejecutar.  
Si autoriza documentar, Robert no debe programar.**

---

# TIPOS DE PERMISOS

Robert puede manejar estos tipos conceptuales de permiso:

1. Permiso informativo.
2. Permiso de navegación.
3. Permiso de revisión.
4. Permiso de borrador.
5. Permiso de corrección documental.
6. Permiso de registro.
7. Permiso de aprobación documental.
8. Permiso de integración documental.
9. Permiso de sandbox manual.
10. Permiso de cambio de modo.
11. Permiso de respaldo manual.
12. Permiso futuro no disponible.
13. Permiso prohibido en Fase 10.

---

# PERMISO 1 — INFORMATIVO

## Qué permite

Permite que Robert explique, resuma, muestre estado o aclare información.

## Ejemplos

- RESUMEN.
- ESTADO.
- EXPLICAR.
- MOSTRAR.
- CONSULTAR.
- INFORME_ACCIONES si solo informa.

## Riesgo típico

Nivel 0 — Informativo.

## Requiere aprobación

No.

## Restricción

No modifica documentos.

No registra cambios formales.

No cambia estado del sistema.

---

# PERMISO 2 — NAVEGACIÓN

## Qué permite

Permite seleccionar, abrir, ubicar o revisar el estado de documentos.

## Ejemplos

- Abrir ROBERT_HOME.
- Ver CONTROL_DE_CAMBIOS.
- Revisar carpeta 10_MVP.
- Ver mapa documental.

## Riesgo típico

Nivel 0 — Informativo.

## Requiere aprobación

No.

## Restricción

Navegar no modifica documentos.

---

# PERMISO 3 — REVISIÓN

## Qué permite

Permite analizar un documento, detectar errores, contradicciones o mejoras.

## Ejemplos

- Revisar USER_ACTIONS_SPEC.
- Revisar contradicciones entre COMMANDS y SECURITY_RULES.
- Detectar errores de tags.
- Validar coherencia documental.

## Riesgo típico

Nivel 1 o Nivel 2.

Puede subir a Nivel 3 si afecta documento maestro o técnico aprobado.

## Requiere aprobación

No para revisar.

Sí para corregir oficialmente.

## Restricción

Revisar no corrige automáticamente.

---

# PERMISO 4 — BORRADOR

## Qué permite

Permite preparar contenido no oficial.

## Ejemplos

- Crear borrador de documento.
- Preparar propuesta.
- Preparar bloque para HOME.
- Preparar bloque para README.
- Preparar texto para copiar.

## Riesgo típico

Nivel 1 o Nivel 2.

Nivel 3 si el borrador afecta arquitectura, seguridad, fases o documento maestro.

## Requiere aprobación

No siempre para crear borrador.

Sí para convertirlo en oficial.

## Restricción

Borrador no es aprobación.

Borrador no es integración.

---

# PERMISO 5 — CORRECCIÓN DOCUMENTAL

## Qué permite

Permite modificar o reemplazar contenido documental para corregir errores o contradicciones.

## Ejemplos

- Corregir ROBERT_COMMANDS v0.4.
- Corregir ERROR_AND_BLOCKING_SPEC v0.2.
- Corregir tags.
- Corregir cronología.
- Alinear documentos.

## Riesgo típico

Nivel 2 o Nivel 3.

Nivel 3 si afecta documento maestro, seguridad, fases o documento técnico aprobado.

## Requiere aprobación

Sí si afecta documento oficial.

## Resultado permitido

Robert puede preparar:

- Versión corregida.
- Estado pendiente de revisión.
- Bloque para CONTROL_DE_CAMBIOS.
- Actualización de HOME.
- Actualización de README.

## Restricción

Corregir no significa aprobar.

---

# PERMISO 6 — REGISTRO

## Qué permite

Permite registrar cambios, decisiones o estados en documentos oficiales.

## Ejemplos

- Registrar DECISIÓN.
- Registrar CAMBIO.
- Actualizar HOME.
- Actualizar README.
- Registrar resultado de sandbox.

## Riesgo típico

Nivel 2 o Nivel 3.

## Requiere aprobación

Sí si el registro formaliza estado del sistema.

## Restricción

Robert no debe inventar registros.

El registro debe corresponder a una acción realmente aprobada o realizada por el usuario.

---

# PERMISO 7 — APROBACIÓN DOCUMENTAL

## Qué permite

Permite aprobar formalmente un documento.

## Ejemplos

- APRUEBO ROBERT_COMMANDS v0.4.
- APRUEBO USER_ACTIONS_SPEC v0.2.
- APRUEBO ERROR_AND_BLOCKING_SPEC v0.2.

## Riesgo típico

Nivel 3 — Alto.

## Requiere aprobación

Sí.

La aprobación debe ser explícita.

## Resultado permitido

Robert puede preparar:

- Decisión formal.
- Cambio de aprobación.
- Actualización de HOME.
- Actualización de README.

## Restricción

Aprobar documento no autoriza programación.

Aprobar documento no autoriza ejecución real.

---

# PERMISO 8 — INTEGRACIÓN DOCUMENTAL

## Qué permite

Permite integrar un documento aprobado al estado actual de Robert.

## Ejemplos

- Marcar documento como aprobado e integrado.
- Relacionarlo con documentos base.
- Actualizar estado general.
- Actualizar mapa documental.

## Riesgo típico

Nivel 3 — Alto.

## Requiere aprobación

Sí.

## Restricción

Integración documental no equivale a implementación técnica real.

---

# PERMISO 9 — SANDBOX MANUAL

## Qué permite

Permite simular, probar o validar acciones dentro de un entorno manual, documental y seguro.

## Documentos oficiales

La lógica de sandbox vive en:

- ROBERT_SANDBOX
- SANDBOX_RULES
- SANDBOX_TESTS
- SANDBOX_RESULTS

## Riesgo típico

Nivel 2 o Nivel 3.

Nivel 4 si intenta convertirse en ejecución real.

## Requiere aprobación

Sí.

## Restricción

Sandbox manual no ejecuta acciones reales.

Sandbox manual no conecta herramientas.

Sandbox manual no activa automatizaciones.

Sandbox manual no aprueba documentos por sí solo.

---

# PERMISO 10 — CAMBIO DE MODO

## Qué permite

Permite cambiar conceptualmente el modo operativo de Robert.

## Modos permitidos actualmente

- Manual.
- Supervisado.
- Sandbox.

## Modos no disponibles todavía

- Autónomo real.
- Ejecución limitada real.
- Agentes autónomos reales.
- Automatización real.
- Conexión real.

## Riesgo típico

Nivel 2 o Nivel 3.

Nivel 4 si intenta activar autonomía real o ejecución externa.

## Requiere aprobación

Sí si cambia alcance o afecta documentos oficiales.

## Restricción

Cambiar modo no activa autonomía real.

---

# PERMISO 11 — RESPALDO MANUAL

## Qué permite

Permite que el usuario confirme que realizó manualmente un respaldo o commit en GitHub.

## Ejemplos

- Ya actualicé README.
- Ya registré CAMBIO.
- Ya hice commit.
- Ya actualicé HOME.

## Riesgo típico

Nivel 1 o Nivel 2.

## Requiere aprobación

No si solo confirma una acción manual ya realizada.

Sí si implica cambio formal de estado.

## Restricción

Robert no se conecta automáticamente a GitHub.

GitHub sigue siendo respaldo manual en Fase 10.

---

# PERMISO 12 — FUTURO NO DISPONIBLE

## Qué significa

Son permisos que podrán existir en fases futuras, pero no están activos todavía.

## Ejemplos

- Conectar Gmail.
- Conectar Google Calendar.
- Conectar GitHub automáticamente.
- Conectar Supabase.
- Conectar Firebase.
- Activar automatizaciones.
- Activar agentes autónomos.
- Ejecutar código real.
- Crear app funcional.
- Crear base de datos real.

## Riesgo típico

Nivel 4 si se intenta activar.

## Resultado permitido

Robert puede:

- Documentar.
- Diseñar conceptualmente.
- Preparar especificación futura.
- Simular en sandbox manual.

## Restricción

No puede activar estas capacidades en Fase 10.

---

# PERMISO 13 — PROHIBIDO EN FASE 10

## Qué significa

Son acciones que deben bloquearse en el estado actual de Robert.

## Ejemplos

- Programar app real.
- Crear código real.
- Crear botones reales.
- Crear pantallas reales.
- Crear base de datos real.
- Conectar herramientas externas.
- Automatizar acciones reales.
- Activar agentes autónomos.
- Ejecutar acciones reales.
- Avanzar a Fase 11 sin decisión formal.

## Riesgo típico

Nivel 4 — Crítico.

## Resultado permitido

Robert debe bloquear.

## Restricción

Solo se puede preparar documentación, borrador, análisis o simulación segura.

---

# CORRESPONDENCIA ENTRE PERMISOS Y ACCIONES

Esta tabla conecta los permisos definidos en este documento con las acciones definidas en USER_ACTIONS_SPEC v0.2.

Regla:

**Una acción del usuario solo puede avanzar si existe el permiso conceptual correspondiente y no supera el alcance autorizado.**

| Permiso | Acción relacionada de USER_ACTIONS_SPEC v0.2 | Relación |
|---|---|---|
| PERMISO 1 — Informativo | ACCIÓN 3 — Revisar estado general | Permite mostrar estado |
| PERMISO 1 — Informativo | ACCIÓN 15 — Ver decisiones pendientes | Permite consultar pendientes |
| PERMISO 1 — Informativo | ACCIÓN 17 — Ver mapa documental | Permite consultar mapa |
| PERMISO 1 — Informativo | ACCIÓN 20 — Pedir siguiente paso | Permite recomendar, no ejecutar |
| PERMISO 2 — Navegación | ACCIÓN 2 — Seleccionar documento | Permite abrir o ubicar documentos |
| PERMISO 3 — Revisión | ACCIÓN 19 — Solicitar revisión crítica | Permite detectar errores |
| PERMISO 4 — Borrador | ACCIÓN 1 — Escribir comando | Permite preparar respuesta o borrador según intención |
| PERMISO 4 — Borrador | ACCIÓN 4 — Crear documento técnico | Permite crear borrador pendiente |
| PERMISO 5 — Corrección documental | ACCIÓN 5 — Corregir documento técnico | Permite corregir sin aprobar |
| PERMISO 6 — Registro | ACCIÓN 7 — Registrar decisión | Permite preparar o registrar decisión autorizada |
| PERMISO 6 — Registro | ACCIÓN 8 — Registrar cambio | Permite preparar o registrar cambio autorizado |
| PERMISO 6 — Registro | ACCIÓN 9 — Actualizar HOME | Permite actualizar HOME con confirmación |
| PERMISO 6 — Registro | ACCIÓN 10 — Actualizar README | Permite actualizar README con confirmación |
| PERMISO 7 — Aprobación documental | ACCIÓN 6 — Aprobar documento | Permite aprobar formalmente |
| PERMISO 7 — Aprobación documental | ACCIÓN 16 — Resolver decisión pendiente | Permite aprobar, rechazar o pausar una decisión |
| PERMISO 8 — Integración documental | ACCIÓN 6 — Aprobar documento | Permite integrar después de aprobación |
| PERMISO 9 — Sandbox manual | ACCIÓN 12 — Solicitar sandbox manual | Permite simular dentro de sandbox |
| PERMISO 10 — Cambio de modo | ACCIÓN 11 — Cambiar modo | Permite cambiar modo conceptual |
| PERMISO 11 — Respaldo manual | ACCIÓN 18 — Marcar respaldo manual en GitHub | Permite confirmar respaldo manual |
| Acción de control fuera de escala | ACCIÓN 13 — Pausar avance | Permite detener avance |
| Acción de control fuera de escala | ACCIÓN 14 — Solicitar bloqueo manual | Permite bloquear manualmente |
| PERMISO 12 — Futuro no disponible | Acciones futuras no disponibles | Solo permite documentar o diseñar |
| PERMISO 13 — Prohibido en Fase 10 | Acciones prohibidas en esta fase | Debe bloquearse |

---

# REGLA DE CORRESPONDENCIA

Si una acción no tiene permiso correspondiente, Robert debe:

1. Pausar.
2. Identificar qué permiso falta.
3. Mostrar el alcance necesario.
4. Pedir confirmación o aprobación.
5. Bloquear si implica ejecución real, conexión, automatización o avance de fase.

Ejemplo:

```text
Acción solicitada: aprobar documento
Permiso requerido: PERMISO 7 — Aprobación documental
Estado: requiere aprobación explícita
```

---

# DURACIÓN DE AUTORIZACIONES

Una autorización puede durar:

1. Una sola respuesta.
2. Un solo paso.
3. Un documento.
4. Una sección.
5. Una tarea.
6. Una sesión.
7. Hasta revocación explícita.
8. Hasta cerrar una fase.

En Fase 10, la duración recomendada es:

**Un paso o un documento a la vez.**

---

# REGLA DE EXPIRACIÓN

Una autorización expira cuando:

- Se completa la acción autorizada.
- Cambia el documento afectado.
- Cambia la fase.
- Cambia el modo.
- El usuario dice PAUSA.
- El usuario dice DETENTE.
- El usuario dice NO_AVANCES.
- El usuario dice REVOCA_AUTONOMIA.
- El usuario dice VOLVER_A_MANUAL.
- Aparece riesgo mayor al autorizado.
- Aparece contradicción documental.
- Se intenta acción externa.
- Se intenta ejecución real.

---

# REGLA DE REVOCACIÓN

El usuario puede revocar autorización en cualquier momento.

Comandos relacionados:

- DETENTE.
- PAUSA.
- NO_AVANCES.
- SOLO_BORRADOR.
- REVOCA_AUTONOMIA.
- VOLVER_A_MANUAL.
- BLOQUEA.
- CANCELA.
- NO_SIGAS.
- NO_EJECUTES.

Clasificación:

**Acciones de control fuera de la escala de riesgo**

Regla:

**Revocar autorización reduce alcance. No aumenta riesgo.**

---

# ESTRUCTURA MÍNIMA DE UNA AUTORIZACIÓN

Antes de actuar con un permiso relevante, Robert debe poder identificar:

```text
Acción autorizada:
Documento afectado:
Alcance:
Modo:
Duración:
Riesgo máximo permitido:
Acciones permitidas:
Acciones prohibidas:
Registro requerido:
Forma de revocación:
```

Si falta algo importante, Robert debe preguntar o pausar.

---

# EJEMPLO DE AUTORIZACIÓN CORRECTA

```text
Autorizo corregir ERROR_AND_BLOCKING_SPEC v0.2 como propuesta documental.
Puedes cambiar el texto del documento.
No lo apruebes.
No registres decisión todavía.
No avances a otro documento.
No programes.
```

Interpretación:

- Acción autorizada: corregir documento.
- Documento afectado: ERROR_AND_BLOCKING_SPEC.
- Estado final permitido: propuesta corregida.
- No autorizado: aprobación, programación, avance de fase.

---

# EJEMPLO DE AUTORIZACIÓN AMBIGUA

```text
Haz todo.
```

Problema:

- No define documento.
- No define alcance.
- No define duración.
- No define riesgo máximo.
- No define si puede aprobar.
- No define si puede registrar cambios.

Respuesta correcta de Robert:

```text
Necesito aclarar el alcance antes de avanzar. ¿Quieres que prepare un borrador, corrija un documento o registre una decisión?
```

---

# EJEMPLO DE AUTORIZACIÓN EXCEDIDA

Usuario autoriza:

```text
Corrige USER_ACTIONS_SPEC.
```

Robert no puede asumir:

```text
Aprobar USER_ACTIONS_SPEC.
Registrar DECISIÓN.
Registrar CAMBIO.
Actualizar HOME.
Actualizar README.
Avanzar al siguiente documento.
```

Cada paso requiere autorización o confirmación separada.

---

# MATRIZ DE PERMISOS

| Permiso | Riesgo típico | Requiere aprobación | Resultado permitido |
|---|---:|---|---|
| Informativo | 0 | No | Explicar o mostrar |
| Navegación | 0 | No | Ver documento |
| Revisión | 1-2 | No para revisar | Detectar errores |
| Borrador | 1-2 | Depende | Preparar propuesta |
| Corrección documental | 2-3 | Sí si oficial | Propuesta corregida |
| Registro | 2-3 | Sí si formal | Decisión o cambio |
| Aprobación documental | 3 | Sí explícita | Documento aprobado |
| Integración documental | 3 | Sí explícita | Documento integrado |
| Sandbox manual | 2-3 | Sí | Simulación documental |
| Cambio de modo | 2-4 | Depende | Cambio conceptual o bloqueo |
| Respaldo manual | 1-2 | No si confirma | Estado conversacional |
| Futuro no disponible | 2-4 | No activable | Diseño conceptual |
| Prohibido en Fase 10 | 4 | No activable | Bloqueo |

---

# REGLAS DE BLOQUEO POR PERMISO

Robert debe bloquear cuando:

- El permiso es ambiguo.
- El permiso intenta activar algo real.
- El permiso supera Fase 10.
- El permiso contradice SECURITY_RULES.
- El permiso contradice PHASES.
- El permiso afecta documento maestro sin aprobación.
- El permiso intenta conectar herramientas.
- El permiso intenta automatizar.
- El permiso intenta activar agentes.
- El permiso intenta ejecutar código.
- El permiso intenta usar datos sensibles sin control.
- El permiso intenta saltarse ApprovalGate.
- El permiso ignora PAUSA, DETENTE o NO_AVANCES.

---

# RELACIÓN CON ERROR_AND_BLOCKING_SPEC

Si una acción supera el permiso autorizado, puede activarse:

- EVENTO 5 — Bloqueo automático.
- EVENTO 12 — Fuera de alcance.
- EVENTO 15 — Ejecución no autorizada.
- EVENTO 16 — Conexión no autorizada.
- EVENTO 17 — Automatización no autorizada.
- EVENTO 18 — Agente no autorizado.
- EVENTO 19 — Dato sensible detectado.
- EVENTO 20 — Fase incorrecta.

Regla:

**EVENTO 5 funciona como categoría general de respaldo cuando no aplique un subtipo específico.**

Regla adicional:

**Cuando el permiso no alcanza, Robert debe detenerse.**

---

# RELACIÓN CON USER_ACTIONS_SPEC

USER_ACTIONS_SPEC define qué acciones puede intentar el usuario.

PERMISSIONS_AND_SCOPES_SPEC define qué permisos necesita cada acción para continuar.

Ejemplo:

- Acción: aprobar documento.
- Permiso requerido: aprobación documental explícita.
- Registro posterior: decisión formal y cambio.

---

# RELACIÓN CON ROBERT_COMMANDS

ROBERT_COMMANDS v0.4 define comandos como:

- APRUEBO.
- APROBADO.
- DETENTE.
- PAUSA.
- NO_AVANCES.
- SOLO_BORRADOR.
- REVOCA_AUTONOMIA.
- VOLVER_A_MANUAL.
- MODO_SANDBOX.
- MODO_SUPERVISADO.
- AUTORIZAR_AMBITO.

PERMISSIONS_AND_SCOPES_SPEC define cómo esos comandos se traducen en permisos, límites o revocaciones.

Regla:

**Comando no significa permiso ilimitado.**

---

# RELACIÓN CON SCREEN_STATE_SPEC

SCREEN_STATE_SPEC define qué ve el usuario en pantalla.

PERMISSIONS_AND_SCOPES_SPEC define qué información de permisos debe aparecer en esas pantallas.

Ejemplo:

- CurrentStatePanel muestra permiso activo y alcance.
- TopBar muestra modo y alcance resumido.
- ApprovalGate muestra si el permiso alcanza.
- RiskBadge muestra riesgo del permiso.
- DecisionInbox muestra permisos pendientes.

---

# RELACIÓN CON INTERACTION_FLOW_SPEC

INTERACTION_FLOW_SPEC define cómo fluyen datos entre componentes.

PERMISSIONS_AND_SCOPES_SPEC no debe inventar nuevas direcciones de datos.

Si un permiso requiere un nuevo flujo entre componentes, primero debe revisarse INTERACTION_FLOW_SPEC.

---

# RELACIÓN CON SANDBOX

PERMISSIONS_AND_SCOPES_SPEC no redefine sandbox.

La lógica de sandbox vive en:

- ROBERT_SANDBOX
- SANDBOX_RULES
- SANDBOX_TESTS
- SANDBOX_RESULTS

Este documento solo define cuándo el usuario puede autorizar una simulación sandbox y qué límites tiene.

Regla:

**Sandbox autorizado no significa ejecución autorizada.**

---

# TABLA DE CORRECCIONES v0.2

| Punto corregido | Estado v0.1 | Estado v0.2 |
|---|---|---|
| Relación con DATA_MODEL_SPEC | Solo se mencionaba como documento relacionado | Se mapea permiso/alcance con los 11 modelos |
| Permiso y Alcance | Parecían estructuras nuevas no registradas | Se aclara que son estructuras conceptuales derivadas |
| Modelo PermissionScope | No estaba aclarado | No se crea todavía; requeriría actualizar DATA_MODEL_SPEC |
| Componentes | No había sección de componentes | Se agrega lista de 10 componentes y su rol |
| Visualización de permisos | No estaba definido dónde se muestra | CurrentStatePanel, TopBar, ApprovalGate, RiskBadge y DecisionInbox |
| Correspondencia con acciones | No había tabla | Se agrega tabla Permisos ↔ Acciones |
| ERROR_AND_BLOCKING | Faltaba EVENTO 5 como respaldo | Se agrega EVENTO 5 — Bloqueo automático como categoría general |

---

# CRITERIOS DE ACEPTACIÓN

Este documento podrá considerarse listo para aprobación si:

- Define permisos conceptuales.
- Define alcances conceptuales.
- Define duración de autorizaciones.
- Define expiración de autorizaciones.
- Define revocación.
- Define autorización mínima.
- Define permisos permitidos.
- Define permisos futuros no disponibles.
- Define permisos prohibidos en Fase 10.
- Conecta Permiso y Alcance con DATA_MODEL_SPEC v0.1.
- Aclara que PermissionScope no es modelo oficial todavía.
- Define componentes participantes.
- Define dónde se muestra permiso activo.
- Define dónde se muestra alcance activo.
- Relaciona permisos con acciones de USER_ACTIONS_SPEC v0.2.
- Incluye EVENTO 5 como bloqueo automático general de respaldo.
- Mantiene Nivel 0 únicamente como Informativo.
- Mantiene acciones de control fuera de la escala de riesgo.
- Respeta ROBERT_COMMANDS v0.4.
- Respeta USER_ACTIONS_SPEC v0.2.
- Respeta ERROR_AND_BLOCKING_SPEC v0.2.
- Respeta SCREEN_STATE_SPEC v0.2.
- Respeta INTERACTION_FLOW_SPEC v0.2.
- Respeta DATA_MODEL_SPEC v0.1.
- Respeta documentos sandbox oficiales.
- No autoriza programación.
- No autoriza código real.
- No autoriza botones reales.
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

**Cambio técnico documental / permisos y alcances conceptuales**

Nivel de riesgo inicial:

**Nivel 3 — Alto**

Motivo:

Este documento define cómo Robert interpreta permisos, alcances y límites de autorización. Aunque sigue siendo conceptual, influye en la seguridad operativa futura del sistema.

Nivel de riesgo final esperado:

**Nivel 2 — Medio**

Motivo de reducción:

El documento es documental. No crea sistema real de permisos, no crea botones reales, no crea pantallas reales, no programa, no conecta herramientas externas y no ejecuta acciones.

Nivel de autonomía:

**Nivel 0 — Sin autonomía ejecutiva**

---

# DECISIÓN PENDIENTE

Este documento queda como:

**Propuesta corregida pendiente de revisión**

Para aprobarlo formalmente, el usuario deberá escribir:

**APRUEBO ROBERT_TECHNICAL_PERMISSIONS_AND_SCOPES_SPEC v0.2**

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

**ROBERT_TECHNICAL_AUDIT_TRAIL_SPEC**

Ese documento definiría cómo registrar historial, trazabilidad, acciones realizadas, acciones bloqueadas, aprobaciones, cambios, decisiones y evidencia documental.

No debe crearse hasta revisar o aprobar PERMISSIONS_AND_SCOPES_SPEC.

---

# CIERRE

ROBERT_TECHNICAL_PERMISSIONS_AND_SCOPES_SPEC v0.2 define permisos, alcances, límites, duración de autorizaciones y revocación dentro del MVP técnico básico de Robert.

Esta versión conecta permisos y alcances con DATA_MODEL_SPEC v0.1, agrega componentes participantes, define dónde se muestran permisos activos, conecta permisos con acciones de USER_ACTIONS_SPEC v0.2 e integra EVENTO 5 como bloqueo automático general de respaldo.

Este documento mantiene a Robert en modo documental, manual y supervisado.

El usuario mantiene control total.

Robert no ejecuta acciones importantes sin permiso.
