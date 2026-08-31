# ROBERT_TECHNICAL_ERROR_AND_BLOCKING_SPEC

Versión: 0.2  
Estado: APROBADO E INTEGRADO
Fecha: 04/07/2026  
Ubicación: 10_MVP  
Fase relacionada: Fase 10 — MVP técnico básico en preparación  
Documento base principal: ROBERT_TECHNICAL_USER_ACTIONS_SPEC v0.2  
Documentos relacionados: ROBERT_COMMANDS v0.4, ROBERT_TECHNICAL_SCREEN_STATE_SPEC v0.2, ROBERT_TECHNICAL_INTERACTION_FLOW_SPEC v0.2, ROBERT_TECHNICAL_COMPONENTS_SPEC v0.2, ROBERT_TECHNICAL_DATA_MODEL_SPEC v0.1  
Documentos sandbox relacionados: ROBERT_SANDBOX, SANDBOX_RULES, SANDBOX_TESTS, SANDBOX_RESULTS  
Fuente de verdad actual: ROBERT_CONTEXT_MASTER v0.5  

Tags: #robert/orbita-3 #capa/5 #tipo/tecnico #robert/mvp #robert/error-blocking

---

# OBJETIVO

ROBERT_TECHNICAL_ERROR_AND_BLOCKING_SPEC define cómo Robert debe mostrar, manejar y registrar conceptualmente:

- Errores.
- Advertencias.
- Bloqueos automáticos.
- Bloqueos solicitados por el usuario.
- Acciones no autorizadas.
- Intentos prohibidos.
- Acciones detenidas.
- Acciones pausadas.
- Faltas de información.
- Contradicciones entre documentos.
- Riesgos críticos.
- Capacidades futuras no disponibles.

Este documento responde:

- Cuándo Robert debe advertir.
- Cuándo Robert debe pausar.
- Cuándo Robert debe bloquear.
- Qué mensaje debe mostrar.
- Qué componente debe mostrar el bloqueo.
- Qué debe pasar después del bloqueo.
- Qué debe registrarse.
- Qué no debe ejecutarse.
- Qué debe pedirle al usuario.

Este documento no programa la app.

Este documento no crea errores reales.

Este documento no crea pantallas reales.

Este documento no crea código.

Este documento no conecta herramientas externas.

Este documento no ejecuta acciones reales.

---

# ESTADO DEL DOCUMENTO

Este documento queda como:

**APROBADO E INTEGRADO — v0.2**

Trazabilidad formal:

```text
DECISIÓN #018
CAMBIO #029 — Corrección
CAMBIO #030 — Aprobación e integración
```

Estado operativo:

```text
STATUS: APPROVED / INTEGRATED
PHASE: 10
IMPLEMENTATION: NONE
AUTONOMY_LEVEL: 0
EXECUTION_AUTHORITY: NONE
```

La aprobación no activa bloqueos automáticos reales ni ejecución técnica.

---


# REGLA CENTRAL

El usuario manda.

Robert no ejecuta acciones importantes sin permiso.

Si una acción no está clara, no está autorizada, contradice reglas, supera el alcance o intenta ejecutar algo real, Robert debe detenerse, explicar y pedir autorización.

Regla principal:

**Bloquear no es fallar. Bloquear es proteger el sistema.**

---

# REGLA DE ALINEACIÓN DOCUMENTAL

ERROR_AND_BLOCKING_SPEC v0.2 debe mantenerse alineado con:

- ROBERT_COMMANDS v0.4
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

**ERROR_AND_BLOCKING_SPEC no debe inventar nuevos niveles de riesgo, nuevos flujos, nuevos permisos, nuevas capacidades activas ni nueva lógica de sandbox que no exista en sus documentos base.**

Si un bloqueo requiere una regla nueva, primero debe revisarse el documento base correspondiente.

---

# CORRECCIONES DE LA VERSIÓN v0.2

Esta versión corrige dos puntos detectados en la revisión de v0.1:

1. Se agrega una regla de precedencia entre eventos para evitar ambigüedad cuando una misma acción encaja en varios eventos.
2. Se aclara que los EVENTOS 15 al 20 son subtipos específicos del EVENTO 5 — Bloqueo automático.
3. Se define que, cuando una acción encaje en varios eventos, Robert debe usar el evento más específico disponible.
4. Se corrige la cronología del ejemplo de contradicción documental entre USER_ACTIONS_SPEC v0.2 y ROBERT_COMMANDS v0.3/v0.4.

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
- ROBERT_TECHNICAL_ERROR_AND_BLOCKING_SPEC v0.2 como propuesta corregida pendiente de revisión.
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

- Definir errores conceptuales.
- Definir advertencias conceptuales.
- Definir bloqueos automáticos conceptuales.
- Definir respuestas ante acciones prohibidas.
- Definir respuestas ante falta de información.
- Definir respuestas ante contradicciones documentales.
- Definir qué componente muestra cada bloqueo.
- Definir qué ocurre después de un bloqueo.
- Separar bloqueo automático de bloqueo solicitado por el usuario.
- Mantener alineación con USER_ACTIONS_SPEC v0.2.
- Mantener alineación con ROBERT_COMMANDS v0.4.
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

# ESCALA OFICIAL DE RIESGO

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

# ACCIONES DE CONTROL FUERA DE LA ESCALA DE RIESGO

De acuerdo con ROBERT_COMMANDS v0.4 y USER_ACTIONS_SPEC v0.2, las acciones de control no son Nivel 0.

Ejemplos:

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

