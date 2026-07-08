# ROBERT_HOME

Versión: 0.11
Estado: Propuesta corregida — pendiente de revisión
Fecha: 07/07/2026
Ubicación: 00_HOME
Función: Punto central de navegación, estado, núcleo visual y control del sistema Robert
Fase actual: Fase 10 — MVP técnico básico en preparación
Cambio relacionado: Pendiente de registro formal si esta corrección se aprueba
Decisión relacionada: Sin nueva decisión formal para esta versión
Estado de aprobación de esta versión: Pendiente de revisión del usuario

Tags: #robert/home #robert/nucleo #robert/estado-actual #robert/navegacion #robert/fase-10

---

# OBJETIVO

ROBERT_HOME es la entrada principal del sistema Robert.

Su función es mostrar de forma rápida:

* Qué es Robert.
* Estado real del proyecto.
* Fase actual.
* Documentos maestros disponibles.
* Documentos técnicos disponibles.
* Documentos aprobados.
* Documentos pendientes.
* Documento vigente cuando existan versiones previas.
* Prioridades actuales.
* Próximos pasos.
* Reglas principales.
* Restricciones activas.
* Dirección general del sistema.
* Núcleo visual del sistema dentro de la navegación documental.

Este documento funciona como el punto central de navegación del proyecto.

---

# CORRECCIÓN PRINCIPAL DE v0.11

ROBERT_HOME v0.11 corrige dos conflictos detectados en `ROBERT_HOME v0.10`.

Conflictos detectados:

```text
1. CAMBIO #047 existía, pero HOME v0.10 no lo mostraba en la trazabilidad reciente.
2. HOME v0.10 seguía usando ROBERT_VISUAL y [[ROBERT_VISUAL]] en lugar de ROBERT_VISUAL_REFERENCE y [[ROBERT_VISUAL_REFERENCE]].
```

Clasificación de los conflictos:

```text
TIPO 3 — Conflicto de versión / numeración
TIPO 5 — Conflicto de cambio
TIPO 16 — Conflicto de fuente vigente
TIPO 17 — Conflicto de trazabilidad insuficiente
```

Correcciones aplicadas en v0.11:

```text
1. Se reconoce CAMBIO #047 en la trazabilidad reciente.
2. Se aclara que CAMBIO #047 pertenece a ROBERT_TECHNICAL_USER_ACTIONS_SPEC v0.2.
3. Se elimina el aparente hueco entre CAMBIO #046 y CAMBIO #048.
4. Se corrige ROBERT_VISUAL por ROBERT_VISUAL_REFERENCE.
5. Se corrige [[ROBERT_VISUAL]] por [[ROBERT_VISUAL_REFERENCE]].
6. Se mantiene APPROVAL_GATE v0.3 como aprobado e integrado.
7. Se mantiene DECISIÓN #027 y CAMBIO #049 como aprobación formal de APPROVAL_GATE v0.3.
8. Se mantiene USER_ACTIONS_SPEC v0.2 como fuente canónica aprobada, integrada y auditada voluntariamente.
9. Se mantiene Fase 10 sin programación, sin gate real, sin conexiones, sin automatizaciones, sin agentes y sin Fase 11.
```

Resultado:

```text
ROBERT_HOME v0.11 corrige la trazabilidad reciente y la nomenclatura del documento visual.
```

---

# TRAZABILIDAD DE ESTA VERSIÓN

Esta versión se apoya en la revisión manual del usuario sobre `ROBERT_HOME v0.10`.

Trazabilidad corregida:

```text
CAMBIO #047 — Corrección de ROBERT_TECHNICAL_USER_ACTIONS_SPEC v0.2
CAMBIO #048 — Corrección de ROBERT_TECHNICAL_APPROVAL_AND_AUTHORIZATION_GATE_SPEC v0.3
CAMBIO #049 — Aprobación e integración de ROBERT_TECHNICAL_APPROVAL_AND_AUTHORIZATION_GATE_SPEC v0.3
```

Estado de esta versión:

```text
ROBERT_HOME v0.11
Estado: Propuesta corregida — pendiente de revisión
```

Restricción:

```text
ROBERT_HOME v0.11 no está aprobado todavía.
ROBERT_HOME v0.11 no está integrado todavía.
ROBERT_HOME v0.11 no crea una nueva decisión formal.
ROBERT_HOME v0.11 no registra por sí mismo un nuevo cambio formal.
```

---

# NOTA DE CONSISTENCIA SOBRE CAMBIO #047

CAMBIO #047 existe y corresponde a:

```text
CAMBIO #047 — Corrección de ROBERT_TECHNICAL_USER_ACTIONS_SPEC v0.2
```

Función de CAMBIO #047:

```text
Registrar la corrección documental de USER_ACTIONS_SPEC v0.2 frente al conflicto entre referencias posteriores a v0.2 y la fuente física disponible.
```

Clasificación relacionada:

```text
TIPO 3 — Conflicto de versión
TIPO 16 — Conflicto de fuente vigente
TIPO 17 — Conflicto de trazabilidad insuficiente
```

Regla de interpretación:

