# ROBERT_TECHNICAL_DATA_CONSISTENCY_AND_CONFLICT_RESOLUTION_SPEC

Versión: 0.1  
Estado: Borrador técnico documental nuevo — pendiente de revisión  
Fecha: 06/07/2026  
Ubicación: 10_MVP  
Fase relacionada: Fase 10 — MVP técnico básico en preparación  
Documento base principal: ROBERT_TECHNICAL_VERSIONING_AND_CHANGE_POLICY_SPEC v0.2  
Documentos relacionados: ROBERT_COMMANDS v0.4, ROBERT_TECHNICAL_DOCUMENT_LIFECYCLE_SPEC v0.2, ROBERT_TECHNICAL_SESSION_AND_CONTEXT_SPEC v0.2, ROBERT_TECHNICAL_NOTIFICATION_AND_ALERTS_SPEC v0.2, ROBERT_TECHNICAL_AUDIT_TRAIL_SPEC v0.2, ROBERT_TECHNICAL_PERMISSIONS_AND_SCOPES_SPEC v0.2, ROBERT_TECHNICAL_ERROR_AND_BLOCKING_SPEC v0.2, ROBERT_TECHNICAL_USER_ACTIONS_SPEC v0.2, ROBERT_TECHNICAL_DATA_MODEL_SPEC v0.1, ROBERT_TECHNICAL_COMPONENTS_SPEC v0.2, ROBERT_TECHNICAL_SCREEN_STATE_SPEC v0.2, ROBERT_TECHNICAL_INTERACTION_FLOW_SPEC v0.2  
Fuente de verdad actual: ROBERT_CONTEXT_MASTER v0.5  

Tags: #robert/orbita-3 #capa/5 #tipo/tecnico #robert/mvp #robert/data-consistency #robert/conflict-resolution

---

# OBJETIVO

ROBERT_TECHNICAL_DATA_CONSISTENCY_AND_CONFLICT_RESOLUTION_SPEC define cómo Robert debe manejar consistencia documental, contradicciones, conflictos entre documentos, reglas de prioridad, resolución de inconsistencias y bloqueos por información contradictoria dentro del MVP técnico básico.

Su objetivo es responder:

- Qué es consistencia documental.
- Qué es una contradicción.
- Qué es un conflicto documental.
- Qué es una inconsistencia menor.
- Qué es una inconsistencia crítica.
- Qué documento gana cuando dos documentos se contradicen.
- Qué pasa si una versión vieja contradice una versión nueva.
- Qué pasa si HOME contradice README.
- Qué pasa si COMMANDS contradice SECURITY_RULES.
- Qué pasa si un documento técnico contradice un documento maestro.
- Qué pasa si una decisión contradice un cambio.
- Qué pasa si falta trazabilidad.
- Qué pasa si una acción se basa en información contradictoria.
- Cuándo se debe pausar.
- Cuándo se debe bloquear.
- Cuándo se debe pedir confirmación.
- Cuándo se debe crear una corrección documental.
- Cómo se registra una contradicción.
- Cómo se resuelve una contradicción.
- Qué relación tiene esto con auditoría, permisos, eventos, notificaciones, versionamiento y ciclo documental.

Este documento no crea sistema real de validación automática.

Este documento no crea base de datos real.

Este documento no crea motor real de resolución de conflictos.

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

No autoriza sistema real de consistencia.

No autoriza base de datos real.

No autoriza verificación automática.

No autoriza resolución automática de conflictos.

No autoriza sincronización automática con GitHub.

No autoriza sincronización automática con Obsidian.

No autoriza agentes autónomos.

No autoriza avanzar a Fase 11.

---

# REGLA CENTRAL

Robert debe preferir seguridad, trazabilidad y control del usuario sobre velocidad.

Regla principal:

**Si existe contradicción documental relevante, Robert no debe avanzar como si el sistema estuviera consistente.**

---

# REGLA DE BLOQUEO POR CONTRADICCIÓN

Cuando Robert detecte una contradicción que afecte seguridad, permisos, fase, ejecución, aprobación, versión, alcance o autonomía, debe pausar o bloquear.

Regla:

**Una contradicción no resuelta impide aprobar, integrar, ejecutar o avanzar de fase.**

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
- ROBERT_TECHNICAL_VERSIONING_AND_CHANGE_POLICY_SPEC v0.2 aprobado.
- ROBERT_TECHNICAL_DATA_CONSISTENCY_AND_CONFLICT_RESOLUTION_SPEC v0.1 creado como borrador.
- Sin programación autorizada.
- Sin código real.
- Sin sistema real de consistencia documental.
- Sin base de datos real.
- Sin conexiones externas.
- Sin automatizaciones reales.
- Sin agentes autónomos activos.

---

# ALCANCE AUTORIZADO

Este documento autoriza únicamente:

- Definir consistencia documental conceptual.
- Definir contradicción documental conceptual.
- Definir tipos de conflicto documental.
- Definir jerarquía conceptual de fuentes.
- Definir reglas de prioridad documental.
- Definir reglas para detectar inconsistencias.
- Definir reglas para pausar por contradicción.
- Definir reglas para bloquear por contradicción.
- Definir reglas para resolver conflictos documentalmente.
- Definir cuándo crear una corrección.
- Definir cuándo registrar cambio.
- Definir cuándo registrar decisión.
- Definir cuándo actualizar HOME.
- Definir cuándo actualizar README.
- Mantener a Robert en modo documental, manual y supervisado.

---

# ALCANCE NO AUTORIZADO

Este documento no autoriza:

- Programar la app.
- Crear código real.
- Crear sistema real de consistencia documental.
- Crear base de datos real.
- Crear motor real de resolución de conflictos.
- Crear validación automática.
- Crear reconciliación automática.
- Crear modelo ConflictRecord.
- Crear modelo ConsistencyCheckRecord.
- Crear modelo ConflictResolutionRecord.
- Crear modelo SourcePriorityRecord.
- Crear componente ConflictPanel.
- Crear componente ConsistencyMap.
- Crear componente ConflictResolver.
- Crear botones reales.
- Crear pantallas reales.
- Crear prototipo funcional.
- Crear endpoints.
- Conectar Supabase.
- Conectar Firebase.
- Conectar GitHub automáticamente.
- Conectar Obsidian automáticamente.
- Sincronizar documentos automáticamente.
- Resolver conflictos automáticamente.
- Automatizar correcciones.
- Automatizar HOME.
- Automatizar README.
- Activar agentes autónomos.
- Ejecutar acciones reales.
- Avanzar automáticamente a Fase 11.

