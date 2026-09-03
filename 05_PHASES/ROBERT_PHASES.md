# ROBERT_PHASES

Versión: 0.5
Estado: Mapa de fases reconciliado — pendiente de revisión y aprobación formal
Fecha: 30/06/2026
Ubicación: 05_PHASES
Documento relacionado: ROBERT_CONTEXT_MASTER v0.10

> Estado operativo vigente (03/09/2026): Fase 10 cerrada; Stages 0–4 completos; Stage 5 no autorizado; Fase 11 no iniciada. Las notas de aprobación de v0.5 conservan su carácter histórico y no amplían autoridad.

Tags: #robert/orbita-2 #capa/4 #tipo/maestro #robert/gobierno #robert/fases

[[ROBERT_HOME]]
[[ROBERT_CONTEXT_MASTER]]
[[ROBERT_SYSTEM_ARCHITECTURE]]
[[ROBERT_SECURITY_RULES]]
[[ROBERT_DECISIONS_LOG]]

---

# OBJETIVO

Este documento define el mapa oficial de fases del Proyecto Robert.

Su función es mantener claro:

* En qué fase está Robert.
* Qué fases ya fueron completadas.
* Qué fases están en preparación.
* Qué fases siguen pendientes.
* Qué no debe adelantarse.
* Qué documentos se relacionan con cada fase.
* Qué condiciones deben cumplirse antes de avanzar.

Esta versión v0.5 corrige contradicciones detectadas en versiones anteriores de ROBERT_PHASES.

---

# ESTADO DE ESTA VERSIÓN

Esta versión deja una sola numeración oficial de fases.

Elimina contradicciones anteriores donde:

* Fase 10 aparecía con significados diferentes.
* Fase 1 aparecía como activa aunque el proyecto ya estaba en Fase 10.
* MVP_PLAN aparecía como pendiente aunque ya fue creado.
* Se mezclaban fases antiguas con fases nuevas.
* El cierre seguía mencionando aprobación de ROBERT_PHASES v0.3.

---

# REGLA CENTRAL

El usuario manda.

Robert no avanza de fase sin autorización clara del usuario.

Robert no debe saltar fases.

Robert no debe convertir una fase documental en ejecución real sin aprobación formal.

---

# FUENTE DE VERDAD RELACIONADA

Este documento debe mantenerse alineado con:

* ROBERT_SECURITY_RULES
* ROBERT_CONTEXT_MASTER
* ROBERT_COMMANDS
* ROBERT_DECISIONS_LOG
* ROBERT_HOME
* ROBERT_CONTROL_DE_CAMBIOS
* ROBERT_MVP_PLAN
* ROBERT_TECHNICAL_MVP_PLAN
* ROBERT_TECHNICAL_MVP_WIREFRAME
* ROBERT_TECHNICAL_COMPONENTS_SPEC

Si ROBERT_PHASES contradice a ROBERT_CONTEXT_MASTER sobre el estado general, debe corregirse ROBERT_PHASES.

---

# PRINCIPIO DE FASES

Robert se construye en orden.

El orden correcto es:

**Identidad → Documentos → Control → Seguridad → MVP manual → Sandbox → MVP técnico → Conexiones → Automatización → Agentes → Expansión**

Regla guía:

**Primero orden. Después poder.**

---

# NUMERACIÓN OFICIAL DE FASES

A partir de esta versión, la numeración oficial queda así:

```text
Fase 1 — Identidad y visión
Fase 2 — Documentos maestros
Fase 3 — Fuente central de verdad
Fase 4 — Comandos
Fase 5 — Módulos
Fase 6 — Arquitectura conceptual
Fase 7 — Diseño visual / UX
Fase 8 — MVP manual
Fase 9 — Sandbox manual
Fase 10 — MVP técnico básico
Fase 11 — Conexión segura con herramientas
Fase 12 — Automatizaciones controladas
Fase 13 — Voz / multimodal
Fase 14 — Agentes especializados
Fase 15 — Business Builder avanzado
Fase 16 — Seguridad avanzada / pruebas
Fase 17 — Iteraciones y expansión
```

No debe usarse otra numeración dentro de Robert sin actualizar formalmente este documento.

---

# ESTADO ACTUAL OFICIAL

Robert se encuentra actualmente en:

**Fase 10 — MVP técnico básico en preparación**

---

# RESUMEN DE ESTADO POR FASE