```text
CAMBIO #047 debe mostrarse como antecedente de trazabilidad.
CAMBIO #047 no debe aparecer como hueco de numeración.
CAMBIO #047 no reemplaza por sí solo a DECISIÓN #017 ni a CAMBIO #028.
```

Estado operativo vigente de USER_ACTIONS_SPEC v0.2:

```text
ROBERT_TECHNICAL_USER_ACTIONS_SPEC v0.2
Estado: Aprobado e integrado
Decisión relacionada: DECISIÓN #017
Cambio relacionado: CAMBIO #028
Auditoría voluntaria completada sin cambios de fondo
```

Nota de control:

```text
Si el texto completo de CAMBIO #047 contiene un cierre distinto, deberá revisarse y reconciliarse.
Mientras tanto, HOME v0.11 reconoce CAMBIO #047 como antecedente de trazabilidad sin reabrir automáticamente USER_ACTIONS_SPEC v0.2.
```

---

# DEFINICIÓN DE ROBERT

Robert no es:

* Un chatbot.
* Una app de productividad simple.
* Una automatización aislada.
* Una bóveda de notas.
* Un sistema autónomo sin control del usuario.

Robert es:

**Un sistema operativo personal de inteligencia artificial tipo AI Command Center.**

Su objetivo es transformar:

```text
Ideas
↓
Conversaciones
↓
Documentos
↓
Decisiones
↓
Sistemas
↓
Acciones supervisadas
```

Robert busca funcionar como un centro de mando personal, documental, visual, modular y seguro.

---

# ROBERT_HOME COMO NÚCLEO

ROBERT_HOME funciona como el núcleo de entrada del sistema.

Esto significa que:

* Es el primer punto de navegación.
* Resume el estado real.
* Enlaza documentos principales.
* Muestra restricciones activas.
* Muestra prioridades.
* Muestra documentos técnicos aprobados.
* Muestra documentos pendientes.
* Conecta la parte documental con la visión visual de Robert.
* Funciona como referencia rápida antes de avanzar.

Alineación visual:

```text
ROBERT_HOME = Núcleo documental y visual de entrada
Tag oficial: #robert/nucleo
```

---

# PRINCIPIO CENTRAL

```text
El usuario manda.
Robert no ejecuta acciones importantes sin permiso.
```

---

# ESTADO ACTUAL DEL PROYECTO

Estado real actualizado:

```text
Fase actual:
Fase 10 — MVP técnico básico en preparación

Modo operativo:
Documental, manual y supervisado

MVP manual:
Validado

Sandbox manual:
Validado

GitHub:
Configurado como respaldo documental privado y manual

Obsidian:
Cerebro documental manual

Programación:
No autorizada

Código real:
No autorizado

Pantallas reales:
No autorizadas

Base de datos real:
No autorizada

Conexiones externas:
No autorizadas

Automatizaciones reales:
No autorizadas

Agentes autónomos:
No autorizados

Fase 11:
No autorizada
```

---

# ESTADO OPERATIVO ACTUAL

Robert se encuentra en:

```text
Fase 10 — MVP técnico básico en preparación
```

Estado consolidado:

```text
MVP manual validado
Sandbox manual validado
GitHub configurado como respaldo documental privado/manual
Obsidian usado como cerebro documental manual
CONTEXT_MASTER v0.5 reanclado
PHASES v0.5 reconciliado
COMMANDS v0.4 aprobado e integrado
Escala de riesgo y autonomía unificada
DOCUMENT_LIFECYCLE_SPEC v0.2 aprobado
VERSIONING_AND_CHANGE_POLICY_SPEC v0.2 aprobado
DATA_CONSISTENCY_AND_CONFLICT_RESOLUTION_SPEC v0.3 aprobado
ROBERT_HOME v0.8 aprobado e integrado
ROBERT_HOME v0.10 creado como propuesta corregida pendiente de revisión
ROBERT_HOME v0.11 en propuesta corregida pendiente de revisión
USER_ACTIONS_SPEC v0.2 aprobado, integrado y auditado voluntariamente
CAMBIO #047 reconocido como antecedente de trazabilidad de USER_ACTIONS_SPEC v0.2
APPROVAL_GATE v0.3 aprobado e integrado
DECISIÓN #027 registrada
CAMBIO #049 registrado
ROBERT_VISUAL_REFERENCE reconocido como documento visual correcto
Wireframe v0.3 reconocido como vigente
Fuente física del wireframe pendiente de normalización manual
```

Restricciones activas:

```text
Sin programación autorizada
Sin código real
Sin base de datos real
Sin gate real
Sin sistema real de autorización
Sin sistema real de consistencia documental
Sin sistema real de control de versiones
Sin motor real de resolución de conflictos
Sin conexiones externas
Sin automatizaciones reales
Sin agentes autónomos activos
Sin avance a Fase 11
```

---

# DOCUMENTOS MAESTROS DEL SISTEMA

## 00_HOME

```text
ROBERT_HOME.md
Versión actual propuesta: v0.11
Estado: Propuesta corregida — pendiente de revisión
Función: Punto central de navegación, estado, núcleo visual y control del sistema
Tag clave: #robert/nucleo
```

Estado previo aprobado:

```text
ROBERT_HOME v0.8
Estado: Aprobado e integrado
Decisión relacionada: DECISIÓN #026
Cambio de integración: CAMBIO #046
```