---

# DATA CONSISTENCY NO CREA MODELO NUEVO OFICIAL

En esta versión, consistencia y resolución de conflictos no crean modelos nuevos.

No se crean:

```text
ConflictRecord
ConsistencyCheckRecord
ConflictResolutionRecord
SourcePriorityRecord
ContradictionRecord
```

Este documento usa modelos ya aprobados en DATA_MODEL_SPEC v0.1.

Si en el futuro se decide crear modelos oficiales de consistencia o conflicto, primero deberá corregirse y aprobarse:

```text
ROBERT_TECHNICAL_DATA_MODEL_SPEC
```

---

# DATA CONSISTENCY NO CREA COMPONENTE NUEVO OFICIAL

En esta versión, consistencia y resolución de conflictos no crean componentes nuevos.

No se crean:

```text
ConflictPanel
ConsistencyMap
ConflictResolver
SourcePriorityViewer
ContradictionBadge
```

Este documento usa componentes ya aprobados en COMPONENTS_SPEC v0.2.

Si en el futuro se decide crear componentes oficiales para conflictos, primero deberá corregirse y aprobarse:

```text
ROBERT_TECHNICAL_COMPONENTS_SPEC
```

---

# DEFINICIONES BASE

## Consistencia documental

Consistencia documental significa que los documentos oficiales de Robert no se contradicen entre sí en reglas, permisos, fases, versiones, estados, restricciones, comandos, riesgos, eventos, acciones, modelos o componentes.

## Contradicción documental

Contradicción documental significa que dos o más documentos dicen cosas incompatibles.

Ejemplo:

```text
Documento A dice: "No hay programación autorizada."
Documento B dice: "Ya se puede programar la app."
```

Resultado:

```text
Contradicción crítica.
Debe bloquearse.
```

## Inconsistencia menor

Inconsistencia menor es una diferencia que no cambia reglas, permisos, riesgos, fases, estado del sistema ni seguridad.

Ejemplo:

```text
Un documento dice "actualización README".
Otro dice "actualización de README.md".
```

## Inconsistencia mayor

Inconsistencia mayor afecta interpretación, flujo, estado, aprobación, versión, auditoría o restricciones.

## Conflicto crítico

Conflicto crítico afecta seguridad, permisos, autonomía, ejecución real, conexiones, agentes, automatizaciones, fase o aprobación formal.

---

# JERARQUÍA CONCEPTUAL DE FUENTES

Cuando dos fuentes se contradicen, Robert debe revisar esta jerarquía.

Orden de prioridad general:

1. Instrucción actual explícita del usuario.
2. Comandos de control del usuario.
3. ROBERT_SECURITY_RULES.
4. ROBERT_CONTEXT_MASTER.
5. ROBERT_PHASES.
6. ROBERT_COMMANDS.
7. ROBERT_DECISIONS_LOG.
8. ROBERT_CONTROL_DE_CAMBIOS.
9. Documento técnico aprobado vigente.
10. ROBERT_HOME.
11. README.
12. Documento técnico borrador o propuesta.
13. Documento reemplazado, depreciado o archivado.
14. Nota informal o comentario no aprobado.

---

# REGLA DE PRIORIDAD MÁXIMA DEL USUARIO

La instrucción actual explícita del usuario tiene prioridad operativa inmediata, siempre que no solicite una acción prohibida, insegura o fuera de fase.

Ejemplo:

```text
Usuario: PAUSA
```

Resultado:

```text
Pausa inmediata.
```

Pero si el usuario dice:

```text
Conecta Gmail automáticamente.
```

Resultado:

```text
Bloqueo.
Motivo: conexión externa no autorizada en Fase 10.
```

---

# REGLA DE SEGURIDAD SOBRE DOCUMENTOS

Si SECURITY_RULES contradice otro documento, gana SECURITY_RULES.

Regla:

**La seguridad tiene prioridad sobre velocidad, comodidad, automatización o avance.**

---

# REGLA DE DOCUMENTO APROBADO SOBRE BORRADOR

Un documento aprobado vigente tiene prioridad sobre un borrador.

Ejemplo:

```text
DOCUMENT_LIFECYCLE_SPEC v0.2 aprobado
vs
VERSIONING_AND_CHANGE_POLICY_SPEC v0.1 borrador
```

Gana:

```text
DOCUMENT_LIFECYCLE_SPEC v0.2 aprobado
```

---

# REGLA DE VERSIÓN VIGENTE SOBRE VERSIÓN HISTÓRICA

Una versión vigente aprobada e integrada tiene prioridad sobre versiones reemplazadas, depreciadas o archivadas.

Ejemplo:

```text
SESSION_AND_CONTEXT_SPEC v0.2 aprobado
vs
SESSION_AND_CONTEXT_SPEC v0.1 borrador
```

Gana:

```text
SESSION_AND_CONTEXT_SPEC v0.2 aprobado
```

---

# REGLA DE DECISIÓN SOBRE INTERPRETACIÓN

Si existe una decisión formal registrada, esa decisión tiene prioridad sobre interpretaciones posteriores no registradas.

Ejemplo:

```text
DECISIÓN #024 aprueba VERSIONING_AND_CHANGE_POLICY_SPEC v0.2.
```

No se debe tratar como pendiente.

---

# REGLA DE CAMBIO SOBRE ESTADO ANTIGUO

Si existe un cambio formal registrado e integrado, ese cambio actualiza el estado documental anterior.

Ejemplo:

```text
CAMBIO #042 aprueba e integra VERSIONING_AND_CHANGE_POLICY_SPEC v0.2.
```

El estado anterior de propuesta corregida ya no debe usarse como estado vigente.

---

# REGLA HOME VS README

HOME y README tienen funciones distintas.

HOME dirige el sistema Robert.