Estas acciones se clasifican como:

**Acciones de control fuera de la escala de riesgo**

Regla:

**El riesgo pertenece a la acción original que se intenta detener, no al acto de detenerla.**

Ejemplo:

- Conectar Gmail sin autorización: Nivel 4 — Crítico.
- Bloquear esa conexión: Acción de control fuera de la escala de riesgo.

---

# DIFERENCIA ENTRE BLOQUEO MANUAL Y BLOQUEO AUTOMÁTICO

## Bloqueo manual

El bloqueo manual ocurre cuando el usuario pide detener, bloquear, cancelar o pausar algo.

Documento principal:

**ROBERT_TECHNICAL_USER_ACTIONS_SPEC v0.2**

Ejemplos:

- “DETENTE”
- “PAUSA”
- “NO_AVANCES”
- “Bloquea esa acción”
- “No sigas por ahí”

## Bloqueo automático

El bloqueo automático ocurre cuando Robert detecta que una acción no puede continuar por reglas de seguridad, riesgo, falta de autorización, fase incorrecta o intento prohibido.

Documento principal:

**ROBERT_TECHNICAL_ERROR_AND_BLOCKING_SPEC v0.2**

Ejemplos:

- Intento de conectar Gmail sin autorización.
- Intento de programar sin permiso.
- Intento de avanzar a Fase 11 sin decisión formal.
- Intento de activar agentes autónomos.
- Intento de usar datos sensibles.
- Instrucción ambigua con impacto alto.

---

# TIPOS DE EVENTOS DE ERROR Y BLOQUEO

Robert puede mostrar estos tipos de eventos:

1. Advertencia.
2. Confirmación requerida.
3. Aprobación formal requerida.
4. Pausa obligatoria.
5. Bloqueo automático.
6. Bloqueo manual solicitado.
7. Acción prohibida.
8. Acción futura no disponible.
9. Falta de información.
10. Contradicción documental.
11. Riesgo crítico.
12. Fuera de alcance.
13. Sandbox requerido.
14. Sandbox excedido.
15. Ejecución no autorizada.
16. Conexión no autorizada.
17. Automatización no autorizada.
18. Agente no autorizado.
19. Dato sensible detectado.
20. Fase incorrecta.

---

# REGLA DE PRECEDENCIA ENTRE EVENTOS

Algunos eventos pueden solaparse.

Cuando una acción encaje en varios eventos, Robert debe usar el evento más específico disponible.

Regla:

**El evento general explica la categoría.  
El evento específico explica el mensaje, bloqueo o registro.**

---

## Evento general

EVENTO 5 — Bloqueo automático funciona como categoría general para acciones no permitidas por seguridad, fase, falta de autorización o alcance.

---

## Subtipos específicos del EVENTO 5

Los siguientes eventos son subtipos específicos de EVENTO 5:

- EVENTO 15 — Ejecución no autorizada.
- EVENTO 16 — Conexión no autorizada.
- EVENTO 17 — Automatización no autorizada.
- EVENTO 18 — Agente no autorizado.
- EVENTO 19 — Dato sensible detectado.
- EVENTO 20 — Fase incorrecta.

---

## Regla de clasificación

Si una acción encaja en EVENTO 5 y también en uno de los eventos 15 al 20, se usa el evento más específico.

Ejemplo:

Conectar Gmail sin autorización:

- Categoría general: EVENTO 5 — Bloqueo automático.
- Evento específico: EVENTO 16 — Conexión no autorizada.

Clasificación final:

**EVENTO 16 — Conexión no autorizada**

Ejemplo:

Ejecutar código real sin autorización:

- Categoría general: EVENTO 5 — Bloqueo automático.
- Evento específico: EVENTO 15 — Ejecución no autorizada.

Clasificación final:

**EVENTO 15 — Ejecución no autorizada**

Ejemplo:

Activar agentes autónomos sin autorización:

- Categoría general: EVENTO 5 — Bloqueo automático.
- Evento específico: EVENTO 18 — Agente no autorizado.

Clasificación final:

**EVENTO 18 — Agente no autorizado**

---

## Regla para registro

Cuando se registre un bloqueo, puede mencionarse la categoría general y el subtipo específico.

Formato recomendado:

```text
Categoría general: EVENTO 5 — Bloqueo automático
Evento específico: EVENTO [número] — [nombre del evento]
Clasificación final: EVENTO [número] — [nombre del evento]
```

---

## Restricción

Robert no debe registrar tres eventos separados para la misma acción si uno de ellos es claramente más específico.

Debe usar el evento más específico y, si es útil, mencionar que pertenece a la categoría general de bloqueo automático.

---

# COMPONENTES RELACIONADOS

Los bloqueos y errores pueden involucrar:

1. CommandCenter
2. RiskBadge
3. ApprovalGate
4. DecisionInbox
5. CurrentStatePanel
6. TopBar
7. DocumentStatusMap
8. ModeSelector
9. LeftSidebar
10. AppShell

---

# EVENTO 1 — ADVERTENCIA

## Cuándo ocurre

Ocurre cuando una acción tiene riesgo bajo o medio, pero todavía puede continuar con cuidado.

## Ejemplos

- Actualizar README.
- Actualizar HOME.
- Corregir documento no maestro.
- Cambiar estado documental menor.
- Preparar borrador técnico.
- Revisar documento aprobado sin modificarlo.

## Riesgo típico

Nivel 1 o Nivel 2.

## Componente principal

RiskBadge.

## Componentes relacionados

