# ROBERT_TECHNICAL_USER_ACTIONS_SPEC

Versión: 0.1  
Estado: Borrador técnico documental nuevo — pendiente de revisión  
Fecha: 04/07/2026  
Ubicación: 10_MVP  
Fase relacionada: Fase 10 — MVP técnico básico en preparación  
Documento base principal: ROBERT_TECHNICAL_SCREEN_STATE_SPEC v0.2  
Documentos relacionados: ROBERT_TECHNICAL_INTERACTION_FLOW_SPEC v0.2, ROBERT_TECHNICAL_COMPONENTS_SPEC v0.2, ROBERT_TECHNICAL_DATA_MODEL_SPEC v0.1  
Fuente de verdad actual: ROBERT_CONTEXT_MASTER v0.5  

Tags: #robert/orbita-3 #capa/5 #tipo/tecnico #robert/mvp #robert/user-actions

---

# OBJETIVO

ROBERT_TECHNICAL_USER_ACTIONS_SPEC define qué acciones puede intentar hacer el usuario desde cada pantalla o panel del MVP técnico básico de Robert.

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

Este documento no programa la app.

Este documento no crea botones reales.

Este documento no crea pantallas reales.

Este documento no crea código.

Este documento no conecta herramientas externas.

Este documento no ejecuta acciones reales.

---

# ESTADO DEL DOCUMENTO

Este documento queda como:

**Borrador técnico documental nuevo — pendiente de revisión**

No está aprobado todavía.

No reemplaza a ningún documento maestro.

No autoriza programación.

No autoriza prototipo funcional.

No autoriza base de datos real.

No autoriza conexiones externas.

No autoriza automatizaciones.

No autoriza agentes autónomos.

No autoriza ejecución real.

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
- ROBERT_CONTEXT_MASTER v0.5 reanclado.
- ROBERT_PHASES v0.5 reconciliado.
- Escala de riesgo y autonomía unificada.
- ROBERT_TECHNICAL_MVP_PLAN aprobado.
- ROBERT_TECHNICAL_MVP_WIREFRAME v0.3 aprobado.
- ROBERT_TECHNICAL_COMPONENTS_SPEC v0.2 aprobado.
- ROBERT_TECHNICAL_DATA_MODEL_SPEC v0.1 aprobado e integrado.
- ROBERT_TECHNICAL_INTERACTION_FLOW_SPEC v0.2 aprobado e integrado.
- ROBERT_TECHNICAL_SCREEN_STATE_SPEC v0.2 aprobado e integrado.
- ROBERT_TECHNICAL_USER_ACTIONS_SPEC v0.1 creado como borrador.
- Sin programación autorizada.
- Sin código real.
- Sin pantallas reales.
- Sin base de datos real.
- Sin conexiones externas.
- Sin automatizaciones reales.
- Sin agentes autónomos activos.

---

# ALCANCE AUTORIZADO

Este documento autoriza únicamente:

- Definir acciones conceptuales del usuario.
- Relacionar acciones con pantallas y componentes.
- Clasificar acciones por riesgo.
- Definir cuándo una acción requiere aprobación.
- Definir cuándo una acción debe bloquearse.
- Definir qué ocurre después de una acción.
- Mantener alineación con SCREEN_STATE_SPEC v0.2.
- Mantener alineación con INTERACTION_FLOW_SPEC v0.2.
- Mantener a Robert en modo documental, manual y supervisado.

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
10. Acción bloqueada por fase.
11. Acción prohibida.
12. Acción futura no disponible.

---

# NIVELES DE RIESGO APLICABLES

Robert usa la escala oficial:

- Nivel 0 — Informativo.
- Nivel 1 — Bajo.
- Nivel 2 — Medio.
- Nivel 3 — Alto.
- Nivel 4 — Crítico.

Regla:

**No existe Nivel 5 como riesgo.**

Nivel 5 solo puede existir como autonomía, no como riesgo.