README resume el estado del repositorio.

Si HOME y README se contradicen:

1. Revisar DECISIONS_LOG.
2. Revisar CONTROL_DE_CAMBIOS.
3. Revisar documento técnico aprobado.
4. Corregir HOME o README según corresponda.

Regla:

**README no reemplaza a HOME. HOME no reemplaza a DECISIONS_LOG ni CONTROL_DE_CAMBIOS.**

---

# TIPOS DE CONFLICTO DOCUMENTAL

Los tipos conceptuales de conflicto son:

1. Conflicto informativo menor.
2. Conflicto de estado.
3. Conflicto de versión.
4. Conflicto de aprobación.
5. Conflicto de cambio.
6. Conflicto de permiso.
7. Conflicto de alcance.
8. Conflicto de fase.
9. Conflicto de seguridad.
10. Conflicto de modelo.
11. Conflicto de componente.
12. Conflicto de flujo.
13. Conflicto de evento.
14. Conflicto de auditoría.
15. Conflicto de ejecución no autorizada.
16. Conflicto de fuente vigente.
17. Conflicto de trazabilidad insuficiente.

---

# ESTRUCTURA UNIFORME DE LOS 17 TIPOS DE CONFLICTO

Cada tipo de conflicto debe poder mostrar:

```text
Qué significa:
Cuándo ocurre:
Riesgo típico:
Fuente que normalmente gana:
Modelo principal:
Componente principal:
Evento relacionado:
Registro de auditoría relacionado:
Notificación relacionada:
Acción esperada del usuario:
Resolución esperada:
Restricción:
```

---

# TIPO 1 — CONFLICTO INFORMATIVO MENOR

## Qué significa

Diferencia menor de redacción, nombre, formato o explicación que no cambia reglas ni estado.

## Cuándo ocurre

Cuando dos documentos expresan lo mismo con palabras distintas.

## Riesgo típico

Nivel 1 — Bajo.

## Fuente que normalmente gana

Documento aprobado vigente.

## Modelo principal

RobertDocument.

## Componente principal

CurrentStatePanel.

## Evento relacionado

Ninguno obligatorio.

EVENTO 9 si causa falta de información.

## Registro de auditoría relacionado

REGISTRO 3 — Revisión.

## Notificación relacionada

TIPO 1 — Notificación informativa.

## Acción esperada del usuario

Aceptar diferencia menor o pedir corrección.

## Resolución esperada

Corrección menor si hace falta.

## Restricción

No debe bloquear si no afecta reglas ni seguridad.

---

# TIPO 2 — CONFLICTO DE ESTADO

## Qué significa

Dos documentos indican estados diferentes para el mismo documento o bloque.

## Cuándo ocurre

Ejemplo:

```text
HOME dice: pendiente de revisión.
README dice: aprobado.
```

## Riesgo típico

Nivel 2 — Medio.

## Fuente que normalmente gana

DECISIONS_LOG y CONTROL_DE_CAMBIOS.

## Modelo principal

SystemState / RobertDocument.

## Componente principal

DocumentStatusMap.

## Evento relacionado

EVENTO 9 — Falta de información.

EVENTO 10 — Contradicción documental.

## Registro de auditoría relacionado

REGISTRO 7 — Cambio.

REGISTRO 16 — Contradicción documental.

## Notificación relacionada

TIPO 10 — Alerta de contradicción documental.

## Acción esperada del usuario

Revisar decisión y cambio registrados.

## Resolución esperada

Actualizar HOME o README según el registro oficial.

## Restricción

No aprobar ni integrar mientras el estado sea contradictorio.

---

# TIPO 3 — CONFLICTO DE VERSIÓN

## Qué significa

Dos fuentes señalan versiones diferentes como vigentes.

## Cuándo ocurre

Ejemplo:

```text
Un documento dice v0.1 vigente.
Otro dice v0.2 aprobado e integrado.
```

## Riesgo típico

Nivel 2 a Nivel 3.

## Fuente que normalmente gana

VERSIONING_AND_CHANGE_POLICY_SPEC + DECISIONS_LOG + CONTROL_DE_CAMBIOS.

## Modelo principal

RobertDocument / ChangeRecord.

## Componente principal

DocumentStatusMap.

## Evento relacionado

EVENTO 10 — Contradicción documental.

## Registro de auditoría relacionado

REGISTRO 7 — Cambio.

REGISTRO 9 — Integración.

REGISTRO 16 — Contradicción documental.

## Notificación relacionada

TIPO 10 — Alerta de contradicción documental.

## Acción esperada del usuario

Confirmar versión vigente.

## Resolución esperada

Marcar versión correcta como vigente y anterior como histórica, reemplazada o depreciada.

## Restricción

La versión más nueva no siempre gana si no fue aprobada e integrada.

---

# TIPO 4 — CONFLICTO DE APROBACIÓN

## Qué significa

Hay contradicción sobre si un documento fue aprobado.

## Cuándo ocurre

Ejemplo:

```text
README dice aprobado.
DECISIONS_LOG no tiene decisión.
```

## Riesgo típico

Nivel 3 — Alto.

## Fuente que normalmente gana

DECISIONS_LOG.

## Modelo principal

DecisionRecord.

## Componente principal

ApprovalGate.

## Evento relacionado

EVENTO 3 — Aprobación formal requerida.

EVENTO 10 — Contradicción documental.

## Registro de auditoría relacionado

REGISTRO 6 — Decisión.

REGISTRO 8 — Aprobación.

REGISTRO 16 — Contradicción documental.

## Notificación relacionada

TIPO 6 — Confirmación requerida.

TIPO 10 — Alerta de contradicción documental.

## Acción esperada del usuario

Registrar decisión o corregir estado.

## Resolución esperada

Si no existe DECISIÓN, el documento no debe tratarse como aprobado.

## Restricción

No se puede aprobar por inferencia.

---

# TIPO 5 — CONFLICTO DE CAMBIO

## Qué significa

Hay contradicción sobre si un cambio fue registrado, aplicado o integrado.

## Cuándo ocurre

Ejemplo:

```text
HOME dice cambio integrado.
CONTROL_DE_CAMBIOS no contiene el cambio.
```