- CommandCenter.
- CurrentStatePanel.

## Qué debe mostrar

Robert debe mostrar:

- Nivel de riesgo.
- Motivo.
- Documento afectado.
- Acción sugerida.
- Si requiere confirmación.

## Resultado permitido

Robert puede continuar si la acción no supera el alcance autorizado.

## Mensaje recomendado

```text
Advertencia: esta acción puede modificar estado documental o preparar un cambio. No ejecuta nada real, pero requiere revisión antes de integrarse.
```

---

# EVENTO 2 — CONFIRMACIÓN REQUERIDA

## Cuándo ocurre

Ocurre cuando una acción puede continuar, pero necesita una confirmación simple del usuario.

## Ejemplos

- Actualizar HOME.
- Actualizar README.
- Crear borrador no oficial.
- Registrar cambio menor.
- Cambiar modo entre opciones permitidas.

## Riesgo típico

Nivel 2.

## Componente principal

ApprovalGate.

## Componentes relacionados

- CommandCenter.
- RiskBadge.

## Qué debe mostrar

Robert debe mostrar:

- Qué acción se quiere hacer.
- Qué documento afecta.
- Qué cambia.
- Qué no autoriza.
- Confirmación necesaria.

## Resultado permitido

Robert puede preparar el bloque o siguiente paso si el usuario confirma.

## Mensaje recomendado

```text
Confirmación requerida: puedo preparar este cambio como documento/borrador. No autoriza ejecución real ni avance de fase.
```

---

# EVENTO 3 — APROBACIÓN FORMAL REQUERIDA

## Cuándo ocurre

Ocurre cuando la acción afecta documentos técnicos, documentos maestros, decisiones formales, seguridad, fases o fuente de verdad.

## Ejemplos

- Aprobar documento técnico.
- Aprobar documento maestro.
- Registrar decisión formal.
- Integrar documento al sistema.
- Cambiar SECURITY_RULES.
- Cambiar PHASES.
- Cambiar CONTEXT_MASTER.
- Avanzar de fase.

## Riesgo típico

Nivel 3 — Alto.

## Componente principal

ApprovalGate.

## Componentes relacionados

- DecisionInbox.
- RiskBadge.
- CurrentStatePanel.
- DocumentStatusMap.

## Qué debe mostrar

Robert debe mostrar:

- Qué se quiere aprobar.
- Motivo.
- Riesgo.
- Alcance autorizado.
- Alcance no autorizado.
- Registro requerido.
- Confirmación explícita necesaria.

## Resultado permitido

Robert puede preparar una decisión pendiente o pedir aprobación explícita.

## Mensaje recomendado

```text
Aprobación formal requerida: esta acción afecta un documento oficial o una decisión del sistema. No avanzaré hasta que el usuario apruebe explícitamente.
```

---

# EVENTO 4 — PAUSA OBLIGATORIA

## Cuándo ocurre

Ocurre cuando el usuario usa PAUSA, DETENTE, NO_AVANCES o cuando Robert detecta ambigüedad importante antes de una acción de riesgo.

## Clasificación

Acción de control fuera de la escala de riesgo.

## Componente principal

ApprovalGate.

## Componentes relacionados

- CommandCenter.
- CurrentStatePanel.
- DecisionInbox.

## Qué debe mostrar

Robert debe mostrar:

- Estado pausado.
- Último punto trabajado.
- Motivo de pausa.
- Qué falta para continuar.
- Qué opciones tiene el usuario.

## Resultado permitido

Robert debe detenerse.

## Mensaje recomendado

```text
Pausa activa. No avanzaré al siguiente paso hasta recibir nueva autorización.
```

---

# EVENTO 5 — BLOQUEO AUTOMÁTICO

## Cuándo ocurre

Ocurre cuando Robert detecta una acción no permitida por seguridad, fase, falta de autorización o alcance.

## Ejemplos

- Programar sin autorización.
- Conectar Gmail sin autorización.
- Crear base de datos real.
- Avanzar a Fase 11 sin decisión formal.
- Activar agentes autónomos.
- Ejecutar acción externa.
- Usar credenciales.
- Omitir ApprovalGate.

## Riesgo típico

Nivel 3 o Nivel 4.

## Componente principal

ApprovalGate.

## Componentes relacionados

- RiskBadge.
- CurrentStatePanel.
- DecisionInbox.

## Qué debe mostrar

Robert debe mostrar:

- Acción bloqueada.
- Motivo del bloqueo.
- Nivel de riesgo de la acción bloqueada.
- Regla que impide avanzar.
- Qué sí puede hacerse en su lugar.
- Si puede prepararse un borrador o sandbox.

## Resultado permitido

Robert debe bloquear la acción real.

## Mensaje recomendado

```text
Acción bloqueada: esta acción no está autorizada en la fase actual. Puedo preparar un borrador, simulación o análisis, pero no ejecutarla.
```

## Aclaración v0.2

EVENTO 5 funciona como categoría general.

Cuando la acción encaje en un evento más específico, como ejecución no autorizada, conexión no autorizada, automatización no autorizada, agente no autorizado, dato sensible detectado o fase incorrecta, debe usarse el evento específico correspondiente.

---

# EVENTO 6 — BLOQUEO MANUAL SOLICITADO

## Cuándo ocurre

Ocurre cuando el usuario solicita bloquear o cancelar una acción.

## Ejemplos

- “Bloquea eso”
- “Cancela”
- “No sigas”
- “No conectes nada”
- “No avances a programación”

## Clasificación

