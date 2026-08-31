# ROBERT_TECHNICAL_VERSIONING_AND_CHANGE_POLICY_SPEC

Versión: 0.1  
Estado: APROBADA
Fecha: 06/07/2026  
Ubicación: 10_MVP  
Fase relacionada: Fase 10 — MVP técnico básico en preparación  
Documento base principal: ROBERT_TECHNICAL_DOCUMENT_LIFECYCLE_SPEC v0.2  
Documentos relacionados: ROBERT_COMMANDS v0.4, ROBERT_TECHNICAL_SESSION_AND_CONTEXT_SPEC v0.2, ROBERT_TECHNICAL_NOTIFICATION_AND_ALERTS_SPEC v0.2, ROBERT_TECHNICAL_AUDIT_TRAIL_SPEC v0.2, ROBERT_TECHNICAL_PERMISSIONS_AND_SCOPES_SPEC v0.2, ROBERT_TECHNICAL_ERROR_AND_BLOCKING_SPEC v0.2, ROBERT_TECHNICAL_USER_ACTIONS_SPEC v0.2, ROBERT_TECHNICAL_DATA_MODEL_SPEC v0.1, ROBERT_TECHNICAL_COMPONENTS_SPEC v0.2, ROBERT_TECHNICAL_SCREEN_STATE_SPEC v0.2, ROBERT_TECHNICAL_INTERACTION_FLOW_SPEC v0.2  
Fuente de verdad actual: ROBERT_CONTEXT_MASTER v0.5  

Tags: #robert/orbita-3 #capa/5 #tipo/tecnico #robert/mvp #robert/versioning

---

# OBJETIVO

ROBERT_TECHNICAL_VERSIONING_AND_CHANGE_POLICY_SPEC define las reglas conceptuales de versiones y cambios documentales de Robert dentro del MVP técnico básico.

Su objetivo es responder:

- Cómo se numeran las versiones.
- Cuándo usar v0.1.
- Cuándo pasar a v0.2.
- Cuándo pasar a v0.3.
- Cuándo pasar a v1.0.
- Qué es una corrección menor.
- Qué es una corrección mayor.
- Qué es una actualización.
- Qué es una integración.
- Qué es un reemplazo.
- Qué es una versión vigente.
- Qué es una versión obsoleta.
- Qué es una versión depreciada.
- Qué documentos pueden coexistir.
- Qué documentos no deben coexistir como fuente principal.
- Cómo evitar contradicciones entre documentos.
- Cómo decidir si un cambio requiere nueva versión.
- Cómo decidir si un cambio requiere nueva aprobación.
- Cómo registrar cambios de versión.
- Cómo actualizar HOME y README después de cambios importantes.

Este documento no crea sistema real de control de versiones.

Este documento no crea base de datos real.

Este documento no crea commits automáticos.

Este documento no conecta GitHub automáticamente.

Este documento no conecta Obsidian automáticamente.

Este documento no programa la app.

Este documento no ejecuta acciones reales.

---

# ESTADO DEL DOCUMENTO

Este documento queda como:

**Borrador técnico documental nuevo — pendiente de revisión**

No está aprobado todavía.

No reemplaza a ningún documento maestro.

No autoriza programación.

No autoriza código real.

No autoriza sistema real de control de versiones.

No autoriza base de datos real.

No autoriza versionado automático.

No autoriza commits automáticos.

No autoriza sincronización automática con GitHub.

No autoriza sincronización automática con Obsidian.

No autoriza agentes autónomos.

No autoriza avanzar a Fase 11.

---

# REGLA CENTRAL

Robert debe versionar documentos de forma clara, trazable y manual.

Regla principal:

**Ninguna versión cambia su estado, número o vigencia sin registro documental y confirmación del usuario.**

---

# REGLA DE VERSIONAMIENTO

Toda versión documental debe poder responder:

```text
Qué cambió
Por qué cambió
Quién lo aprobó
Dónde se registró
Qué documento reemplaza
Qué documento queda vigente
Qué documento queda histórico
Qué restricciones siguen activas
```

Regla:

**Una versión nueva no elimina automáticamente una versión anterior.**

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
- ROBERT_TECHNICAL_DATA_MODEL_SPEC v0.1 aprobado.
- ROBERT_TECHNICAL_INTERACTION_FLOW_SPEC v0.2 aprobado.
- ROBERT_TECHNICAL_SCREEN_STATE_SPEC v0.2 aprobado.
- ROBERT_TECHNICAL_USER_ACTIONS_SPEC v0.2 aprobado.
- ROBERT_TECHNICAL_ERROR_AND_BLOCKING_SPEC v0.2 aprobado.
- ROBERT_TECHNICAL_PERMISSIONS_AND_SCOPES_SPEC v0.2 aprobado.
- ROBERT_TECHNICAL_AUDIT_TRAIL_SPEC v0.2 aprobado.
- ROBERT_TECHNICAL_NOTIFICATION_AND_ALERTS_SPEC v0.2 aprobado.
- ROBERT_TECHNICAL_SESSION_AND_CONTEXT_SPEC v0.2 aprobado.
- ROBERT_TECHNICAL_DOCUMENT_LIFECYCLE_SPEC v0.2 aprobado.
- ROBERT_TECHNICAL_VERSIONING_AND_CHANGE_POLICY_SPEC v0.1 creado como borrador.
- Sin programación autorizada.
- Sin código real.
- Sin sistema real de control de versiones.
- Sin base de datos real.
- Sin conexiones externas.
- Sin automatizaciones reales.
- Sin agentes autónomos activos.

---

# ALCANCE AUTORIZADO

Este documento autoriza únicamente:

- Definir reglas conceptuales de versionamiento.
- Definir niveles de versión.
- Definir tipos de cambio documental.
- Definir cuándo cambiar de v0.1 a v0.2.
- Definir cuándo cambiar de v0.2 a v0.3.
- Definir cuándo cambiar a v1.0.
- Definir cuándo una versión reemplaza a otra.
- Definir cuándo una versión queda depreciada.
- Definir cuándo una versión queda archivada.
- Definir compatibilidad entre versiones documentales.
- Definir reglas para registrar cambios.
- Definir reglas para actualizar HOME y README.
- Mantener a Robert en modo documental, manual y supervisado.

---

# ALCANCE NO AUTORIZADO

Este documento no autoriza:

- Programar la app.
- Crear código real.
- Crear sistema real de control de versiones.
- Crear base de datos real.
- Crear tabla real de versiones.
- Crear modelo VersionRecord.
- Crear modelo VersionPolicyRecord.
- Crear modelo CompatibilityRecord.
- Crear modelo BreakingChangeRecord.
- Crear componente VersionTimeline.
- Crear componente CompatibilityPanel.
- Crear control automático de versiones.
- Crear commits automáticos.
- Conectar GitHub automáticamente.
- Conectar Obsidian automáticamente.
- Sincronizar documentos automáticamente.
- Automatizar aprobaciones.
- Automatizar cambios de versión.
- Automatizar HOME.
- Automatizar README.
- Ejecutar acciones reales.
- Activar agentes autónomos.
- Avanzar automáticamente a Fase 11.

---

# VERSIONING NO CREA MODELO NUEVO OFICIAL

En esta versión, la política de versiones no crea modelos nuevos.

No se crean:

```text
VersionRecord
VersionPolicyRecord
CompatibilityRecord
BreakingChangeRecord
VersionTransitionRecord
```

Este documento usa modelos ya aprobados en DATA_MODEL_SPEC v0.1.

Si en el futuro se decide crear modelos oficiales de versionamiento, primero deberá corregirse y aprobarse:

```text
ROBERT_TECHNICAL_DATA_MODEL_SPEC
```

---

# VERSIONING NO CREA COMPONENTE NUEVO OFICIAL

En esta versión, la política de versiones no crea componentes nuevos.

No se crean:

```text
VersionTimeline
CompatibilityPanel
VersionStatusBadge
ChangePolicyMap
```

Este documento usa componentes ya aprobados en COMPONENTS_SPEC v0.2.

Si en el futuro se decide crear componentes oficiales de versionamiento, primero deberá corregirse y aprobarse:

```text
ROBERT_TECHNICAL_COMPONENTS_SPEC
```

---

# MODELOS RELACIONADOS

Este documento se apoya en los 11 modelos de DATA_MODEL_SPEC v0.1.

Modelos principales:

- RobertDocument.
- ChangeRecord.
- DecisionRecord.
- PendingDecision.
- SystemState.
- CommandRequest.
- RiskRecord.
- ModeState.
- ComponentState.
- GitHubBackupStatus.
- ObsidianGraphStatus.

---

# MAPEO DE VERSIONAMIENTO A MODELOS EXISTENTES

| Elemento de versionamiento | Modelo relacionado | Uso |
|---|---|---|
| Documento versionado | RobertDocument | Identifica nombre, versión y estado |
| Cambio de versión | ChangeRecord | Registra corrección, actualización o reemplazo |
| Aprobación de versión | DecisionRecord | Registra aprobación formal |
| Versión pendiente | PendingDecision | Indica aprobación o revisión pendiente |
| Estado general | SystemState | Refleja versión vigente y bloque activo |
| Comando del usuario | CommandRequest | Inicia creación, corrección o aprobación |
| Riesgo de versión | RiskRecord | Evalúa cambio mayor, contradicción o ruptura |
| Modo operativo | ModeState | Manual, supervisado, sandbox o pausado |
| Estado visual | ComponentState | Muestra versión en interfaz conceptual |
| Respaldo manual | GitHubBackupStatus | Confirma commit manual |
| Grafo documental | ObsidianGraphStatus | Refleja versiones y relaciones en Obsidian |

---

# COMPONENTES PARTICIPANTES

Este documento usa componentes ya aprobados:

1. AppShell.
2. TopBar.
3. LeftSidebar.
4. CommandCenter.
5. ModeSelector.
6. RiskBadge.
7. ApprovalGate.
8. DecisionInbox.
9. DocumentStatusMap.
10. CurrentStatePanel.

---

# ROL DE CADA COMPONENTE

## AppShell

Contiene la vista general del sistema.

No gestiona versiones reales.

No guarda historial real automático.

---

## TopBar

Muestra estado general de versión.

Puede mostrar:

- Fase activa.
- Modo activo.
- Documento activo.
- Versión activa.
- Estado de versión.
- Bloque abierto.
- Bloque cerrado.

---

## LeftSidebar

Muestra navegación documental.

Puede mostrar:

- Documento vigente.
- Documento anterior.
- Documento reemplazado.
- Documento depreciado.
- Documento archivado.
- Documentos relacionados.

---

## CommandCenter

Recibe instrucciones del usuario.

Puede iniciar:

- Crear versión.
- Corregir versión.
- Revisar versión.
- Aprobar versión.
- Reemplazar versión.
- Depreciar versión.
- Pausar.
- Bloquear.

---

## ModeSelector

Muestra modo operativo.

Puede mostrar:

- Manual.
- Supervisado.
- Sandbox.
- Pausado.
- Bloqueado.

---

## RiskBadge

Muestra riesgo de cambio de versión.

Puede mostrar:

- Riesgo bajo.
- Riesgo medio.
- Riesgo alto.
- Riesgo crítico.
- Riesgo por cambio mayor.
- Riesgo por contradicción documental.
- Riesgo por incompatibilidad.
- Riesgo por fase incorrecta.

---

## ApprovalGate

Controla cambios que requieren aprobación.

Puede bloquear:

- Cambio mayor no aprobado.
- Reemplazo no aprobado.
- v1.0 no autorizado.
- Modificación silenciosa de documento aprobado.
- Cambio incompatible.
- Eliminación de versión anterior.
- Avance de fase.
- Ejecución no autorizada.

---

## DecisionInbox

Muestra decisiones pendientes o registradas.

Puede mostrar:

- Versión pendiente de aprobación.
- Cambio mayor pendiente.
- Reemplazo pendiente.
- Depreciación pendiente.
- Decisión registrada.
- Revisión pendiente.

---

## DocumentStatusMap

Muestra el estado de versiones documentales.

Puede mostrar:

- v0.1 borrador.
- v0.2 propuesta corregida.
- v0.3 nueva corrección.
- v1.0 estable conceptual.
- Versión vigente.
- Versión reemplazada.
- Versión depreciada.
- Versión archivada.

---

## CurrentStatePanel

Muestra el estado completo de la versión activa.

Debe poder mostrar:

- Documento activo.
- Versión activa.
- Estado actual.
- Último cambio.
- Última decisión.
- Versión anterior.
- Versión vigente.
- Riesgo.
- Restricción.
- Próximo paso.

---

# NIVELES DE VERSIÓN

Los niveles conceptuales de versión en v0.1 son:

1. v0.0 — Idea o placeholder.
2. v0.1 — Borrador inicial.
3. v0.2 — Propuesta corregida.
4. v0.3+ — Corrección adicional o iteración documental.
5. v0.x aprobado — Documento aprobado antes de estabilidad completa.
6. v1.0 — Versión estable conceptual.
7. v1.x — Actualización menor estable.
8. v2.0 — Cambio mayor estructural futuro.

---

# ESTRUCTURA UNIFORME DE LOS 8 NIVELES DE VERSIÓN

Cada nivel de versión debe poder mostrar:

```text
Qué significa:
Cuándo se usa:
Riesgo típico:
Modelo principal:
Componente principal:
Registro de auditoría relacionado:
Notificación relacionada:
Transición siguiente permitida:
Restricción:
```

---

# NIVEL 1 — v0.0 IDEA O PLACEHOLDER

## Qué significa

Existe una idea de documento o una referencia futura, pero todavía no hay documento formal.

## Cuándo se usa

Cuando se identifica una necesidad documental, pero todavía no se crea archivo.

## Riesgo típico

Nivel 0 — Informativo.

Puede subir a Nivel 1 si la idea afecta prioridades.

## Modelo principal

PendingDecision.

## Componente principal

DecisionInbox.

## Registro de auditoría relacionado

REGISTRO 1 — Informativo.

REGISTRO 2 — Comando, si nace de solicitud del usuario.

## Notificación relacionada

TIPO 17 — Aviso de siguiente paso.

## Transición siguiente permitida

v0.0 → v0.1 cuando el usuario autoriza crear el documento.

## Restricción

v0.0 no es documento oficial.

---

# NIVEL 2 — v0.1 BORRADOR INICIAL

## Qué significa

Primera versión formal de un documento.

## Cuándo se usa

Cuando se crea por primera vez un documento técnico, maestro o de soporte.

## Riesgo típico

Nivel 1 a Nivel 3, según el documento.

## Modelo principal

RobertDocument.

## Componente principal

DocumentStatusMap.

## Registro de auditoría relacionado

REGISTRO 4 — Borrador.

REGISTRO 2 — Comando, si el usuario pidió crearlo.

## Notificación relacionada

TIPO 2 — Notificación de estado.

## Transición siguiente permitida

v0.1 → v0.2 si requiere corrección.

v0.1 → Aprobado si el documento es correcto y el usuario lo aprueba.

## Restricción

v0.1 no significa aprobado.

---

# NIVEL 3 — v0.2 PROPUESTA CORREGIDA

## Qué significa

Versión corregida después de detectar huecos, riesgos, errores o mejoras necesarias.

## Cuándo se usa

Cuando v0.1 requiere ajustes antes de aprobación.

## Riesgo típico

Nivel 2 o Nivel 3.

## Modelo principal

ChangeRecord.

## Componente principal

DocumentStatusMap.

## Registro de auditoría relacionado

REGISTRO 5 — Corrección.

REGISTRO 11 — Riesgo, si corrige hueco crítico.

REGISTRO 16 — Contradicción documental, si corrige contradicción.

## Notificación relacionada

TIPO 13 — Aviso de cambio registrado.

## Transición siguiente permitida

v0.2 → Aprobado si el usuario aprueba.

v0.2 → v0.3 si requiere nueva corrección.

## Restricción

v0.2 corregido no significa aprobado.

---

# NIVEL 4 — v0.3+ CORRECCIÓN ADICIONAL O ITERACIÓN DOCUMENTAL

## Qué significa

Versión posterior a v0.2 usada cuando todavía hay correcciones adicionales antes de cerrar el documento.

## Cuándo se usa

Cuando v0.2 aún tiene huecos, contradicciones, ambigüedades o cambios importantes pendientes.

## Riesgo típico

Nivel 2 o Nivel 3.

Puede subir a Nivel 4 si corrige algo que podría activar ejecución no autorizada.

## Modelo principal

ChangeRecord.

## Componente principal

RiskBadge.

## Registro de auditoría relacionado

REGISTRO 5 — Corrección.

REGISTRO 11 — Riesgo, si aplica.

REGISTRO 16 — Contradicción documental, si aplica.

## Notificación relacionada

TIPO 5 — Advertencia de riesgo.

TIPO 13 — Aviso de cambio registrado.

## Transición siguiente permitida

v0.3+ → Aprobado si el usuario aprueba.

v0.3+ → v0.4+ si requiere nueva corrección.

## Restricción

No debe usarse para esconder cambios mayores sin registrarlos.

---

# NIVEL 5 — v0.x APROBADO

## Qué significa

Documento aprobado formalmente antes de considerarse versión estable v1.0.

## Cuándo se usa

Cuando el documento ya puede ser referencia oficial dentro de Fase 10, pero el sistema completo sigue en MVP técnico básico.

## Riesgo típico

Nivel 2 o Nivel 3.

## Modelo principal

DecisionRecord.

## Componente principal

ApprovalGate.

## Registro de auditoría relacionado

REGISTRO 6 — Decisión.

REGISTRO 8 — Aprobación.

REGISTRO 9 — Integración, si ya fue integrado.

## Notificación relacionada

TIPO 14 — Aviso de decisión registrada.

TIPO 13 — Aviso de cambio registrado.

## Transición siguiente permitida

v0.x aprobado → v0.x+1 si requiere corrección controlada.

v0.x aprobado → v1.0 si el conjunto documental está estable y el usuario lo aprueba formalmente.

## Restricción

Aprobado no significa programado.

---

# NIVEL 6 — v1.0 VERSIÓN ESTABLE CONCEPTUAL

## Qué significa

Versión considerada estable como referencia principal del sistema.

## Cuándo se usa

Solo cuando el documento ya fue probado, revisado, aprobado, integrado y no quedan huecos críticos conocidos.

## Riesgo típico

Nivel 3 — Alto.

Motivo:

Convertir a v1.0 establece una referencia principal más fuerte.

## Modelo principal

DecisionRecord.

## Componente principal

ApprovalGate.

## Registro de auditoría relacionado

REGISTRO 6 — Decisión.

REGISTRO 8 — Aprobación.

REGISTRO 9 — Integración.

REGISTRO 13 — Alcance.

## Notificación relacionada

TIPO 6 — Confirmación requerida.

TIPO 14 — Aviso de decisión registrada.

## Transición siguiente permitida