## Riesgo típico

Nivel 2 a Nivel 3.

## Fuente que normalmente gana

ROBERT_CONTROL_DE_CAMBIOS.

## Modelo principal

ChangeRecord.

## Componente principal

CurrentStatePanel.

## Evento relacionado

EVENTO 9 — Falta de información.

EVENTO 10 — Contradicción documental.

## Registro de auditoría relacionado

REGISTRO 7 — Cambio.

REGISTRO 9 — Integración.

REGISTRO 16 — Contradicción documental.

## Notificación relacionada

TIPO 10 — Alerta de contradicción documental.

## Acción esperada del usuario

Registrar cambio faltante o corregir documento que afirma el cambio.

## Resolución esperada

Cambio debe existir en CONTROL_DE_CAMBIOS para tratarse como formal.

## Restricción

No asumir cambio registrado sin confirmación.

---

# TIPO 6 — CONFLICTO DE PERMISO

## Qué significa

Un documento permite algo que otro restringe o prohíbe.

## Cuándo ocurre

Ejemplo:

```text
Un documento dice: conectar Gmail.
PERMISSIONS_AND_SCOPES_SPEC dice: conexiones externas no autorizadas.
```

## Riesgo típico

Nivel 3 a Nivel 4.

## Fuente que normalmente gana

PERMISSIONS_AND_SCOPES_SPEC + SECURITY_RULES.

## Modelo principal

RiskRecord / PendingDecision.

## Componente principal

ApprovalGate.

## Evento relacionado

EVENTO 12 — Fuera de alcance.

EVENTO 16 — Conexión no autorizada.

## Registro de auditoría relacionado

REGISTRO 11 — Riesgo.

REGISTRO 12 — Permiso.

REGISTRO 16 — Contradicción documental.

## Notificación relacionada

TIPO 7 — Alerta de permiso insuficiente.

TIPO 9 — Mensaje de bloqueo.

## Acción esperada del usuario

Reducir alcance, documentar como futuro o aprobar fase correspondiente cuando sea permitido.

## Resolución esperada

Bloquear acción no autorizada.

## Restricción

Permiso dudoso se trata como permiso insuficiente.

---

# TIPO 7 — CONFLICTO DE ALCANCE

## Qué significa

Un documento intenta hacer más de lo autorizado.

## Cuándo ocurre

Ejemplo:

```text
Documento técnico conceptual empieza a autorizar prototipo real.
```

## Riesgo típico

Nivel 3.

Puede subir a Nivel 4 si intenta ejecución real.

## Fuente que normalmente gana

PERMISSIONS_AND_SCOPES_SPEC + PHASES + SECURITY_RULES.

## Modelo principal

RiskRecord.

## Componente principal

RiskBadge / ApprovalGate.

## Evento relacionado

EVENTO 12 — Fuera de alcance.

EVENTO 20 — Fase incorrecta si aplica.

## Registro de auditoría relacionado

REGISTRO 11 — Riesgo.

REGISTRO 13 — Alcance.

## Notificación relacionada

TIPO 8 — Alerta de alcance excedido.

## Acción esperada del usuario

Corregir documento o reducirlo a diseño conceptual.

## Resolución esperada

Eliminar o bloquear alcance excedido.

## Restricción

Alcance conceptual no autoriza ejecución real.

---

# TIPO 8 — CONFLICTO DE FASE

## Qué significa

Un documento intenta mover a Robert a una fase no autorizada.

## Cuándo ocurre

Ejemplo:

```text
Fase 10 documental intenta iniciar Fase 11 técnica real.
```

## Riesgo típico

Nivel 4 — Crítico.

## Fuente que normalmente gana

ROBERT_PHASES + SECURITY_RULES.

## Modelo principal

ModeState / RiskRecord.

## Componente principal

ModeSelector / ApprovalGate.

## Evento relacionado

EVENTO 20 — Fase incorrecta.

## Registro de auditoría relacionado

REGISTRO 11 — Riesgo.

REGISTRO 13 — Alcance.

REGISTRO 16 — Contradicción documental.

## Notificación relacionada

TIPO 11 — Alerta de fase incorrecta.

TIPO 9 — Mensaje de bloqueo.

## Acción esperada del usuario

Mantener Fase 10 o aprobar formalmente transición de fase en el futuro.

## Resolución esperada

Bloquear avance de fase.

## Restricción

Ningún documento técnico aprueba Fase 11 por sí mismo.

---

# TIPO 9 — CONFLICTO DE SEGURIDAD

## Qué significa

Un documento contradice reglas de seguridad.

## Cuándo ocurre

Ejemplo:

```text
Un documento permite ejecutar acciones importantes sin permiso.
```

## Riesgo típico

Nivel 4 — Crítico.

## Fuente que normalmente gana

ROBERT_SECURITY_RULES.

## Modelo principal

RiskRecord.

## Componente principal

ApprovalGate / RiskBadge.

## Evento relacionado

EVENTO 7 — Acción prohibida.

EVENTO 11 — Riesgo crítico.

## Registro de auditoría relacionado

REGISTRO 10 — Bloqueo.

REGISTRO 11 — Riesgo.

REGISTRO 16 — Contradicción documental.

## Notificación relacionada

TIPO 5 — Advertencia de riesgo.

TIPO 9 — Mensaje de bloqueo.

## Acción esperada del usuario

Corregir documento o bloquear acción.

## Resolución esperada

Seguridad gana.

## Restricción

No se negocia seguridad sin decisión formal futura.

---

# TIPO 10 — CONFLICTO DE MODELO

## Qué significa

Un documento usa modelos no aprobados como si fueran oficiales.

## Cuándo ocurre

Ejemplo:

```text
Documento crea ConflictRecord sin corregir DATA_MODEL_SPEC.
```

## Riesgo típico

Nivel 2 a Nivel 3.

## Fuente que normalmente gana

DATA_MODEL_SPEC v0.1.

## Modelo principal

RobertDocument / RiskRecord.

## Componente principal

DocumentStatusMap / ApprovalGate.

## Evento relacionado

EVENTO 12 — Fuera de alcance.

EVENTO 10 — Contradicción documental.