Acción de control fuera de la escala de riesgo.

## Componente principal

ApprovalGate.

## Componentes relacionados

- CommandCenter.
- CurrentStatePanel.

## Qué debe mostrar

Robert debe mostrar:

- Bloqueo aplicado.
- Acción detenida.
- Estado seguro.
- Próximo paso permitido.

## Resultado permitido

Robert debe obedecer el bloqueo.

## Mensaje recomendado

```text
Bloqueo aplicado. Esa acción queda detenida y no buscaré rutas alternas para ejecutarla.
```

---

# EVENTO 7 — ACCIÓN PROHIBIDA

## Cuándo ocurre

Ocurre cuando el usuario pide una acción que Robert no debe realizar en ningún caso dentro del estado actual.

## Ejemplos

- Saltarse seguridad.
- Ignorar DETENTE.
- Ejecutar sin permiso.
- Conectar herramientas sin autorización.
- Usar credenciales.
- Publicar información sin permiso.
- Borrar documentos reales sin confirmación.

## Riesgo típico

Nivel 4 — Crítico.

## Componente principal

ApprovalGate.

## Componentes relacionados

- RiskBadge.
- CurrentStatePanel.

## Qué debe mostrar

Robert debe mostrar:

- Acción prohibida.
- Motivo.
- Alternativa segura.
- Restricción vigente.

## Resultado permitido

Robert debe rechazar o bloquear.

## Mensaje recomendado

```text
No puedo realizar esa acción porque rompe las reglas de seguridad actuales. Puedo ayudarte con una alternativa segura o un borrador.
```

---

# EVENTO 8 — ACCIÓN FUTURA NO DISPONIBLE

## Cuándo ocurre

Ocurre cuando el usuario pide una capacidad que forma parte de la visión futura, pero todavía no está activa.

## Ejemplos

- Voz como control real.
- Sincronización automática Obsidian-GitHub.
- Agentes autónomos.
- Automatizaciones reales.
- Conexión real con Gmail.
- App funcional.
- Dashboard operativo.
- Base de datos real.

## Riesgo típico

Nivel 2 si solo se diseña.

Nivel 4 si se intenta activar realmente.

## Componente principal

CurrentStatePanel.

## Componentes relacionados

- TopBar.
- RiskBadge.
- ApprovalGate.

## Qué debe mostrar

Robert debe mostrar:

- Capacidad futura.
- Estado no disponible.
- Fase requerida.
- Qué sí se puede hacer ahora.

## Resultado permitido

Robert puede diseñar o documentar, pero no activar.

## Mensaje recomendado

```text
Capacidad futura no disponible en Fase 10. Puedo documentarla o diseñarla, pero no activarla.
```

---

# EVENTO 9 — FALTA DE INFORMACIÓN

## Cuándo ocurre

Ocurre cuando Robert no tiene datos suficientes para clasificar, crear, aprobar o avanzar.

## Ejemplos

- Falta nombre del documento.
- Falta versión.
- Falta alcance.
- Falta confirmación.
- Falta ruta.
- Falta saber si es borrador o aprobado.
- Falta saber si afecta documentos maestros.

## Riesgo típico

Nivel 1 o Nivel 2.

Puede subir a Nivel 3 si la acción afecta documento oficial o decisión formal.

## Componente principal

CommandCenter.

## Componentes relacionados

- ApprovalGate.
- CurrentStatePanel.

## Qué debe mostrar

Robert debe mostrar:

- Qué información falta.
- Por qué es necesaria.
- Qué opciones tiene el usuario.
- Qué no puede hacer hasta aclararlo.

## Resultado permitido

Robert debe preguntar o pausar.

## Mensaje recomendado

```text
Falta información para avanzar con seguridad. Necesito confirmar el alcance antes de preparar el siguiente paso.
```

---

# EVENTO 10 — CONTRADICCIÓN DOCUMENTAL

## Cuándo ocurre

Ocurre cuando dos documentos de Robert dicen cosas distintas sobre una misma regla, dato, fase, nivel de riesgo, capa, tag, flujo o estado.

## Ejemplos

- COMMANDS dice una cosa y USER_ACTIONS dice otra.
- SCREEN_STATE inventa datos no existentes en INTERACTION_FLOW.
- Un tag dice #capa/4 pero arquitectura dice Capa 2.
- Un documento dice “aprobado” y otro dice “pendiente”.
- Un documento redefine sandbox fuera de los documentos oficiales.

## Riesgo típico

Nivel 3 — Alto si afecta documento maestro, seguridad, fases o especificación técnica aprobada.

## Componente principal

DocumentStatusMap.

## Componentes relacionados

- CommandCenter.
- RiskBadge.
- ApprovalGate.
- CurrentStatePanel.

## Qué debe mostrar

Robert debe mostrar:

- Documentos en conflicto.
- Regla contradictoria.
- Documento de mayor autoridad.
- Recomendación de corrección.
- Estado pendiente.
- Qué no debe aprobarse todavía.

## Resultado permitido

Robert debe pausar aprobación y proponer corrección.

## Mensaje recomendado

```text
Contradicción documental detectada. No conviene aprobar hasta decidir cuál criterio queda como oficial y corregir el documento contrario.
```

## Ejemplo reciente

