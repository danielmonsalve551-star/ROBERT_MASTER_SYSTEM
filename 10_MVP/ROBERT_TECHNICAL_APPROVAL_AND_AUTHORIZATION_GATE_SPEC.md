# ROBERT_TECHNICAL_APPROVAL_AND_AUTHORIZATION_GATE_SPEC

Versión: v0.3  
Estado: Propuesta corregida — pendiente de revisión  
Fecha: 07/07/2026  
Ubicación: 10_MVP  
Fase relacionada: Fase 10 — MVP técnico básico en preparación  
Documento base principal: ROBERT_TECHNICAL_USER_ACTIONS_SPEC v0.2 auditado  
Documentos relacionados: ROBERT_TECHNICAL_COMPONENTS_SPEC v0.2, ROBERT_TECHNICAL_DATA_MODEL_SPEC v0.1, ROBERT_TECHNICAL_INTERACTION_FLOW_SPEC v0.2, ROBERT_TECHNICAL_SCREEN_STATE_SPEC v0.2, ROBERT_TECHNICAL_ERROR_AND_BLOCKING_SPEC v0.2, ROBERT_TECHNICAL_PERMISSIONS_AND_SCOPES_SPEC v0.2, ROBERT_TECHNICAL_AUDIT_TRAIL_SPEC v0.2, ROBERT_TECHNICAL_NOTIFICATION_AND_ALERTS_SPEC v0.2, ROBERT_TECHNICAL_SESSION_AND_CONTEXT_SPEC v0.2, ROBERT_TECHNICAL_DOCUMENT_LIFECYCLE_SPEC v0.2, ROBERT_TECHNICAL_VERSIONING_AND_CHANGE_POLICY_SPEC v0.2, ROBERT_TECHNICAL_DATA_CONSISTENCY_AND_CONFLICT_RESOLUTION_SPEC v0.3  
Fuente de verdad actual: ROBERT_CONTEXT_MASTER v0.5  

Tags: #robert/orbita-3 #capa/5 #tipo/tecnico #robert/mvp #robert/approval-gate

---

# OBJETIVO

ROBERT_TECHNICAL_APPROVAL_AND_AUTHORIZATION_GATE_SPEC define cómo Robert debe decidir, de forma conceptual y documental, si una acción del usuario puede continuar, requiere confirmación, requiere aprobación formal, debe pausarse o debe bloquearse.

Su objetivo es responder:

- Qué pasa cuando el usuario intenta una acción.
- Qué acciones pasan directo.
- Qué acciones requieren confirmación simple.
- Qué acciones requieren aprobación formal.
- Qué acciones deben bloquearse.
- Qué acciones deben pausarse por orden del usuario.
- Qué gate interviene según el tipo de acción.
- Qué componente muestra el estado del gate.
- Qué modelo conceptual se relaciona con cada gate.
- Qué evento, registro y notificación se relaciona con cada gate.
- Qué precedencia tienen los gates cuando una acción activa más de uno.
- Cómo se mantiene el control total del usuario.

Este documento no programa el gate.

Este documento no crea un sistema real de autorización.

Este documento no crea botones reales.

Este documento no crea pantallas reales.

Este documento no crea código.

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

# CORRECCIÓN PRINCIPAL DE v0.3

Esta versión corrige los errores detectados en ROBERT_TECHNICAL_APPROVAL_AND_AUTHORIZATION_GATE_SPEC v0.2.

Problemas detectados:

```text
1. El documento usaba MainCanvas como componente participante.
2. MainCanvas no pertenece a la lista canónica de componentes aprobados.
3. El componente correcto es AppShell.
4. La tabla de correspondencia con USER_ACTIONS_SPEC tenía numeración incorrecta.
5. Trece de las veinte acciones no coincidían con la numeración canónica.
```

Correcciones aplicadas:

```text
1. Se reemplaza MainCanvas por AppShell en todo el documento.
2. Se corrige la lista de componentes participantes.
3. Se corrige la tabla de mapeo entre Gates y componentes.
4. Se corrige la tabla de dónde se muestra cada elemento.
5. Se corrige la tabla de correspondencia con USER_ACTIONS_SPEC v0.2.
6. Se usa la lista canónica de 20 acciones confirmada en USER_ACTIONS_SPEC v0.2 auditado.
7. Se mantiene ApprovalGate como especificación conceptual, no como sistema real.
```

Clasificación de los conflictos corregidos:

```text
TIPO 11 — Conflicto de componente
TIPO 12 — Conflicto de flujo
TIPO 16 — Conflicto de fuente vigente
TIPO 17 — Conflicto de trazabilidad insuficiente
```

Estado resultante:

```text
ROBERT_TECHNICAL_APPROVAL_AND_AUTHORIZATION_GATE_SPEC v0.3
Estado: Propuesta corregida — pendiente de revisión
```

---

# REGLA CENTRAL

El usuario manda.

Robert no ejecuta acciones importantes sin permiso.

Intentar una acción no significa ejecutarla.

Toda acción importante debe pasar por control de alcance, riesgo y autorización cuando aplique.

Regla principal:

```text
ApprovalGate decide si una acción puede continuar, requiere confirmación, requiere aprobación, debe pausarse o debe bloquearse.
```

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
- ROBERT_TECHNICAL_USER_ACTIONS_SPEC v0.2 aprobado, integrado y auditado voluntariamente.
- ROBERT_TECHNICAL_ERROR_AND_BLOCKING_SPEC v0.2 aprobado.
- ROBERT_TECHNICAL_PERMISSIONS_AND_SCOPES_SPEC v0.2 aprobado.
- ROBERT_TECHNICAL_AUDIT_TRAIL_SPEC v0.2 aprobado.
- ROBERT_TECHNICAL_NOTIFICATION_AND_ALERTS_SPEC v0.2 aprobado.
- ROBERT_TECHNICAL_SESSION_AND_CONTEXT_SPEC v0.2 aprobado.
- ROBERT_TECHNICAL_DOCUMENT_LIFECYCLE_SPEC v0.2 aprobado.
- ROBERT_TECHNICAL_VERSIONING_AND_CHANGE_POLICY_SPEC v0.2 aprobado.
- ROBERT_TECHNICAL_DATA_CONSISTENCY_AND_CONFLICT_RESOLUTION_SPEC v0.3 aprobado.
- ROBERT_HOME v0.8 aprobado e integrado.
- ROBERT_TECHNICAL_APPROVAL_AND_AUTHORIZATION_GATE_SPEC v0.3 creado como propuesta corregida pendiente de revisión.
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

- Definir gates conceptuales de aprobación.
- Definir gates conceptuales de autorización.
- Definir gates conceptuales de bloqueo.
- Definir gates conceptuales de pausa.
- Relacionar gates con acciones del usuario.
- Relacionar gates con componentes aprobados.
- Relacionar gates con modelos conceptuales existentes.
- Relacionar gates con eventos, registros y notificaciones.
- Definir precedencia entre gates.
- Mantener control total del usuario.
- Mantener alineación con USER_ACTIONS_SPEC v0.2 auditado.
- Mantener alineación con COMPONENTS_SPEC v0.2.
- Mantener alineación con DATA_MODEL_SPEC v0.1.
- Mantener alineación con DATA_CONSISTENCY_AND_CONFLICT_RESOLUTION_SPEC v0.3.

---

# ALCANCE NO AUTORIZADO

Este documento no autoriza:

- Programar ApprovalGate.
- Crear código real.
- Crear botones reales.
- Crear pantallas reales.
- Crear prototipo funcional.
- Crear sistema real de autorización.
- Crear sistema real de permisos.
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

# PRINCIPIO GENERAL DE APPROVAL GATE

ApprovalGate debe responder seis preguntas:

1. ¿Qué intenta hacer el usuario?
2. ¿La acción es informativa, documental, sensible, futura, prohibida o de control?
3. ¿Qué nivel de riesgo tiene la acción original?
4. ¿Existe permiso suficiente para continuar?
5. ¿Requiere confirmación, aprobación formal, pausa o bloqueo?
6. ¿Qué debe mostrarse al usuario antes de avanzar?

Regla:

```text
ApprovalGate no ejecuta acciones.
ApprovalGate solo decide el estado conceptual de autorización de una acción.
```

---

# GATES DEFINIDOS

Este documento define ocho gates conceptuales:

```text
Gate 0 — Informativo
Gate 1 — Confirmación simple
Gate 2 — Autorización documental
Gate 3 — Aprobación formal
Gate 4 — Integración documental
Gate 5 — Acción sensible bloqueada en Fase 10
Gate 6 — Acción futura no disponible
Gate 7 — Revocación o control manual
```

---

# TABLA DE PRECEDENCIA ENTRE GATES

Cuando una acción pueda activar varios gates, Robert debe aplicar el gate de mayor precedencia.

| Precedencia | Gate | Nombre |
|---:|---|---|
| 1 | Gate 7 | Revocación o control manual |
| 2 | Gate 5 | Acción sensible bloqueada en Fase 10 |
| 3 | Gate 6 | Acción futura no disponible |
| 4 | Gate 4 | Integración documental |
| 5 | Gate 3 | Aprobación formal |
| 6 | Gate 2 | Autorización documental |
| 7 | Gate 1 | Confirmación simple |
| 8 | Gate 0 | Informativo |

Regla:

```text
Si el usuario dice DETENTE, PAUSA, NO_AVANCES, CANCELA, BLOQUEA o NO EJECUTES, Gate 7 tiene prioridad sobre cualquier otro gate.
```

---

# COMPONENTES PARTICIPANTES DE COMPONENTS_SPEC v0.2