## Registro de auditoría relacionado

REGISTRO 11 — Riesgo.

REGISTRO 13 — Alcance.

REGISTRO 16 — Contradicción documental.

## Notificación relacionada

TIPO 8 — Alerta de alcance excedido.

TIPO 10 — Contradicción documental.

## Acción esperada del usuario

Eliminar modelo no aprobado o proponer corrección formal a DATA_MODEL_SPEC.

## Resolución esperada

No tratar modelo nuevo como oficial.

## Restricción

Este documento no crea modelos nuevos.

---

# TIPO 11 — CONFLICTO DE COMPONENTE

## Qué significa

Un documento usa componentes no aprobados como si fueran oficiales.

## Cuándo ocurre

Ejemplo:

```text
Documento crea ConflictPanel sin corregir COMPONENTS_SPEC.
```

## Riesgo típico

Nivel 2 a Nivel 3.

## Fuente que normalmente gana

COMPONENTS_SPEC v0.2.

## Modelo principal

ComponentState / RiskRecord.

## Componente principal

DocumentStatusMap / ApprovalGate.

## Evento relacionado

EVENTO 12 — Fuera de alcance.

EVENTO 10 — Contradicción documental.

## Registro de auditoría relacionado

REGISTRO 11 — Riesgo.

REGISTRO 13 — Alcance.

REGISTRO 16 — Contradicción documental.

## Notificación relacionada

TIPO 8 — Alerta de alcance excedido.

TIPO 10 — Contradicción documental.

## Acción esperada del usuario

Eliminar componente no aprobado o proponer corrección formal a COMPONENTS_SPEC.

## Resolución esperada

No tratar componente nuevo como oficial.

## Restricción

Este documento no crea componentes nuevos.

---

# TIPO 12 — CONFLICTO DE FLUJO

## Qué significa

Un documento define un flujo que contradice INTERACTION_FLOW_SPEC.

## Cuándo ocurre

Ejemplo:

```text
Documento salta aprobación y pasa directo a integración.
```

## Riesgo típico

Nivel 3.

## Fuente que normalmente gana

INTERACTION_FLOW_SPEC v0.2 + DOCUMENT_LIFECYCLE_SPEC v0.2.

## Modelo principal

SystemState / RiskRecord.

## Componente principal

CurrentStatePanel / ApprovalGate.

## Evento relacionado

EVENTO 3 — Aprobación formal requerida.

EVENTO 10 — Contradicción documental.

## Registro de auditoría relacionado

REGISTRO 11 — Riesgo.

REGISTRO 16 — Contradicción documental.

## Notificación relacionada

TIPO 10 — Contradicción documental.

## Acción esperada del usuario

Corregir flujo o pedir aprobación formal si aplica.

## Resolución esperada

Usar flujo aprobado.

## Restricción

No saltar aprobación, cambio, HOME o README cuando correspondan.

---

# TIPO 13 — CONFLICTO DE EVENTO

## Qué significa

Un documento usa eventos incorrectos o incompletos.

## Cuándo ocurre

Ejemplo:

```text
Un bloqueo por fase incorrecta no referencia EVENTO 20.
```

## Riesgo típico

Nivel 2 a Nivel 3.

## Fuente que normalmente gana

ERROR_AND_BLOCKING_SPEC v0.2.

## Modelo principal

RiskRecord.

## Componente principal

RiskBadge.

## Evento relacionado

EVENTO 10 — Contradicción documental.

El evento específico depende del caso.

## Registro de auditoría relacionado

REGISTRO 11 — Riesgo.

REGISTRO 16 — Contradicción documental.

## Notificación relacionada

TIPO 10 — Contradicción documental.

## Acción esperada del usuario

Corregir evento o tabla de relación.

## Resolución esperada

Alinear con ERROR_AND_BLOCKING_SPEC.

## Restricción

Evento omitido puede causar bloqueo incorrecto.

---

# TIPO 14 — CONFLICTO DE AUDITORÍA

## Qué significa

Un documento usa registros de auditoría incorrectos o incompletos.

## Cuándo ocurre

Ejemplo:

```text
Una corrección no referencia REGISTRO 5 — Corrección.
```

## Riesgo típico

Nivel 2 a Nivel 3.

## Fuente que normalmente gana

AUDIT_TRAIL_SPEC v0.2.

## Modelo principal

ChangeRecord / RiskRecord.

## Componente principal

CurrentStatePanel.

## Evento relacionado

EVENTO 10 — Contradicción documental.

## Registro de auditoría relacionado

REGISTRO 16 — Contradicción documental.

El registro específico depende del caso.

## Notificación relacionada

TIPO 10 — Contradicción documental.

## Acción esperada del usuario

Corregir registros faltantes.

## Resolución esperada

Alinear con AUDIT_TRAIL_SPEC.

## Restricción

Auditoría incompleta impide trazabilidad completa.

---

# TIPO 15 — CONFLICTO DE EJECUCIÓN NO AUTORIZADA

## Qué significa

Un documento o solicitud intenta convertir diseño documental en ejecución real.

## Cuándo ocurre

Ejemplo:

```text
Crear documento técnico y al mismo tiempo conectar una API real.
```

## Riesgo típico

Nivel 4 — Crítico.

## Fuente que normalmente gana

SECURITY_RULES + PHASES + PERMISSIONS_AND_SCOPES_SPEC.

## Modelo principal

RiskRecord / ModeState.

## Componente principal

ApprovalGate.

## Evento relacionado

EVENTO 15 — Ejecución no autorizada.

EVENTO 16 — Conexión no autorizada.

EVENTO 17 — Automatización no autorizada.

EVENTO 18 — Agente no autorizado.

## Registro de auditoría relacionado

REGISTRO 10 — Bloqueo.

REGISTRO 11 — Riesgo.

REGISTRO 13 — Alcance.

## Notificación relacionada

TIPO 9 — Mensaje de bloqueo.

TIPO 12 — Capacidad futura no disponible si aplica.

## Acción esperada del usuario

Mantenerlo como documentación futura o cancelar.

## Resolución esperada

Bloquear ejecución real.

## Restricción

Fase 10 no autoriza ejecución real.

---