```text
Fase 1 — Identidad y visión: Completada
Fase 2 — Documentos maestros: Completada como base inicial
Fase 3 — Fuente central de verdad: Completada / reanclada en CONTEXT_MASTER v0.5
Fase 4 — Comandos: Completada como base inicial
Fase 5 — Módulos: Completada como estructura inicial
Fase 6 — Arquitectura conceptual: Completada como base conceptual
Fase 7 — Diseño visual / UX: En desarrollo documental / convención Obsidian validada
Fase 8 — MVP manual: Completada y validada
Fase 9 — Sandbox manual: Completada y validada
Fase 10 — MVP técnico básico: En preparación
Fase 11 — Conexión segura con herramientas: Pendiente
Fase 12 — Automatizaciones controladas: Pendiente
Fase 13 — Voz / multimodal: Pendiente
Fase 14 — Agentes especializados: Pendiente
Fase 15 — Business Builder avanzado: Pendiente
Fase 16 — Seguridad avanzada / pruebas: Pendiente
Fase 17 — Iteraciones y expansión: Pendiente
```

---

# FASE 1 — IDENTIDAD Y VISIÓN

## Estado

Completada.

## Objetivo

Definir qué es Robert, qué problema resuelve y hacia dónde debe evolucionar.

## Resultado

Robert quedó definido como un sistema operativo personal de inteligencia artificial tipo AI Command Center.

## Documentos relacionados

* ROBERT_CONTEXT_MASTER
* ROBERT_HOME

## Criterio de cierre

La identidad base de Robert fue definida y registrada.

---

# FASE 2 — DOCUMENTOS MAESTROS

## Estado

Completada como base inicial.

## Objetivo

Crear los documentos principales que sostienen el sistema.

## Documentos principales

* ROBERT_HOME
* ROBERT_CONTEXT_MASTER
* ROBERT_COMMANDS
* ROBERT_DECISIONS_LOG
* ROBERT_SECURITY_RULES
* ROBERT_PHASES
* ROBERT_MODULES
* ROBERT_VISUAL
* ROBERT_PROMPTS
* ROBERT_SYSTEM_ARCHITECTURE
* ROBERT_MVP_PLAN

## Criterio de cierre

Existe una base documental suficiente para continuar el proyecto sin depender únicamente de conversaciones sueltas.

---

# FASE 3 — FUENTE CENTRAL DE VERDAD

## Estado

Completada / reanclada.

## Objetivo

Definir dónde vive la verdad actual del proyecto.

## Fuente principal actual

**ROBERT_CONTEXT_MASTER v0.5**

## Apoyos

* ROBERT_HOME
* ROBERT_DECISIONS_LOG
* ROBERT_CONTROL_DE_CAMBIOS
* GitHub como respaldo documental manual

## Criterio de cierre

Robert cuenta con una fuente central de contexto actualizada y respaldada.

---

# FASE 4 — COMANDOS

## Estado

Completada como base inicial.

## Objetivo

Definir comandos que permitan operar Robert de forma controlada.

## Comandos base

* RESUMEN
* CONCLUSION / CONCLUCION
* IDEA PRINCIPAL
* DETENTE
* PAUSA
* NO_AVANCES
* SOLO_BORRADOR
* MODO_SUPERVISADO
* MODO_SANDBOX
* APRUEBO / APROBADO
* ACTUALIZA
* DECISION
* INFORME_ACCIONES

## Documento relacionado

* ROBERT_COMMANDS

## Criterio de cierre

Los comandos base están definidos y se han usado durante el MVP manual y el sandbox manual.

---

# FASE 5 — MÓDULOS

## Estado

Completada como estructura inicial.

## Objetivo

Definir las áreas funcionales de Robert.

## Documento relacionado

* ROBERT_MODULES

## Resultado

Robert cuenta con una estructura modular inicial para organizar capacidades futuras.

## Criterio de cierre

Los módulos principales existen como mapa inicial, aunque no todos estén activos técnicamente.

---

# FASE 6 — ARQUITECTURA CONCEPTUAL

## Estado

Completada como base conceptual.

## Objetivo

Definir las capas conceptuales de Robert.

## Capas principales

```text
Capa 0 — Identidad / Kernel
Capa 1 — Memoria
Capa 2 — Control
Capa 3 — Capacidades
Capa 4 — Gobierno
Capa 5 — Presentación
```

## Documento relacionado

* ROBERT_SYSTEM_ARCHITECTURE

## Criterio de cierre

Robert cuenta con una arquitectura conceptual suficiente para guiar documentos técnicos y visuales.

---

# FASE 7 — DISEÑO VISUAL / UX

