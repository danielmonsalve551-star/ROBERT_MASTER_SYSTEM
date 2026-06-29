# ROBERT_TECHNICAL_MVP_WIREFRAME_v0.3_PROPUESTA

Versión: 0.3
Estado: Propuesta pendiente de revisión y aprobación
Fecha: 29/06/2026
Ubicación: 10_MVP
Documento base relacionado: ROBERT_TECHNICAL_MVP_WIREFRAME v0.2

---

# OBJETIVO

Este documento propone una mejora visual y funcional para el wireframe del MVP técnico básico de Robert.

La versión v0.3 no reemplaza automáticamente al wireframe aprobado v0.2.

Su función es presentar mejoras para revisión antes de integrarlas oficialmente.

---

# ESTADO ACTUAL

Robert ya cuenta con:

* MVP manual validado
* Sandbox manual validado
* ROBERT_TECHNICAL_MVP_PLAN aprobado
* ROBERT_TECHNICAL_MVP_WIREFRAME v0.2 aprobado
* ROBERT_CONTROL_DE_CAMBIOS aprobado
* Repositorio privado en GitHub iniciado como respaldo documental

Esta propuesta pertenece a la fase:

**Fase 10 — MVP técnico básico**

---

# REGLA CENTRAL

El usuario manda.

Robert no ejecuta acciones importantes sin permiso.

Esta propuesta no autoriza programación, conexiones reales, automatizaciones ni ejecución externa.

---

# TIPO DE CAMBIO

Tipo de cambio:

**Tipo 3 — Cambio visual / UX**

Motivo:

La propuesta modifica la forma en que el usuario verá riesgos, decisiones pendientes y estado documental dentro del MVP técnico básico.

---

# NIVEL DE RIESGO

Nivel inicial de riesgo:

**Nivel 2 — Medio**

Motivo del riesgo:

Aunque no ejecuta acciones reales, modifica la estructura visual del wireframe aprobado y puede afectar cómo se interpreta el estado de riesgo, aprobación y avance del sistema.

---

# DOCUMENTOS AFECTADOS

Documentos relacionados:

* ROBERT_TECHNICAL_MVP_WIREFRAME
* ROBERT_TECHNICAL_MVP_PLAN
* ROBERT_CONTROL_DE_CAMBIOS
* ROBERT_SECURITY_RULES
* ROBERT_DECISIONS_LOG
* ROBERT_HOME

---

# PROPUESTA GENERAL

Agregar tres mejoras principales al wireframe técnico de Robert:

1. RiskBadge con motivo visible
2. Vista “Pendiente de mi decisión”
3. Mapa visual de documentos por fase y estado

Estas mejoras buscan que Robert sea más claro, más seguro y más fácil de controlar por el usuario.

---

# MEJORA 1 — RISKBADGE CON MOTIVO VISIBLE

## Descripción

Cada acción, documento, comando o cambio mostrado en el MVP técnico deberá incluir un indicador visible de riesgo.

Este indicador no solo mostrará el nivel de riesgo, sino también el motivo.

---

## Objetivo

Evitar que el usuario vea únicamente:

“Riesgo Nivel 3”

sin entender por qué.

Robert debe explicar de forma simple el motivo del riesgo antes de continuar.

---

## Estructura visual propuesta

Ejemplo:

```text
Riesgo: Nivel 3 — Alto
Motivo: Esta acción modifica un documento aprobado y puede cambiar reglas activas del sistema.
Estado: Requiere aprobación del usuario
```

---

## Niveles permitidos

Robert solo usará la escala oficial:

* Nivel 1 — Bajo
* Nivel 2 — Medio
* Nivel 3 — Alto
* Nivel 4 — Crítico

No existe Nivel 5.

“No permitido” no es un nivel de riesgo.

“No permitido” es un estado de resultado.

---

## Regla nueva propuesta

Todo riesgo visible debe incluir:

* Nivel de riesgo
* Nombre del riesgo
* Motivo del riesgo
* Estado de aprobación
* Acción recomendada

---

## Ejemplo aplicado

```text
Acción: Actualizar ROBERT_SECURITY_RULES
Riesgo: Nivel 4 — Crítico
Motivo: Cambia reglas centrales de seguridad y autorización.
Estado: Aprobación obligatoria del usuario.
Acción recomendada: Revisar, corregir y aprobar formalmente antes de actualizar.
```