Este documento usa los 10 componentes conceptuales aprobados:

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
MainCanvas no debe aparecer como componente oficial en este documento.
El componente correcto para contenedor raíz es AppShell.
```

---

# MODELOS PARTICIPANTES DE DATA_MODEL_SPEC v0.1

Este documento se apoya en los 11 modelos conceptuales aprobados:

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

Este documento no crea modelos nuevos.

No crea:

```text
ApprovalGateRecord
AuthorizationRecord
GateDecisionRecord
GateStateRecord
```

Si en el futuro se requiere alguno de esos modelos, deberá actualizarse DATA_MODEL_SPEC.

---

# ESTRUCTURA UNIFORME DE LOS 8 GATES

Cada Gate debe contener:

```text
Nombre:
Función:
Cuándo se activa:
Acciones relacionadas:
Componente principal:
Componentes relacionados:
Modelo principal:
Modelos relacionados:
Evento relacionado:
Registro de auditoría relacionado:
Notificación relacionada:
Acción esperada:
Resultado esperado:
Restricción:
Precedencia:
```

---

# GATE 0 — INFORMATIVO

## Función

Gate 0 permite acciones informativas que no modifican documentos, estados, decisiones, cambios, permisos, modos ni fases.

## Cuándo se activa

Se activa cuando el usuario solo quiere consultar información o visualizar estado.

## Acciones relacionadas

- ACCIÓN 2 — SELECCIONAR DOCUMENTO.
- ACCIÓN 3 — REVISAR ESTADO GENERAL.
- ACCIÓN 15 — VER DECISIONES PENDIENTES.
- ACCIÓN 17 — VER MAPA DOCUMENTAL.
- ACCIÓN 20 — PEDIR SIGUIENTE PASO.
- ACCIÓN 1 — ESCRIBIR COMANDO, si el comando es solo informativo.
- ACCIÓN 19 — SOLICITAR REVISIÓN CRÍTICA, si solo solicita diagnóstico sin corrección.

## Componente principal

CurrentStatePanel.

## Componentes relacionados

- AppShell.
- TopBar.
- LeftSidebar.
- CommandCenter.
- DecisionInbox.
- DocumentStatusMap.

## Modelo principal

SystemState.

## Modelos relacionados

- RobertDocument.
- PendingDecision.
- ComponentState.
- ObsidianGraphStatus.

## Evento relacionado

Ninguno obligatorio.

Puede relacionarse con:

```text
EVENTO 9 — Falta de información
```

si la consulta no tiene contexto suficiente.

## Registro de auditoría relacionado

```text
REGISTRO 3 — Revisión
```

si la acción forma parte de una revisión documental.

## Notificación relacionada

```text
TIPO 1 — Informativa
```

## Acción esperada

Mostrar información solicitada sin modificar nada.

## Resultado esperado

El usuario recibe información, estado o recomendación.

## Restricción

Gate 0 no autoriza avanzar, aprobar, corregir, integrar ni ejecutar.

## Precedencia

Precedencia 8.

---

# GATE 1 — CONFIRMACIÓN SIMPLE

## Función

Gate 1 pide confirmación simple cuando una acción es de bajo o medio impacto, pero puede cambiar el estado conversacional o documental menor.

## Cuándo se activa

Se activa cuando el usuario confirma que terminó un paso, actualizó algo manualmente o pide continuar con una acción menor.

## Acciones relacionadas

- ACCIÓN 1 — ESCRIBIR COMANDO, si la acción requiere aclaración o confirmación.
- ACCIÓN 2 — SELECCIONAR DOCUMENTO, si cambia documento activo.
- ACCIÓN 18 — MARCAR RESPALDO MANUAL EN GITHUB.
- ACCIÓN 20 — PEDIR SIGUIENTE PASO, si implica continuar a un bloque siguiente.

## Componente principal

CommandCenter.

## Componentes relacionados

- AppShell.
- TopBar.
- CurrentStatePanel.
- DocumentStatusMap.

## Modelo principal

CommandRequest.

## Modelos relacionados

- SystemState.
- GitHubBackupStatus.
- RobertDocument.
- ComponentState.

## Evento relacionado

```text
EVENTO 9 — Falta de información
```

si la confirmación es ambigua.

## Registro de auditoría relacionado

```text
REGISTRO 2 — Comando
REGISTRO 3 — Revisión
```

## Notificación relacionada

```text
TIPO 1 — Informativa
TIPO 6 — Confirmación requerida
```

## Acción esperada

Pedir o interpretar confirmación simple del usuario.

## Resultado esperado

Robert continúa únicamente si la confirmación es clara y no implica acción sensible.

## Restricción

Gate 1 no puede aprobar documentos, integrar cambios ni ejecutar acciones reales.

## Precedencia

Precedencia 7.

---

# GATE 2 — AUTORIZACIÓN DOCUMENTAL

## Función

Gate 2 controla acciones documentales que crean, corrigen, revisan o preparan contenido, pero todavía no aprueban ni integran formalmente.

## Cuándo se activa

Se activa cuando el usuario pide crear o corregir un documento técnico, activar sandbox manual o revisar críticamente un documento.

## Acciones relacionadas

- ACCIÓN 1 — ESCRIBIR COMANDO, si solicita creación o corrección documental.
- ACCIÓN 4 — CREAR DOCUMENTO TÉCNICO.
- ACCIÓN 5 — CORREGIR DOCUMENTO TÉCNICO.
- ACCIÓN 11 — CAMBIAR MODO, si cambia entre modos permitidos.
- ACCIÓN 12 — ACTIVAR SANDBOX MANUAL.
- ACCIÓN 19 — SOLICITAR REVISIÓN CRÍTICA.

## Componente principal

ApprovalGate.

## Componentes relacionados

- AppShell.
- CommandCenter.
- ModeSelector.
- RiskBadge.
- CurrentStatePanel.
- DocumentStatusMap.

## Modelo principal

CommandRequest.

## Modelos relacionados

- RobertDocument.
- RiskRecord.
- ModeState.
- PendingDecision.
- ComponentState.

## Evento relacionado

```text
EVENTO 9 — Falta de información
EVENTO 10 — Contradicción documental
EVENTO 12 — Fuera de alcance
EVENTO 13 — Sandbox requerido
EVENTO 14 — Sandbox excedido
```

## Registro de auditoría relacionado

```text
REGISTRO 3 — Revisión
REGISTRO 5 — Corrección
REGISTRO 11 — Riesgo
REGISTRO 16 — Contradicción documental
```

## Notificación relacionada

```text
TIPO 5 — Advertencia de riesgo
TIPO 6 — Confirmación requerida
TIPO 10 — Alerta de contradicción documental
```

## Acción esperada

Permitir creación, revisión o corrección documental solo como borrador o propuesta.

## Resultado esperado

El documento queda como borrador, propuesta o propuesta corregida pendiente de revisión.

## Restricción

Gate 2 no aprueba formalmente documentos ni ejecuta acciones reales.

## Precedencia

Precedencia 6.

---

# GATE 3 — APROBACIÓN FORMAL

## Función

Gate 3 controla acciones que requieren aprobación explícita del usuario.

## Cuándo se activa

Se activa cuando el usuario aprueba documentos, registra decisiones formales o resuelve decisiones pendientes.

## Acciones relacionadas

- ACCIÓN 1 — ESCRIBIR COMANDO, si incluye aprobación explícita.
- ACCIÓN 6 — APROBAR DOCUMENTO.
- ACCIÓN 7 — REGISTRAR DECISIÓN.
- ACCIÓN 16 — RESOLVER DECISIÓN PENDIENTE.

## Componente principal

DecisionInbox.

## Componentes relacionados

- AppShell.
- ApprovalGate.
- CommandCenter.
- RiskBadge.
- CurrentStatePanel.
- DocumentStatusMap.

## Modelo principal

DecisionRecord.

## Modelos relacionados

- PendingDecision.
- CommandRequest.
- RiskRecord.
- RobertDocument.
- ChangeRecord.

## Evento relacionado

```text
EVENTO 3 — Aprobación formal requerida
EVENTO 9 — Falta de información
```

## Registro de auditoría relacionado

```text
REGISTRO 6 — Decisión
REGISTRO 8 — Aprobación
```

## Notificación relacionada

```text
TIPO 6 — Confirmación requerida
```

## Acción esperada

Validar que exista aprobación explícita, documento correcto y versión correcta.

## Resultado esperado

Se prepara la decisión formal y, si aplica, el cambio posterior.

## Restricción

Gate 3 no debe inventar aprobaciones.

Aprobar documento no autoriza ejecución real.

## Precedencia

Precedencia 5.

---

# GATE 4 — INTEGRACIÓN DOCUMENTAL

## Función

Gate 4 controla acciones que integran cambios ya aprobados o actualizan documentos centrales como HOME, README o CONTROL_DE_CAMBIOS.

## Cuándo se activa

Se activa cuando una acción cambia el estado documental oficial del sistema.

## Acciones relacionadas

- ACCIÓN 8 — REGISTRAR CAMBIO.
- ACCIÓN 9 — ACTUALIZAR HOME.
- ACCIÓN 10 — ACTUALIZAR README.
- ACCIÓN 16 — RESOLVER DECISIÓN PENDIENTE, si genera integración.
- ACCIÓN 18 — MARCAR RESPALDO MANUAL EN GITHUB, si confirma actualización oficial.

## Componente principal

DocumentStatusMap.

## Componentes relacionados

- AppShell.
- ApprovalGate.
- CommandCenter.
- CurrentStatePanel.
- TopBar.
- DecisionInbox.

## Modelo principal

ChangeRecord.

## Modelos relacionados

- DecisionRecord.
- RobertDocument.
- GitHubBackupStatus.
- SystemState.
- ComponentState.

## Evento relacionado

```text
EVENTO 3 — Aprobación formal requerida
EVENTO 9 — Falta de información
EVENTO 10 — Contradicción documental
EVENTO 16 — Conexión no autorizada
```

## Registro de auditoría relacionado

```text
REGISTRO 7 — Cambio
REGISTRO 9 — Integración
REGISTRO 12 — Permiso
REGISTRO 16 — Contradicción documental
```

## Notificación relacionada

```text
TIPO 1 — Informativa
TIPO 6 — Confirmación requerida
TIPO 9 — Mensaje de bloqueo
TIPO 10 — Alerta de contradicción documental
```

## Acción esperada

Verificar que la integración tenga decisión, cambio o confirmación manual suficiente.

## Resultado esperado

HOME, README, CONTROL_DE_CAMBIOS o estado documental quedan alineados.

## Restricción

Gate 4 no puede integrar cambios sin trazabilidad suficiente.

Gate 4 no conecta GitHub automáticamente.

## Precedencia

Precedencia 4.

---

# GATE 5 — ACCIÓN SENSIBLE BLOQUEADA EN FASE 10

## Función

Gate 5 bloquea acciones sensibles que no están autorizadas en Fase 10.

## Cuándo se activa

Se activa cuando el usuario intenta programación, conexión externa, automatización, ejecución real o activación de agentes.

## Acciones relacionadas

- ACCIÓN 1 — ESCRIBIR COMANDO, si intenta ejecución real.
- ACCIÓN 11 — CAMBIAR MODO, si intenta activar autonomía real.
- ACCIÓN 14 — BLOQUEAR ACCIÓN, cuando se bloquea una acción sensible.

## Componente principal

ApprovalGate.

## Componentes relacionados

- AppShell.
- RiskBadge.
- CommandCenter.
- CurrentStatePanel.
- TopBar.
- DecisionInbox.

## Modelo principal

RiskRecord.

## Modelos relacionados

- CommandRequest.
- ModeState.
- PendingDecision.
- SystemState.
- ComponentState.

## Evento relacionado

```text
EVENTO 5 — Bloqueo automático
EVENTO 7 — Acción prohibida
EVENTO 11 — Riesgo crítico
EVENTO 12 — Fuera de alcance
EVENTO 15 — Ejecución no autorizada
EVENTO 16 — Conexión no autorizada
EVENTO 17 — Automatización no autorizada
EVENTO 18 — Agente no autorizado
EVENTO 20 — Fase incorrecta
```

## Registro de auditoría relacionado

```text
REGISTRO 10 — Bloqueo
REGISTRO 11 — Riesgo
REGISTRO 12 — Permiso
```

## Notificación relacionada

```text
TIPO 5 — Advertencia de riesgo
TIPO 9 — Mensaje de bloqueo
TIPO 11 — Fase incorrecta
TIPO 12 — Capacidad futura no disponible
```

## Acción esperada

Bloquear la acción y explicar por qué no está autorizada.

## Resultado esperado

La acción no continúa.

Robert mantiene Fase 10 y modo documental.

## Restricción

Robert no debe buscar rutas alternas para ejecutar lo bloqueado.

## Precedencia

Precedencia 2.

---

# GATE 6 — ACCIÓN FUTURA NO DISPONIBLE

## Función

Gate 6 identifica capacidades futuras que pueden existir como visión, pero no están disponibles en Fase 10.

## Cuándo se activa

Se activa cuando el usuario pide una capacidad futura como si ya estuviera activa.

## Acciones relacionadas

- ACCIÓN 11 — CAMBIAR MODO, si intenta activar modo futuro.
- ACCIÓN 1 — ESCRIBIR COMANDO, si pide herramienta futura real.
- ACCIÓN 20 — PEDIR SIGUIENTE PASO, si el siguiente paso solicitado corresponde a Fase 11 o posterior.

## Componente principal

CurrentStatePanel.

## Componentes relacionados

- AppShell.
- ApprovalGate.
- RiskBadge.
- ModeSelector.
- TopBar.
- CommandCenter.

## Modelo principal

SystemState.

## Modelos relacionados

- ModeState.
- RiskRecord.
- CommandRequest.
- ComponentState.

## Evento relacionado

```text
EVENTO 8 — Acción futura no disponible
EVENTO 20 — Fase incorrecta
```

Si la acción futura intenta activarse como acción real, también puede relacionarse con:

```text
EVENTO 15 — Ejecución no autorizada
EVENTO 16 — Conexión no autorizada
EVENTO 17 — Automatización no autorizada
EVENTO 18 — Agente no autorizado
```

## Registro de auditoría relacionado

```text
REGISTRO 17 — Capacidad futura no disponible
REGISTRO 11 — Riesgo
```

## Notificación relacionada

```text
TIPO 12 — Capacidad futura no disponible
TIPO 11 — Fase incorrecta
```

## Acción esperada

Informar que la capacidad es futura y no está activa.

## Resultado esperado

La acción queda detenida sin ejecutar.

## Restricción

Gate 6 no debe presentar capacidades futuras como activas.

## Precedencia

Precedencia 3.

---

# GATE 7 — REVOCACIÓN O CONTROL MANUAL

## Función

Gate 7 da prioridad absoluta a las órdenes de control del usuario.

## Cuándo se activa

Se activa cuando el usuario ordena pausar, detener, bloquear, cancelar, no avanzar o no ejecutar.

## Acciones relacionadas

- ACCIÓN 1 — ESCRIBIR COMANDO, si contiene orden de control.
- ACCIÓN 12 — ACTIVAR SANDBOX MANUAL, si el usuario pausa o detiene la prueba.
- ACCIÓN 13 — PAUSAR AVANCE.
- ACCIÓN 14 — BLOQUEAR ACCIÓN.

## Componente principal

ApprovalGate.

## Componentes relacionados

- AppShell.
- CommandCenter.
- CurrentStatePanel.
- DecisionInbox.
- TopBar.
- RiskBadge.

## Modelo principal

ModeState.

## Modelos relacionados

- CommandRequest.
- RiskRecord.
- PendingDecision.
- SystemState.
- ComponentState.

## Evento relacionado

```text
EVENTO 4 — Pausa obligatoria
EVENTO 6 — Bloqueo manual solicitado
```

Si el control bloquea una acción sensible, también puede relacionarse con:

```text
EVENTO 15 — Ejecución no autorizada
EVENTO 16 — Conexión no autorizada
EVENTO 17 — Automatización no autorizada
EVENTO 18 — Agente no autorizado
```

## Registro de auditoría relacionado

```text
REGISTRO 3 — Revisión
REGISTRO 10 — Bloqueo
REGISTRO 11 — Riesgo
```

## Notificación relacionada

```text
TIPO 1 — Informativa
TIPO 9 — Mensaje de bloqueo
```

## Acción esperada

Detener avance inmediatamente.

## Resultado esperado

Robert no continúa hasta nueva autorización explícita.

## Restricción

Gate 7 tiene prioridad máxima.

Robert no debe continuar con otro gate si Gate 7 fue activado.

## Precedencia

Precedencia 1.

---

# TABLA DE MAPEO ENTRE GATES Y COMPONENTES

| Gate | Nombre | Componente principal | Componentes relacionados |
|---|---|---|---|
| Gate 0 | Informativo | CurrentStatePanel | AppShell, TopBar, LeftSidebar, CommandCenter, DecisionInbox, DocumentStatusMap |
| Gate 1 | Confirmación simple | CommandCenter | AppShell, TopBar, CurrentStatePanel, DocumentStatusMap |
| Gate 2 | Autorización documental | ApprovalGate | AppShell, CommandCenter, ModeSelector, RiskBadge, CurrentStatePanel, DocumentStatusMap |
| Gate 3 | Aprobación formal | DecisionInbox | AppShell, ApprovalGate, CommandCenter, RiskBadge, CurrentStatePanel, DocumentStatusMap |
| Gate 4 | Integración documental | DocumentStatusMap | AppShell, ApprovalGate, CommandCenter, CurrentStatePanel, TopBar, DecisionInbox |
| Gate 5 | Acción sensible bloqueada en Fase 10 | ApprovalGate | AppShell, RiskBadge, CommandCenter, CurrentStatePanel, TopBar, DecisionInbox |
| Gate 6 | Acción futura no disponible | CurrentStatePanel | AppShell, ApprovalGate, RiskBadge, ModeSelector, TopBar, CommandCenter |
| Gate 7 | Revocación o control manual | ApprovalGate | AppShell, CommandCenter, CurrentStatePanel, DecisionInbox, TopBar, RiskBadge |

---

# TABLA DE DÓNDE SE MUESTRA CADA ELEMENTO

| Elemento | Dónde se muestra | Componente responsable |
|---|---|---|
| Estado general del sistema | Vista principal / panel de estado | CurrentStatePanel |
| Fase actual | Barra superior / panel de estado | TopBar / CurrentStatePanel |
| Documento activo | Sidebar / mapa documental / panel de estado | LeftSidebar / DocumentStatusMap / CurrentStatePanel |
| Acción intentada | Centro de comandos | CommandCenter |
| Riesgo detectado | Indicador de riesgo | RiskBadge |
| Confirmación requerida | Centro de comandos / gate | CommandCenter / ApprovalGate |
| Aprobación formal requerida | Bandeja de decisiones / gate | DecisionInbox / ApprovalGate |
| Bloqueo activo | Gate / indicador de riesgo / panel de estado | ApprovalGate / RiskBadge / CurrentStatePanel |
| Capacidad futura no disponible | Panel de estado / barra superior | CurrentStatePanel / TopBar |
| Modo activo | Selector de modo / barra superior | ModeSelector / TopBar |
| Respaldo manual de GitHub | Barra superior / panel de estado | TopBar / CurrentStatePanel |
| Relación documental | Mapa documental | DocumentStatusMap |
| Pausa o revocación manual | Gate / centro de comandos | ApprovalGate / CommandCenter |
| Contenedor raíz de la vista conceptual | Estructura general del MVP | AppShell |

Regla:

```text
AppShell es el contenedor raíz conceptual.
MainCanvas no debe usarse como componente oficial.
```

---

# TABLA DE CORRESPONDENCIA CON USER_ACTIONS_SPEC v0.2

| Acción | Nombre canónico | Gate probable |
|---:|---|---|
| 1 | Escribir comando | Gate 0 / Gate 1 / Gate 2 / Gate 3 / Gate 5 / Gate 7 |
| 2 | Seleccionar documento | Gate 0 / Gate 1 |
| 3 | Revisar estado general | Gate 0 |
| 4 | Crear documento técnico | Gate 2 |
| 5 | Corregir documento técnico | Gate 2 |
| 6 | Aprobar documento | Gate 3 |
| 7 | Registrar decisión | Gate 3 |
| 8 | Registrar cambio | Gate 4 |
| 9 | Actualizar HOME | Gate 4 |
| 10 | Actualizar README | Gate 4 |
| 11 | Cambiar modo | Gate 2 / Gate 5 / Gate 6 |
| 12 | Activar sandbox manual | Gate 2 / Gate 7 |
| 13 | Pausar avance | Gate 7 |
| 14 | Bloquear acción | Gate 5 / Gate 7 |
| 15 | Ver decisiones pendientes | Gate 0 |
| 16 | Resolver decisión pendiente | Gate 3 / Gate 4 |
| 17 | Ver mapa documental | Gate 0 |
| 18 | Marcar respaldo manual en GitHub | Gate 1 / Gate 4 |
| 19 | Solicitar revisión crítica | Gate 0 / Gate 2 |
| 20 | Pedir siguiente paso | Gate 0 / Gate 1 |

Regla:

```text
Esta tabla usa la numeración canónica de USER_ACTIONS_SPEC v0.2 auditado.
No debe alterarse sin revisar USER_ACTIONS_SPEC.
```

---

# RELACIÓN CON COMPONENTS_SPEC v0.2

Este documento usa exclusivamente los componentes canónicos:

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

Corrección aplicada:

```text
MainCanvas fue eliminado como componente participante.
AppShell queda como componente correcto.
```

---

# RELACIÓN CON DATA_MODEL_SPEC v0.1

Este documento no crea modelos nuevos.

Relación principal por Gate:

| Gate | Modelo principal |
|---|---|
| Gate 0 | SystemState |
| Gate 1 | CommandRequest |
| Gate 2 | CommandRequest |
| Gate 3 | DecisionRecord |
| Gate 4 | ChangeRecord |
| Gate 5 | RiskRecord |
| Gate 6 | SystemState |
| Gate 7 | ModeState |

Modelos relacionados:

```text
RobertDocument
PendingDecision
RiskRecord
CommandRequest
DecisionRecord
ChangeRecord
ModeState
SystemState
ComponentState
GitHubBackupStatus
ObsidianGraphStatus
```

---

# RELACIÓN CON ERROR_AND_BLOCKING_SPEC v0.2

ERROR_AND_BLOCKING_SPEC define los eventos y bloqueos.

APPROVAL_AND_AUTHORIZATION_GATE_SPEC define el gate que decide si la acción puede avanzar.

Relación principal:

```text
Gate 5 usa eventos de bloqueo.
Gate 6 usa eventos de capacidad futura no disponible.
Gate 7 usa eventos de pausa o bloqueo manual.
```

---

# RELACIÓN CON PERMISSIONS_AND_SCOPES_SPEC v0.2

PERMISSIONS_AND_SCOPES_SPEC define límites de permiso y alcance.

APPROVAL_AND_AUTHORIZATION_GATE_SPEC usa esos límites para decidir si una acción puede continuar.

Regla:

```text
Si una acción excede permiso o alcance, ApprovalGate debe bloquear, pausar o pedir aprobación según corresponda.
```

---

# RELACIÓN CON AUDIT_TRAIL_SPEC v0.2

AUDIT_TRAIL_SPEC define qué debe quedar registrado.

APPROVAL_AND_AUTHORIZATION_GATE_SPEC define cuándo una acción genera registro.

Ejemplos:

```text
Aprobación formal → REGISTRO 8 — Aprobación
Cambio documental → REGISTRO 7 — Cambio
Bloqueo → REGISTRO 10 — Bloqueo
Riesgo → REGISTRO 11 — Riesgo
Contradicción documental → REGISTRO 16 — Contradicción documental
```

---

# RELACIÓN CON NOTIFICATION_AND_ALERTS_SPEC v0.2

NOTIFICATION_AND_ALERTS_SPEC define qué aviso mostrar.

APPROVAL_AND_AUTHORIZATION_GATE_SPEC define cuándo mostrarlo.

Ejemplos:

```text
Gate 0 → Notificación informativa
Gate 1 → Confirmación requerida
Gate 3 → Confirmación requerida / aprobación formal
Gate 5 → Mensaje de bloqueo
Gate 6 → Capacidad futura no disponible
Gate 7 → Mensaje de pausa o bloqueo manual
```

---

# RELACIÓN CON DATA_CONSISTENCY_AND_CONFLICT_RESOLUTION_SPEC v0.3

Si una acción genera conflicto, ApprovalGate debe respetar la precedencia definida por DATA_CONSISTENCY_AND_CONFLICT_RESOLUTION_SPEC v0.3.

Ejemplos:

```text
Uso de MainCanvas como componente oficial:
TIPO 11 — Conflicto de componente