Estado previo no aprobado:

```text
ROBERT_HOME v0.10
Estado: Propuesta corregida pendiente de revisión
Conflictos detectados:
1. No mostraba CAMBIO #047.
2. Usaba ROBERT_VISUAL en lugar de ROBERT_VISUAL_REFERENCE.
```

---

## 01_CONTEXT

```text
ROBERT_CONTEXT_MASTER.md
Versión actual: v0.5
Estado: Reanclado
Función: Fuente central de verdad contextual
```

---

## 02_COMMANDS

```text
ROBERT_COMMANDS.md
Versión actual: v0.4
Estado: Aprobado e integrado
Función: Comandos, acciones de control e interpretación operativa
```

---

## 03_DECISIONS

```text
ROBERT_DECISIONS_LOG.md
Estado: Activo
Función: Registro formal de decisiones aprobadas por el usuario
Última decisión relevante: DECISIÓN #027
```

---

## 04_SECURITY

```text
ROBERT_SECURITY_RULES.md
Estado: Aprobado
Función: Seguridad, límites, permisos y control del usuario
```

```text
ROBERT_CONTROL_DE_CAMBIOS.md
Estado: Activo
Función: Registro formal de cambios, correcciones e integraciones
Nota: Documento maestro operativo de trazabilidad
Cambios recientes relevantes: CAMBIO #047, CAMBIO #048, CAMBIO #049
```

---

## 05_PHASES

```text
ROBERT_PHASES.md
Versión actual: v0.5
Estado: Reconciliado
Función: Mapa de fases del proyecto Robert
```

---

## 06_MODULES

```text
ROBERT_MODULES.md
Estado: Estructura inicial aprobada
Función: Módulos funcionales del sistema Robert
```

---

## 07_VISUAL

```text
ROBERT_VISUAL_REFERENCE.md
Estado: En desarrollo conceptual
Función: Dirección visual, núcleo, galaxias, paneles y experiencia visual
Nota: HOME funciona como núcleo documental y visual de entrada
```

Regla de nomenclatura visual:

```text
El documento visual correcto es ROBERT_VISUAL_REFERENCE.
No usar ROBERT_VISUAL como documento oficial si la fuente vigente confirmada es ROBERT_VISUAL_REFERENCE.
```

---

## 08_PROMPTS

```text
ROBERT_PROMPTS.md
Estado: Activo / en evolución
Función: Prompts base para trabajar con ChatGPT, Claude y otros modelos
```

---

## 09_ARCHITECTURE

```text
ROBERT_SYSTEM_ARCHITECTURE.md
Estado: Activo
Función: Arquitectura conceptual por capas
```

---

## 10_MVP

```text
ROBERT_MVP_PLAN.md
Estado: Aprobado
Función: Plan del MVP manual y técnico
```

---

## 15_SANDBOX

```text
ROBERT_SANDBOX.md
Estado: Validado
Función: Área de pruebas manuales y simulaciones controladas
```

```text
SANDBOX_RULES.md
Estado: Activo
Función: Reglas del sandbox manual
```

```text
SANDBOX_TESTS.md
Estado: Activo
Función: Pruebas manuales del sistema
```

```text
SANDBOX_RESULTS.md
Estado: Activo
Función: Resultados de pruebas del sandbox
```

---

# DOCUMENTOS TÉCNICOS DE FASE 10

## Wireframe oficial vigente

```text
ROBERT_TECHNICAL_MVP_WIREFRAME
Versión vigente: v0.3
Estado: Aprobado
Función: Wireframe conceptual vigente del MVP técnico
Nota: v0.3 reemplaza funcionalmente versiones previas del wireframe.
```

Regla de fuente vigente:

```text
No existen dos wireframes oficiales vigentes en paralelo.
El wireframe vigente conceptual es ROBERT_TECHNICAL_MVP_WIREFRAME v0.3.
Cualquier versión anterior queda como histórica/reemplazada.
```

Pendiente físico:

```text
ROBERT_TECHNICAL_MVP_WIREFRAME.md
ROBERT_TECHNICAL_MVP_WIREFRAME_v0.3_PROPUESTA.md
```

Regla:

```text
La corrección conceptual no basta.
Debe resolverse también la fuente física del archivo en la bóveda/repositorio.
```

---

## Documentos aprobados e integrados

```text
ROBERT_TECHNICAL_MVP_PLAN.md
Estado: Aprobado
```

```text
ROBERT_TECHNICAL_MVP_WIREFRAME.md
Versión vigente: v0.3
Estado: Aprobado
Nota: Wireframe oficial vigente
Pendiente operativo: confirmar/normalizar archivo físico frente a ROBERT_TECHNICAL_MVP_WIREFRAME_v0.3_PROPUESTA.md
```

```text
ROBERT_TECHNICAL_COMPONENTS_SPEC.md
Versión: v0.2
Estado: Aprobado
```

```text
ROBERT_TECHNICAL_DATA_MODEL_SPEC.md
Versión: v0.1
Estado: Aprobado
```

```text
ROBERT_TECHNICAL_INTERACTION_FLOW_SPEC.md
Versión: v0.2
Estado: Aprobado
```