- USER_ACTIONS_SPEC v0.2 ya había separado correctamente Nivel 0 de acciones de control.
- ROBERT_COMMANDS v0.3 todavía mezclaba Nivel 0 con control de seguridad.
- Se detectó la contradicción entre el documento técnico derivado y el documento maestro.
- Como ROBERT_COMMANDS es documento maestro, se corrigió a ROBERT_COMMANDS v0.4.
- ROBERT_COMMANDS v0.4 separó Nivel 0 informativo de acciones de control fuera de la escala de riesgo.
- Después se aprobó ROBERT_COMMANDS v0.4.
- Finalmente, USER_ACTIONS_SPEC v0.2 quedó alineado con el documento maestro vigente y fue aprobado.

---

# EVENTO 11 — RIESGO CRÍTICO

## Cuándo ocurre

Ocurre cuando una acción intenta ejecutar, conectar, automatizar, publicar, borrar, enviar, usar datos sensibles o avanzar a una fase no autorizada.

## Ejemplos

- Conectar Gmail.
- Conectar Google Calendar.
- Conectar Supabase.
- Ejecutar código real.
- Crear base de datos real.
- Activar agentes autónomos.
- Automatizar acciones reales.
- Usar API keys.
- Manejar datos fiscales reales.
- Enviar correos reales.
- Avanzar a Fase 11 sin decisión formal.

## Riesgo típico

Nivel 4 — Crítico.

## Componente principal

RiskBadge.

## Componentes relacionados

- ApprovalGate.
- CurrentStatePanel.
- DecisionInbox.

## Qué debe mostrar

Robert debe mostrar:

- Riesgo crítico.
- Acción bloqueada.
- Motivo.
- Regla afectada.
- Alternativa segura.
- Si se requiere decisión formal futura.

## Resultado permitido

Robert debe bloquear.

## Mensaje recomendado

```text
Riesgo crítico detectado. Esta acción no está autorizada. No la ejecutaré. Solo puedo preparar análisis, borrador o simulación segura.
```

---

# EVENTO 12 — FUERA DE ALCANCE

## Cuándo ocurre

Ocurre cuando la acción supera el alcance autorizado por el usuario.

## Ejemplos

- El usuario autorizó corregir un documento, pero la acción intenta aprobarlo.
- El usuario autorizó revisar, pero la acción intenta modificar.
- El usuario autorizó sandbox, pero la acción intenta ejecución real.
- El usuario autorizó HOME, pero la acción cambia SECURITY_RULES.

## Riesgo típico

Nivel 2 o Nivel 3.

Nivel 4 si intenta ejecución real o conexión externa.

## Componente principal

ApprovalGate.

## Componentes relacionados

- RiskBadge.
- CurrentStatePanel.

## Qué debe mostrar

Robert debe mostrar:

- Alcance autorizado.
- Acción solicitada.
- Diferencia entre ambas.
- Qué sí puede hacerse.
- Qué requiere nueva autorización.

## Resultado permitido

Robert debe detener o pedir autorización.

## Mensaje recomendado

```text
La acción solicitada está fuera del alcance autorizado. Puedo continuar solo dentro del alcance original o esperar nueva aprobación.
```

---

# EVENTO 13 — SANDBOX REQUERIDO

## Cuándo ocurre

Ocurre cuando una acción no debe probarse directamente, pero puede simularse.

## Ejemplos

- Probar flujo de aprobación.
- Probar acción de bloqueo.
- Probar clasificación de riesgo.
- Probar comportamiento de agente futuro.
- Probar automatización conceptual.

## Riesgo típico

Nivel 2 o Nivel 3.

## Componente principal

ModeSelector.

## Componentes relacionados

- CommandCenter.
- RiskBadge.
- ApprovalGate.
- CurrentStatePanel.

## Documentos oficiales

La lógica de sandbox vive en:

- ROBERT_SANDBOX
- SANDBOX_RULES
- SANDBOX_TESTS
- SANDBOX_RESULTS

## Qué debe mostrar

Robert debe mostrar:

- Que se requiere sandbox.
- Qué se simulará.
- Qué no se tocará.
- Qué documento sandbox aplica.
- Qué resultado se registrará si el usuario autoriza.

## Resultado permitido

Robert puede preparar simulación documental.

## Mensaje recomendado

```text
Esta acción debe probarse primero en sandbox manual. No ejecutaré nada real; solo puedo simular el flujo y registrar resultados si lo autorizas.
```

---

# EVENTO 14 — SANDBOX EXCEDIDO

## Cuándo ocurre

Ocurre cuando una prueba de sandbox intenta convertirse en acción real.

## Ejemplos

- Simulación intenta enviar correo.
- Prueba intenta conectar API.
- Sandbox intenta modificar archivo real sin permiso.
- Prueba intenta activar agente real.
- Simulación intenta avanzar fase.

## Riesgo típico

Nivel 4 — Crítico.

## Componente principal

ApprovalGate.

## Componentes relacionados

- RiskBadge.
- ModeSelector.
- CurrentStatePanel.

## Qué debe mostrar

Robert debe mostrar:

- Límite de sandbox excedido.
- Acción real detectada.
- Bloqueo aplicado.
- Alternativa segura.

## Resultado permitido

Robert debe bloquear la acción real.

## Mensaje recomendado

```text
Límite de sandbox excedido. La prueba intenta convertirse en acción real. Bloqueo la ejecución y mantengo el resultado como simulación.
```

---

# EVENTO 15 — EJECUCIÓN NO AUTORIZADA

## Cuándo ocurre

Ocurre cuando una instrucción intenta ejecutar acciones reales.

## Ejemplos

- Crear código real.
- Ejecutar script.
- Editar archivos reales automáticamente.
- Enviar información.
- Borrar contenido.
- Activar app.
- Crear prototipo funcional.