## Estado

En desarrollo documental.

## Objetivo

Definir cómo debe verse y sentirse Robert.

## Avance actual

La convención visual de Obsidian fue validada como navegación documental.

## Regla visual validada

**Órbita = posición / cercanía al núcleo**
**Capa o función = color visual**

## Centro visual

**ROBERT_HOME**

## Centro conceptual

**ROBERT_CONTEXT_MASTER**

## Documentos relacionados

* ROBERT_VISUAL
* ROBERT_TECHNICAL_MVP_WIREFRAME
* ROBERT_HOME

## Importante

Obsidian Graph View no reemplaza el futuro Command Center visual.

Obsidian solo funciona como mapa documental inicial.

## Criterio de cierre

La fase visual documental está avanzada, pero el HUD final y la interfaz visual real pertenecen al MVP técnico futuro.

---

# FASE 8 — MVP MANUAL

## Estado

Completada y validada.

## Objetivo

Probar Robert manualmente usando ChatGPT, Claude, Obsidian, documentos, comandos y decisiones.

## Resultado

Robert demostró que puede:

* ordenar ideas;
* clasificar solicitudes;
* detectar riesgos;
* preparar borradores;
* registrar decisiones;
* proponer actualizaciones;
* trabajar sin ejecutar acciones reales.

## Documento relacionado

* ROBERT_MVP_PLAN

## Criterio de cierre

El MVP manual fue validado documentalmente.

---

# FASE 9 — SANDBOX MANUAL

## Estado

Completada y validada.

## Objetivo

Probar Robert en simulaciones seguras sin afectar el mundo real.

## Resultado

Robert pudo simular procesos sin ejecutar acciones externas.

## Caso de prueba relevante

**Agrocribas**

## Documentos relacionados

* ROBERT_SANDBOX
* SANDBOX_RULES
* SANDBOX_TESTS
* SANDBOX_RESULTS
* ROBERT_DECISIONS_LOG

## Criterio de cierre

El sandbox manual fue validado documentalmente y no autorizó ejecución real.

---

# FASE 10 — MVP TÉCNICO BÁSICO

## Estado

Cerrada mediante DECISIÓN #041 / CAMBIO #067.

## Objetivo

Convertir Robert de sistema documental/manual a una primera especificación técnica e interfaz básica, sin conexiones reales.

## Documentos actuales relacionados

* ROBERT_TECHNICAL_MVP_PLAN
* ROBERT_TECHNICAL_MVP_WIREFRAME v0.3
* ROBERT_TECHNICAL_COMPONENTS_SPEC v0.2
* ROBERT_TECHNICAL_DATA_MODEL_SPEC v0.1
* ROBERT_IMPLEMENTATION_CONTRACTS v0.1
* ROBERT_PHASE_10_EXIT_CRITERIA v0.1
* ROBERT_BUILD_ORDER v0.1

## Estado actual dentro de la fase

* ROBERT_TECHNICAL_MVP_PLAN aprobado
* ROBERT_TECHNICAL_MVP_WIREFRAME v0.3 aprobado
* ROBERT_TECHNICAL_COMPONENTS_SPEC v0.2 vigente
* ROBERT_TECHNICAL_DATA_MODEL_SPEC v0.1 vigente
* ROBERT_CONTEXT_MASTER v0.6 sincronizado
* Core Architecture cerrada
* Implementation Contracts aprobados
* Phase 10 Exit Criteria aprobados
* Build Order aprobado
* Audit físico final registrado con resultado PASS
* Cierre formal autorizado mediante DECISIÓN #041
* Stage 0 autorizado mediante DECISIÓN #042
* Stage 0 implementado y verificado mediante CAMBIO #068
* Stage 1 autorizado mediante DECISIÓN #043
* Stage 1 implementado y verificado mediante CAMBIO #069
* Stage 2 autorizado mediante DECISIÓN #044
* Stage 2 implementado y verificado mediante CAMBIO #070
* Stage 3 autorizado mediante DECISIÓN #045
* Stage 3 implementado y verificado mediante CAMBIO #071
* Stage 4 autorizado mediante DECISIÓN #046
* Stage 4 implementado y verificado mediante CAMBIO #072
* Stage 5 y cualquier alcance adicional no autorizados

## Criterio para cerrar la fase

Cumplido: el audit físico final resultó `PASS` y el usuario emitió la DECISIÓN #041 de cierre. El cierre no autoriza programación ni transición automática.

## No autorizado en esta fase todavía