v1.0 → v1.1 para actualización menor.

v1.0 → v2.0 para cambio mayor futuro.

## Restricción

v1.0 no autoriza programación por sí mismo.

v1.0 requiere aprobación explícita del usuario.

---

# NIVEL 7 — v1.x ACTUALIZACIÓN MENOR ESTABLE

## Qué significa

Actualización menor sobre una versión estable.

## Cuándo se usa

Cuando se mejora claridad, ejemplos, formato o referencias sin cambiar la regla central.

## Riesgo típico

Nivel 1 a Nivel 2.

Puede subir a Nivel 3 si toca reglas de seguridad o permisos.

## Modelo principal

ChangeRecord.

## Componente principal

DocumentStatusMap.

## Registro de auditoría relacionado

REGISTRO 7 — Cambio.

REGISTRO 5 — Corrección, si corrige error.

## Notificación relacionada

TIPO 13 — Aviso de cambio registrado.

## Transición siguiente permitida

v1.x → v1.x+1 si hay otra actualización menor.

v1.x → v2.0 si el cambio altera estructura, alcance o regla central.

## Restricción

No debe usarse v1.x para cambios mayores disfrazados.

---

# NIVEL 8 — v2.0 CAMBIO MAYOR ESTRUCTURAL FUTURO

## Qué significa

Cambio mayor que modifica estructura, alcance, compatibilidad o regla central de un documento estable.

## Cuándo se usa

Solo en una fase futura o con aprobación explícita del usuario.

## Riesgo típico

Nivel 3 o Nivel 4.

## Modelo principal

RiskRecord / DecisionRecord.

## Componente principal

ApprovalGate.

## Registro de auditoría relacionado

REGISTRO 6 — Decisión.

REGISTRO 7 — Cambio.

REGISTRO 8 — Aprobación.

REGISTRO 11 — Riesgo.

REGISTRO 13 — Alcance.

## Notificación relacionada

TIPO 5 — Advertencia de riesgo.

TIPO 6 — Confirmación requerida.

TIPO 9 — Mensaje de bloqueo si falta permiso.

## Transición siguiente permitida

v2.0 solo puede activarse con aprobación formal y registro completo.

## Restricción

v2.0 no debe crearse automáticamente en Fase 10.

---

# TIPOS DE CAMBIO DOCUMENTAL

Los tipos conceptuales de cambio son:

1. Cambio informativo.
2. Cambio de formato.
3. Corrección menor.
4. Corrección mayor.
5. Corrección crítica.
6. Actualización documental.
7. Integración documental.
8. Reemplazo documental.
9. Depreciación documental.
10. Archivo documental.
11. Cambio de alcance.
12. Cambio incompatible.

---

# ESTRUCTURA UNIFORME DE LOS 12 TIPOS DE CAMBIO

Cada tipo de cambio debe poder mostrar:

```text
Qué significa:
Cuándo ocurre:
Impacto en versión:
Riesgo típico:
Registro de auditoría relacionado:
Requiere decisión:
Requiere cambio:
Requiere HOME:
Requiere README:
Restricción:
```

---

# TIPO 1 — CAMBIO INFORMATIVO

## Qué significa

Cambio que solo explica, resume o aclara sin modificar contenido oficial.

## Cuándo ocurre

Cuando se agrega una nota informativa o explicación sin cambiar regla, estado ni alcance.

## Impacto en versión

No siempre requiere nueva versión.

## Riesgo típico

Nivel 0 — Informativo.

## Registro de auditoría relacionado

REGISTRO 1 — Informativo.

## Requiere decisión

No.

## Requiere cambio

No siempre.

## Requiere HOME

No.

## Requiere README

No.

## Restricción

No debe alterar reglas oficiales.

---

# TIPO 2 — CAMBIO DE FORMATO

## Qué significa

Cambio de orden, estilo, títulos o legibilidad sin alterar contenido.

## Cuándo ocurre

Cuando se mejora presentación del documento.

## Impacto en versión

No siempre requiere nueva versión.

Puede requerir v0.x+1 si el documento es oficial y el cambio es amplio.

## Riesgo típico

Nivel 1 — Bajo.

## Registro de auditoría relacionado

REGISTRO 7 — Cambio, si se registra formalmente.

## Requiere decisión

No normalmente.

## Requiere cambio

Solo si afecta documento importante.

## Requiere HOME

No normalmente.

## Requiere README

No normalmente.

## Restricción

No debe ocultar cambios de contenido.

---

# TIPO 3 — CORRECCIÓN MENOR

## Qué significa

Corrige errores menores, ambigüedad pequeña o redacción.

## Cuándo ocurre

Cuando no cambia alcance, regla central, riesgo ni estructura.

## Impacto en versión

Puede pasar de v0.1 a v0.2 si es primera corrección formal.

Puede ser v0.2 a v0.3 si ya existía v0.2.

## Riesgo típico

Nivel 1 a Nivel 2.

## Registro de auditoría relacionado

REGISTRO 5 — Corrección.

## Requiere decisión

No siempre.

## Requiere cambio

Sí, si se registra formalmente.

## Requiere HOME

Solo si el documento es importante.

## Requiere README

Solo si el documento es importante.

## Restricción

Corrección menor no aprueba documento.

---

# TIPO 4 — CORRECCIÓN MAYOR

## Qué significa

Corrige estructura, relaciones, eventos, registros, estados, permisos o reglas relevantes.

## Cuándo ocurre

Cuando la versión anterior tiene huecos reales que afectan coherencia documental.

## Impacto en versión

Debe crear nueva versión.

Ejemplo:

```text
v0.1 → v0.2
v0.2 → v0.3
```

## Riesgo típico

Nivel 2 a Nivel 3.

## Registro de auditoría relacionado

REGISTRO 5 — Corrección.

REGISTRO 11 — Riesgo si aplica.

REGISTRO 16 — Contradicción documental si aplica.

## Requiere decisión

No para corregir.

Sí para aprobar.

## Requiere cambio

Sí.

## Requiere HOME

Sí, si el documento es técnico importante.

## Requiere README

Sí, si el documento es técnico importante.

## Restricción

No puede aprobarse automáticamente.

---

# TIPO 5 — CORRECCIÓN CRÍTICA

## Qué significa

Corrige un hueco que podría permitir ejecución no autorizada, contradicción grave, permiso incorrecto o ruptura de seguridad.

## Cuándo ocurre

Cuando una versión aprobada o propuesta tiene riesgo crítico.

