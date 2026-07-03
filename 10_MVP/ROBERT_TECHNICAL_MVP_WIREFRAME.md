# ROBERT_TECHNICAL_MVP_WIREFRAME — WIREFRAME DEL MVP TÉCNICO BÁSICO DE ROBERT

Proyecto: Robert  
Tipo de documento: Wireframe funcional del MVP técnico básico  
Versión: 0.3
Estado: Aprobado como wireframe oficial del MVP técnico básico
Fecha: 29/06/2026

---

Tags: #robert/orbita-2 #capa/5 #tipo/tecnico #robert/mvp-tecnico

---

# ENLACES DEL WIREFRAME TÉCNICO

ROBERT_TECHNICAL_MVP_WIREFRAME define la estructura visual funcional del MVP técnico básico de Robert.

Enlaces relacionados:

- [[ROBERT_HOME]]
- [[ROBERT_TECHNICAL_MVP_PLAN]]
- [[ROBERT_TECHNICAL_COMPONENTS_SPEC]]
- [[ROBERT_CONTROL_DE_CAMBIOS]]

# 1. OBJETIVO DEL DOCUMENTO

ROBERT_TECHNICAL_MVP_WIREFRAME define cómo debe verse y funcionar visualmente la primera versión técnica básica de Robert.

Este documento traduce ROBERT_TECHNICAL_MVP_PLAN a una estructura visual clara.

Su objetivo es diseñar la interfaz inicial de:

Robert Command Center Lite

Este documento no autoriza programación todavía.

Solo define el diseño funcional mínimo antes de construir.


---

# ACTUALIZACIÓN v0.3 — MEJORAS APROBADAS

Fecha: 29/06/2026  
Estado: Aprobada  
Decisión relacionada: DECISIÓN #010 — Aprobación de ROBERT_TECHNICAL_MVP_WIREFRAME v0.3  
Documento anterior: ROBERT_TECHNICAL_MVP_WIREFRAME v0.2  
Documento base de propuesta: ROBERT_TECHNICAL_MVP_WIREFRAME_v0.3_PROPUESTA

---

## Resumen de actualización

Esta versión actualiza el wireframe técnico oficial de Robert de v0.2 a v0.3.

La actualización integra tres mejoras visuales y funcionales aprobadas:

1. RiskBadge con motivo visible
    
2. Vista “Pendiente de mi decisión”
    
3. Mapa visual de documentos por fase y estado
    

Estas mejoras hacen que el MVP técnico básico sea más claro, más seguro y más fácil de controlar por el usuario.

---

# NUEVO COMPONENTE — RISKBADGE CON MOTIVO VISIBLE

## Descripción

Cada acción, documento, comando o cambio dentro del MVP técnico deberá mostrar un indicador visible de riesgo.

Este indicador no solo mostrará el nivel de riesgo, también debe mostrar el motivo.

---

## Estructura obligatoria

Todo RiskBadge debe incluir:

- Nivel de riesgo
    
- Nombre del riesgo
    
- Motivo del riesgo
    
- Estado de aprobación
    
- Acción recomendada
    

---

## Escala oficial permitida

La escala oficial de riesgo se toma de ROBERT_SECURITY_RULES y va de Nivel 0 a Nivel 4:

- Nivel 0 — Informativo
- Nivel 1 — Bajo
- Nivel 2 — Medio
- Nivel 3 — Alto
- Nivel 4 — Crítico

No existe Nivel 5 como riesgo.
El Nivel 5 solo puede pertenecer a la escala de autonomía, si SECURITY_RULES lo define.

"No permitido" es un estado de resultado, no un nivel de riesgo.

"No permitido" no es un nivel de riesgo; es un estado de resultado.
---

## Ejemplo visual

```text
Acción: Actualizar ROBERT_SECURITY_RULES
Riesgo: Nivel 4 — Crítico
Motivo: Cambia reglas centrales de seguridad y autorización.
Estado: Aprobación obligatoria del usuario.
Acción recomendada: Revisar, corregir y aprobar formalmente antes de actualizar.
```

---

# NUEVA VISTA — PENDIENTE DE MI DECISIÓN

## Nombre técnico

DecisionInbox

## Nombre visible para el usuario

Pendiente de mi decisión

---

## Objetivo

Agrupar en una sola vista todo lo que requiere decisión directa del usuario.

Esta vista evita que decisiones importantes queden perdidas dentro de conversaciones largas, documentos, pruebas o cambios pendientes.

---

## Elementos que deben aparecer

La vista “Pendiente de mi decisión” debe mostrar elementos con estados como:

- Aprobación requerida
    
- Pendiente de revisión
    
- Parcial
    
- Parcial avanzada
    
- Inconclusa
    
- En conflicto
    
- Bloqueado por dependencia
    
- Borrador pendiente de aprobación
    
- Cambio pendiente
    
- Riesgo alto pendiente
    
- Riesgo crítico pendiente
    

---

## Acciones permitidas para el usuario

Desde esta vista, el usuario podrá elegir:

- Aprobar
    
- Rechazar
    
- Pausar
    
- Corregir
    
- Pedir resumen
    
- Pedir comparación
    
- Bloquear
    
- Mandar a archivo
    

---

## Regla de seguridad

Robert no podrá aprobar automáticamente elementos dentro de esta vista.

Solo el usuario puede cerrar una decisión importante.

---

# NUEVA VISTA — MAPA DE DOCUMENTOS

## Nombre técnico

DocumentStatusMap

## Nombre visible para el usuario

Mapa de documentos

---

## Objetivo

Mostrar visualmente el estado de los documentos principales de Robert.

Esta vista permite saber rápidamente:

- Qué documentos existen
    
- Qué documentos están aprobados
    
- Qué documentos están pendientes
    
- Qué documentos están en borrador
    
- Qué documentos están bloqueados
    
- Qué documentos pertenecen a cada fase
    

