# ROBERT_TECHNICAL_COMPONENTS_SPEC

Versión: 0.1
Estado: Borrador técnico inicial pendiente de revisión
Fecha: 29/06/2026
Ubicación: 10_MVP
Documento base relacionado: ROBERT_TECHNICAL_MVP_WIREFRAME v0.3
Fase: Fase 10 — MVP técnico básico en preparación

---

# OBJETIVO

Este documento convierte el wireframe técnico v0.3 de Robert en una especificación inicial de componentes técnicos.

Su función es definir qué partes visuales y funcionales tendría el MVP técnico básico antes de programar.

Este documento no programa la app.

Este documento no conecta herramientas reales.

Este documento no automatiza acciones.

Este documento solo prepara la estructura técnica para una futura fase de desarrollo.

---

# REGLA CENTRAL

El usuario manda.

Robert no ejecuta acciones importantes sin permiso.

Ningún componente puede ejecutar acciones reales sin autorización explícita del usuario.

---

# ESTADO ACTUAL DEL PROYECTO

Robert se encuentra en:

**Fase 10 — MVP técnico básico en preparación**

Estado operativo:

* MVP manual validado
* Sandbox manual validado
* GitHub configurado como respaldo documental privado
* ROBERT_TECHNICAL_MVP_PLAN aprobado
* ROBERT_TECHNICAL_MVP_WIREFRAME v0.3 aprobado
* ROBERT_HOME actualizado
* ROBERT_CONTROL_DE_CAMBIOS actualizado
* Sin programación autorizada todavía
* Sin conexiones reales
* Sin automatizaciones reales

---

# PROPÓSITO DE ESTA ESPECIFICACIÓN

Esta especificación sirve para responder:

* Qué componentes necesita Robert
* Qué debe mostrar cada componente
* Qué datos necesita cada componente
* Qué acciones puede permitir cada componente
* Qué acciones debe bloquear
* Qué reglas de seguridad debe respetar
* Qué flujo seguirá el MVP técnico básico

---

# ALCANCE AUTORIZADO

Este documento autoriza únicamente:

* Diseñar componentes técnicos
* Definir nombres de componentes
* Definir estructura visual
* Definir estados
* Definir datos internos simulados
* Definir reglas de interacción
* Preparar una base para futura programación

---

# ALCANCE NO AUTORIZADO

Este documento no autoriza:

* Programar la app
* Conectar Gmail
* Conectar Google Calendar
* Conectar GitHub automáticamente
* Conectar APIs reales
* Crear agentes autónomos
* Automatizar acciones reales
* Enviar correos
* Modificar archivos automáticamente
* Ejecutar decisiones fiscales, legales o financieras
* Usar datos sensibles reales

---

# PRINCIPIOS TÉCNICOS DEL MVP

El MVP técnico básico debe ser:

* Manual primero
* Visualmente claro
* Seguro por defecto
* Modular
* Fácil de auditar
* Fácil de pausar
* Fácil de revisar
* Sin ejecución externa real
* Sin permisos peligrosos
* Sin automatización oculta

---

# MODOS OPERATIVOS

Robert debe manejar tres modos principales:

## 1. MODO_MANUAL

El usuario controla todo.

Robert solo organiza, muestra, resume y prepara información.

No ejecuta acciones externas.

---

## 2. MODO_SUPERVISADO

Robert puede:

* Revisar
* Proponer
* Detectar riesgos
* Preparar borradores
* Sugerir cambios
* Marcar decisiones pendientes

Robert no puede:

* Aprobar automáticamente
* Ejecutar acciones reales
* Modificar documentos sin permiso
* Conectar herramientas reales

---

## 3. MODO_SANDBOX

Robert puede simular procesos sin afectar nada real.

Se usa para pruebas, flujos, escenarios y validación.

Robert no puede ejecutar acciones fuera del entorno simulado.

---

# ESCALA OFICIAL DE RIESGO

Robert solo usará esta escala:

* Nivel 1 — Bajo
* Nivel 2 — Medio
* Nivel 3 — Alto
* Nivel 4 — Crítico

No existe Nivel 5.

“No permitido” no es nivel de riesgo.