## Impacto en versión

Debe crear nueva versión.

Puede requerir bloquear temporalmente la versión anterior.

## Riesgo típico

Nivel 3 o Nivel 4.

## Registro de auditoría relacionado

REGISTRO 5 — Corrección.

REGISTRO 10 — Bloqueo si aplica.

REGISTRO 11 — Riesgo.

REGISTRO 16 — Contradicción documental si aplica.

## Requiere decisión

Sí para aprobar la nueva versión.

## Requiere cambio

Sí.

## Requiere HOME

Sí.

## Requiere README

Sí.

## Restricción

No debe quedar sin revisión.

---

# TIPO 6 — ACTUALIZACIÓN DOCUMENTAL

## Qué significa

Agrega contenido, referencias o mejoras a un documento vigente sin reemplazarlo completamente.

## Cuándo ocurre

Cuando un documento aprobado necesita mantenerse actualizado.

## Impacto en versión

Puede ser v0.x+1 o v1.x+1 según estabilidad.

## Riesgo típico

Nivel 2.

Puede subir a Nivel 3 si afecta reglas principales.

## Registro de auditoría relacionado

REGISTRO 7 — Cambio.

REGISTRO 5 — Corrección si corrige error.

## Requiere decisión

Solo si cambia alcance o reglas.

## Requiere cambio

Sí.

## Requiere HOME

Sí si afecta estado central.

## Requiere README

Sí si afecta estado del repositorio.

## Restricción

Actualización no autoriza implementación.

---

# TIPO 7 — INTEGRACIÓN DOCUMENTAL

## Qué significa

Documento aprobado se incorpora al estado oficial de Robert.

## Cuándo ocurre

Después de decisión formal y cambio registrado.

## Impacto en versión

No cambia número de versión por sí sola.

Cambia estado a aprobado e integrado.

## Riesgo típico

Nivel 2 a Nivel 3.

## Registro de auditoría relacionado

REGISTRO 7 — Cambio.

REGISTRO 9 — Integración.

REGISTRO 15 — Respaldo manual si aplica.

## Requiere decisión

Sí, debe existir aprobación previa.

## Requiere cambio

Sí.

## Requiere HOME

Sí.

## Requiere README

Sí.

## Restricción

Integrado no significa programado.

---

# TIPO 8 — REEMPLAZO DOCUMENTAL

## Qué significa

Una versión o documento sustituye a otro como referencia principal.

## Cuándo ocurre

Cuando una nueva versión aprobada supera a una anterior.

## Impacto en versión

La versión anterior queda reemplazada o depreciada.

## Riesgo típico

Nivel 3.

## Registro de auditoría relacionado

REGISTRO 7 — Cambio.

REGISTRO 9 — Integración.

REGISTRO 13 — Alcance.

## Requiere decisión

Sí.

## Requiere cambio

Sí.

## Requiere HOME

Sí.

## Requiere README

Sí.

## Restricción

No debe eliminar la versión anterior.

---

# TIPO 9 — DEPRECIACIÓN DOCUMENTAL

## Qué significa

Una versión sigue existiendo, pero deja de ser fuente principal.

## Cuándo ocurre

Cuando una versión nueva o documento superior la reemplaza parcialmente.

## Impacto en versión

La versión depreciada conserva su número, pero cambia estado.

## Riesgo típico

Nivel 2.

## Registro de auditoría relacionado

REGISTRO 7 — Cambio.

REGISTRO 13 — Alcance.

## Requiere decisión

Sí si afecta documentos oficiales.

## Requiere cambio

Sí.

## Requiere HOME

Sí si afecta estado central.

## Requiere README

Sí si afecta repositorio.

## Restricción

Depreciar no significa borrar.

---

# TIPO 10 — ARCHIVO DOCUMENTAL

## Qué significa

Una versión queda conservada como historial.

## Cuándo ocurre

Cuando ya no forma parte del flujo activo.

## Impacto en versión

No cambia número de versión.

Cambia estado a archivado.

## Riesgo típico

Nivel 1 a Nivel 2.

## Registro de auditoría relacionado

REGISTRO 7 — Cambio.

REGISTRO 15 — Respaldo manual si aplica.

## Requiere decisión

No siempre.

## Requiere cambio

Sí si es documento importante.

## Requiere HOME

No siempre.

## Requiere README

No siempre.

## Restricción

Archivar no significa eliminar.

---

# TIPO 11 — CAMBIO DE ALCANCE

## Qué significa

Cambio que modifica qué puede o no puede hacer un documento.

## Cuándo ocurre

Cuando se alteran permisos, restricciones, fases, capacidades o límites.

## Impacto en versión

Debe crear nueva versión.

Puede requerir v0.x+1 o v1.x+1.

## Riesgo típico

Nivel 3.

Puede subir a Nivel 4 si toca ejecución, conexiones, agentes o automatizaciones.

## Registro de auditoría relacionado

REGISTRO 11 — Riesgo.

REGISTRO 12 — Permiso.

REGISTRO 13 — Alcance.

## Requiere decisión

Sí.

## Requiere cambio

Sí.

## Requiere HOME

Sí.

## Requiere README

Sí.

## Restricción

No puede hacerse silenciosamente.

---

# TIPO 12 — CAMBIO INCOMPATIBLE

## Qué significa

Cambio que rompe compatibilidad con documentos anteriores o contradice reglas vigentes.

## Cuándo ocurre

Cuando una versión nueva ya no puede coexistir como equivalente con la anterior.

## Impacto en versión

Debe crear nueva versión mayor o corrección formal.

## Riesgo típico

Nivel 3 o Nivel 4.

## Registro de auditoría relacionado

REGISTRO 10 — Bloqueo si aplica.

REGISTRO 11 — Riesgo.

REGISTRO 13 — Alcance.

REGISTRO 16 — Contradicción documental.

## Requiere decisión

Sí.

## Requiere cambio

Sí.

## Requiere HOME

Sí.

## Requiere README

Sí.

## Restricción

Debe resolverse antes de aprobar.

---

# REGLAS PARA CAMBIAR NÚMERO DE VERSIÓN

## v0.1

Usar v0.1 cuando:

- Es primer borrador.
- Documento nace por primera vez.
- Todavía no fue corregido.
- Todavía no fue aprobado.
- Todavía no está integrado.

---

## v0.2

Usar v0.2 cuando:

- v0.1 fue revisado.
- Se detectaron huecos reales.
- Se aplicaron correcciones.
- Se agregó estructura faltante.
- Se corrigieron relaciones con documentos base.
- Se corrigieron eventos, registros, acciones, permisos, estados o transiciones.
- Todavía falta aprobación.

---

## v0.3

Usar v0.3 cuando:

- v0.2 todavía tiene huecos.
- v0.2 requiere nueva corrección.
- Se detecta ambigüedad adicional.
- Se requiere mejorar una corrección previa.
- El documento todavía no debe aprobarse.

---

## v0.x aprobado

Usar v0.x aprobado cuando:

- El usuario aprueba formalmente.
- Se registra DECISIÓN.
- Se registra CAMBIO.
- Se actualiza HOME.
- Se actualiza README si aplica.
- El documento queda como referencia oficial de Fase 10.

---

## v1.0

Usar v1.0 solo cuando:

- El documento está estable.
- No quedan huecos críticos conocidos.
- Ya fue probado en uso documental.
- Ya fue aprobado e integrado.
- El usuario aprueba explícitamente elevarlo a v1.0.
- El conjunto documental relacionado es consistente.

Regla:

**Ningún documento pasa a v1.0 automáticamente.**

---

# REGLAS DE COMPATIBILIDAD ENTRE VERSIONES

Una versión es compatible cuando:

- No contradice reglas vigentes.
- No cambia la regla central sin aprobación.
- No elimina restricciones de seguridad.
- No autoriza capacidades futuras.
- No altera permisos sin registro.
- No rompe el flujo documental aprobado.
- Puede coexistir como historial con versiones anteriores.

Una versión es incompatible cuando:

- Contradice un documento aprobado.
- Reabre una capacidad bloqueada.
- Permite ejecución no autorizada.
- Modifica alcance sin aprobación.
- Cambia fase sin decisión.
- Reemplaza un documento sin trazabilidad.
- Usa modelos o componentes no aprobados como si fueran oficiales.

---

# REGLAS DE VERSIÓN VIGENTE

Una versión vigente es la versión que Robert debe usar como referencia principal.

Para ser vigente debe cumplir:

- Estar aprobada.
- Estar integrada.
- Tener decisión registrada.
- Tener cambio registrado.
- Estar reflejada en HOME si es documento importante.
- Estar reflejada en README si afecta el repositorio.
- No estar depreciada.
- No estar reemplazada.
- No estar bloqueada.

Regla:

**La versión más nueva no siempre es la versión vigente.**

---

# REGLAS DE VERSIÓN HISTÓRICA

Una versión histórica:

- Puede consultarse.
- No debe usarse como fuente principal.
- Debe conservar trazabilidad.
- Puede estar reemplazada, depreciada o archivada.
- No debe eliminarse automáticamente.

---

# REGLAS PARA DOCUMENTOS APROBADOS QUE NECESITAN CORRECCIÓN

Si un documento aprobado necesita corrección:

1. No modificar silenciosamente.
2. Detectar el problema.
3. Crear nueva versión corregida.
4. Registrar cambio de corrección.
5. Actualizar HOME si aplica.
6. Actualizar README si aplica.
7. Revisar nueva versión.
8. Pedir aprobación formal.
9. Registrar decisión.
10. Registrar cambio de aprobación e integración.
11. Actualizar HOME con estado aprobado.
12. Actualizar README con estado aprobado.
13. Cerrar bloque.

---

# REGLAS PARA REEMPLAZO DE VERSIONES

Una versión reemplaza a otra cuando:

- La nueva versión fue aprobada.
- La nueva versión integra correcciones o cambios necesarios.
- Existe registro de decisión.
- Existe registro de cambio.
- HOME y README reflejan el nuevo estado si aplica.
- La versión anterior queda como histórica, depreciada o reemplazada.

Regla:

**Reemplazar no significa borrar.**

---

# REGLAS PARA CAMBIO MAYOR

Un cambio es mayor cuando:

- Cambia regla central.
- Cambia alcance.
- Cambia permisos.
- Cambia eventos importantes.
- Cambia registros de auditoría.
- Cambia acciones de usuario.
- Cambia modelos oficiales.
- Cambia componentes oficiales.
- Cambia flujo aprobado.
- Cambia ciclo de vida.
- Cambia fase.
- Autoriza o bloquea capacidades importantes.

Cambio mayor requiere:

- Revisión.
- Registro de cambio.
- Aprobación formal.
- Actualización de HOME.
- Actualización de README.
- Control de compatibilidad.

---

# REGLAS PARA CAMBIO MENOR

Un cambio es menor cuando:

- Mejora redacción.
- Aclara una nota.
- Corrige formato.
- Corrige typo.
- Agrega ejemplo sin cambiar regla.
- Ordena contenido sin cambiar alcance.
- Mejora lectura.

Cambio menor puede requerir:

- Registro de cambio si afecta documento importante.
- HOME si afecta estado central.
- README si afecta estado del repositorio.

---

# REGLAS PARA PARCHE DOCUMENTAL

Un parche documental corrige algo pequeño sin cambiar versión principal.

Se permite solo cuando:

- No cambia regla.
- No cambia alcance.
- No cambia permisos.
- No cambia estado.
- No altera documentos relacionados.
- No afecta seguridad.

Regla:

**Si el parche toca seguridad, permisos, auditoría, bloqueos, fases o autonomía, debe tratarse como corrección formal, no como parche simple.**

---

# RELACIÓN CON DOCUMENT_LIFECYCLE_SPEC v0.2

DOCUMENT_LIFECYCLE_SPEC define estados.

VERSIONING_AND_CHANGE_POLICY_SPEC define cuándo cambia el número de versión y cómo se registra el cambio.

Relación:

- Lifecycle dice si un documento está en borrador, aprobado, integrado, depreciado o archivado.
- Versioning dice si ese documento es v0.1, v0.2, v0.3, v1.0 o superior.
- Lifecycle define transiciones de estado.
- Versioning define transiciones de número.
- Ambos deben respetarse al mismo tiempo.

---

# RELACIÓN CON SESSION_AND_CONTEXT_SPEC v0.2

SESSION_AND_CONTEXT_SPEC define continuidad.

VERSIONING_AND_CHANGE_POLICY_SPEC define cómo interpretar cambios de versión dentro de esa continuidad.

Ejemplo:

```text
Último documento activo: DOCUMENT_LIFECYCLE_SPEC v0.2
Último estado: Aprobado e integrado
Última decisión: DECISIÓN #023
Último cambio: CAMBIO #040
Próximo documento: VERSIONING_AND_CHANGE_POLICY_SPEC v0.1
```

---

# RELACIÓN CON AUDIT_TRAIL_SPEC v0.2

AUDIT_TRAIL_SPEC define registros.

VERSIONING_AND_CHANGE_POLICY_SPEC define cuándo se usan para cambios de versión.

Registros especialmente relevantes:

- REGISTRO 2 — Comando.
- REGISTRO 3 — Revisión.
- REGISTRO 4 — Borrador.
- REGISTRO 5 — Corrección.
- REGISTRO 6 — Decisión.
- REGISTRO 7 — Cambio.
- REGISTRO 8 — Aprobación.
- REGISTRO 9 — Integración.
- REGISTRO 10 — Bloqueo.
- REGISTRO 11 — Riesgo.
- REGISTRO 12 — Permiso.
- REGISTRO 13 — Alcance.
- REGISTRO 15 — Respaldo manual.
- REGISTRO 16 — Contradicción documental.
- REGISTRO 17 — Capacidad futura no disponible.

Regla:

**Toda versión importante debe poder rastrearse desde auditoría documental.**

---

# RELACIÓN CON NOTIFICATION_AND_ALERTS_SPEC v0.2

NOTIFICATION_AND_ALERTS_SPEC define avisos.

VERSIONING_AND_CHANGE_POLICY_SPEC define cuándo una versión debe generar aviso.

Ejemplos:

- Nueva versión creada → Notificación de estado.
- Corrección aplicada → Aviso de cambio registrado.
- Aprobación requerida → Confirmación requerida.
- Cambio mayor detectado → Advertencia de riesgo.
- Cambio incompatible detectado → Mensaje de bloqueo.
- Respaldo manual hecho → Aviso de respaldo manual.

---

# RELACIÓN CON USER_ACTIONS_SPEC v0.2

| Acción del usuario | Resultado de versión esperado |
|---|---|
| Crear documento técnico | v0.1 |
| Corregir documento técnico | v0.2 o v0.x+1 |
| Revisar documento | No cambia versión por sí solo |
| Aprobar documento | Mantiene número, cambia estado a aprobado |
| Registrar decisión | Confirma aprobación o rechazo |
| Registrar cambio | Confirma corrección, integración o reemplazo |
| Actualizar HOME | Refleja estado de versión |
| Actualizar README | Refleja estado de versión |
| Solicitar pausa | No cambia versión por sí solo |
| Solicitar bloqueo manual | Puede bloquear transición de versión |
| Pedir siguiente paso | Puede recomendar nueva versión o nuevo documento |

---

# RELACIÓN CON ERROR_AND_BLOCKING_SPEC v0.2

Eventos relevantes:

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
- EVENTO 15 — Ejecución no autorizada.
- EVENTO 16 — Conexión no autorizada.
- EVENTO 17 — Automatización no autorizada.
- EVENTO 18 — Agente no autorizado.
- EVENTO 20 — Fase incorrecta.

Regla:

**Si un cambio de versión intenta activar una capacidad no autorizada, debe bloquearse.**

---

# RELACIÓN CON PERMISSIONS_AND_SCOPES_SPEC v0.2

Cada cambio de versión requiere permiso suficiente.

Ejemplos:

| Cambio | Permiso necesario |
|---|---|
| Crear v0.1 | Solicitud simple |
| Corregir v0.1 a v0.2 | Autorización de corrección |
| Aprobar v0.2 | Aprobación explícita |
| Integrar versión aprobada | Decisión y cambio registrados |
| Depreciar versión | Decisión documental |
| Reemplazar versión | Aprobación formal |
| Elevar a v1.0 | Aprobación explícita especial |
| Crear v2.0 | Aprobación mayor y revisión de alcance |

Regla:

**Permiso para corregir no es permiso para aprobar. Permiso para aprobar no es permiso para elevar a v1.0.**

---

# RELACIÓN CON DATA_MODEL_SPEC v0.1

Este documento no crea modelos nuevos.

Usa:

- RobertDocument para nombre, versión y estado.
- ChangeRecord para cambios.
- DecisionRecord para aprobaciones.
- PendingDecision para decisiones pendientes.
- SystemState para estado general.
- RiskRecord para riesgo de cambio.
- CommandRequest para instrucciones.
- ModeState para modo operativo.
- ComponentState para visualización conceptual.
- GitHubBackupStatus para respaldo manual.
- ObsidianGraphStatus para estado visual documental.

---

# RELACIÓN CON COMPONENTS_SPEC v0.2

Este documento no crea componentes nuevos.

Usa:

- DocumentStatusMap para versiones documentales.
- CurrentStatePanel para versión activa.
- DecisionInbox para aprobaciones pendientes.
- ApprovalGate para cambios de versión bloqueados.
- RiskBadge para riesgo de versión.
- CommandCenter para comandos.
- TopBar para fase, modo y versión activa.
- LeftSidebar para navegación documental.

---

# RELACIÓN CON SCREEN_STATE_SPEC v0.2

SCREEN_STATE_SPEC define cómo se ve el estado.

VERSIONING_AND_CHANGE_POLICY_SPEC define qué versión debe mostrarse.

Ejemplo:

```text
Documento activo: DOCUMENT_LIFECYCLE_SPEC
Versión activa: v0.2
Estado: Aprobado e integrado
Versión anterior: v0.1
Última decisión: DECISIÓN #023
Último cambio: CAMBIO #040
```

---

# RELACIÓN CON INTERACTION_FLOW_SPEC v0.2

INTERACTION_FLOW_SPEC define cómo fluye la interacción.

VERSIONING_AND_CHANGE_POLICY_SPEC define cuándo una interacción produce nueva versión, corrección, aprobación o reemplazo.

Regla:

**Un flujo de interacción no puede modificar versión sin respetar permisos, auditoría y ciclo documental.**

---

# RELACIÓN CON GITHUB Y OBSIDIAN

GitHub y Obsidian siguen siendo manuales.

GitHub se usa como:

- Respaldo documental privado.
- Historial manual.
- Control de versiones manual.
- Commit manual.

Obsidian se usa como:

- Cerebro documental.
- Grafo visual.
- Navegación por documentos.
- Fuente organizada de lectura.

No se autoriza:

- Conexión automática.
- Sincronización automática.
- Commits automáticos.
- Versionado automático.
- Actualización automática de documentos.
- Agentes que modifiquen archivos.

---

# FORMATO MÍNIMO DE VERSIÓN DOCUMENTAL

Todo documento técnico importante debe poder mostrar:

```text
Nombre del documento:
Versión actual:
Estado:
Versión anterior:
Versión que reemplaza:
Documento vigente:
Fecha:
Ubicación:
Fase relacionada:
Documento base principal:
Documentos relacionados:
Último cambio:
Última decisión:
Tipo de cambio:
Riesgo:
Compatibilidad:
Alcance autorizado:
Alcance no autorizado:
Próximo paso:
Restricción:
```

---

# EJEMPLO DE ESTADO DE VERSIÓN

```text
Nombre del documento: ROBERT_TECHNICAL_DOCUMENT_LIFECYCLE_SPEC
Versión actual: v0.2
Estado: Aprobado e integrado
Versión anterior: v0.1
Versión que reemplaza: v0.1
Documento vigente: v0.2
Última decisión: DECISIÓN #023
Último cambio: CAMBIO #040
Tipo de cambio: Corrección mayor / integración documental
Riesgo: Nivel 3 inicial / Nivel 2 final
Compatibilidad: Compatible como reemplazo documental
Restricción: Sin programación, sin Fase 11
```

---

# CRITERIOS DE ACEPTACIÓN

Este documento podrá considerarse listo para aprobación si:

- Define reglas de versionamiento.
- Define niveles de versión.
- Define v0.0.
- Define v0.1.
- Define v0.2.
- Define v0.3+.
- Define v0.x aprobado.
- Define v1.0.
- Define v1.x.
- Define v2.0.
- Incluye estructura uniforme de los 8 niveles de versión.
- Define tipos de cambio documental.
- Incluye estructura uniforme de los 12 tipos de cambio.
- Define cuándo cambiar número de versión.
- Define cuándo usar v0.1.
- Define cuándo usar v0.2.
- Define cuándo usar v0.3.
- Define cuándo elevar a v1.0.
- Define compatibilidad entre versiones.
- Define versión vigente.
- Define versión histórica.
- Define reglas para corregir documentos aprobados.
- Define reglas para reemplazo de versiones.
- Define cambio mayor.
- Define cambio menor.
- Define parche documental.
- Define relación con DOCUMENT_LIFECYCLE_SPEC v0.2.
- Define relación con SESSION_AND_CONTEXT_SPEC v0.2.
- Define relación con AUDIT_TRAIL_SPEC v0.2.
- Define relación con NOTIFICATION_AND_ALERTS_SPEC v0.2.
- Define relación con USER_ACTIONS_SPEC v0.2.
- Define relación con ERROR_AND_BLOCKING_SPEC v0.2.
- Define relación con PERMISSIONS_AND_SCOPES_SPEC v0.2.
- Define relación con DATA_MODEL_SPEC v0.1.
- Define relación con COMPONENTS_SPEC v0.2.
- Define relación con SCREEN_STATE_SPEC v0.2.
- Define relación con INTERACTION_FLOW_SPEC v0.2.
- Aclara que no crea VersionRecord.
- Aclara que no crea VersionPolicyRecord.
- Aclara que no crea CompatibilityRecord.
- Aclara que no crea VersionTimeline.
- Aclara que no crea CompatibilityPanel.
- Aclara que no automatiza GitHub.
- Aclara que no automatiza Obsidian.
- Mantiene a Robert en Fase 10.
- Mantiene Nivel 0 únicamente como Informativo.
- Mantiene acciones de control fuera de la escala de riesgo.
- Mantiene control total del usuario.

---

# RIESGO DEL DOCUMENTO

Tipo de cambio:

**Cambio técnico documental / política conceptual de versiones y cambios**

Nivel de riesgo inicial:

**Nivel 3 — Alto**

Motivo:

Este documento define cómo Robert numera versiones, registra cambios, corrige documentos, reemplaza versiones, mantiene compatibilidad y evita contradicciones entre documentos.

Nivel de riesgo final esperado:

**Nivel 2 — Medio**

Motivo de reducción:

El documento es documental. No crea sistema real de control de versiones, no crea base de datos real, no crea control automático de versiones, no crea modelos nuevos oficiales, no crea componentes nuevos oficiales, no conecta herramientas externas y no ejecuta acciones.

Nivel de autonomía:

**Nivel 0 — Sin autonomía ejecutiva**

---

# DECISIÓN PENDIENTE

Este documento queda como:

**Borrador técnico documental pendiente de revisión**

Para aprobarlo formalmente, el usuario deberá escribir:

**APRUEBO ROBERT_TECHNICAL_VERSIONING_AND_CHANGE_POLICY_SPEC v0.1**

---

# EFECTO DE UNA APROBACIÓN FUTURA

Si se aprueba este documento, se deberá:

1. Registrar decisión formal en ROBERT_DECISIONS_LOG.
2. Registrar cambio en ROBERT_CONTROL_DE_CAMBIOS.
3. Actualizar ROBERT_HOME.
4. Actualizar README si aplica.
5. Mantenerlo como base para futuras especificaciones técnicas.
6. No crear sistema real de control de versiones.
7. No crear base de datos real.
8. No crear control automático de versiones.
9. No conectar GitHub automáticamente.
10. No conectar Obsidian automáticamente.
11. No pasar automáticamente a programación.
12. No avanzar automáticamente a Fase 11.

---

# PRÓXIMO PASO RECOMENDADO

Después de revisar este documento, el siguiente documento posible sería:

**ROBERT_TECHNICAL_DATA_CONSISTENCY_AND_CONFLICT_RESOLUTION_SPEC**

Ese documento definiría cómo Robert detecta contradicciones entre documentos, qué documento gana en caso de conflicto, cómo se resuelven inconsistencias y cómo se bloquea una acción cuando hay información contradictoria.

No debe crearse hasta revisar o aprobar VERSIONING_AND_CHANGE_POLICY_SPEC.

---

# CIERRE

ROBERT_TECHNICAL_VERSIONING_AND_CHANGE_POLICY_SPEC v0.1 define las reglas conceptuales de versiones, cambios, compatibilidad, reemplazos, correcciones, parches, versiones vigentes y versiones históricas de Robert.

Este documento mantiene a Robert en modo documental, manual y supervisado.

El usuario mantiene control total.

Robert no ejecuta acciones importantes sin permiso.