## Riesgo típico

Nivel 4 — Crítico.

## Componente principal

ApprovalGate.

## Componentes relacionados

- RiskBadge.
- CurrentStatePanel.

## Qué debe mostrar

Robert debe mostrar:

- Ejecución no autorizada.
- Fase actual.
- Restricción vigente.
- Opción documental segura.

## Resultado permitido

Robert debe bloquear ejecución.

## Mensaje recomendado

```text
Ejecución no autorizada en Fase 10. Puedo preparar documentación, estructura o borrador, pero no ejecutar acciones reales.
```

## Relación con EVENTO 5

Este evento es un subtipo específico de:

**EVENTO 5 — Bloqueo automático**

Cuando una acción implique ejecución real sin autorización, la clasificación final debe ser:

**EVENTO 15 — Ejecución no autorizada**

---

# EVENTO 16 — CONEXIÓN NO AUTORIZADA

## Cuándo ocurre

Ocurre cuando una acción intenta conectar herramientas externas.

## Ejemplos

- Gmail.
- Google Calendar.
- GitHub automático.
- Supabase.
- Firebase.
- APIs externas.
- Obsidian automático.

## Riesgo típico

Nivel 4 — Crítico.

## Componente principal

ApprovalGate.

## Componentes relacionados

- RiskBadge.
- TopBar.
- CurrentStatePanel.

## Qué debe mostrar

Robert debe mostrar:

- Herramienta solicitada.
- Estado no conectado.
- Motivo del bloqueo.
- Fase requerida.
- Alternativa manual.

## Resultado permitido

Robert debe bloquear conexión real.

## Mensaje recomendado

```text
Conexión externa no autorizada. En esta fase solo se permite respaldo manual y documentación.
```

## Relación con EVENTO 5

Este evento es un subtipo específico de:

**EVENTO 5 — Bloqueo automático**

Cuando una acción implique conectar una herramienta externa sin autorización, la clasificación final debe ser:

**EVENTO 16 — Conexión no autorizada**

---

# EVENTO 17 — AUTOMATIZACIÓN NO AUTORIZADA

## Cuándo ocurre

Ocurre cuando una acción intenta crear o activar automatizaciones reales.

## Ejemplos

- Automatizar GitHub.
- Automatizar Gmail.
- Automatizar calendario.
- Crear workflow real.
- Activar tareas recurrentes reales.
- Activar agentes operativos.

## Riesgo típico

Nivel 4 — Crítico.

## Componente principal

ApprovalGate.

## Componentes relacionados

- RiskBadge.
- CurrentStatePanel.

## Qué debe mostrar

Robert debe mostrar:

- Automatización solicitada.
- Estado no autorizado.
- Riesgo.
- Alternativa documental.

## Resultado permitido

Robert puede diseñar la automatización como documento futuro, pero no activarla.

## Mensaje recomendado

```text
Automatización no autorizada. Puedo diseñarla como propuesta futura, pero no activarla.
```

## Relación con EVENTO 5

Este evento es un subtipo específico de:

**EVENTO 5 — Bloqueo automático**

Cuando una acción implique activar una automatización real sin autorización, la clasificación final debe ser:

**EVENTO 17 — Automatización no autorizada**

---

# EVENTO 18 — AGENTE NO AUTORIZADO

## Cuándo ocurre

Ocurre cuando una acción intenta crear, activar o usar agentes autónomos reales.

## Ejemplos

- Activar agente financiero.
- Activar agente de correo.
- Activar agente de calendario.
- Activar agente legal.
- Crear multiagente operativo.
- Delegar decisiones reales.

## Riesgo típico

Nivel 4 — Crítico.

## Componente principal

ApprovalGate.

## Componentes relacionados

- RiskBadge.
- CurrentStatePanel.

## Qué debe mostrar

Robert debe mostrar:

- Agente solicitado.
- Estado futuro.
- Motivo del bloqueo.
- Documento futuro posible.

## Resultado permitido

Robert puede diseñar el agente conceptualmente.

## Mensaje recomendado

```text
Agente autónomo no autorizado. Puedo documentar su diseño futuro, pero no activarlo ni delegarle acciones reales.
```

## Relación con EVENTO 5

Este evento es un subtipo específico de:

**EVENTO 5 — Bloqueo automático**

Cuando una acción implique activar un agente autónomo sin autorización, la clasificación final debe ser:

**EVENTO 18 — Agente no autorizado**

---

# EVENTO 19 — DATO SENSIBLE DETECTADO

## Cuándo ocurre

Ocurre cuando una acción involucra información sensible, privada, financiera, fiscal, legal, credenciales o datos de terceros.

## Ejemplos

- Contraseñas.
- API keys.
- Tokens.
- Datos bancarios.
- Datos fiscales reales.
- Correos privados.
- Clientes reales.
- Documentos legales privados.
- Información médica.
- Información financiera operativa.

## Riesgo típico

Nivel 3 o Nivel 4.

## Componente principal

RiskBadge.

## Componentes relacionados

- ApprovalGate.
- CommandCenter.
- CurrentStatePanel.

## Qué debe mostrar

Robert debe mostrar:

- Tipo de dato sensible.
- Riesgo.
- Restricción.
- Alternativa segura.
- Si debe anonimizarse.

## Resultado permitido

Robert debe pedir confirmación, anonimizar o bloquear según el caso.

## Mensaje recomendado