---

## Estados visuales permitidos

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

## Mapa documental inicial

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
✓ 10_MVP / ROBERT_TECHNICAL_MVP_WIREFRAME_v0.3_PROPUESTA
✓ 15_SANDBOX / ROBERT_SANDBOX
✓ 15_SANDBOX / SANDBOX_RULES
✓ 15_SANDBOX / SANDBOX_TESTS
✓ 15_SANDBOX / SANDBOX_RESULTS
```

---

# ALCANCE DE LA ACTUALIZACIÓN v0.3

Esta actualización autoriza únicamente cambios documentales y visuales del wireframe.

No autoriza:

- Programar la app
    
- Conectar APIs reales
    
- Conectar GitHub automáticamente
    
- Conectar Gmail
    
- Conectar Google Calendar
    
- Automatizar acciones
    
- Ejecutar agentes autónomos
    
- Modificar archivos automáticamente
    
- Tomar decisiones por el usuario
    

---

# ESTADO FINAL DEL WIREFRAME

ROBERT_TECHNICAL_MVP_WIREFRAME v0.3 queda aprobado como wireframe oficial actualizado para el MVP técnico básico de Robert.

La versión v0.3 reemplaza funcionalmente a la v0.2 como referencia principal del wireframe.

La propuesta v0.3 queda conservada como documento histórico de origen.

---
---

# 2. RELACIÓN CON DOCUMENTOS ANTERIORES

Este documento depende de:

- ROBERT_CONTEXT_MASTER
    
- ROBERT_HOME
    
- ROBERT_PHASES
    
- ROBERT_MVP_PLAN
    
- ROBERT_TECHNICAL_MVP_PLAN
    
- ROBERT_COMMANDS
    
- ROBERT_SECURITY_RULES
    
- ROBERT_SANDBOX
    
- SANDBOX_RULES
    
- SANDBOX_TESTS
    
- SANDBOX_RESULTS
    
- ROBERT_SYSTEM_ARCHITECTURE
    

Decisión relacionada:

DECISIÓN #005 — ROBERT_TECHNICAL_MVP_PLAN aprobado como base del MVP técnico básico.

---

# 3. DEFINICIÓN DEL WIREFRAME

El wireframe es el mapa visual inicial de Robert Command Center Lite.

Debe mostrar:

- dónde escribe el usuario;
    
- dónde se muestra el modo activo;
    
- dónde aparece el análisis;
    
- dónde se muestra el nivel de riesgo;
    
- dónde aparece el estado del resultado;
    
- dónde aparecen documentos relacionados;
    
- dónde aparecen módulos relacionados;
    
- dónde se muestra la respuesta;
    
- dónde se muestran acciones permitidas;
    
- dónde se muestran acciones bloqueadas;
    
- dónde se genera INFORME_ACCIONES;
    
- dónde queda el historial;
    
- cómo se separa visualmente trabajo manual de simulaciones sandbox.
    

El wireframe no es diseño final.

Es la estructura mínima para entender cómo funcionará la interfaz.

---

# 4. PRINCIPIO CENTRAL DEL WIREFRAME

Función antes que estética.

Robert debe verse claro, controlado y seguro antes de verse avanzado.

La primera interfaz debe evitar exceso visual.

No debe intentar parecer una app final.

Debe probar el flujo:

instrucción → análisis → riesgo → estado → resultado → informe → historial

---

# 5. NOMBRE DE LA INTERFAZ

Nombre:

Robert Command Center Lite

Descripción:

Primera interfaz técnica básica de Robert para probar comandos, clasificación, riesgo, documentos, módulos, respuestas, informes, estados de resultado y sandbox simulado.

---

# 6. ESTRUCTURA GENERAL DE PANTALLA

La pantalla principal debe dividirse en 5 zonas:

1. Barra superior.
    
2. Panel lateral izquierdo.
    
3. Área central de comando.
    
4. Panel derecho de análisis.
    
5. Panel inferior de historial / informe.
    

Representación simple:

```text
┌──────────────────────────────────────────────────────────────┐
│ BARRA SUPERIOR — ROBERT / ESTADO / MODO / RIESGO GENERAL       │
├───────────────┬──────────────────────────────┬───────────────┤
│ PANEL         │ ÁREA CENTRAL                 │ PANEL DERECHO │
│ IZQUIERDO     │ COMMAND CENTER               │ ANÁLISIS      │
│               │                              │               │
│ Documentos    │ Input principal              │ Intención     │
│ Módulos       │ Respuesta                    │ Riesgo        │
│ Comandos      │ Borrador                     │ Estado        │
│ Seguridad     │ Siguiente paso               │ Documento     │
│               │                              │ Módulo        │
│               │                              │ Bloqueos      │
├───────────────┴──────────────────────────────┴───────────────┤
│ PANEL INFERIOR — HISTORIAL / INFORME_ACCIONES / EVENTOS        │
└──────────────────────────────────────────────────────────────┘
```

---

# 7. BARRA SUPERIOR

## Objetivo

Mostrar el estado general del sistema.

## Elementos mínimos

La barra superior debe mostrar:

- Nombre: Robert
    
- Versión: Command Center Lite
    
- Estado del sistema
    
- Modo activo
    
- Indicador de riesgo general
    
- Estado del resultado actual
    
- Botón DETENTE
    
- Botón PAUSA
    

## Ejemplo visual

```text
ROBERT COMMAND CENTER LITE     Estado: MVP Técnico Simulado     Modo: Manual     Riesgo: Bajo     Resultado: Borrador     [PAUSA] [DETENTE]
```

## Reglas

El botón DETENTE debe tener prioridad visual.

El botón PAUSA debe estar visible.

El modo activo debe verse claramente.

El usuario siempre debe saber si está en:

- Modo Manual
    
- Modo Supervisado
    
- Modo Sandbox
    
- Modo Control
    

---

# 8. PANEL LATERAL IZQUIERDO

## Objetivo

Mostrar navegación base del sistema.

## Secciones del panel

### 1. Documentos

Debe listar:

- ROBERT_HOME
    
- ROBERT_CONTEXT_MASTER
    
- ROBERT_COMMANDS
    
- ROBERT_DECISIONS_LOG
    
- ROBERT_SECURITY_RULES
    
- ROBERT_PHASES
    
- ROBERT_MODULES
    
- ROBERT_MVP_PLAN
    
- ROBERT_TECHNICAL_MVP_PLAN
    
- ROBERT_TECHNICAL_MVP_WIREFRAME
    
- ROBERT_SANDBOX
    
- SANDBOX_RULES
    
- SANDBOX_TESTS
    
- SANDBOX_RESULTS
    

### 2. Módulos

Debe listar:

- Command Center
    
- Security
    
- Documents
    
- Business Builder
    
- Sandbox
    
- Automation
    
- Apps Connector
    
- Decisions Log
    
- Memory
    
- Voice
    

### 3. Comandos

Debe mostrar comandos activos:

- RESUMEN
    
- CONCLUSION
    
- CONCLUCION
    
- CLASIFICAR
    
- DECISION
    
- ACTUALIZA
    
- INFORME_ACCIONES
    
- MODO_SUPERVISADO
    
- MODO_SANDBOX
    
- DETENTE
    
- PAUSA
    
- NO_AVANCES
    
- SOLO_BORRADOR
    

### 4. Seguridad

Debe mostrar:

- No ejecución real
    
- No apps conectadas
    
- No automatización real
    
- Usuario mantiene control
    
- Simular no es ejecutar
    
- Preparar no es enviar
    
- Diseñar no es activar
    
- Proponer no es decidir
    

---

# 9. ÁREA CENTRAL — COMMAND CENTER

## Objetivo

Ser el área principal donde el usuario interactúa con Robert.

## Elementos mínimos

Debe incluir:

1. Input principal.
    
2. Selector de modo.
    
3. Botón de analizar.
    
4. Resultado generado.
    
5. Borrador preparado.
    
6. Estado del resultado.
    
7. Siguiente paso.
    

---

# 10. INPUT PRINCIPAL

## Función

Aquí el usuario escribe la instrucción.

## Placeholder sugerido

```text
Escribe una instrucción para Robert...
```

## Ejemplos de uso

```text
Actualiza ROBERT_HOME post-sandbox.
```

```text
Simula una campaña para Agrocribas.
```

```text
Crea una decisión para aprobar el wireframe.
```

```text
DETENTE.
```

---

# 11. SELECTOR DE MODO

## Modos disponibles

### Modo Manual

Uso:

Trabajo normal.

Robert clasifica, responde y prepara.

No ejecuta.

### Modo Supervisado

Uso:

Robert revisa, propone mejoras y detecta errores.

No aprueba ni modifica sin permiso.

### Modo Sandbox

Uso:

Robert simula acciones operativas.

No ejecuta acciones reales.

### Modo Control

Uso:

Comandos de interrupción o seguridad como DETENTE, PAUSA y NO_AVANCES.

Prioridad máxima.

## Ejemplo visual

```text
Modo activo: [Manual ▼]
Opciones: Manual / Supervisado / Sandbox / Control
```

---

# 12. PANEL DE RESPUESTA

## Objetivo

Mostrar la respuesta generada por Robert.

Debe separar claramente:

- Respuesta normal.
    
- Borrador.
    
- Estado del resultado.
    
- Acción bloqueada.
    
- Informe.
    
- Siguiente paso.
    

## Estructura

```text
Respuesta generada:

[Texto de Robert]

Estado del resultado:

[Parcial / Parcial avanzada / Borrador preparado / Acción bloqueada / etc.]

Borrador preparado:

[Texto si aplica]

Siguiente paso:

[Acción recomendada]
```

---

# 13. PANEL DERECHO — ANÁLISIS DE INSTRUCCIÓN

## Objetivo

Mostrar cómo Robert entendió la instrucción.

## Campos obligatorios

El panel derecho debe mostrar:

- Instrucción recibida
    
- Intención detectada
    
- Tipo de solicitud
    
- Documento relacionado
    
- Módulo relacionado
    
- Nivel de riesgo
    
- Estado del resultado
    
- ¿Requiere autorización?
    
- Qué puede hacer Robert
    
- Qué no puede hacer Robert
    
- Acciones bloqueadas
    

## Ejemplo

```text
Intención detectada:
Actualizar documento

Tipo de solicitud:
Cambio documental

Documento relacionado:
ROBERT_HOME

Módulo relacionado:
Documents / Command Center

Nivel de riesgo:
Nivel 2 — Medio

Estado del resultado:
Borrador preparado

¿Requiere autorización?
Sí

Acciones permitidas:
Preparar borrador

Acciones bloqueadas:
Modificar documento oficial sin aprobación
```

---

# 14. INDICADOR DE RIESGO

## Objetivo

Mostrar de forma rápida el nivel de riesgo de la instrucción.

Robert mantendrá una sola escala oficial de riesgo.

La escala oficial es de Nivel 0 a Nivel 4.

No se crea Nivel 5.

“No permitido” no es un nivel de riesgo.

“No permitido” es un estado de resultado o bloqueo.

---
## Nivel 0 — Informativo

Texto:
Informativo

Uso:
Explicar, resumir, mostrar estado, navegar o responder sin cambiar nada.

Estado típico:
Permitido / Informativo.


## Nivel 1 — Bajo

Texto:

Riesgo bajo

Uso:

Resumen, clasificación, explicación, organización o borrador simple.

Estado típico:

Permitido / Borrador preparado.

---

## Nivel 2 — Medio

Texto:

Requiere revisión

Uso:

Cambios documentales, decisiones internas, actualizaciones de documentos, cambios de estructura o impacto moderado.

Estado típico:

Borrador preparado / Aprobación requerida / Pendiente de revisión.

---

## Nivel 3 — Alto

Texto:

Solo sandbox

Uso:

Acciones relacionadas con clientes, campañas, datos, herramientas externas, automatizaciones simuladas o decisiones operativas importantes.

Estado típico:

Simulación preparada / Parcial / Parcial avanzada / Acción bloqueada si intenta ejecución real.

---

## Nivel 4 — Crítico

Texto:

Bloqueado

Uso:

Acciones legales, fiscales, financieras, datos sensibles, ejecución externa peligrosa, productos regulados, acciones irreversibles o acciones que Robert no debe realizar en esta fase.

Estado típico:

Acción bloqueada / No permitido / Inconclusa.

---

# 15. ESTADOS DE RESULTADO

## Objetivo

Separar el nivel de riesgo del resultado real de la solicitud.

Robert debe mostrar siempre dos campos diferentes:

```text
Nivel de riesgo:
Nivel 3 — Alto