# TIPO 16 — CONFLICTO DE FUENTE VIGENTE

## Qué significa

No está claro cuál documento o versión es la fuente vigente.

## Cuándo ocurre

Ejemplo:

```text
Dos versiones aparecen como vigentes.
```

## Riesgo típico

Nivel 3.

## Fuente que normalmente gana

VERSIONING_AND_CHANGE_POLICY_SPEC + DOCUMENT_LIFECYCLE_SPEC + DECISIONS_LOG + CONTROL_DE_CAMBIOS.

## Modelo principal

RobertDocument / SystemState.

## Componente principal

DocumentStatusMap.

## Evento relacionado

EVENTO 9 — Falta de información.

EVENTO 10 — Contradicción documental.

## Registro de auditoría relacionado

REGISTRO 7 — Cambio.

REGISTRO 9 — Integración.

REGISTRO 16 — Contradicción documental.

## Notificación relacionada

TIPO 10 — Contradicción documental.

TIPO 4 — Falta de información si aplica.

## Acción esperada del usuario

Identificar fuente vigente o registrar corrección.

## Resolución esperada

Definir versión vigente y marcar otra como histórica, reemplazada, depreciada o archivada.

## Restricción

Robert no debe elegir fuente vigente sin trazabilidad.

---

# TIPO 17 — CONFLICTO DE TRAZABILIDAD INSUFICIENTE

## Qué significa

No hay suficiente registro para saber qué ocurrió.

## Cuándo ocurre

Ejemplo:

```text
El usuario dice “ya”, pero no existe último paso claro.
```

O:

```text
Documento aparece aprobado, pero falta DECISIÓN.
```

## Riesgo típico

Nivel 2 a Nivel 3.

Puede subir a Nivel 4 si podría activar ejecución no autorizada.

## Fuente que normalmente gana

SESSION_AND_CONTEXT_SPEC v0.2 + AUDIT_TRAIL_SPEC v0.2.

## Modelo principal

PendingDecision / SystemState.

## Componente principal

CurrentStatePanel / ApprovalGate.

## Evento relacionado

EVENTO 9 — Falta de información.

EVENTO 10 — Contradicción documental si aplica.

## Registro de auditoría relacionado

REGISTRO 3 — Revisión.

REGISTRO 16 — Contradicción documental si aplica.

## Notificación relacionada

TIPO 4 — Falta de información.

TIPO 10 — Contradicción documental si aplica.

## Acción esperada del usuario

Confirmar estado, registrar faltante o pausar.

## Resolución esperada

Pedir confirmación explícita.

## Restricción

Sin trazabilidad, no avanzar.

---

# TABLA DE PRIORIDAD ENTRE FUENTES

| Conflicto | Fuente que gana primero | Fuente secundaria | Acción |
|---|---|---|---|
| Seguridad vs comodidad | SECURITY_RULES | PERMISSIONS_AND_SCOPES_SPEC | Bloquear si hay riesgo |
| Fase actual vs fase futura | PHASES | SECURITY_RULES | Bloquear avance |
| Permiso vs solicitud | PERMISSIONS_AND_SCOPES_SPEC | USER_ACTIONS_SPEC | Pedir permiso o bloquear |
| Aprobación dudosa | DECISIONS_LOG | CONTROL_DE_CAMBIOS | No aprobar por inferencia |
| Cambio dudoso | CONTROL_DE_CAMBIOS | HOME / README | Registrar o corregir |
| Versión vigente dudosa | VERSIONING_AND_CHANGE_POLICY_SPEC | DOCUMENT_LIFECYCLE_SPEC | Revisar decisión/cambio |
| Estado documental dudoso | DOCUMENT_LIFECYCLE_SPEC | SESSION_AND_CONTEXT_SPEC | Revisar trazabilidad |
| Evento dudoso | ERROR_AND_BLOCKING_SPEC | NOTIFICATION_AND_ALERTS_SPEC | Corregir evento |
| Auditoría dudosa | AUDIT_TRAIL_SPEC | CONTROL_DE_CAMBIOS | Corregir registro |
| Modelo dudoso | DATA_MODEL_SPEC | Documento técnico relacionado | No crear modelo nuevo |
| Componente dudoso | COMPONENTS_SPEC | SCREEN_STATE_SPEC | No crear componente nuevo |
| HOME vs README | DECISIONS_LOG / CONTROL_DE_CAMBIOS | Documento técnico vigente | Corregir el que esté mal |

---

# MATRIZ DE SEVERIDAD DE CONFLICTOS

| Severidad | Descripción | Riesgo típico | Acción |
|---|---|---|---|
| Menor | Diferencia de redacción o formato | Nivel 1 | Corregir si conviene |
| Media | Diferencia de estado, versión o referencia | Nivel 2 | Revisar y corregir |
| Alta | Afecta aprobación, cambio, permiso o alcance | Nivel 3 | Pausar y pedir decisión |
| Crítica | Afecta seguridad, fase, ejecución o autonomía | Nivel 4 | Bloquear |

---

# REGLA DE RESOLUCIÓN PASO A PASO

Cuando Robert detecta conflicto, debe seguir este orden:

1. Identificar los documentos en conflicto.
2. Identificar el tipo de conflicto.
3. Identificar la versión vigente de cada documento.
4. Revisar DECISIONS_LOG.
5. Revisar CONTROL_DE_CAMBIOS.
6. Revisar SECURITY_RULES si afecta seguridad.
7. Revisar PHASES si afecta fase.
8. Revisar PERMISSIONS_AND_SCOPES_SPEC si afecta permiso.
9. Revisar DOCUMENT_LIFECYCLE_SPEC si afecta estado.
10. Revisar VERSIONING_AND_CHANGE_POLICY_SPEC si afecta versión.
11. Determinar si se puede corregir o si debe bloquearse.
12. Pedir confirmación si falta información.
13. Registrar corrección si aplica.
14. Actualizar HOME si aplica.
15. Actualizar README si aplica.
16. No avanzar hasta resolver conflicto crítico.

---

# RELACIÓN CON VERSIONING_AND_CHANGE_POLICY_SPEC v0.2