---

# COMPONENTES BASE

Este documento usa los componentes aprobados:

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

# MODELOS RELACIONADOS

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

Este documento no crea un modelo de datos nuevo oficial.

Las acciones del usuario se entienden conceptualmente como instrucciones, solicitudes o intentos de operación que pueden convertirse en CommandRequest, PendingDecision, RiskRecord, DecisionRecord o ChangeRecord según el caso.

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

## Flujo activado

- CommandRequest.
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

## Restricción

CommandCenter no ejecuta acciones reales.

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

## Restricción

Seleccionar un documento no lo modifica.

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

## Riesgo

Nivel 0 — Informativo.

## Resultado permitido

Robert puede mostrar estado actual.

## Restricción

Ver estado no autoriza avanzar.

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

## Riesgo

Nivel 3 — Alto.

## Motivo

Crear documentos técnicos puede cambiar la arquitectura conceptual de Robert y acercar el proyecto a implementación futura.

## Resultado permitido

Robert puede crear:

- Borrador documental.
- Propuesta pendiente de revisión.
- Texto para copiar y pegar.
- Commit sugerido.

## Requiere aprobación

No siempre para crear borrador, pero sí para aprobar formalmente.

## Restricción

Crear documento técnico no autoriza programación.

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

## Restricción

Corregir no significa aprobar.

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

## Riesgo

Nivel 3 — Alto.

## Resultado permitido

Robert puede preparar:

- Registro de decisión.
- Registro de cambio.
- Actualización de HOME.
- Actualización de README.
- Estado aprobado e integrado.

## Requiere aprobación explícita

Sí.

Debe existir instrucción clara del usuario.

## Restricción

Aprobar documento no autoriza ejecución real.

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

## Riesgo

Nivel 2 o Nivel 3.

Nivel 3 si afecta documento técnico, maestro, seguridad o fases.

## Resultado permitido

Robert puede preparar bloque para pegar en DECISIONS_LOG.

## Restricción

La decisión debe representar una aprobación real del usuario.

Robert no debe inventar aprobaciones.

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

## Riesgo

Nivel 2 o Nivel 3.

Nivel 3 si el cambio afecta documentos técnicos, maestros, seguridad o fases.

## Resultado permitido

Robert puede preparar bloque de cambio para pegar.

## Restricción

Registrar cambio no autoriza acciones externas.

---

# ACCIÓN 9 — ACTUALIZAR HOME

## Dónde ocurre

CommandCenter.

## Qué intenta hacer el usuario

El usuario actualiza ROBERT_HOME con el nuevo estado del sistema.

## Componente principal

CommandCenter.

## Componentes relacionados

- CurrentStatePanel.
- DocumentStatusMap.
- TopBar.

## Riesgo

Nivel 2 — Medio.

## Resultado permitido

Robert puede preparar bloque para ROBERT_HOME.

## Restricción

HOME debe reflejar estado real, no capacidades futuras como si estuvieran activas.

---

# ACCIÓN 10 — ACTUALIZAR README

## Dónde ocurre

CommandCenter.

## Qué intenta hacer el usuario

El usuario actualiza README.md con el estado general del repositorio.

## Componente principal

CommandCenter.

## Componentes relacionados

- DocumentStatusMap.
- TopBar.
- CurrentStatePanel.

## Riesgo

Nivel 2 — Medio.

## Resultado permitido

Robert puede preparar bloque para README.

## Restricción

README no debe decir que hay app funcional si todavía no existe.

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

## Componente principal

ModeSelector.

## Componentes relacionados

- ApprovalGate.
- RiskBadge.
- CurrentStatePanel.

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

## Restricción

Cambiar modo no activa autonomía real.

---

# ACCIÓN 12 — ACTIVAR SANDBOX MANUAL

## Dónde ocurre

ModeSelector o CommandCenter.

## Qué intenta hacer el usuario

El usuario quiere entrar en modo de prueba controlada.