Estado del resultado:
Parcial avanzada
```

El nivel de riesgo responde:

¿Qué tan delicada es la acción?

El estado del resultado responde:

¿Qué pasó con la solicitud?

---

## Estados permitidos

La interfaz debe reconocer estos estados:

- Borrador preparado
    
- Aprobación requerida
    
- Simulación preparada
    
- Acción bloqueada
    
- Parcial
    
- Parcial avanzada
    
- Inconclusa
    
- Interrumpida
    
- Fallida
    
- Aprobada
    
- Pendiente de revisión
    
- No permitido
    

---

# 16. ESTADO: BORRADOR PREPARADO

## Uso

Cuando Robert puede preparar contenido, pero todavía no es versión oficial.

Ejemplo visual:

```text
ESTADO: BORRADOR PREPARADO

Robert preparó un texto o estructura para revisión.

Este resultado no está aprobado todavía.

Siguiente paso:
El usuario debe revisar, corregir o aprobar.
```

---

# 17. ESTADO: APROBACIÓN REQUERIDA

## Uso

Cuando una acción afecta documentos, decisiones, estructura o algo importante del sistema.

Ejemplo visual:

```text
APROBACIÓN REQUERIDA

Documento afectado:
ROBERT_PHASES

Nivel de riesgo:
Nivel 2 — Medio

Consecuencia:
El cambio actualizaría la fase actual del proyecto.

Opciones:
[APRUEBO] [CORREGIR] [PAUSA]
```

---

# 18. ESTADO: SIMULACIÓN PREPARADA

## Uso

Cuando Robert trabaja en MODO_SANDBOX.

Ejemplo visual:

```text
ESTADO: SIMULACIÓN PREPARADA

Modo:
Sandbox

Esta salida es una simulación documental.

No se ejecutó ninguna acción real.
No se contactó a ninguna persona.
No se conectó ninguna app.
```

---

# 19. ESTADO: ACCIÓN BLOQUEADA

## Uso

Cuando Robert no puede realizar una acción solicitada.

Ejemplo visual:

```text
ACCIÓN BLOQUEADA

Motivo:
Esta acción no está autorizada en el MVP técnico básico.

Nivel de riesgo:
Nivel 3 — Alto

Regla aplicada:
Preparar no es enviar.

Alternativa segura:
Robert puede preparar un borrador para revisión.
```

---

# 20. ESTADO: PARCIAL

## Uso

Cuando Robert puede avanzar, pero falta información importante.

Ejemplo visual:

```text
ESTADO: PARCIAL

Robert pudo preparar una respuesta útil, pero falta información para cerrar el resultado.

Información faltante:

- precio vigente;
- contacto oficial;
- condiciones de entrega;
- facturación;
- capacidad real por periodo.

Siguiente paso:

Completar información pendiente antes de usar este resultado como versión final.
```

Uso típico:

- propuestas incompletas;
    
- fichas comerciales incompletas;
    
- información insuficiente;
    
- documentos con datos pendientes;
    
- resultados que sirven como base, pero no como versión final.
    

---

# 21. ESTADO: PARCIAL AVANZADA

## Uso

Cuando Robert avanzó más que un borrador básico, pero todavía faltan datos para uso real.

Ejemplo visual:

```text
ESTADO: PARCIAL AVANZADA

Robert preparó una versión útil y estructurada, pero todavía no puede considerarse lista para ejecución real.

Puede usarse para:

- revisión interna;
- completar datos;
- preparar siguiente versión;
- simulación documental.

No puede usarse para:

- enviar a clientes;
- publicar;
- ejecutar;
- automatizar;
- tomar decisiones finales.
```

Uso típico:

Prueba Sandbox 005 — Información insuficiente durante simulación.

---

# 22. ESTADO: INCONCLUSA

## Uso

Cuando Robert no puede avanzar de forma útil porque falta información crítica o la instrucción no se puede resolver.

Ejemplo visual:

```text
ESTADO: INCONCLUSA

Robert no puede cerrar esta solicitud porque falta información crítica.

Motivo:

La instrucción no tiene suficiente contexto o requiere datos que no han sido proporcionados.

Siguiente paso:

El usuario debe aclarar o completar la información.
```

---

# 23. ESTADO: INTERRUMPIDA

## Uso

Cuando el usuario use comandos como:

- DETENTE
    
- PAUSA
    
- NO_AVANCES
    

Ejemplo visual:

```text
ESTADO: INTERRUMPIDA

La tarea fue detenida por instrucción del usuario.

Robert no continuará hasta recibir una nueva autorización.
```

---

# 24. ESTADO: NO PERMITIDO

## Uso

“No permitido” no será Nivel 5.

Será un estado de resultado cuando la solicitud no puede realizarse bajo ninguna condición dentro de la fase actual.

Ejemplo visual:

```text
ESTADO: NO PERMITIDO