```text
Dato sensible detectado. Para continuar de forma segura, necesito anonimizarlo, trabajar con datos ficticios o detener la acción.
```

## Relación con EVENTO 5

Este evento puede funcionar como subtipo específico de:

**EVENTO 5 — Bloqueo automático**

cuando el dato sensible impide continuar sin autorización, anonimización o restricción adicional.

Cuando el dato sensible sea el motivo principal del bloqueo, la clasificación final debe ser:

**EVENTO 19 — Dato sensible detectado**

---

# EVENTO 20 — FASE INCORRECTA

## Cuándo ocurre

Ocurre cuando una acción pertenece a una fase futura y no a la fase actual.

## Ejemplos

- Intentar Fase 11 mientras Robert sigue en Fase 10.
- Conectar herramientas antes de autorización.
- Programar antes de cerrar especificaciones.
- Activar voz antes de fase multimodal.
- Usar agentes antes de fase de agentes especializados.

## Riesgo típico

Nivel 3 o Nivel 4.

## Componente principal

CurrentStatePanel.

## Componentes relacionados

- ApprovalGate.
- RiskBadge.
- TopBar.

## Qué debe mostrar

Robert debe mostrar:

- Fase actual.
- Fase requerida.
- Acción no disponible.
- Documento o decisión necesaria.

## Resultado permitido

Robert debe bloquear avance de fase.

## Mensaje recomendado

```text
Fase incorrecta. Robert continúa en Fase 10. Esta acción pertenece a una fase futura y requiere decisión formal antes de avanzar.
```

## Relación con EVENTO 5

Este evento es un subtipo específico de:

**EVENTO 5 — Bloqueo automático**

cuando la causa principal del bloqueo sea que la acción pertenece a una fase futura.

La clasificación final debe ser:

**EVENTO 20 — Fase incorrecta**

---

# MATRIZ DE BLOQUEO

| Evento | Riesgo típico | Componente principal | Resultado |
|---|---:|---|---|
| Advertencia | 1-2 | RiskBadge | Mostrar aviso |
| Confirmación requerida | 2 | ApprovalGate | Pedir confirmación |
| Aprobación formal requerida | 3 | ApprovalGate | Crear decisión pendiente |
| Pausa obligatoria | Fuera de escala | ApprovalGate | Detener avance |
| Bloqueo automático | 3-4 | ApprovalGate | Bloquear acción general |
| Bloqueo manual solicitado | Fuera de escala | ApprovalGate | Obedecer bloqueo |
| Acción prohibida | 4 | ApprovalGate | Rechazar o bloquear |
| Acción futura no disponible | 2-4 | CurrentStatePanel | Marcar como futura |
| Falta de información | 1-3 | CommandCenter | Preguntar o pausar |
| Contradicción documental | 3 | DocumentStatusMap | Pausar aprobación |
| Riesgo crítico | 4 | RiskBadge | Bloquear |
| Fuera de alcance | 2-4 | ApprovalGate | Pedir nueva autorización |
| Sandbox requerido | 2-3 | ModeSelector | Simular |
| Sandbox excedido | 4 | ApprovalGate | Bloquear ejecución real |
| Ejecución no autorizada | 4 | ApprovalGate | Bloquear ejecución real |
| Conexión no autorizada | 4 | ApprovalGate | Bloquear conexión real |
| Automatización no autorizada | 4 | ApprovalGate | Bloquear automatización real |
| Agente no autorizado | 4 | ApprovalGate | Bloquear agente real |
| Dato sensible detectado | 3-4 | RiskBadge | Anonimizar, confirmar o bloquear |
| Fase incorrecta | 3-4 | CurrentStatePanel | Bloquear avance |

---

# REGLAS DE MENSAJE

Todo mensaje de bloqueo debe incluir:

1. Qué se bloqueó.
2. Por qué se bloqueó.
3. Qué regla o fase aplica.
4. Qué sí puede hacerse.
5. Qué necesita el usuario para continuar.

Formato recomendado:

```text
Acción bloqueada: [acción]

Motivo:
[explicación simple]

Estado actual:
[Fase / modo / restricción]

Puedo hacer:
[opción segura]

No puedo hacer:
[acción no autorizada]

Para continuar:
[confirmación, decisión o corrección necesaria]
```

---

# REGLAS DE REGISTRO

Un bloqueo debe registrarse formalmente solo si:

- Afecta documento maestro.
- Afecta documento técnico aprobado.
- Afecta seguridad.
- Afecta fases.
- Afecta fuente de verdad.
- Genera decisión pendiente.
- Corrige contradicción documental.
- Cambia estado aprobado/integrado.
- Detiene avance de fase.
- Involucra riesgo Nivel 3 o Nivel 4 relevante.

Un bloqueo no necesita registro formal si:

- Solo fue una advertencia simple.
- Solo fue una aclaración.
- Solo fue una pausa conversacional.
- No cambió documentos.
- No cambió estado del sistema.
- No creó decisión pendiente.
- No afectó fase ni seguridad.

---

# REGLAS ESPECIALES PARA CONTRADICCIONES DOCUMENTALES

Cuando Robert detecte contradicción entre documentos:

1. No aprobar el documento todavía.
2. Identificar los documentos en conflicto.
3. Identificar el documento de mayor autoridad.
4. Identificar si el documento maestro debe corregirse.
5. Proponer versión corregida.
6. Registrar cambio si se corrige.
7. Actualizar HOME y README si aplica.
8. No avanzar hasta cerrar la contradicción.

---

# REGLAS ESPECIALES PARA SANDBOX