“No permitido” es estado de resultado.

---

# ESTADOS GENERALES DEL SISTEMA

Estados permitidos:

* Borrador
* En revisión
* Pendiente de aprobación
* Aprobado
* Rechazado
* Pausado
* Bloqueado
* No permitido
* Parcial
* Parcial avanzada
* Inconclusa
* Interrumpida
* Fallida
* Archivada
* Reemplazada

---

# COMPONENTES PRINCIPALES DEL MVP

## 1. AppShell

### Descripción

Componente principal que contiene toda la estructura visual del MVP técnico.

### Función

Organiza la pantalla completa de Robert.

### Debe incluir

* Barra lateral izquierda
* Área central de trabajo
* Panel derecho de estado
* Barra superior
* Zona de alertas
* Zona de historial

### No debe hacer

* Ejecutar acciones reales
* Aprobar cambios automáticamente
* Conectar herramientas externas

---

## 2. TopBar

### Descripción

Barra superior del sistema.

### Debe mostrar

* Nombre del sistema: Robert
* Fase actual
* Modo activo
* Estado general
* Indicador de seguridad
* Fecha de última actualización

### Ejemplo visual

```text
Robert Command Center
Fase 10 — MVP técnico básico
Modo: Supervisado
Estado: Sin ejecución real
```

---

## 3. LeftSidebar

### Descripción

Menú lateral principal.

### Debe incluir accesos a

* Home
* Contexto
* Comandos
* Decisiones
* Seguridad
* Fases
* Módulos
* Visual
* Prompts
* Arquitectura
* MVP
* Sandbox
* GitHub Backup

### Función

Permitir navegación visual entre áreas del sistema.

---

## 4. CommandCenter

### Descripción

Área central donde el usuario escribe o selecciona instrucciones.

### Función

Recibir comandos del usuario y convertirlos en solicitudes clasificadas.

### Debe permitir

* Escribir una instrucción
* Elegir modo operativo
* Ver riesgo detectado
* Ver acción recomendada
* Enviar a revisión
* Enviar a sandbox
* Marcar como decisión pendiente

### No debe permitir

* Ejecutar acciones externas directamente
* Saltarse aprobación del usuario
* Conectar herramientas reales sin decisión formal

---

## 5. ModeSelector

### Descripción

Selector del modo operativo actual.

### Opciones

* Manual
* Supervisado
* Sandbox

### Regla

El modo activo debe estar visible en todo momento.

Si el usuario cambia de modo, Robert debe registrar el cambio en historial.

---

## 6. RiskBadge

### Descripción

Indicador visual de riesgo aprobado en el wireframe v0.3.

### Debe mostrar

* Nivel de riesgo
* Nombre del riesgo
* Motivo del riesgo
* Estado de aprobación
* Acción recomendada

### Ejemplo

```text
Riesgo: Nivel 3 — Alto
Motivo: Esta acción modifica un documento aprobado.
Estado: Requiere aprobación.
Acción recomendada: Revisar antes de actualizar.
```

### Regla

Ningún riesgo puede mostrarse sin motivo.

---

## 7. ApprovalGate

### Descripción

Componente de control antes de cualquier cambio importante.

### Función

Bloquear acciones que requieren aprobación.

### Debe activarse cuando

* Se modifica un documento aprobado
* Se cambia una regla de seguridad
* Se cambia una decisión
* Se altera el alcance del proyecto
* Se intenta conectar una herramienta externa
* Se intenta automatizar una acción
* Se detecta riesgo Nivel 3 o Nivel 4

### Opciones visibles

* Aprobar
* Rechazar
* Pausar
* Corregir
* Enviar a revisión
* Enviar a sandbox

### Regla

Solo el usuario puede aprobar.

---

## 8. DecisionInbox

### Nombre visible

Pendiente de mi decisión

### Descripción

Vista aprobada en wireframe v0.3 para agrupar todo lo que necesita decisión del usuario.

### Debe mostrar

* Elemento pendiente
* Documento afectado
* Tipo de cambio
* Nivel de riesgo
* Motivo del riesgo
* Estado actual
* Acción recomendada
* Opciones de decisión

### Debe incluir elementos con estados

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