VERSIONING_AND_CHANGE_POLICY_SPEC define qué versión es vigente, histórica, reemplazada, depreciada o archivada.

DATA_CONSISTENCY_AND_CONFLICT_RESOLUTION_SPEC define qué hacer cuando esas versiones se contradicen.

Regla:

**La versión más nueva no gana automáticamente. Gana la versión aprobada, integrada y vigente según trazabilidad.**

---

# RELACIÓN CON DOCUMENT_LIFECYCLE_SPEC v0.2

DOCUMENT_LIFECYCLE_SPEC define estados documentales.

DATA_CONSISTENCY_AND_CONFLICT_RESOLUTION_SPEC define qué hacer cuando los estados documentales se contradicen.

Ejemplo:

```text
Un documento no puede estar al mismo tiempo:
Aprobado e integrado
y
Pendiente de revisión
como estado vigente.
```

Debe resolverse revisando DECISIONS_LOG y CONTROL_DE_CAMBIOS.

---

# RELACIÓN CON SESSION_AND_CONTEXT_SPEC v0.2

SESSION_AND_CONTEXT_SPEC define continuidad y contexto activo.

DATA_CONSISTENCY_AND_CONFLICT_RESOLUTION_SPEC define qué hacer cuando el contexto activo contradice los documentos.

Regla:

**Si el contexto de sesión contradice la trazabilidad documental, Robert debe pausar y revisar.**

---

# RELACIÓN CON AUDIT_TRAIL_SPEC v0.2

AUDIT_TRAIL_SPEC define registros.

Este documento usa especialmente:

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
- REGISTRO 16 — Contradicción documental.
- REGISTRO 17 — Capacidad futura no disponible.

Regla:

**Toda contradicción relevante debe poder rastrearse o corregirse.**

---

# RELACIÓN CON NOTIFICATION_AND_ALERTS_SPEC v0.2

NOTIFICATION_AND_ALERTS_SPEC define qué aviso mostrar.

Este documento define cuándo mostrar avisos por conflicto.

Ejemplos:

- Falta de información → TIPO 4.
- Riesgo crítico → TIPO 5.
- Confirmación requerida → TIPO 6.
- Permiso insuficiente → TIPO 7.
- Alcance excedido → TIPO 8.
- Bloqueo → TIPO 9.
- Contradicción documental → TIPO 10.
- Fase incorrecta → TIPO 11.
- Capacidad futura no disponible → TIPO 12.

---

# RELACIÓN CON ERROR_AND_BLOCKING_SPEC v0.2

Este documento usa especialmente:

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

**Conflicto crítico debe activar bloqueo o pausa obligatoria.**

---

# RELACIÓN CON PERMISSIONS_AND_SCOPES_SPEC v0.2

PERMISSIONS_AND_SCOPES_SPEC define permisos y alcances.

Este documento define qué pasa si otro documento contradice esos permisos.

Regla:

**Si un permiso está en duda, se trata como no concedido.**

---

# RELACIÓN CON USER_ACTIONS_SPEC v0.2

| Acción del usuario | Resultado si hay conflicto |
|---|---|
| Crear documento | Permitido si no contradice fase ni alcance |
| Corregir documento | Permitido como corrección documental |
| Aprobar documento | Bloqueado si hay contradicción crítica |
| Registrar decisión | Permitido si el alcance es claro |
| Registrar cambio | Permitido si el cambio está identificado |
| Actualizar HOME | Permitido si se sabe qué estado es correcto |
| Actualizar README | Permitido si se sabe qué estado es correcto |
| Solicitar pausa | Siempre permitido como acción de control |
| Solicitar bloqueo manual | Siempre permitido como acción de control |
| Pedir siguiente paso | Debe resolver conflicto primero si es crítico |

---

# RELACIÓN CON DATA_MODEL_SPEC v0.1

Este documento no crea modelos nuevos.

Usa:

- RobertDocument para documentos en conflicto.
- ChangeRecord para cambios contradictorios.
- DecisionRecord para aprobaciones.
- PendingDecision para dudas o faltantes.
- SystemState para estado general.
- RiskRecord para severidad.
- CommandRequest para solicitud del usuario.
- ModeState para pausa, bloqueo o modo activo.
- ComponentState para visualización conceptual.
- GitHubBackupStatus para respaldo manual.
- ObsidianGraphStatus para ubicación documental.

---

# RELACIÓN CON COMPONENTS_SPEC v0.2

Este documento no crea componentes nuevos.

Usa:

- ApprovalGate para bloquear.
- RiskBadge para mostrar riesgo.
- CurrentStatePanel para mostrar conflicto.
- DocumentStatusMap para mostrar documentos afectados.
- DecisionInbox para decisiones pendientes.
- CommandCenter para recibir corrección o confirmación.
- TopBar para mostrar pausa o bloqueo.
- LeftSidebar para ubicar documentos relacionados.

---

# RELACIÓN CON SCREEN_STATE_SPEC v0.2

SCREEN_STATE_SPEC define cómo se ve el estado.

Este documento define qué debe verse cuando hay conflicto.

Ejemplo:

```text
Estado: Bloqueado por contradicción documental
Documento A: HOME
Documento B: README
Fuente de resolución: DECISIONS_LOG + CONTROL_DE_CAMBIOS
Acción requerida: Corregir README
```

---

# RELACIÓN CON INTERACTION_FLOW_SPEC v0.2

INTERACTION_FLOW_SPEC define flujo.

Este documento define cuándo detener flujo por conflicto.

Regla:

**Un flujo no puede continuar si depende de información contradictoria crítica.**

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

- Verificación automática de conflictos.
- Sincronización automática.
- Corrección automática.
- Commits automáticos.
- Agentes que modifiquen archivos.

---

# FORMATO MÍNIMO DE REPORTE DE CONFLICTO

Todo conflicto importante debe poder mostrar:

```text
Tipo de conflicto:
Documentos involucrados:
Versiones involucradas:
Estado de cada documento:
Fuente que normalmente gana:
Decisión relacionada:
Cambio relacionado:
Evento relacionado:
Registro de auditoría relacionado:
Riesgo:
Acción recomendada:
Acción bloqueada:
Resolución esperada:
Restricción:
```

---