Nivel de riesgo:
Nivel 4 — Crítico

Motivo:
La acción solicitada está fuera del alcance autorizado de Robert.

Regla aplicada:
Robert no puede ejecutar esta acción en la fase actual.

Alternativa segura:
Preparar análisis, borrador, checklist o explicación general, si aplica.
```

---

# 25. PANEL DE ACCIONES PERMITIDAS

## Objetivo

Mostrar lo que Robert sí puede hacer con la instrucción.

Ejemplos:

- Preparar borrador.
    
- Clasificar solicitud.
    
- Generar informe.
    
- Crear plantilla.
    
- Simular flujo.
    
- Marcar riesgos.
    
- Pedir autorización.
    
- Proponer siguiente paso.
    

Ejemplo visual:

```text
Acciones permitidas:

✓ Preparar borrador  
✓ Clasificar solicitud  
✓ Marcar riesgo  
✓ Generar INFORME_ACCIONES  
```

---

# 26. PANEL DE ACCIONES BLOQUEADAS

## Objetivo

Mostrar lo que Robert no puede hacer.

Ejemplos:

- Enviar correo real.
    
- Crear evento real.
    
- Contactar clientes.
    
- Usar listas reales.
    
- Conectar Gmail.
    
- Activar automatización.
    
- Ejecutar acción externa.
    
- Modificar documentos sin aprobación.
    

Ejemplo visual:

```text
ACCIÓN BLOQUEADA

Motivo:
Esta acción no está autorizada en el MVP técnico básico.

Acciones bloqueadas:

✕ Enviar correo real  
✕ Usar lista real de clientes  
✕ Conectar Gmail  
✕ Automatizar seguimiento  
```

---

# 27. PANEL INFERIOR — HISTORIAL

## Objetivo

Guardar registro básico de las instrucciones procesadas.

El historial no debe mezclar visualmente trabajo real/manual con simulaciones sandbox.

Debe mostrar etiquetas claras de modo.

---

## Campos mínimos

Cada registro debe guardar:

- Fecha
    
- Hora
    
- Modo
    
- Tipo de entrada
    
- Instrucción
    
- Intención
    
- Documento
    
- Módulo
    
- Riesgo
    
- Estado del resultado
    
- Si fue trabajo real/manual o simulación
    
- Siguiente paso
    

---

## Etiquetas obligatorias

El historial debe usar etiquetas visibles:

- [MANUAL]
    
- [SUPERVISADO]
    
- [SANDBOX]
    
- [CONTROL]
    
- [BLOQUEADA]
    
- [PARCIAL]
    
- [DECISIÓN]
    

---

## Ejemplo visual corregido

```text
Historial

[MANUAL] 29/06/2026 18:10
Instrucción: Actualiza ROBERT_HOME post-sandbox.
Riesgo: Nivel 2 — Medio
Estado: Borrador preparado
Tipo: Trabajo documental real/manual

[SANDBOX] 29/06/2026 18:18
Instrucción: Simula una campaña para Agrocribas.
Riesgo: Nivel 3 — Alto
Estado: Simulación preparada
Tipo: Simulación — no ejecución real

[PARCIAL] 29/06/2026 18:20
Instrucción: Prepara propuesta comercial de Agrocribas.
Riesgo: Nivel 2 — Medio
Estado: Parcial avanzada
Tipo: Resultado incompleto útil — requiere datos faltantes

[CONTROL] 29/06/2026 18:22
Instrucción: DETENTE.
Riesgo: Prioridad máxima
Estado: Interrumpida
Tipo: Control del usuario

[BLOQUEADA] 29/06/2026 18:25
Instrucción: Manda correos reales a clientes.
Riesgo: Nivel 3 — Alto
Estado: Acción bloqueada
Tipo: Ejecución real no autorizada
```

---

# 28. FILTROS DEL HISTORIAL

La interfaz debe poder mostrar el historial con filtros o pestañas:

```text
Todo | Manual | Supervisado | Sandbox | Bloqueadas | Parciales | Decisiones | Control
```

Esto permite evitar confusión entre:

- trabajo documental real/manual;
    
- revisiones supervisadas;
    
- simulaciones sandbox;
    
- acciones bloqueadas;
    
- decisiones;
    
- resultados parciales;
    
- interrupciones del usuario.
    

---

# 29. PANEL DE INFORME_ACCIONES

## Objetivo

Mostrar qué hizo Robert, qué no hizo y qué queda pendiente.

## Formato

```text
INFORME_ACCIONES

Acción solicitada:

Modo usado:

Nivel de riesgo:

Estado del resultado:

Resultado:

Qué hizo Robert:

Qué no hizo Robert:

Acciones bloqueadas:

Documentos relacionados:

Riesgos detectados:

Información faltante:

Pendientes:

Siguiente paso:
```

---

# 30. ESTADO CUANDO ROBERT BLOQUEA UNA ACCIÓN

Cuando Robert bloquea algo, la interfaz debe mostrar:

```text
ACCIÓN BLOQUEADA
```

Y debajo:

- motivo;
    
- nivel de riesgo;
    
- estado del resultado;
    
- regla aplicada;
    
- alternativa segura.
    

Ejemplo:

```text
ACCIÓN BLOQUEADA

Nivel de riesgo:
Nivel 3 — Alto

Estado del resultado:
Acción bloqueada

Motivo:
La solicitud implica enviar correos reales.

Regla aplicada:
Preparar no es enviar.