```text
ROBERT_TECHNICAL_SCREEN_STATE_SPEC.md
Versión: v0.2
Estado: Aprobado
```

```text
ROBERT_TECHNICAL_USER_ACTIONS_SPEC.md
Versión: v0.2
Estado: Aprobado e integrado — auditoría voluntaria completada sin cambios de fondo
Decisión relacionada: DECISIÓN #017
Cambio relacionado: CAMBIO #028
Antecedente de trazabilidad: CAMBIO #047
Nota: Fuente canónica usada para APPROVAL_GATE v0.3
```

```text
ROBERT_TECHNICAL_ERROR_AND_BLOCKING_SPEC.md
Versión: v0.2
Estado: Aprobado
```

```text
ROBERT_TECHNICAL_PERMISSIONS_AND_SCOPES_SPEC.md
Versión: v0.2
Estado: Aprobado
```

```text
ROBERT_TECHNICAL_AUDIT_TRAIL_SPEC.md
Versión: v0.2
Estado: Aprobado
```

```text
ROBERT_TECHNICAL_NOTIFICATION_AND_ALERTS_SPEC.md
Versión: v0.2
Estado: Aprobado
```

```text
ROBERT_TECHNICAL_SESSION_AND_CONTEXT_SPEC.md
Versión: v0.2
Estado: Aprobado
```

```text
ROBERT_TECHNICAL_DOCUMENT_LIFECYCLE_SPEC.md
Versión: v0.2
Estado: Aprobado
```

```text
ROBERT_TECHNICAL_VERSIONING_AND_CHANGE_POLICY_SPEC.md
Versión: v0.2
Estado: Aprobado
```

```text
ROBERT_TECHNICAL_DATA_CONSISTENCY_AND_CONFLICT_RESOLUTION_SPEC.md
Versión: v0.3
Estado: Aprobado
```

```text
ROBERT_TECHNICAL_APPROVAL_AND_AUTHORIZATION_GATE_SPEC.md
Versión: v0.3
Estado: Aprobado e integrado
Decisión relacionada: DECISIÓN #027
Cambio relacionado: CAMBIO #049
Cambio de corrección previo: CAMBIO #048
Nota: Especificación conceptual del ApprovalGate. No crea gate real.
```

---

# ESTADO DE APPROVAL_GATE v0.3

Documento:

```text
ROBERT_TECHNICAL_APPROVAL_AND_AUTHORIZATION_GATE_SPEC.md
```

Versión:

```text
v0.3
```

Estado:

```text
Aprobado e integrado
```

Relación formal:

```text
DECISIÓN #027 — Aprobación de ROBERT_TECHNICAL_APPROVAL_AND_AUTHORIZATION_GATE_SPEC v0.3
CAMBIO #049 — Aprobación e integración de ROBERT_TECHNICAL_APPROVAL_AND_AUTHORIZATION_GATE_SPEC v0.3
CAMBIO #048 — Corrección de ROBERT_TECHNICAL_APPROVAL_AND_AUTHORIZATION_GATE_SPEC v0.3
```

Función:

```text
Definir conceptualmente cómo Robert debe decidir si una acción del usuario puede continuar, requiere confirmación, requiere aprobación formal, debe pausarse o debe bloquearse.
```

Correcciones integradas:

```text
1. Reemplazo de MainCanvas por AppShell.
2. Corrección de componentes participantes.
3. Corrección de mapeo Gates ↔ componentes.
4. Corrección de dónde se muestra cada elemento.
5. Corrección de correspondencia con USER_ACTIONS_SPEC v0.2.
6. Uso de las 20 acciones canónicas.
7. Confirmación de ApprovalGate como especificación conceptual.
8. Confirmación de ACCIÓN 12 — Activar sandbox manual como Gate 2 / Gate 7.
9. Alineación con los 10 componentes canónicos aprobados.
10. Exclusión de MainCanvas como componente oficial.
```

Regla:

```text
APPROVAL_GATE v0.3 está aprobado e integrado como documento técnico conceptual.
APPROVAL_GATE v0.3 no crea gate real.
APPROVAL_GATE v0.3 no autoriza programación.
APPROVAL_GATE v0.3 no autoriza ejecución real.
APPROVAL_GATE v0.3 no autoriza Fase 11.
```

---

# FUENTE CANÓNICA USADA PARA APPROVAL_GATE v0.3

La fuente canónica usada para APPROVAL_GATE v0.3 es:

```text
ROBERT_TECHNICAL_USER_ACTIONS_SPEC v0.2
Estado: Aprobado e integrado
DECISIÓN #017
CAMBIO #028
Antecedente de trazabilidad: CAMBIO #047
Auditoría voluntaria: completada sin cambios de fondo
```

La auditoría voluntaria confirmó:

```text
1. Lista canónica de 20 acciones.
2. Numeración correcta de las 20 acciones.
3. Uso de los 10 componentes canónicos.
4. Inclusión de AppShell como componente oficial.
5. Exclusión de MainCanvas como componente oficial.
6. ACCIÓN 12 mapeada correctamente como Gate 2 / Gate 7.
7. Uso como referencia canónica para corregir APPROVAL_GATE v0.3.
```

Lista canónica de 20 acciones:

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