## Componente principal

ModeSelector.

## Componentes relacionados

- RiskBadge.
- ApprovalGate.
- CurrentStatePanel.
- DocumentStatusMap.

## Riesgo

Nivel 2 o Nivel 3.

## Resultado permitido

Robert puede operar en simulación documental.

## Restricción

Sandbox manual no ejecuta acciones reales.

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

## Componente principal

ApprovalGate.

## Componentes relacionados

- CommandCenter.
- CurrentStatePanel.
- DecisionInbox.

## Riesgo

Nivel 0 — Control de seguridad.

## Resultado permitido

Robert debe detener el avance.

## Restricción

Robert no debe continuar al siguiente paso hasta nueva autorización.

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

## Riesgo

Nivel 0 como acción de control.

La acción bloqueada puede tener Nivel 3 o Nivel 4.

## Resultado permitido

Robert debe mostrar motivo del bloqueo.

## Restricción

Robert no debe buscar rutas alternas para ejecutar lo bloqueado.

---

# ACCIÓN 15 — VER DECISIONES PENDIENTES

## Dónde ocurre

DecisionInbox.

## Qué intenta hacer el usuario

El usuario quiere revisar qué decisiones siguen pendientes.

## Componente principal

DecisionInbox.

## Componentes relacionados

- CurrentStatePanel.
- DocumentStatusMap.

## Riesgo

Nivel 0 — Informativo.

## Resultado permitido

Robert puede mostrar:

- Decisiones pendientes.
- Motivo.
- Riesgo.
- Documento afectado.
- Opciones disponibles.

## Restricción

Ver pendientes no resuelve decisiones.

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

## Riesgo

Nivel 2 o Nivel 3.

## Resultado permitido

Robert puede preparar el registro correspondiente.

## Restricción

Robert no resuelve decisiones sin instrucción del usuario.

---

# ACCIÓN 17 — VER MAPA DOCUMENTAL

## Dónde ocurre

DocumentStatusMap.

## Qué intenta hacer el usuario

El usuario quiere ver los documentos, estados y relaciones del sistema.

## Componente principal

DocumentStatusMap.

## Componentes relacionados

- LeftSidebar.
- CurrentStatePanel.

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

## Restricción

Ver el mapa no modifica documentos.

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

## Componente principal

CurrentStatePanel.

## Componentes relacionados

- TopBar.
- DocumentStatusMap.
- CommandCenter.

## Riesgo

Nivel 1 o Nivel 2.

## Resultado permitido

Robert puede actualizar el estado documental de la conversación y preparar el siguiente paso.

## Restricción

Robert no debe asumir que puede conectarse a GitHub automáticamente.

---

# ACCIÓN 19 — SOLICITAR REVISIÓN CRÍTICA

## Dónde ocurre

CommandCenter.

## Qué intenta hacer el usuario

El usuario pide revisar un documento para detectar contradicciones.

## Componente principal

CommandCenter.

## Componentes relacionados

- RiskBadge.
- DocumentStatusMap.
- CurrentStatePanel.

## Riesgo

Nivel 2.

Puede subir a Nivel 3 si la revisión afecta documento maestro o técnico aprobado.

## Resultado permitido

Robert puede:

- Señalar inconsistencias.
- Recomendar correcciones.
- Proponer v0.2 o nueva versión.
- Mantener pendiente de aprobación.

## Restricción

Revisar no aprueba ni modifica por sí solo.

---

# ACCIÓN 20 — PEDIR SIGUIENTE PASO

## Dónde ocurre

CommandCenter.

## Qué intenta hacer el usuario

El usuario pregunta qué sigue.

## Componente principal

CommandCenter.

## Componentes relacionados

- CurrentStatePanel.
- DecisionInbox.
- DocumentStatusMap.

## Riesgo

Nivel 0 o Nivel 1.

## Resultado permitido

Robert puede recomendar siguiente paso.