Alternativa segura:
Robert puede preparar un borrador de correo para revisión del usuario.
```

---

# 31. ESTADO CUANDO ROBERT REQUIERE APROBACIÓN

Cuando una acción requiera aprobación, la interfaz debe mostrar:

```text
APROBACIÓN REQUERIDA
```

Debe incluir:

- qué se quiere cambiar;
    
- documento afectado;
    
- nivel de riesgo;
    
- estado del resultado;
    
- consecuencia;
    
- botones sugeridos.
    

Botones:

```text
[APRUEBO] [CORREGIR] [PAUSA]
```

---

# 32. ESTADO CUANDO ROBERT ESTÁ EN SANDBOX

Cuando el modo Sandbox esté activo, la interfaz debe mostrar una alerta:

```text
MODO SANDBOX ACTIVO

Todo lo que ocurra aquí es simulación.

No se ejecutan acciones reales.
No se conectan apps.
No se contactan personas.
No se usan datos reales.
```

Debe mostrarse de forma visible.

---

# 33. EJEMPLO DE FLUJO 1 — ACTUALIZAR DOCUMENTO

## Instrucción

```text
Actualiza ROBERT_PHASES post-sandbox.
```

## Resultado esperado en interfaz

Modo:

Manual

Intención:

Actualizar documento

Documento relacionado:

ROBERT_PHASES

Módulo:

Documents / Phases

Riesgo:

Nivel 2 — Medio

Estado del resultado:

Borrador preparado

Requiere autorización:

Sí

Acción permitida:

Preparar texto para copiar.

Acción bloqueada:

Modificar documento oficial automáticamente.

Siguiente paso:

Usuario debe pegar, revisar y aprobar.

---

# 34. EJEMPLO DE FLUJO 2 — SANDBOX AGROCRIBAS

## Instrucción

```text
Simula una campaña para Agrocribas.
```

## Resultado esperado en interfaz

Modo:

Sandbox

Intención:

Simular campaña comercial

Documento relacionado:

SANDBOX_RESULTS

Módulo:

Business Builder / Sandbox / Marketing

Riesgo:

Nivel 3 — Alto

Estado del resultado:

Simulación preparada

Requiere autorización:

Sí, para cualquier ejecución real.

Acción permitida:

Preparar campaña simulada.

Acción bloqueada:

Enviar campaña, contactar clientes, usar listas reales.

---

# 35. EJEMPLO DE FLUJO 3 — ACCIÓN EXTERNA BLOQUEADA

## Instrucción

```text
Manda este correo a un cliente.
```

## Resultado esperado en interfaz

Modo:

Manual

Intención:

Enviar correo real

Documento relacionado:

Ninguno o Gmail futuro

Módulo:

Apps Connector / Email

Riesgo:

Nivel 3 — Alto

Estado del resultado:

Acción bloqueada

Resultado:

Acción bloqueada.

Alternativa:

Preparar borrador de correo.

Regla aplicada:

Preparar no es enviar.

---

# 36. EJEMPLO DE FLUJO 4 — DETENTE

## Instrucción

```text
DETENTE
```

## Resultado esperado en interfaz

Modo:

Control

Intención:

Interrupción inmediata

Riesgo:

Prioridad máxima

Estado del resultado:

Interrumpida

Resultado:

Tarea detenida.

Acciones:

- detener proceso actual;
    
- no continuar;
    
- no generar pasos nuevos;
    
- registrar interrupción.
    

---

# 37. EJEMPLO DE FLUJO 5 — RESULTADO PARCIAL

## Instrucción

```text
Prepara una propuesta comercial para Agrocribas.
```

## Resultado esperado en interfaz

Modo:

Manual o Sandbox, según contexto.

Intención:

Preparar propuesta comercial.

Documento relacionado:

SANDBOX_RESULTS / Business Builder / Documents

Módulo:

Business Builder / Sales / Documents

Riesgo:

Nivel 2 — Medio o Nivel 3 — Alto si se conecta con clientes reales.

Estado del resultado:

Parcial avanzada

Resultado:

Robert prepara una propuesta útil, pero marca información faltante.

Información faltante:

- contacto oficial;
    
- vigencia de precios;
    
- condiciones de entrega;
    
- facturación;
    
- ficha técnica;
    
- capacidad real por periodo.
    

Acciones bloqueadas:

- enviar propuesta;
    
- contactar clientes;
    
- usar lista real;
    
- prometer condiciones no verificadas.
    

---

# 38. COMPONENTES MÍNIMOS

Componentes necesarios:

- TopBar
    
- Sidebar
    
- CommandInput
    
- ModeSelector
    
- AnalyzeButton
    
- RiskBadge
    
- ResultStatusBadge
    
- AnalysisPanel
    
- AllowedActionsPanel
    
- BlockedActionsPanel
    
- ResultPanel
    
- DraftPanel
    
- ReportPanel
    
- HistoryPanel
    
- HistoryFilters
    
- SandboxBanner
    
- ApprovalNotice
    
- PartialResultNotice
    
- InconclusiveNotice
    
- StopButton
    
- PauseButton
    

---

# 39. DISEÑO VISUAL BASE

Estilo recomendado:

- dark mode;
    
- fondo negro o gris muy oscuro;
    
- paneles en gris oscuro;
    
- bordes sutiles;
    
- acentos azul/cian;
    
- indicadores de riesgo visibles;
    
- estados de resultado visibles;
    
- etiquetas claras de modo;
    
- tarjetas limpias;
    
- texto claro;
    
- jerarquía visual simple.
    

Prioridad:

Claridad.

No saturar.

No usar demasiadas animaciones.

No crear diseño futurista complejo en la primera versión.

---

# 40. JERARQUÍA VISUAL

Orden de importancia visual:

1. Modo activo.
    
2. Input principal.
    
3. Nivel de riesgo.
    
4. Estado del resultado.
    
5. Acciones bloqueadas.
    
6. Resultado.
    
7. Informe.
    
8. Historial.
    
9. Documentos y módulos.
    

La seguridad debe verse antes que la estética.

---

# 41. BOTONES MÍNIMOS

Botones necesarios:

- Analizar
    
- Limpiar
    
- Copiar resultado
    
- Generar informe
    
- APRUEBO
    
- CORREGIR
    
- PAUSA
    
- DETENTE
    

Botones que no deben existir todavía:

- Enviar correo
    
- Crear evento
    
- Conectar app
    
- Activar automatización
    
- Contactar cliente
    
- Publicar campaña
    
- Ejecutar agente
    

---

# 42. DATOS SIMULADOS INICIALES

El wireframe puede usar datos simulados.

Ejemplo:

```text
Modo activo:
Manual