Componentes canónicos confirmados:

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
MainCanvas no debe usarse como componente oficial.
```

---

# ENLACES CENTRALES DEL SISTEMA

## Documentos base

```text
[[ROBERT_HOME]]
[[ROBERT_CONTEXT_MASTER]]
[[ROBERT_COMMANDS]]
[[ROBERT_DECISIONS_LOG]]
[[ROBERT_CONTROL_DE_CAMBIOS]]
[[ROBERT_SECURITY_RULES]]
[[ROBERT_PHASES]]
[[ROBERT_MODULES]]
[[ROBERT_VISUAL_REFERENCE]]
[[ROBERT_PROMPTS]]
[[ROBERT_SYSTEM_ARCHITECTURE]]
[[ROBERT_MVP_PLAN]]
```

---

## MVP técnico

```text
[[ROBERT_TECHNICAL_MVP_PLAN]]
[[ROBERT_TECHNICAL_MVP_WIREFRAME]]
[[ROBERT_TECHNICAL_COMPONENTS_SPEC]]
[[ROBERT_TECHNICAL_DATA_MODEL_SPEC]]
[[ROBERT_TECHNICAL_INTERACTION_FLOW_SPEC]]
[[ROBERT_TECHNICAL_SCREEN_STATE_SPEC]]
[[ROBERT_TECHNICAL_USER_ACTIONS_SPEC]]
[[ROBERT_TECHNICAL_ERROR_AND_BLOCKING_SPEC]]
[[ROBERT_TECHNICAL_PERMISSIONS_AND_SCOPES_SPEC]]
[[ROBERT_TECHNICAL_AUDIT_TRAIL_SPEC]]
[[ROBERT_TECHNICAL_NOTIFICATION_AND_ALERTS_SPEC]]
[[ROBERT_TECHNICAL_SESSION_AND_CONTEXT_SPEC]]
[[ROBERT_TECHNICAL_DOCUMENT_LIFECYCLE_SPEC]]
[[ROBERT_TECHNICAL_VERSIONING_AND_CHANGE_POLICY_SPEC]]
[[ROBERT_TECHNICAL_DATA_CONSISTENCY_AND_CONFLICT_RESOLUTION_SPEC]]
[[ROBERT_TECHNICAL_APPROVAL_AND_AUTHORIZATION_GATE_SPEC]]
```

---

## Sandbox

```text
[[ROBERT_SANDBOX]]
[[SANDBOX_RULES]]
[[SANDBOX_TESTS]]
[[SANDBOX_RESULTS]]
```

---

# PRIORIDAD ACTUAL

Prioridad actual real:

```text
1. Reemplazar ROBERT_HOME con v0.11 como propuesta corregida pendiente de revisión.
2. Revisar ROBERT_HOME v0.11 completo.
3. Confirmar que HOME v0.11 reconoce CAMBIO #047.
4. Confirmar que HOME v0.11 ya no muestra hueco entre CAMBIO #046 y CAMBIO #048.
5. Confirmar que HOME v0.11 usa ROBERT_VISUAL_REFERENCE y [[ROBERT_VISUAL_REFERENCE]].
6. Confirmar que HOME v0.11 mantiene APPROVAL_GATE v0.3 como aprobado e integrado.
7. Confirmar que HOME v0.11 cita DECISIÓN #027 y CAMBIO #049.
8. Confirmar que HOME v0.11 mantiene ApprovalGate como especificación conceptual, no como gate real.
9. Actualizar README después de HOME v0.11 si se acepta la corrección.
10. Mantener Fase 10 sin programación.
11. Mantener GitHub y Obsidian manuales.
12. Resolver fuente física vigente del wireframe v0.3.
13. Registrar en CONTROL_DE_CAMBIOS la normalización del wireframe si se renombra, archiva o marca histórico.
14. Definir el siguiente documento técnico solo con autorización del usuario.
15. No avanzar a programación.
16. No avanzar a Fase 11.
```

---

# PRÓXIMOS PASOS

Próximos pasos recomendados:

```text
Paso 1:
Reemplazar ROBERT_HOME con v0.11.

Paso 2:
Revisar ROBERT_HOME v0.11 completo.

Paso 3:
Si ROBERT_HOME v0.11 queda correcto, actualizar README para reflejar:

- ROBERT_HOME v0.11 como propuesta corregida pendiente de revisión.
- CAMBIO #047 reconocido en trazabilidad.
- ROBERT_VISUAL_REFERENCE como documento visual correcto.
- APPROVAL_GATE v0.3 aprobado e integrado.
- DECISIÓN #027 registrada.
- CAMBIO #049 registrado.
- Sin gate real.
- Sin programación.
- Sin conexiones.
- Sin automatizaciones.
- Sin agentes.
- Sin Fase 11.

Paso 4:
No aprobar HOME automáticamente.

Paso 5:
Si el usuario decide aprobar HOME v0.11, deberá escribir:

APRUEBO ROBERT_HOME v0.11

Paso 6:
Solo después de esa aprobación explícita:

- Registrar decisión formal.
- Registrar cambio de aprobación e integración.
- Actualizar README si aplica.