---

# MEJORA 2 — VISTA “PENDIENTE DE MI DECISIÓN”

## Descripción

Crear una vista especial dentro del MVP técnico donde Robert agrupe todo lo que necesita decisión directa del usuario.

Nombre técnico sugerido:

**DecisionInbox**

Nombre visible para el usuario:

**Pendiente de mi decisión**

---

## Objetivo

Evitar que las decisiones importantes queden perdidas dentro de conversaciones largas, documentos, pruebas o cambios pendientes.

Robert debe mostrar claramente qué necesita aprobación, rechazo, pausa o corrección.

---

## Elementos que deben aparecer en esta vista

La vista “Pendiente de mi decisión” debe incluir elementos con estados como:

* Aprobación requerida
* Pendiente de revisión
* Parcial
* Parcial avanzada
* Inconclusa
* En conflicto
* Bloqueado por dependencia
* Borrador pendiente de aprobación
* Cambio pendiente
* Riesgo alto pendiente
* Riesgo crítico pendiente

---

## Estructura visual propuesta

```text
PENDIENTE DE MI DECISIÓN

1. ROBERT_TECHNICAL_MVP_WIREFRAME_v0.3_PROPUESTA
   Estado: Pendiente de aprobación
   Riesgo: Nivel 2 — Medio
   Motivo: Modifica estructura visual del MVP técnico.
   Opciones: Aprobar / Corregir / Pausar / Rechazar

2. Cambio en SECURITY_RULES
   Estado: Requiere revisión
   Riesgo: Nivel 4 — Crítico
   Motivo: Puede modificar reglas centrales del sistema.
   Opciones: Revisar / Bloquear / Aprobar
```

---

## Acciones permitidas desde esta vista

El usuario podrá decidir:

* Aprobar
* Rechazar
* Pausar
* Corregir
* Pedir resumen
* Pedir comparación
* Bloquear
* Mandar a archivo

---

## Regla de seguridad

Robert no podrá aprobar automáticamente elementos dentro de esta vista.

Solo el usuario puede cerrar una decisión importante.

---

# MEJORA 3 — MAPA VISUAL DE DOCUMENTOS POR FASE Y ESTADO

## Descripción

Crear una vista tipo mapa documental donde se vea el estado de los documentos principales de Robert.

Nombre técnico sugerido:

**DocumentStatusMap**

Nombre visible para el usuario:

**Mapa de documentos**

---

## Objetivo

Que el usuario pueda ver rápidamente:

* Qué documentos existen
* Qué documentos están aprobados
* Qué documentos están pendientes
* Qué documentos están en borrador
* Qué documentos están bloqueados
* Qué documentos pertenecen a cada fase

---

# AGRUPACIÓN PROPUESTA

## DOCUMENTAL / BASE

```text
00_HOME
- ROBERT_HOME.md
  Estado: Aprobado

01_CONTEXT
- ROBERT_CONTEXT_MASTER.md
  Estado: Aprobado

02_COMMANDS
- ROBERT_COMMANDS.md
  Estado: Aprobado

03_DECISIONS
- ROBERT_DECISIONS_LOG.md
  Estado: Activo

04_SECURITY
- ROBERT_SECURITY_RULES.md
  Estado: Aprobado

- ROBERT_CONTROL_DE_CAMBIOS.md
  Estado: Aprobado
```

---

## ESTRUCTURA DEL SISTEMA

```text
05_PHASES
- ROBERT_PHASES.md
  Estado: Aprobado

06_MODULES
- ROBERT_MODULES.md
  Estado: Aprobado

07_VISUAL
- ROBERT_VISUAL.md
  Estado: En desarrollo / referencia visual

08_PROMPTS
- ROBERT_PROMPTS.md
  Estado: Activo

09_ARCHITECTURE
- ROBERT_SYSTEM_ARCHITECTURE.md
  Estado: Aprobado
```

---

## MVP TÉCNICO

```text
10_MVP
- ROBERT_MVP_PLAN.md
  Estado: Aprobado

- ROBERT_TECHNICAL_MVP_PLAN.md
  Estado: Aprobado

- ROBERT_TECHNICAL_MVP_WIREFRAME.md
  Estado: Aprobado

- ROBERT_TECHNICAL_MVP_WIREFRAME_v0.3_PROPUESTA.md
  Estado: Propuesta pendiente de aprobación
```