## 9. DocumentStatusMap

### Nombre visible

Mapa de documentos

### Descripción

Vista aprobada en wireframe v0.3 para visualizar documentos por fase y estado.

### Debe mostrar

* Carpeta
* Documento
* Estado
* Versión
* Última actualización
* Relación con decisiones
* Riesgo si aplica

### Estados visuales permitidos

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

## 10. CurrentStatePanel

### Descripción

Panel lateral derecho que muestra el estado actual de Robert.

### Debe mostrar

* Fase actual
* Última decisión registrada
* Último cambio documental
* Modo activo
* Riesgo actual
* Documento en revisión
* Pendientes abiertos
* Estado de GitHub manual

### Ejemplo

```text
Fase actual: 10 — MVP técnico básico
Modo: Supervisado
Última decisión: #010 — Wireframe v0.3 aprobado
GitHub: Respaldo manual privado
Ejecución real: No autorizada
```

---

## 11. ActionComposer

### Descripción

Componente donde Robert prepara una acción antes de presentarla al usuario.

### Puede preparar

* Borrador documental
* Resumen
* Prompt para Claude
* Propuesta de cambio
* Registro de decisión
* Registro de control de cambios
* Simulación sandbox

### No puede hacer

* Ejecutar automáticamente
* Aprobar solo
* Modificar archivos reales
* Enviar información externa

---

## 12. ChangeRequestCard

### Descripción

Tarjeta que representa una propuesta de cambio.

### Debe incluir

* Título del cambio
* Documento afectado
* Tipo de cambio
* Riesgo inicial
* Riesgo final
* Motivo
* Dependencias
* Conflictos
* Estado
* Recomendación

---

## 13. HistoryLog

### Descripción

Historial visible de acciones, cambios y decisiones.

### Debe registrar

* Fecha
* Acción solicitada
* Modo operativo
* Documento afectado
* Riesgo detectado
* Estado final
* Decisión relacionada

### Etiquetas permitidas

* [MANUAL]
* [SUPERVISADO]
* [SANDBOX]
* [CONTROL]
* [BLOQUEADA]
* [PARCIAL]
* [DECISIÓN]
* [GITHUB]
* [DOCUMENTO]

---

## 14. SandboxPanel

### Descripción

Vista para simular acciones sin afectar nada real.

### Debe permitir

* Crear prueba simulada
* Ver entrada
* Ver respuesta de Robert
* Ver riesgo
* Ver bloqueo si aplica
* Ver resultado
* Guardar resultado como texto

### No debe permitir

* Enviar correos reales
* Conectar apps
* Ejecutar automatizaciones
* Usar datos sensibles reales

---

## 15. DocumentViewer

### Descripción

Vista para leer documentos principales de Robert.

### Debe permitir

* Ver documento
* Ver versión
* Ver estado
* Ver decisiones relacionadas
* Ver cambios relacionados
* Marcar si necesita actualización

### No debe permitir

* Editar automáticamente sin aprobación
* Reemplazar documentos aprobados sin registro

---

## 16. PromptLibrary

### Descripción

Biblioteca de prompts del proyecto Robert.

### Debe incluir

* Prompts para Claude
* Prompts para ChatGPT
* Prompts de revisión
* Prompts de auditoría
* Prompts de sandbox
* Prompts de documentación
* Prompts de MVP técnico

---

## 17. GitHubBackupStatus

### Descripción

Componente que muestra el estado del respaldo manual en GitHub.

### Debe mostrar

* Repositorio: ROBERT_MASTER_SYSTEM
* Estado: Privado
* Uso: Respaldo documental manual
* Último checkpoint
* Advertencia de no automatización

### Regla

GitHub no debe tratarse como conexión activa.

GitHub es solo respaldo manual hasta nueva aprobación formal.

---

# MODELOS DE DATOS CONCEPTUALES

Estos modelos no son código final.

Sirven para entender qué información necesita manejar Robert.

---

## Modelo: RobertDocument

Campos sugeridos:

```text
id
nombre
carpeta
version
estado
fase
ultima_actualizacion
decision_relacionada
riesgo
descripcion
```

---