# EJEMPLO DE REPORTE DE CONFLICTO

```text
Tipo de conflicto: Conflicto de estado
Documento A: ROBERT_HOME
Documento B: README
Conflicto: HOME dice pendiente; README dice aprobado
Fuente que gana: DECISIONS_LOG + CONTROL_DE_CAMBIOS
Evento relacionado: EVENTO 10 — Contradicción documental
Registro relacionado: REGISTRO 16 — Contradicción documental
Riesgo: Nivel 2
Acción recomendada: Revisar DECISIÓN y CAMBIO relacionados
Acción bloqueada: Aprobar de nuevo sin verificar trazabilidad
Resolución esperada: Corregir el documento que tenga estado incorrecto
Restricción: No avanzar hasta confirmar estado vigente
```

---

# CRITERIOS DE ACEPTACIÓN

Este documento podrá considerarse listo para aprobación si:

- Define consistencia documental.
- Define contradicción documental.
- Define inconsistencia menor.
- Define inconsistencia mayor.
- Define conflicto crítico.
- Define jerarquía conceptual de fuentes.
- Define prioridad del usuario.
- Define prioridad de SECURITY_RULES.
- Define prioridad de documento aprobado sobre borrador.
- Define prioridad de versión vigente sobre versión histórica.
- Define prioridad de DECISIONS_LOG.
- Define prioridad de CONTROL_DE_CAMBIOS.
- Define regla HOME vs README.
- Define 17 tipos de conflicto documental.
- Incluye estructura uniforme de los 17 tipos.
- Define fuente que normalmente gana por tipo.
- Define riesgo típico por tipo.
- Define evento relacionado por tipo.
- Define registro de auditoría relacionado por tipo.
- Define notificación relacionada por tipo.
- Define resolución esperada por tipo.
- Define tabla de prioridad entre fuentes.
- Define matriz de severidad.
- Define regla de resolución paso a paso.
- Define relación con VERSIONING_AND_CHANGE_POLICY_SPEC v0.2.
- Define relación con DOCUMENT_LIFECYCLE_SPEC v0.2.
- Define relación con SESSION_AND_CONTEXT_SPEC v0.2.
- Define relación con AUDIT_TRAIL_SPEC v0.2.
- Define relación con NOTIFICATION_AND_ALERTS_SPEC v0.2.
- Define relación con ERROR_AND_BLOCKING_SPEC v0.2.
- Define relación con PERMISSIONS_AND_SCOPES_SPEC v0.2.
- Define relación con USER_ACTIONS_SPEC v0.2.
- Define relación con DATA_MODEL_SPEC v0.1.
- Define relación con COMPONENTS_SPEC v0.2.
- Define relación con SCREEN_STATE_SPEC v0.2.
- Define relación con INTERACTION_FLOW_SPEC v0.2.
- Aclara que no crea ConflictRecord.
- Aclara que no crea ConsistencyCheckRecord.
- Aclara que no crea ConflictResolutionRecord.
- Aclara que no crea ConflictPanel.
- Aclara que no crea ConsistencyMap.
- Aclara que no automatiza GitHub.
- Aclara que no automatiza Obsidian.
- Mantiene a Robert en Fase 10.
- Mantiene Nivel 0 únicamente como Informativo.
- Mantiene acciones de control fuera de la escala de riesgo.
- Mantiene control total del usuario.

---

# RIESGO DEL DOCUMENTO

Tipo de cambio:

**Cambio técnico documental / consistencia documental y resolución conceptual de conflictos**

Nivel de riesgo inicial:

**Nivel 3 — Alto**

Motivo:

Este documento define cómo Robert detecta contradicciones, prioriza fuentes, bloquea acciones por conflictos y resuelve inconsistencias documentales.

Nivel de riesgo final esperado:

**Nivel 2 — Medio**

Motivo de reducción:

El documento es documental. No crea sistema real de validación automática, no crea base de datos real, no crea modelos nuevos oficiales, no crea componentes nuevos oficiales, no conecta herramientas externas y no ejecuta acciones.

Nivel de autonomía:

**Nivel 0 — Sin autonomía ejecutiva**

---

# DECISIÓN PENDIENTE

Este documento queda como:

**Borrador técnico documental pendiente de revisión**

Para aprobarlo formalmente, el usuario deberá escribir:

**APRUEBO ROBERT_TECHNICAL_DATA_CONSISTENCY_AND_CONFLICT_RESOLUTION_SPEC v0.1**

---

# EFECTO DE UNA APROBACIÓN FUTURA

Si se aprueba este documento, se deberá:

1. Registrar decisión formal en ROBERT_DECISIONS_LOG.
2. Registrar cambio en ROBERT_CONTROL_DE_CAMBIOS.
3. Actualizar ROBERT_HOME.
4. Actualizar README si aplica.
5. Mantenerlo como base para futuras especificaciones técnicas.
6. No crear sistema real de consistencia documental.
7. No crear base de datos real.
8. No crear resolución automática de conflictos.
9. No conectar GitHub automáticamente.
10. No conectar Obsidian automáticamente.
11. No pasar automáticamente a programación.
12. No avanzar automáticamente a Fase 11.

---

# PRÓXIMO PASO RECOMENDADO

Después de revisar este documento, el siguiente documento posible sería:

**ROBERT_TECHNICAL_APPROVAL_AND_AUTHORIZATION_GATE_SPEC**

Ese documento definiría con más precisión cómo Robert bloquea acciones que requieren aprobación, cómo se valida autorización explícita y qué pasa cuando una aprobación es parcial, ambigua o revocada.

No debe crearse hasta revisar o aprobar DATA_CONSISTENCY_AND_CONFLICT_RESOLUTION_SPEC.

---

# CIERRE

ROBERT_TECHNICAL_DATA_CONSISTENCY_AND_CONFLICT_RESOLUTION_SPEC v0.1 define reglas conceptuales para consistencia documental, contradicciones, conflictos, prioridad entre fuentes, resolución de inconsistencias y bloqueos por información contradictoria.

Este documento mantiene a Robert en modo documental, manual y supervisado.

El usuario mantiene control total.

Robert no ejecuta acciones importantes sin permiso.