## Restricción

Recomendar no significa avanzar sin autorización.

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

# TABLA RESUMEN DE ACCIONES

| Acción | Componente principal | Riesgo típico | Resultado permitido |
|---|---|---:|---|
| Escribir comando | CommandCenter | Variable | Clasificar, responder o pedir aprobación |
| Seleccionar documento | LeftSidebar | 0 | Mostrar documento |
| Revisar estado | CurrentStatePanel | 0 | Mostrar estado |
| Crear documento técnico | CommandCenter | 3 | Borrador pendiente |
| Corregir documento | CommandCenter | 2-3 | Propuesta corregida |
| Aprobar documento | DecisionInbox | 3 | Decisión y cambio |
| Registrar decisión | CommandCenter | 2-3 | Bloque para DECISIONS_LOG |
| Registrar cambio | CommandCenter | 2-3 | Bloque para CONTROL_DE_CAMBIOS |
| Actualizar HOME | CommandCenter | 2 | Bloque para HOME |
| Actualizar README | CommandCenter | 2 | Bloque para README |
| Cambiar modo | ModeSelector | 2-4 | Cambio conceptual o bloqueo |
| Activar sandbox manual | ModeSelector | 2-3 | Simulación documental |
| Pausar avance | ApprovalGate | 0 | Detener avance |
| Bloquear acción | ApprovalGate | 0 | Bloqueo visible |
| Ver decisiones pendientes | DecisionInbox | 0 | Mostrar pendientes |
| Resolver decisión | DecisionInbox | 2-3 | Registro correspondiente |
| Ver mapa documental | DocumentStatusMap | 0 | Mostrar mapa |
| Marcar respaldo manual | CurrentStatePanel | 1-2 | Actualizar estado conversacional |
| Solicitar revisión crítica | CommandCenter | 2-3 | Detectar inconsistencias |
| Pedir siguiente paso | CommandCenter | 0-1 | Recomendar, no ejecutar |

---

# CRITERIOS DE ACEPTACIÓN

Este documento podrá considerarse listo para aprobación si:

- Define qué acciones puede intentar el usuario.
- Relaciona acciones con componentes.
- Clasifica acciones por riesgo.
- Define resultados permitidos.
- Define restricciones.
- Define acciones prohibidas.
- Define acciones futuras no disponibles.
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

**Cambio técnico documental / acciones conceptuales del usuario**

Nivel de riesgo inicial:

**Nivel 3 — Alto**

Motivo:

Este documento define qué acciones podría intentar hacer el usuario desde el MVP técnico básico. Aunque sigue siendo conceptual, acerca el sistema a una futura lógica de interacción.

Nivel de riesgo final esperado:

**Nivel 2 — Medio**

Motivo de reducción:

El documento es documental. No crea botones reales, no crea pantallas reales, no programa, no conecta herramientas externas y no ejecuta acciones.

Nivel de autonomía:

**Nivel 0 — Sin autonomía ejecutiva**

---

# DECISIÓN PENDIENTE

Este documento queda como:

**Borrador técnico documental pendiente de revisión**

Para aprobarlo formalmente, el usuario deberá escribir:

**APRUEBO ROBERT_TECHNICAL_USER_ACTIONS_SPEC v0.1**

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

**ROBERT_TECHNICAL_ERROR_AND_BLOCKING_SPEC**

Ese documento definiría cómo Robert debe mostrar errores, bloqueos, advertencias, intentos prohibidos y acciones detenidas.

No debe crearse hasta revisar o aprobar USER_ACTIONS_SPEC.

---

# CIERRE

ROBERT_TECHNICAL_USER_ACTIONS_SPEC v0.1 define las acciones conceptuales que el usuario puede intentar desde cada pantalla o panel del MVP técnico básico.

Este documento mantiene a Robert en modo documental, manual y supervisado.

El usuario mantiene control total.

Robert no ejecuta acciones importantes sin permiso.