* Programar la app
* Conectar APIs reales
* Conectar Gmail
* Conectar Calendar
* Automatizar GitHub
* Activar agentes autónomos
* Ejecutar acciones reales

---

# FASE 11 — CONEXIÓN SEGURA CON HERRAMIENTAS

## Estado

Pendiente.

## Objetivo

Preparar conexiones seguras con herramientas externas.

## Herramientas futuras posibles

* GitHub
* Obsidian
* Google Drive
* Gmail
* Google Calendar
* Claude
* ChatGPT
* Notion
* Tana
* Make
* Zapier
* n8n

## Regla

Ninguna herramienta externa se conecta automáticamente sin autorización formal.

## Condición para iniciar

Debe existir:

* seguridad actualizada;
* permisos definidos;
* alcance por herramienta;
* sandbox técnico;
* trazabilidad;
* aprobación del usuario.

---

# FASE 12 — AUTOMATIZACIONES CONTROLADAS

## Estado

Pendiente.

## Objetivo

Diseñar automatizaciones con límites, permisos y revisión.

## Regla

Automatizar no significa ejecutar sin control.

Toda automatización debe tener:

* alcance;
* permiso;
* límite;
* trazabilidad;
* forma de pausa;
* forma de revocación.

---

# FASE 13 — VOZ / MULTIMODAL

## Estado

Pendiente.

## Objetivo

Permitir que Robert pueda ser controlado por voz, imágenes, documentos y otros formatos.

## Regla

La voz no debe saltarse seguridad.

Un comando por voz debe respetar las mismas reglas que un comando escrito.

---

# FASE 14 — AGENTES ESPECIALIZADOS

## Estado

Pendiente.

## Objetivo

Diseñar agentes especializados por función.

## Posibles agentes futuros

* Research Agent
* Finance Agent
* Business Builder Agent
* Design Agent
* Marketing Agent
* Security Agent
* Memory Agent
* Legal Reference Agent
* Fiscal Reference Agent

## Regla

No existen agentes autónomos activos todavía.

Los agentes futuros requieren gobierno, permisos, límites y revisión.

---

# FASE 15 — BUSINESS BUILDER AVANZADO

## Estado

Pendiente.

## Objetivo

Desarrollar Business Builder como capacidad avanzada para estructurar ideas de negocio y empresas completas.

## Base actual

Business Builder ya fue probado manualmente como capacidad inicial.

## Regla

Business Builder no debe ejecutar acciones legales, fiscales, comerciales o financieras reales sin autorización formal.

---

# FASE 16 — SEGURIDAD AVANZADA / PRUEBAS

## Estado

Pendiente.

## Objetivo

Probar Robert bajo escenarios más complejos de riesgo, ambigüedad, permisos y errores.

## Pruebas futuras

* Ambigüedad
* Instrucciones contradictorias
* Falsa autorización
* Escalamiento de riesgo
* Datos sensibles
* Acciones externas
* Automatización no autorizada
* Agentes autónomos
* Conexiones inseguras

---

# FASE 17 — ITERACIONES Y EXPANSIÓN

## Estado

Pendiente.

## Objetivo

Mejorar Robert continuamente después de validar el MVP técnico, conexiones y seguridad.

## Posibles expansiones

* Dashboard visual avanzado
* Sistema multiagente
* Voz completa
* Apps conectadas
* Automatizaciones por área
* Business Builder avanzado
* Módulos por proyecto
* Sistema operativo personal funcional

---

# ESCALA DE RIESGO Y AUTONOMÍA

ROBERT_PHASES no redefine la escala oficial de riesgo.

Sin embargo, para evitar contradicciones, este documento reconoce la separación entre:

```text
Riesgo
Autonomía
Tipo de cambio
Estado de fase
```

---

## Riesgo

El riesgo debe interpretarse como una escala de seguridad.

Escala recomendada para reconciliación documental:

```text
Nivel 0 — Informativo
Nivel 1 — Bajo
Nivel 2 — Medio
Nivel 3 — Alto
Nivel 4 — Crítico
```

No existe Nivel 5 como riesgo.

---

## Autonomía

La autonomía es una escala distinta.

Puede llegar hasta Nivel 5 si ROBERT_SECURITY_RULES lo define así.

Nivel 5 pertenece a autonomía, no a riesgo.

---

## Tipo de cambio

El tipo de cambio es una categoría documental.

Ejemplos:

* Cambio documental
* Cambio visual
* Cambio técnico
* Cambio de seguridad
* Cambio de conexión externa
* Cambio de automatización