Numeración incorrecta de acciones:
TIPO 12 — Conflicto de flujo

Citar fuente no vigente:
TIPO 16 — Conflicto de fuente vigente

Falta de trazabilidad:
TIPO 17 — Conflicto de trazabilidad insuficiente

Intento de ejecución real:
TIPO 15 — Conflicto de ejecución no autorizada
```

---

# REGLAS DE BLOQUEO

ApprovalGate debe bloquear cuando:

- La acción intenta programar.
- La acción intenta crear código real.
- La acción intenta crear pantallas reales.
- La acción intenta crear base de datos real.
- La acción intenta conectar herramientas externas.
- La acción intenta conectar Gmail.
- La acción intenta conectar Google Calendar.
- La acción intenta conectar GitHub automáticamente.
- La acción intenta automatizar.
- La acción intenta activar agentes autónomos.
- La acción intenta ejecutar acciones reales.
- La acción intenta avanzar a Fase 11 sin decisión formal.
- La acción ignora DETENTE, PAUSA o NO_AVANCES.
- La acción intenta saltarse ApprovalGate.

---

# REGLAS DE CONFIRMACIÓN

ApprovalGate debe pedir confirmación simple cuando:

- El usuario da una instrucción ambigua.
- El usuario confirma “ya” y el contexto no es suficiente.
- El usuario pide continuar a un siguiente paso.
- El usuario confirma respaldo manual.
- El usuario cambia estado documental menor.
- El usuario actualiza HOME o README sin afectar aprobación formal.
- El usuario pide revisar o corregir sin aprobar.

---

# REGLAS DE APROBACIÓN FORMAL

ApprovalGate debe pedir aprobación formal cuando:

- Se aprueba documento técnico.
- Se aprueba documento maestro.
- Se cambia fase.
- Se cambia fuente de verdad.
- Se cambian reglas de seguridad.
- Se integra documento técnico.
- Se registra decisión formal.
- Se modifica arquitectura conceptual.
- Se acerca el sistema a programación.
- Se acerca el sistema a conexiones externas.

---

# REGLAS DE PAUSA Y CONTROL MANUAL

Gate 7 debe activarse inmediatamente cuando el usuario use comandos como:

```text
DETENTE
PAUSA
NO_AVANCES
NO SIGAS
CANCELA
BLOQUEA
NO EJECUTES
SOLO BORRADOR
REVOCA_AUTONOMIA
VOLVER_A_MANUAL
```

Regla:

```text
Gate 7 tiene prioridad sobre todos los demás gates.
```

---

# CRITERIOS DE ACEPTACIÓN

Este documento podrá considerarse listo para aprobación si:

- Define los 8 gates conceptuales.
- Mantiene estructura uniforme para los 8 gates.
- Usa AppShell como componente canónico.
- Elimina MainCanvas como componente oficial.
- Usa los 10 componentes aprobados de COMPONENTS_SPEC v0.2.
- Usa los 11 modelos aprobados de DATA_MODEL_SPEC v0.1.
- Corrige la tabla de correspondencia con USER_ACTIONS_SPEC v0.2.
- Usa las 20 acciones canónicas de USER_ACTIONS_SPEC v0.2 auditado.
- Mantiene la precedencia correcta entre gates.
- Relaciona gates con eventos.
- Relaciona gates con registros de auditoría.
- Relaciona gates con notificaciones.
- Mantiene alineación con ERROR_AND_BLOCKING_SPEC v0.2.
- Mantiene alineación con PERMISSIONS_AND_SCOPES_SPEC v0.2.
- Mantiene alineación con AUDIT_TRAIL_SPEC v0.2.
- Mantiene alineación con NOTIFICATION_AND_ALERTS_SPEC v0.2.
- Mantiene alineación con DATA_CONSISTENCY_AND_CONFLICT_RESOLUTION_SPEC v0.3.
- No autoriza programación.
- No autoriza código real.
- No autoriza pantallas reales.
- No autoriza base de datos real.
- No autoriza conexiones externas.
- No autoriza automatizaciones.
- No autoriza agentes autónomos.
- No autoriza ejecución real.
- No autoriza avanzar a Fase 11.
- Mantiene control total del usuario.

---

# RIESGO DEL DOCUMENTO

Tipo de cambio:

**Corrección técnica documental / ApprovalGate conceptual**

Nivel de riesgo inicial:

**Nivel 3 — Alto**

Motivo:

Este documento define cómo Robert decidirá conceptualmente si una acción puede continuar, requiere aprobación o debe bloquearse. Aunque es documental, influye en la futura lógica de autorización del MVP técnico.

Nivel de riesgo final esperado:

**Nivel 2 — Medio**

Motivo de reducción:

El documento es conceptual y documental. No crea gate real, no programa, no conecta herramientas externas y no ejecuta acciones.

Nivel de autonomía:

**Nivel 0 — Sin autonomía ejecutiva**

---

# DECISIÓN PENDIENTE

Este documento queda como:

```text
Propuesta corregida — pendiente de revisión
```

Para aprobarlo formalmente, el usuario deberá escribir:

```text
APRUEBO ROBERT_TECHNICAL_APPROVAL_AND_AUTHORIZATION_GATE_SPEC v0.3
```

---

# EFECTO DE UNA APROBACIÓN FUTURA

Si se aprueba este documento, se deberá:

1. Registrar decisión formal en ROBERT_DECISIONS_LOG.
2. Registrar cambio en ROBERT_CONTROL_DE_CAMBIOS.
3. Actualizar ROBERT_HOME.
4. Actualizar README si aplica.
5. Mantenerlo como especificación conceptual del ApprovalGate.
6. No pasar automáticamente a programación.
7. No crear gate real.
8. No avanzar automáticamente a Fase 11.

---

# PRÓXIMO PASO RECOMENDADO

Después de revisar este documento, el siguiente paso será decidir si:

```text
ROBERT_TECHNICAL_APPROVAL_AND_AUTHORIZATION_GATE_SPEC v0.3
```

queda aprobado o requiere otra corrección.

No debe aprobarse automáticamente.

---

# CIERRE

ROBERT_TECHNICAL_APPROVAL_AND_AUTHORIZATION_GATE_SPEC v0.3 corrige los errores detectados en v0.2.

Correcciones principales:

```text
1. MainCanvas fue reemplazado por AppShell.
2. La tabla de componentes participantes fue corregida.
3. La tabla de mapeo entre Gates y componentes fue corregida.
4. La tabla de dónde se muestra cada elemento fue corregida.
5. La tabla de correspondencia con USER_ACTIONS_SPEC v0.2 fue corregida con las 20 acciones canónicas.
```

Este documento mantiene a Robert en modo documental, manual y supervisado.

El usuario mantiene control total.

Robert no ejecuta acciones importantes sin permiso.