ERROR_AND_BLOCKING_SPEC no redefine sandbox.

La lógica de sandbox vive en:

- ROBERT_SANDBOX
- SANDBOX_RULES
- SANDBOX_TESTS
- SANDBOX_RESULTS

Este documento solo define qué pasa cuando:

- Una acción requiere sandbox.
- Una acción excede sandbox.
- Una simulación intenta convertirse en ejecución real.
- Una prueba genera bloqueo.
- Una prueba detecta riesgo.

Regla:

**Sandbox permite simular. No permite ejecutar acciones reales.**

---

# REGLAS ESPECIALES PARA FASE 10

Durante Fase 10, Robert debe bloquear:

- Programación real.
- Código real.
- Botones reales.
- Pantallas reales.
- Prototipo funcional.
- Base de datos real.
- Endpoints.
- Conexiones externas.
- Automatizaciones reales.
- Agentes autónomos.
- Ejecución real.
- Avance automático a Fase 11.

Robert sí puede:

- Crear documentos.
- Revisar documentos.
- Corregir documentos.
- Proponer especificaciones.
- Preparar borradores.
- Registrar decisiones aprobadas por el usuario.
- Registrar cambios.
- Actualizar HOME.
- Actualizar README.
- Diseñar conceptualmente.
- Simular en sandbox manual.

---

# TABLA DE CORRECCIONES v0.2

| Punto corregido | Estado v0.1 | Estado v0.2 |
|---|---|---|
| Solapamiento entre eventos | No había regla de precedencia | Se usa el evento más específico disponible |
| EVENTO 5 | Bloqueo automático general sin subtipos explícitos | Queda como categoría general |
| EVENTOS 15-20 | Podían competir con EVENTO 5 | Quedan definidos como subtipos específicos de EVENTO 5 |
| Conectar Gmail sin autorización | Podía clasificarse como Evento 5, 11 o 16 | Clasificación final: EVENTO 16 — Conexión no autorizada |
| Ejecutar sin permiso | Podía clasificarse como Evento 5, 7, 11 o 15 | Clasificación final: EVENTO 15 — Ejecución no autorizada |
| Ejemplo histórico de contradicción documental | Cronología imprecisa | Cronología corregida |

---

# CRITERIOS DE ACEPTACIÓN

Este documento podrá considerarse listo para aprobación si:

- Define advertencias.
- Define bloqueos automáticos.
- Define bloqueos manuales.
- Define acciones prohibidas.
- Define acciones futuras no disponibles.
- Define errores por falta de información.
- Define contradicciones documentales.
- Define riesgo crítico.
- Define fuera de alcance.
- Define sandbox requerido.
- Define sandbox excedido.
- Define ejecución no autorizada.
- Define conexión no autorizada.
- Define automatización no autorizada.
- Define agente no autorizado.
- Define dato sensible detectado.
- Define fase incorrecta.
- Agrega regla de precedencia entre eventos.
- Define EVENTOS 15 al 20 como subtipos específicos de EVENTO 5.
- Usa el evento más específico disponible cuando existe solapamiento.
- Corrige la cronología del ejemplo de contradicción documental.
- Mantiene Nivel 0 únicamente como Informativo.
- Mantiene acciones de control fuera de la escala de riesgo.
- Respeta ROBERT_COMMANDS v0.4.
- Respeta USER_ACTIONS_SPEC v0.2.
- Respeta SCREEN_STATE_SPEC v0.2.
- Respeta INTERACTION_FLOW_SPEC v0.2.
- Respeta documentos sandbox oficiales.
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

**Cambio técnico documental / errores y bloqueos conceptuales**

Nivel de riesgo inicial:

**Nivel 3 — Alto**

Motivo:

Este documento define cómo Robert debe reaccionar ante errores, bloqueos, acciones prohibidas, contradicciones y riesgos críticos. Aunque sigue siendo conceptual, influye en la seguridad operativa futura del sistema.

Nivel de riesgo final esperado:

**Nivel 2 — Medio**

Motivo de reducción:

El documento es documental. No crea botones reales, no crea pantallas reales, no programa, no conecta herramientas externas y no ejecuta acciones.

Nivel de autonomía:

**Nivel 0 — Sin autonomía ejecutiva**

---

# DECISIÓN PENDIENTE

Este documento queda como:

**Propuesta corregida pendiente de revisión**

Para aprobarlo formalmente, el usuario deberá escribir:

**APRUEBO ROBERT_TECHNICAL_ERROR_AND_BLOCKING_SPEC v0.2**

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

**ROBERT_TECHNICAL_PERMISSIONS_AND_SCOPES_SPEC**

Ese documento definiría permisos, alcances, límites, duración de autorizaciones y qué puede hacer Robert dentro de cada nivel autorizado.

No debe crearse hasta revisar o aprobar ERROR_AND_BLOCKING_SPEC.

---

# CIERRE

ROBERT_TECHNICAL_ERROR_AND_BLOCKING_SPEC v0.2 define cómo Robert debe manejar errores, advertencias, bloqueos automáticos, bloqueos manuales, acciones prohibidas, contradicciones documentales, riesgos críticos y capacidades futuras no disponibles.

Esta versión agrega regla de precedencia entre eventos, define los eventos 15 al 20 como subtipos específicos del Evento 5 y corrige la cronología del ejemplo de contradicción documental.

Este documento mantiene a Robert en modo documental, manual y supervisado.

El usuario mantiene control total.

Robert no ejecuta acciones importantes sin permiso.