---

## SANDBOX

```text
15_SANDBOX
- ROBERT_SANDBOX.md
  Estado: Validado

- SANDBOX_RULES.md
  Estado: Aprobado

- SANDBOX_TESTS.md
  Estado: Completado

- SANDBOX_RESULTS.md
  Estado: Completado
```

---

# ESTADOS VISUALES PROPUESTOS

Robert podrá usar estos estados visuales:

```text
✓ Aprobado
⏳ Pendiente
📝 Borrador
⚠️ En revisión
⛔ Bloqueado
🔁 Reemplazado
📦 Archivado
🧪 En prueba
🔒 Protegido
```

---

# EJEMPLO DE MAPA VISUAL

```text
ROBERT DOCUMENT STATUS MAP

✓ 00_HOME / ROBERT_HOME
✓ 01_CONTEXT / ROBERT_CONTEXT_MASTER
✓ 02_COMMANDS / ROBERT_COMMANDS
✓ 03_DECISIONS / ROBERT_DECISIONS_LOG
✓ 04_SECURITY / ROBERT_SECURITY_RULES
✓ 04_SECURITY / ROBERT_CONTROL_DE_CAMBIOS
✓ 05_PHASES / ROBERT_PHASES
✓ 06_MODULES / ROBERT_MODULES
⚠️ 07_VISUAL / ROBERT_VISUAL
✓ 08_PROMPTS / ROBERT_PROMPTS
✓ 09_ARCHITECTURE / ROBERT_SYSTEM_ARCHITECTURE
✓ 10_MVP / ROBERT_MVP_PLAN
✓ 10_MVP / ROBERT_TECHNICAL_MVP_PLAN
✓ 10_MVP / ROBERT_TECHNICAL_MVP_WIREFRAME
⏳ 10_MVP / ROBERT_TECHNICAL_MVP_WIREFRAME_v0.3_PROPUESTA
✓ 15_SANDBOX / ROBERT_SANDBOX
✓ 15_SANDBOX / SANDBOX_RULES
✓ 15_SANDBOX / SANDBOX_TESTS
✓ 15_SANDBOX / SANDBOX_RESULTS
```

---

# BENEFICIOS DE LA PROPUESTA

Estas mejoras ayudan a Robert a ser:

* Más claro
* Más seguro
* Más visual
* Más fácil de controlar
* Menos confuso en sesiones largas
* Más útil para revisar decisiones
* Más preparado para un MVP técnico real

---

# LO QUE ESTA PROPUESTA NO AUTORIZA

Esta propuesta no autoriza:

* Programar la app
* Conectar Gmail
* Conectar Google Calendar
* Conectar APIs reales
* Automatizar acciones
* Enviar correos
* Modificar archivos automáticamente
* Ejecutar decisiones legales, fiscales o financieras
* Activar agentes autónomos

---

# CONDICIONES PARA APROBACIÓN

Para aprobar esta propuesta, el usuario debe escribir una aprobación formal, por ejemplo:

```text
APRUEBO ROBERT_TECHNICAL_MVP_WIREFRAME v0.3
```

Después de la aprobación, se deberá:

1. Registrar la decisión en ROBERT_DECISIONS_LOG
2. Actualizar ROBERT_TECHNICAL_MVP_WIREFRAME
3. Actualizar ROBERT_HOME si cambia el estado general
4. Actualizar ROBERT_CONTROL_DE_CAMBIOS si aplica
5. Mantener la versión anterior como referencia

---

# DECISIÓN PENDIENTE

Estado actual:

```text
Pendiente de revisión y aprobación del usuario.
```

Opciones disponibles:

```text
APROBAR
CORREGIR
PAUSAR
RECHAZAR
ARCHIVAR
```

---

# CIERRE

ROBERT_TECHNICAL_MVP_WIREFRAME_v0.3_PROPUESTA es una mejora visual y funcional para hacer el MVP técnico básico más claro, seguro y controlable.

La propuesta mantiene la regla central:

El usuario manda.

Robert no ejecuta acciones importantes sin permiso.