Paso 7:
No avanzar a programación.
No activar conexiones.
No activar automatizaciones.
No activar agentes.
No avanzar a Fase 11.
```

---

# REGLAS PRINCIPALES ACTIVAS

```text
El usuario manda.
Robert no ejecuta acciones importantes sin permiso.
Primero orden. Después poder.
Simular no es ejecutar.
Preparar no es enviar.
Diseñar no es activar.
Proponer no es decidir.
Aprobar no es ejecutar.
Documento técnico no es sistema real.
ApprovalGate conceptual no es gate real.
Fase 10 no autoriza programación.
Fase 10 no autoriza conexiones externas.
Fase 10 no autoriza automatizaciones reales.
Fase 10 no autoriza agentes autónomos.
```

---

# ACCIONES DE CONTROL

Las acciones de control están fuera de la escala de riesgo.

Comandos de control:

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
Si el usuario usa una acción de control, Robert debe obedecer inmediatamente.
```

---

# ESCALA DE RIESGO ACTUAL

```text
Nivel 0 — Informativo
Nivel 1 — Bajo
Nivel 2 — Medio
Nivel 3 — Alto
Nivel 4 — Crítico
```

Regla corregida:

```text
Nivel 0 = Informativo
Acciones de control = fuera de la escala de riesgo
```

---

# AUTONOMÍA ACTUAL

Nivel de autonomía actual:

```text
Nivel 0 — Sin autonomía ejecutiva
```

Robert puede:

```text
Explicar
Resumir
Ordenar
Proponer
Redactar documentos
Corregir documentos
Detectar contradicciones
Sugerir siguientes pasos
Preparar bloques para copiar/pegar
```

Robert no puede:

```text
Ejecutar acciones reales
Programar
Crear sistemas reales
Conectar apps
Automatizar flujos
Modificar GitHub automáticamente
Modificar Obsidian automáticamente
Enviar correos
Crear bases de datos
Activar agentes autónomos
Avanzar de fase por su cuenta
```

---

# ESTADO DE GITHUB

Repositorio:

```text
ROBERT_MASTER_SYSTEM
```

Uso autorizado:

```text
Respaldo documental privado
Control de versiones manual
Historial manual de cambios
Base documental para futura fase técnica
```

No autorizado:

```text
Commits automáticos
Sincronización automática
Agentes modificando archivos
Conexiones automáticas
Automatización de GitHub
```

Últimas acciones manuales relevantes:

```text
CAMBIO #047 identificado como antecedente de USER_ACTIONS_SPEC v0.2
CAMBIO #048 registrado como corrección de APPROVAL_GATE v0.3
DECISIÓN #027 registrada manualmente
CAMBIO #049 registrado manualmente
APPROVAL_GATE v0.3 aprobado e integrado
ROBERT_HOME v0.11 preparado como propuesta corregida pendiente de revisión
```

---

# ESTADO DE OBSIDIAN

Uso actual:

```text
Cerebro documental manual
Organización por carpetas
Grafo visual conceptual
Lectura y navegación de documentos
```

No autorizado:

```text
Sincronización automática
Automatización de notas
Agentes modificando archivos
Conexiones automáticas
```

Documento visual correcto:

```text
ROBERT_VISUAL_REFERENCE
```

---

# FASES DEL PROYECTO

Estado resumido:

```text
Fase 1 — Identidad y visión: completada
Fase 2 — Documentos maestros: completada
Fase 3 — Fuente central de verdad: completada
Fase 4 — Comandos: completada
Fase 5 — Módulos: completada
Fase 6 — Arquitectura conceptual: completada
Fase 7 — Diseño visual/UX: en evolución conceptual
Fase 8 — MVP manual: validado
Fase 9 — Sandbox manual: validado
Fase 10 — MVP técnico básico: en preparación
Fase 11 — Conexión de herramientas: no autorizada
Fase 12 — Automatizaciones controladas: no autorizada
Fase 13 — Voz/multimodal: futura
Fase 14 — Agentes especializados: futura
Fase 15 — Business Builder avanzado: futura
Fase 16 — Seguridad avanzada/pruebas: futura
Fase 17 — Iteraciones: futura
```

Fase activa:

```text
Fase 10 — MVP técnico básico en preparación
```

---

# CONTROL DE VERSIONES DE ROBERT_HOME