## Modelo: DecisionRecord

Campos sugeridos:

```text
id
titulo
fecha
estado
tipo_cambio
riesgo_inicial
riesgo_final
documentos_afectados
decision
alcance_autorizado
alcance_no_autorizado
```

---

## Modelo: RiskRecord

Campos sugeridos:

```text
nivel
nombre
motivo
estado_aprobacion
accion_recomendada
documento_afectado
modo_operativo
```

---

## Modelo: ChangeRequest

Campos sugeridos:

```text
id
titulo
tipo_cambio
documento_afectado
modulo_afectado
riesgo_inicial
riesgo_final
motivo
dependencias
conflictos
estado
decision_relacionada
```

---

## Modelo: CommandRequest

Campos sugeridos:

```text
id
comando
entrada_usuario
modo
documento_afectado
riesgo_detectado
accion_recomendada
estado
resultado
```

---

# FLUJO PRINCIPAL DEL MVP

## Flujo 1 — Usuario solicita acción

```text
Usuario escribe instrucción
↓
CommandCenter recibe solicitud
↓
Robert identifica modo operativo
↓
Robert clasifica acción
↓
Robert detecta documento o módulo afectado
↓
Robert calcula riesgo
↓
RiskBadge muestra nivel y motivo
↓
ApprovalGate decide si requiere aprobación
↓
Robert prepara borrador o bloquea
↓
Usuario decide
↓
HistoryLog registra resultado
```

---

## Flujo 2 — Cambio documental

```text
Usuario pide actualizar documento
↓
Robert identifica documento afectado
↓
Robert revisa si está aprobado
↓
Robert clasifica tipo de cambio
↓
Robert asigna riesgo
↓
Robert revisa dependencias
↓
Robert prepara borrador
↓
Usuario aprueba o corrige
↓
Se actualiza documento manualmente
↓
Se registra en DECISIONS_LOG si aplica
↓
Se registra en CONTROL_DE_CAMBIOS
```

---

## Flujo 3 — Decisión pendiente

```text
Robert detecta decisión requerida
↓
Crea elemento en DecisionInbox
↓
Muestra riesgo y motivo
↓
Usuario elige acción
↓
Robert registra decisión
↓
Se actualizan documentos relacionados si el usuario autoriza
```

---

## Flujo 4 — Sandbox

```text
Usuario activa MODO_SANDBOX
↓
Robert crea simulación
↓
Robert clasifica riesgo
↓
Robert ejecuta solo respuesta simulada
↓
Robert muestra resultado
↓
Robert marca bloqueos si aplica
↓
Usuario decide si registra aprendizaje
```

---

# ESTRUCTURA VISUAL PROPUESTA

```text
┌─────────────────────────────────────────────────────────────┐
│ Robert Command Center | Fase 10 | Modo Supervisado | Seguro │
├───────────────┬───────────────────────────────┬─────────────┤
│ Sidebar       │ CommandCenter                 │ Estado      │
│               │                               │             │
│ Home          │ Instrucción del usuario        │ Fase actual │
│ Contexto      │ Resultado preparado            │ Riesgo      │
│ Comandos      │ RiskBadge                      │ Pendientes  │
│ Decisiones    │ ApprovalGate                   │ GitHub      │
│ Seguridad     │                               │             │
│ MVP           │                               │             │
│ Sandbox       │                               │             │
├───────────────┴───────────────────────────────┴─────────────┤
│ HistoryLog                                                  │
└─────────────────────────────────────────────────────────────┘
```

---

# ESTRUCTURA DE ARCHIVOS FUTURA PROPUESTA

Esta estructura es solo conceptual para una futura app.

No autoriza programación todavía.