Documento seleccionado:
ROBERT_HOME

Módulo:
Documents

Riesgo:
Nivel 2 — Medio

Estado:
Borrador preparado
```

Estos datos no deben conectarse a herramientas reales todavía.

---

# 43. CRITERIOS DE ÉXITO DEL WIREFRAME

El wireframe funciona si permite entender claramente:

- dónde escribe el usuario;
    
- qué modo está activo;
    
- qué entendió Robert;
    
- qué nivel de riesgo detectó;
    
- qué estado de resultado tiene la solicitud;
    
- qué documento afecta;
    
- qué módulo afecta;
    
- qué puede hacer Robert;
    
- qué no puede hacer Robert;
    
- qué resultado preparó;
    
- qué acciones bloqueó;
    
- qué quedó parcial o inconcluso;
    
- qué entradas fueron sandbox;
    
- qué entradas fueron trabajo manual;
    
- qué queda pendiente;
    
- cuál es el siguiente paso.
    

---

# 44. CRITERIOS DE FRACASO DEL WIREFRAME

El wireframe falla si:

- parece una app completa antes de tiempo;
    
- oculta el nivel de riesgo;
    
- oculta el estado del resultado;
    
- no muestra acciones bloqueadas;
    
- no muestra modo activo;
    
- mezcla sandbox con trabajo manual sin etiquetas;
    
- no muestra resultados parciales o inconclusos;
    
- confunde sandbox con ejecución real;
    
- permite imaginar botones de ejecución real;
    
- es demasiado complejo;
    
- no deja claro qué debe hacer el usuario después;
    
- prioriza estética sobre seguridad.
    

---

# 45. QUÉ NO AUTORIZA ESTE DOCUMENTO

Este documento no autoriza:

- programación;
    
- conexión de apps;
    
- automatizaciones;
    
- agentes autónomos;
    
- correos reales;
    
- eventos reales;
    
- contacto con clientes;
    
- edición automática de Obsidian;
    
- uso de datos personales reales;
    
- ejecución comercial real.
    

---

# 46. CAMBIOS INCLUIDOS EN LA VERSIÓN 0.2

Esta versión corrige tres puntos importantes detectados durante la revisión:

## Corrección 1 — Nivel 5 eliminado

Se eliminó “Nivel 5 — No permitido”.

Robert mantiene una escala oficial de riesgo de Nivel 1 a Nivel 4.

“No permitido” queda como estado de resultado, no como nivel de riesgo.

## Corrección 2 — Estados parciales e inconclusos agregados

Se agregaron estados visuales para:

- Parcial
    
- Parcial avanzada
    
- Inconclusa
    
- Interrumpida
    
- No permitido
    

Esto permite representar casos como la Prueba Sandbox 005.

## Corrección 3 — Historial separado por etiquetas

El historial ahora distingue visualmente entre:

- [MANUAL]
    
- [SUPERVISADO]
    
- [SANDBOX]
    
- [CONTROL]
    
- [BLOQUEADA]
    
- [PARCIAL]
    
- [DECISIÓN]
    

Esto evita confundir simulaciones con trabajo real/manual.

---

# 47. SIGUIENTE PASO

Después de reemplazar el documento con esta versión corregida, se debe hacer una revisión final.

Si el usuario lo aprueba, se puede registrar:

DECISIÓN #006 — ROBERT_TECHNICAL_MVP_WIREFRAME aprobado

Después de eso, el siguiente paso recomendado será crear:

ROBERT_CONTROL_DE_CAMBIOS

Objetivo:

Asegurar que futuras mejoras, rediseños visuales y nuevas funciones se hagan sin romper Robert.

---

# 48. ESTADO FINAL DEL DOCUMENTO

Estado:

Borrador corregido pendiente de revisión final.

Este documento solo define la estructura visual funcional.

No autoriza programación todavía.

No autoriza conexión de herramientas.

No autoriza automatizaciones.

No autoriza agentes autónomos.

---

# 49. PRINCIPIO FINAL

Primero orden.

Después interfaz.

Después pruebas.

Después programación.

Después conexiones.

Después automatización.

Robert debe verse como un sistema controlado antes de convertirse en sistema poderoso.

# REVISIÓN FINAL — ROBERT_TECHNICAL_MVP_WIREFRAME

Fecha: 29/06/2026

Documento revisado:

ROBERT_TECHNICAL_MVP_WIREFRAME

Versión revisada:

v0.2

Estado de la revisión:

Revisión final completada — pendiente de aprobación del usuario

---

# 1. OBJETIVO DE LA REVISIÓN FINAL

Esta revisión final valida si ROBERT_TECHNICAL_MVP_WIREFRAME v0.2 está listo para aprobarse como base visual funcional del MVP técnico básico de Robert.

La revisión confirma que el documento ya corrigió los huecos detectados antes de la aprobación.

Esta revisión no autoriza programación.

Solo valida el wireframe como estructura visual funcional.

---

# 2. RESULTADO GENERAL

Resultado:

ROBERT_TECHNICAL_MVP_WIREFRAME v0.2 está correctamente corregido y listo para aprobación.

El documento ya define:

- estructura general de pantalla;
    
- barra superior;
    
- panel lateral izquierdo;
    
- área central de comando;
    
- panel derecho de análisis;
    
- panel inferior de historial;
    
- modo activo;
    
- riesgo;
    
- estado del resultado;
    
- acciones permitidas;
    
- acciones bloqueadas;
    
- estados parciales;
    
- estados inconclusos;
    
- historial separado por etiquetas;
    
- modo sandbox claramente diferenciado;
    
- límites de no ejecución real.
    

---

# 3. CORRECCIONES VALIDADAS

## Corrección 1 — Nivel 5 eliminado

Estado:

Corregido.

Resultado:

Robert mantiene una sola escala oficial de riesgo:

- Nivel 1 — Bajo
    
- Nivel 2 — Medio
    
- Nivel 3 — Alto
    
- Nivel 4 — Crítico
    

“No permitido” ya no aparece como Nivel 5.

“No permitido” queda correctamente definido como estado del resultado.

---

## Corrección 2 — Riesgo separado del estado del resultado

Estado:

Corregido.

Resultado:

El wireframe ahora separa claramente:

- nivel de riesgo;
    
- estado del resultado.
    

Regla validada:

Nivel de riesgo ≠ Estado del resultado.

Ejemplo correcto:

Nivel de riesgo:

Nivel 3 — Alto.

Estado del resultado:

Parcial avanzada.

---

## Corrección 3 — Estados parciales e inconclusos agregados

Estado:

Corregido.

Resultado:

El wireframe ya incluye estados para:

- Parcial;
    
- Parcial avanzada;
    
- Inconclusa;
    
- Interrumpida;
    
- No permitido.
    

Esto permite representar correctamente casos como la Prueba Sandbox 005.

---

## Corrección 4 — Historial separado por etiquetas

Estado:

Corregido.

Resultado:

El historial ahora distingue visualmente entre:

- [MANUAL]
    
- [SUPERVISADO]
    
- [SANDBOX]
    
- [CONTROL]
    
- [BLOQUEADA]
    
- [PARCIAL]
    
- [DECISIÓN]
    

Esto evita confundir simulaciones con trabajo manual o real.

---

# 4. QUÉ QUEDA VALIDADO

El wireframe valida que Robert Command Center Lite debe mostrar:

- dónde escribe el usuario;
    
- qué modo está activo;
    
- qué entendió Robert;
    
- qué documento se relaciona;
    
- qué módulo se relaciona;
    
- qué nivel de riesgo tiene la solicitud;
    
- qué estado tiene el resultado;
    
- qué puede hacer Robert;
    
- qué no puede hacer Robert;
    
- qué acciones bloqueó;
    
- qué resultado preparó;
    
- qué quedó parcial;
    
- qué quedó inconcluso;
    
- qué fue sandbox;
    
- qué fue manual;
    
- qué fue control;
    
- cuál es el siguiente paso.
    

---

# 5. QUÉ NO AUTORIZA ESTA REVISIÓN

Esta revisión no autoriza:

- programación;
    
- conexión de apps;
    
- conexión con Gmail;
    
- conexión con Calendar;
    
- conexión con WhatsApp;
    
- conexión con CRM;
    
- conexión con Google Sheets;
    
- Zapier;
    
- Make;
    
- n8n;
    
- automatizaciones reales;
    
- agentes autónomos;
    
- correos reales;
    
- eventos reales;
    
- contacto con clientes;
    
- uso de datos personales reales;
    
- edición automática de Obsidian;
    
- ejecución comercial real.
    

---

# 6. RIESGOS RESTANTES

Aunque el wireframe está listo para aprobación, siguen activos estos riesgos:

- querer pasar a programación demasiado pronto;
    
- convertir el wireframe en app completa antes de tiempo;
    
- agregar botones de ejecución real;
    
- conectar herramientas externas sin autorización;
    
- perder separación entre manual y sandbox;
    
- meter demasiadas funciones en la primera versión;
    
- cambiar visual sin control de versiones;
    
- agregar funciones sin revisar seguridad.
    

---

# 7. RECOMENDACIÓN FINAL

Se recomienda aprobar ROBERT_TECHNICAL_MVP_WIREFRAME v0.2 como base visual funcional del MVP técnico básico.

Esta aprobación debe permitir pasar al siguiente documento:

ROBERT_CONTROL_DE_CAMBIOS

Motivo:

Antes de seguir con diseño visual, mockups, prompts para Figma, Claude, Cursor o programación, Robert necesita una regla clara para manejar cambios futuros sin romper lo ya aprobado.

---

# 8. DECISIÓN RECOMENDADA

Decisión recomendada:

Aprobar ROBERT_TECHNICAL_MVP_WIREFRAME v0.2 como base visual funcional del MVP técnico básico.

Nombre sugerido:

DECISIÓN #006 — ROBERT_TECHNICAL_MVP_WIREFRAME aprobado

Estado actual:

Pendiente de aprobación del usuario.

---

# 9. SIGUIENTE PASO SI SE APRUEBA

Si el usuario aprueba este documento, se debe registrar:

DECISIÓN #006 — ROBERT_TECHNICAL_MVP_WIREFRAME aprobado

Después se debe crear:

ROBERT_CONTROL_DE_CAMBIOS

Objetivo:

Definir cómo Robert manejará futuras mejoras, rediseños visuales, nuevas funciones, cambios de módulos, cambios de seguridad y nuevas versiones sin romper el sistema.

---

# 10. CONCLUSIÓN

ROBERT_TECHNICAL_MVP_WIREFRAME v0.2 está listo para aprobación.

El documento ya integra las correcciones necesarias sobre:

- escala oficial de riesgo;
    
- estados de resultado;
    
- resultados parciales;
    
- resultados inconclusos;
    
- historial diferenciado;
    
- separación entre sandbox y trabajo manual.
    

Resultado final:

Aprobable como wireframe funcional inicial.

No autoriza programación.

No autoriza conexiones.

No autoriza automatizaciones.

No autoriza agentes autónomos.

Autoriza únicamente usar este wireframe como base visual funcional del MVP técnico básico.