Tipo de cambio no es nivel de riesgo.

---

# REGLA DE NO SALTO DE FASE

Robert no puede avanzar a una fase posterior si la fase actual tiene contradicciones graves.

Antes de avanzar a programación o conexiones, deben estar alineados:

* ROBERT_CONTEXT_MASTER
* ROBERT_PHASES
* ROBERT_SECURITY_RULES
* ROBERT_CONTROL_DE_CAMBIOS
* ROBERT_DECISIONS_LOG
* ROBERT_TECHNICAL_MVP_PLAN
* ROBERT_TECHNICAL_MVP_WIREFRAME
* ROBERT_TECHNICAL_COMPONENTS_SPEC

---

# BLOQUEOS ACTUALES

Antes de aprobar ROBERT_TECHNICAL_COMPONENTS_SPEC v0.2, se recomienda cerrar estos puntos:

1. Aprobar o validar ROBERT_PHASES v0.5.
2. Unificar escala de riesgo en SECURITY_RULES y CONTROL_DE_CAMBIOS.
3. Verificar que DECISIONS_LOG contenga las decisiones recientes.
4. Confirmar que ROBERT_TECHNICAL_MVP_PLAN está aprobado.
5. Confirmar que ROBERT_TECHNICAL_MVP_WIREFRAME v0.3 está aprobado.

---

# DECISIONES RECIENTES RELACIONADAS

Decisiones recientes que deben estar en ROBERT_DECISIONS_LOG:

* DECISIÓN #004 — Sandbox manual validado
* DECISIÓN #008 — GitHub como respaldo documental manual
* DECISIÓN #009 — Checkpoint documental GitHub completado
* DECISIÓN #010 — Aprobación de ROBERT_TECHNICAL_MVP_WIREFRAME v0.3

Si alguna decisión no aparece en DECISIONS_LOG, debe agregarse o verificarse antes de aprobar documentos técnicos dependientes.

---

# CAMBIOS RECIENTES RELACIONADOS

Cambios recientes que deben estar en ROBERT_CONTROL_DE_CAMBIOS:

* CAMBIO #010 — Actualización del wireframe técnico a v0.3
* CAMBIO #011 — Creación de ROBERT_TECHNICAL_COMPONENTS_SPEC v0.1
* CAMBIO #012 — Convención visual del grafo en Obsidian
* CAMBIO #013 — Reanclaje de ROBERT_CONTEXT_MASTER v0.5

---

# ESTADO DE GITHUB

GitHub queda autorizado únicamente como:

* respaldo documental privado;
* control de versiones manual;
* historial de cambios;
* base organizada para futura fase técnica.

GitHub no está autorizado como automatización activa.

GitHub no está conectado automáticamente a Robert.

---

# LO QUE ESTA VERSIÓN NO AUTORIZA

ROBERT_PHASES v0.5 no autoriza:

* Programar la app.
* Conectar herramientas externas.
* Automatizar GitHub.
* Crear agentes autónomos.
* Ejecutar acciones reales.
* Cambiar reglas de seguridad sin aprobación.
* Aprobar automáticamente COMPONENTS_SPEC.
* Avanzar a Fase 11.

---

# PRÓXIMO PASO RECOMENDADO

Después de pegar esta versión, el siguiente paso recomendado es:

1. Revisar ROBERT_PHASES v0.5.
2. Registrar el cambio en ROBERT_CONTROL_DE_CAMBIOS.
3. Actualizar ROBERT_HOME.
4. Actualizar README si aplica.
5. Revisar la escala de riesgo en SECURITY_RULES y CONTROL_DE_CAMBIOS.
6. Verificar DECISIONS_LOG.
7. Después volver a revisar COMPONENTS_SPEC v0.2.

---

# DECISIÓN PENDIENTE

Esta versión queda como:

**ROBERT_PHASES v0.5 — Mapa de fases reconciliado pendiente de aprobación formal**

Para aprobarla formalmente, el usuario deberá escribir:

```text
APRUEBO ROBERT_PHASES v0.5
```

---

# CIERRE

ROBERT_PHASES v0.5 corrige la contradicción de fases detectada en versiones anteriores.

A partir de esta versión, Robert tiene una sola numeración oficial de fases.

El estado actual queda reanclado a:

**Fase 10 — MVP técnico básico en preparación**

Robert sigue sin programación autorizada, sin conexiones reales, sin automatizaciones reales y sin agentes autónomos activos.

El usuario mantiene control total.

Robert no ejecuta acciones importantes sin permiso.