| Versión | Estado                                      | Descripción                                                                                                                                                                        |
| ------- | ------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| v0.1    | Inicial                                     | Primer documento HOME del sistema                                                                                                                                                  |
| v0.2    | Actualización                               | Se integró dirección general del proyecto Robert                                                                                                                                   |
| v0.3    | Base actualizada                            | Se organizaron documentos maestros y navegación inicial                                                                                                                            |
| v0.4    | Parcial / inconsistente                     | Se agregaron múltiples logs de avances, pero la parte superior quedó desactualizada                                                                                                |
| v0.5    | Propuesta corregida no cerrada              | Se reconcilió HOME con Fase 10, pero quedaron huecos de wireframe, trazabilidad y tag de núcleo                                                                                    |
| v0.6    | Propuesta corregida no cerrada              | Se corrigió fuente vigente del wireframe, trazabilidad pendiente de APPROVAL_GATE y tag #robert/nucleo, pero faltó tarea operativa para normalizar el archivo físico del wireframe |
| v0.7    | Propuesta corregida no cerrada              | Se agregó tarea manual para resolver la fuente física vigente del wireframe v0.3, pero aún faltaba trazabilidad formal del propio HOME                                             |
| v0.8    | Aprobado e integrado                        | Se cita CAMBIO #045 para cerrar trazabilidad acumulada de HOME v0.5–v0.7 y se integra mediante DECISIÓN #026 / CAMBIO #046                                                         |
| v0.9    | Propuesta corregida pendiente de revisión   | Actualizó HOME después de CAMBIO #048 y reconoció APPROVAL_GATE v0.3 como propuesta corregida pendiente de revisión                                                                |
| v0.10   | Propuesta corregida con conflicto detectado | Actualizó HOME después de DECISIÓN #027 / CAMBIO #049, pero omitió CAMBIO #047 y mantuvo ROBERT_VISUAL en lugar de ROBERT_VISUAL_REFERENCE                                         |
| v0.11   | Propuesta corregida pendiente de revisión   | Corrige trazabilidad de CAMBIO #047 y reemplaza ROBERT_VISUAL por ROBERT_VISUAL_REFERENCE                                                                                          |

---

# MOTIVO DE v0.11

ROBERT_HOME v0.11 existe para corregir:

```text
1. El aparente hueco de numeración de CAMBIO #047.
2. La ausencia de CAMBIO #047 en la trazabilidad reciente.
3. La persistencia de ROBERT_VISUAL como nombre de documento visual.
4. La persistencia de [[ROBERT_VISUAL]] como enlace central.
5. La necesidad de usar ROBERT_VISUAL_REFERENCE como fuente visual correcta.
6. La necesidad de mantener APPROVAL_GATE v0.3 como aprobado e integrado sin convertirlo en gate real.
```

---

# ESTADO DE DOCUMENTOS Y CAMBIOS RECIENTES

## Aprobaciones recientes

```text
DECISIÓN #024 — Aprobación de VERSIONING_AND_CHANGE_POLICY_SPEC v0.2
CAMBIO #042 — Aprobación e integración de VERSIONING_AND_CHANGE_POLICY_SPEC v0.2

DECISIÓN #025 — Aprobación de DATA_CONSISTENCY_AND_CONFLICT_RESOLUTION_SPEC v0.3
CAMBIO #044 — Aprobación e integración de DATA_CONSISTENCY_AND_CONFLICT_RESOLUTION_SPEC v0.3

DECISIÓN #026 — Aprobación de ROBERT_HOME v0.8
CAMBIO #046 — Aprobación e integración de ROBERT_HOME v0.8

DECISIÓN #027 — Aprobación de ROBERT_TECHNICAL_APPROVAL_AND_AUTHORIZATION_GATE_SPEC v0.3
CAMBIO #049 — Aprobación e integración de ROBERT_TECHNICAL_APPROVAL_AND_AUTHORIZATION_GATE_SPEC v0.3
```

---

## Cambios recientes registrados

```text
CAMBIO #047 — Corrección de ROBERT_TECHNICAL_USER_ACTIONS_SPEC v0.2
Estado: Registrado como antecedente de corrección / trazabilidad
Función: Resolver conflicto de versión, fuente vigente y trazabilidad de USER_ACTIONS_SPEC v0.2
```

```text
CAMBIO #048 — Corrección de ROBERT_TECHNICAL_APPROVAL_AND_AUTHORIZATION_GATE_SPEC v0.3
Estado: Registrado
Función: Registrar APPROVAL_GATE v0.3 como propuesta corregida pendiente de revisión antes de su aprobación formal
```

```text
CAMBIO #049 — Aprobación e integración de ROBERT_TECHNICAL_APPROVAL_AND_AUTHORIZATION_GATE_SPEC v0.3
Estado: Aprobado e integrado
Función: Registrar APPROVAL_GATE v0.3 como documento técnico conceptual aprobado e integrado
```

Nota:

```text
CAMBIO #049 no autoriza programación.
CAMBIO #049 no crea gate real.
CAMBIO #049 no autoriza conexiones externas.
CAMBIO #049 no autoriza automatizaciones.
CAMBIO #049 no autoriza agentes.
CAMBIO #049 no autoriza Fase 11.
```

---

# NORMALIZACIÓN PENDIENTE DEL WIREFRAME

Pendiente de resolver manualmente:

```text
ROBERT_TECHNICAL_MVP_WIREFRAME.md
ROBERT_TECHNICAL_MVP_WIREFRAME_v0.3_PROPUESTA.md
```

Objetivo:

```text
Evitar dos fuentes físicas paralelas para el wireframe v0.3.
```

Acción manual requerida:

```text
1. Revisar cuál archivo contiene el wireframe v0.3 aprobado.
2. Elegir el archivo oficial vigente.
3. Renombrar el archivo oficial si hace falta.
4. Marcar el archivo duplicado como histórico/reemplazado o archivarlo.
5. Registrar el cambio en ROBERT_CONTROL_DE_CAMBIOS.
6. Actualizar ROBERT_HOME y README si cambia el índice o el nombre del archivo.
```

Regla:

```text
La fuente conceptual vigente ya está definida como v0.3.
La fuente física vigente todavía debe normalizarse manualmente.
```

---