```text
robert-command-center/
│
├── app/
│   ├── page.tsx
│   ├── layout.tsx
│   └── globals.css
│
├── components/
│   ├── AppShell.tsx
│   ├── TopBar.tsx
│   ├── LeftSidebar.tsx
│   ├── CommandCenter.tsx
│   ├── ModeSelector.tsx
│   ├── RiskBadge.tsx
│   ├── ApprovalGate.tsx
│   ├── DecisionInbox.tsx
│   ├── DocumentStatusMap.tsx
│   ├── CurrentStatePanel.tsx
│   ├── ActionComposer.tsx
│   ├── ChangeRequestCard.tsx
│   ├── HistoryLog.tsx
│   ├── SandboxPanel.tsx
│   ├── DocumentViewer.tsx
│   ├── PromptLibrary.tsx
│   └── GitHubBackupStatus.tsx
│
├── data/
│   ├── documents.json
│   ├── decisions.json
│   ├── changes.json
│   ├── risks.json
│   └── sandbox.json
│
├── lib/
│   ├── risk-classifier.ts
│   ├── command-router.ts
│   ├── approval-rules.ts
│   └── document-status.ts
│
└── README.md
```

---

# COMPONENTES PRIORITARIOS PARA MVP TÉCNICO BÁSICO

Para una primera versión técnica, los componentes más importantes serían:

1. AppShell
2. TopBar
3. LeftSidebar
4. CommandCenter
5. RiskBadge
6. ApprovalGate
7. DecisionInbox
8. DocumentStatusMap
9. CurrentStatePanel
10. HistoryLog

Los demás componentes pueden agregarse después.

---

# CRITERIOS DE ACEPTACIÓN DEL MVP TÉCNICO

El MVP técnico básico estará listo para revisión cuando pueda mostrar de forma simulada:

* Fase actual de Robert
* Modo operativo activo
* Documentos principales
* Estado de documentos
* Comandos del usuario
* Riesgo con motivo visible
* Decisiones pendientes
* Historial de acciones
* Estado de GitHub manual
* Bloqueo de acciones no autorizadas

---

# CRITERIOS DE SEGURIDAD

El MVP técnico debe bloquear o marcar como no permitido:

* Intentos de ejecutar acciones reales
* Intentos de conectar apps sin aprobación
* Intentos de automatizar GitHub
* Intentos de enviar correos
* Intentos de usar datos sensibles
* Intentos de modificar reglas críticas sin aprobación
* Intentos de aprobar decisiones automáticamente

---

# DEPENDENCIAS DOCUMENTALES

Este documento depende de:

* ROBERT_HOME
* ROBERT_CONTEXT_MASTER
* ROBERT_COMMANDS
* ROBERT_SECURITY_RULES
* ROBERT_CONTROL_DE_CAMBIOS
* ROBERT_PHASES
* ROBERT_MODULES
* ROBERT_SYSTEM_ARCHITECTURE
* ROBERT_MVP_PLAN
* ROBERT_TECHNICAL_MVP_PLAN
* ROBERT_TECHNICAL_MVP_WIREFRAME v0.3
* ROBERT_DECISIONS_LOG

---

# RIESGO DEL DOCUMENTO

Tipo de cambio:

**Tipo 5 — Cambio técnico**

Nivel de riesgo inicial:

**Nivel 3 — Alto**

Motivo:

Este documento empieza a transformar el diseño visual aprobado en estructura técnica de componentes. Aunque no programa nada, acerca el proyecto a una futura fase de desarrollo.

Nivel de riesgo final:

**Nivel 2 — Medio**

Motivo de reducción:

El documento es solo especificación. No incluye programación, conexiones reales, automatizaciones ni ejecución externa.

---

# DECISIÓN PENDIENTE

Este documento queda como:

**Borrador técnico inicial pendiente de revisión**

Para aprobarlo formalmente, el usuario deberá escribir:

```text
APRUEBO ROBERT_TECHNICAL_COMPONENTS_SPEC v0.1
```

---

# PRÓXIMO PASO RECOMENDADO

Después de revisar este documento, el siguiente paso sería crear:

**ROBERT_TECHNICAL_DATA_MODEL_SPEC**

Ese documento definiría con más detalle los datos internos simulados que necesita Robert para funcionar en el MVP técnico.

---

# CIERRE

ROBERT_TECHNICAL_COMPONENTS_SPEC v0.1 define los componentes técnicos iniciales del MVP básico de Robert.

Este documento prepara la futura construcción técnica, pero no la autoriza.

Robert sigue en modo documental y supervisado.

El usuario mantiene control total.

Robert no ejecuta acciones importantes sin permiso.