# DOCUMENTO TÉCNICO RECIÉN APROBADO

```text
ROBERT_TECHNICAL_APPROVAL_AND_AUTHORIZATION_GATE_SPEC v0.3
Estado: Aprobado e integrado
Decisión relacionada: DECISIÓN #027
Cambio relacionado: CAMBIO #049
```

Regla:

```text
APPROVAL_GATE v0.3 queda aprobado únicamente como especificación técnica documental conceptual.
No aprobar programación.
No crear gate real.
No avanzar a Fase 11.
```

---

# CRITERIOS PARA REVISAR ROBERT_HOME v0.11

ROBERT_HOME v0.11 podrá considerarse correcto si:

* Refleja Fase 10 como fase activa.
* Reconoce ROBERT_HOME v0.8 como aprobado e integrado.
* Reconoce ROBERT_HOME v0.11 como propuesta corregida pendiente de revisión.
* Reconoce CAMBIO #047.
* No muestra hueco entre CAMBIO #046 y CAMBIO #048.
* Reconoce APPROVAL_GATE v0.3 como aprobado e integrado.
* Cita DECISIÓN #027.
* Cita CAMBIO #049.
* Reconoce USER_ACTIONS_SPEC v0.2 como aprobado, integrado y auditado.
* Reconoce DECISIÓN #017 y CAMBIO #028 para USER_ACTIONS_SPEC v0.2.
* Reconoce CAMBIO #047 como antecedente de trazabilidad.
* Usa ROBERT_VISUAL_REFERENCE.
* Usa [[ROBERT_VISUAL_REFERENCE]].
* No usa ROBERT_VISUAL como documento visual oficial.
* Reconoce AppShell como componente canónico.
* Excluye MainCanvas como componente canónico.
* Mantiene las 20 acciones canónicas.
* Mantiene ACCIÓN 12 como Gate 2 / Gate 7.
* Mantiene ApprovalGate como especificación conceptual.
* No convierte ApprovalGate en gate real.
* Mantiene la normalización física del wireframe como pendiente.
* Actualiza prioridades actuales.
* Actualiza próximos pasos.
* Mantiene restricciones de Fase 10.
* No autoriza programación.
* No autoriza código real.
* No autoriza gate real.
* No autoriza conexiones externas.
* No autoriza automatizaciones.
* No autoriza agentes autónomos.
* No autoriza Fase 11.
* Mantiene control total del usuario.

---

# DECISIÓN PENDIENTE SOBRE ROBERT_HOME v0.11

Este documento queda como:

```text
ROBERT_HOME v0.11
Estado: Propuesta corregida — pendiente de revisión
```

Para aprobarlo formalmente como nueva versión integrada, el usuario deberá escribir:

```text
APRUEBO ROBERT_HOME v0.11
```

Mientras eso no ocurra:

```text
ROBERT_HOME v0.11 no queda aprobado.
ROBERT_HOME v0.11 no queda integrado.
ROBERT_HOME v0.8 sigue siendo la última versión aprobada e integrada.
```

---

# EFECTO DE UNA APROBACIÓN FUTURA DE HOME v0.11

Si se aprueba ROBERT_HOME v0.11:

1. Registrar decisión formal en `ROBERT_DECISIONS_LOG`.
2. Registrar cambio de aprobación e integración en `ROBERT_CONTROL_DE_CAMBIOS`.
3. Actualizar README.
4. Mantener APPROVAL_GATE v0.3 como aprobado e integrado.
5. Mantener ROBERT_VISUAL_REFERENCE como documento visual correcto.
6. Mantener CAMBIO #047 visible en trazabilidad reciente.
7. Mantener Robert en Fase 10.
8. No programar.
9. No conectar apps.
10. No automatizar.
11. No activar agentes.
12. No avanzar a Fase 11.

---

# CIERRE

ROBERT_HOME v0.11 corrige el punto central de navegación del sistema Robert después de detectar conflictos en `ROBERT_HOME v0.10`.

El HOME ahora refleja el estado real:

```text
Fase 10 — MVP técnico básico en preparación
Modo documental, manual y supervisado
ROBERT_HOME v0.8 aprobado e integrado
ROBERT_HOME v0.11 como propuesta corregida pendiente de revisión
CAMBIO #047 reconocido en trazabilidad reciente
USER_ACTIONS_SPEC v0.2 aprobado, integrado y auditado voluntariamente
USER_ACTIONS_SPEC v0.2 como fuente canónica usada para APPROVAL_GATE v0.3
APPROVAL_GATE v0.3 aprobado e integrado
DECISIÓN #027 registrada
CAMBIO #049 registrado
ROBERT_VISUAL_REFERENCE como documento visual correcto
AppShell como componente canónico
MainCanvas excluido como componente canónico
20 acciones canónicas reconocidas
ApprovalGate como especificación conceptual
Wireframe v0.3 vigente conceptualmente
Fuente física del wireframe pendiente de normalización manual
Sin programación autorizada
Sin código real
Sin gate real
Sin ejecución real
Sin conexiones externas
Sin automatizaciones reales
Sin agentes autónomos
Sin Fase 11
```

Robert continúa bajo control total del usuario.

Robert no ejecuta acciones importantes sin permiso.
