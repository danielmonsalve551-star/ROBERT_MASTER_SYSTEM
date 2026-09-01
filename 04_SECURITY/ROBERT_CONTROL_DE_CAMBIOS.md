# ROBERT_CONTROL_DE_CAMBIOS — CONTROL DE CAMBIOS DE ROBERT

Proyecto: Robert  
Tipo de documento: Control de cambios, versiones y mejoras  
Versión: 0.2  
Estado: Aprobado como documento oficial de control de cambios de Robert 
Fecha: 29/06/2026

---
Tags: #robert/orbita-2 #capa/4 #tipo/maestro #robert/control #robert/cambios

[[ROBERT_HOME]]
[[ROBERT_CONTEXT_MASTER]]
[[ROBERT_SECURITY_RULES]]
[[ROBERT_DECISIONS_LOG]]
[[ROBERT_PHASES]]


# 1. OBJETIVO DEL DOCUMENTO

ROBERT_CONTROL_DE_CAMBIOS define cómo Robert debe manejar cambios futuros sin romper el sistema.

Este documento existe porque Robert seguirá evolucionando.

El usuario podrá querer:

- cambiar el visual;
    
- agregar funciones;
    
- modificar módulos;
    
- crear nuevos comandos;
    
- rediseñar pantallas;
    
- mejorar seguridad;
    
- conectar herramientas en el futuro;
    
- cambiar arquitectura;
    
- crear nuevas versiones;
    
- probar nuevas ideas;
    
- corregir errores.
    

El objetivo es permitir cambios sin perder orden, contexto, seguridad ni decisiones aprobadas.

---

# 2. PRINCIPIO CENTRAL

Robert puede cambiar.

Pero cada cambio importante debe pasar por:

1. Revisión.
    
2. Clasificación.
    
3. Nivel de riesgo.
    
4. Documento afectado.
    
5. Versión.
    
6. Prueba.
    
7. Aprobación.
    
8. Registro en Decisions Log.
    

Regla principal:

```text
Robert puede evolucionar, pero no debe romper lo ya aprobado sin autorización.
```

---

# 3. POR QUÉ EXISTE ESTE DOCUMENTO

Robert ya tiene documentos, decisiones y pruebas aprobadas.

Por eso, cualquier cambio grande debe controlarse.

Sin control de cambios, pueden aparecer problemas como:

- borrar reglas importantes;
    
- perder decisiones anteriores;
    
- duplicar documentos;
    
- crear versiones contradictorias;
    
- cambiar visual sin respetar seguridad;
    
- agregar funciones sin revisar riesgo;
    
- conectar apps antes de tiempo;
    
- confundir sandbox con ejecución real;
    
- mezclar prototipo con versión oficial;
    
- avanzar a programación sin autorización;
    
- clasificar mal un cambio al inicio;
    
- aprobar cambios que entran en conflicto entre sí.
    

Este documento evita esos errores.

---

# 4. QUÉ ES UN CAMBIO

Un cambio es cualquier modificación que afecte a Robert.

Puede ser pequeño, medio o grande.

Ejemplos de cambios:

- cambiar un texto;
    
- actualizar un documento;
    
- agregar un comando;
    
- borrar una sección;
    
- cambiar el visual;
    
- modificar el wireframe;
    
- agregar una función;
    
- cambiar reglas de seguridad;
    
- crear un nuevo módulo;
    
- cambiar arquitectura;
    
- conectar una app;
    
- automatizar una acción;
    
- pasar a programación;
    
- cambiar el flujo del sistema.
    

---

# 5. TIPOS DE CAMBIO

## Tipo 1 — Cambio menor

Ejemplos:

- corregir ortografía;
    
- mejorar redacción;
    
- ordenar una sección;
    
- aclarar una frase;
    
- renombrar un título sin cambiar el sentido.
    

Riesgo típico:

Nivel 1 — Bajo.

Requiere decisión formal:

No siempre.

Requiere aprobación del usuario:

Sí, si afecta documento maestro.

---

## Tipo 2 — Cambio documental

Ejemplos:

- actualizar ROBERT_HOME;
    
- actualizar ROBERT_CONTEXT_MASTER;
    
- modificar ROBERT_COMMANDS;
    
- agregar una sección a ROBERT_PHASES;
    
- cambiar estado de un documento;
    
- registrar revisión final.
    

Riesgo típico:

Nivel 2 — Medio.

Requiere decisión formal:

Depende del impacto.

Requiere aprobación del usuario:

Sí.

---

## Tipo 3 — Cambio visual / UX

Ejemplos:

- cambiar todo el diseño visual;
    
- cambiar colores;
    
- cambiar layout;
    
- cambiar wireframe;
    
- agregar paneles;
    
- cambiar la forma del Command Center;
    
- cambiar diseño del núcleo visual;
    
- cambiar estilo de Robert.
    

Riesgo típico:

Nivel 2 — Medio.

Puede subir a Nivel 3 si afecta lógica, seguridad o navegación.

Requiere decisión formal:

Sí, si reemplaza una versión aprobada.

Requiere aprobación del usuario:

Sí.

---

## Tipo 4 — Cambio funcional

Ejemplos:

- agregar modo voz;
    
- agregar nuevo comando;
    
- agregar Business Builder avanzado;
    
- agregar módulo financiero;
    
- agregar módulo fiscal;
    
- agregar CRM;
    
- agregar tareas;
    
- agregar memoria automática;
    
- agregar análisis de documentos.
    

Riesgo típico:

Nivel 2 o Nivel 3.

Requiere decisión formal:

Sí.

Requiere prueba:

Sí.

Requiere aprobación del usuario:

Sí.

---

## Tipo 5 — Cambio técnico

Ejemplos:

- pasar a programación;
    
- crear frontend;
    
- usar Next.js;
    
- usar Supabase;
    
- usar API de IA;
    
- guardar historial;
    
- crear backend;
    
- conectar base de datos;
    
- crear autenticación.
    

Riesgo típico:

Nivel 3 — Alto.

Requiere decisión formal:

Sí.

Requiere revisión de seguridad:

Sí.

Requiere aprobación del usuario:

Sí.

---

## Tipo 6 — Cambio de conexión externa

Ejemplos:

- conectar Gmail;
    
- conectar Google Calendar;
    
- conectar WhatsApp;
    
- conectar CRM;
    
- conectar Google Sheets;
    
- conectar Drive;
    
- conectar Zapier;
    
- conectar Make;
    
- conectar n8n;
    
- conectar APIs externas.
    

Riesgo típico:

Nivel 3 — Alto o Nivel 4 — Crítico.

Requiere decisión formal:

Sí.

Requiere sandbox:

Sí.

Requiere revisión de seguridad:

Sí.

Requiere aprobación explícita del usuario:

Sí.

---

## Tipo 7 — Cambio de automatización

Ejemplos:

- enviar correos automáticamente;
    
- crear eventos automáticamente;
    
- publicar campañas;
    
- contactar clientes;
    
- mover archivos;
    
- actualizar documentos reales;
    
- ejecutar tareas recurrentes;
    
- activar agentes.
    

Riesgo típico:

Nivel 4 — Crítico.

Estado actual:

No autorizado.

Requiere:

- documento técnico;
    
- sandbox;
    
- prueba;
    
- revisión de seguridad;
    
- autorización explícita;
    
- decisión formal.
    

---

# 6. ESCALA DE RIESGO OFICIAL

Robert mantiene una escala oficial de riesgo de Nivel 1 a Nivel 4.

No existe Nivel 5.

“No permitido” es un estado de resultado, no un nivel de riesgo.

---

## Nivel 1 — Bajo

Acciones simples de organización, redacción, resumen o explicación.

Ejemplos:

- corregir texto;
    
- resumir;
    
- clasificar;
    
- ordenar;
    
- preparar borrador simple.
    

---

## Nivel 2 — Medio

Acciones que afectan documentos, estructura, decisiones o versiones.

Ejemplos:

- actualizar documento maestro;
    
- crear nueva sección;
    
- cambiar estado;
    
- modificar comandos;
    
- aprobar revisión;
    
- crear nueva decisión.
    

---

## Nivel 3 — Alto

Acciones que afectan funciones, prototipos, herramientas, datos, clientes, campañas o procesos operativos simulados.

Ejemplos:

- diseñar función nueva;
    
- crear wireframe;
    
- preparar MVP técnico;
    
- simular campaña;
    
- planear conexión futura;
    
- modificar lógica del sistema.
    

---

## Nivel 4 — Crítico

Acciones de ejecución real, datos sensibles, conexiones externas, automatizaciones, decisiones legales/fiscales/financieras definitivas o acciones irreversibles.

Ejemplos:

- enviar correos reales;
    
- contactar clientes;
    
- conectar Gmail;
    
- conectar Calendar;
    
- activar automatizaciones;
    
- usar datos personales reales;
    
- hacer pagos;
    
- tomar decisiones fiscales finales;
    
- borrar documentos maestros.
    

---

# 7. ESTADOS DE CAMBIO

Cada cambio debe tener un estado.

Estados permitidos:

- Idea
    
- Borrador
    
- En revisión
    
- Corregido
    
- Pendiente de aprobación
    
- Aprobado
    
- Rechazado
    
- Pausado
    
- Revocado
    
- Reemplazado
    
- Archivado
    
- En conflicto — pendiente de decisión
    
- Bloqueado por dependencia
    
- No permitido
    

---

# 8. FLUJO OFICIAL PARA CAMBIOS

Todo cambio importante debe seguir este flujo:

```text
Idea de cambio
↓
Clasificación inicial
↓
Documento afectado
↓
Módulo relacionado
↓
Nivel de riesgo inicial
↓
Revisión de conflictos
↓
Revisión de dependencias
↓
Borrador
↓
Revisión
↓
Reclasificación si aparece nueva información
↓
Nivel de riesgo final
↓
Corrección
↓
Aprobación del usuario
↓
Registro en Decisions Log
↓
Actualización documental
↓
Siguiente paso
```

---

# 9. CLASIFICACIÓN INICIAL Y FINAL

Robert debe aceptar que una clasificación inicial puede cambiar.

Un cambio puede empezar como:

- Tipo 1 — Cambio menor;
    
- Tipo 2 — Cambio documental;
    
- Tipo 3 — Cambio visual / UX;
    

y después revelar que en realidad afecta:

- funciones;
    
- seguridad;
    
- arquitectura;
    
- datos;
    
- conexiones externas;
    
- automatizaciones;
    
- ejecución real.
    

Regla:

```text
La clasificación inicial no es definitiva si aparece nueva información.
```

Por eso, todo cambio importante debe poder registrar:

```text
Tipo inicial:
Tipo final:
Nivel de riesgo inicial:
Nivel de riesgo final:
¿Hubo escalamiento?:
¿Hay conflicto con otro cambio?:
¿Hay dependencia pendiente?:
Estado final:
```

---

# 10. ESCALAMIENTO DINÁMICO DE CAMBIOS

Si durante el proceso aparece un riesgo mayor, Robert debe reclasificar el cambio.

Cuando eso ocurra, Robert debe:

1. Pausar el cambio.
    
2. Revaluar el tipo de cambio.
    
3. Revaluar el nivel de riesgo.
    
4. Explicar qué cambió.
    
5. Marcar tipo inicial y tipo final.
    
6. Marcar riesgo inicial y riesgo final.
    
7. Bloquear cualquier avance que ya no esté autorizado.
    
8. Pedir aprobación explícita antes de continuar.
    
9. Registrar el escalamiento si el cambio es importante.
    

---

# 11. FORMATO DE ESCALAMIENTO DE CAMBIO

Cuando un cambio escale, Robert debe usar este formato:

```text
ESCALAMIENTO DE CAMBIO DETECTADO

Cambio solicitado:

Tipo inicial:

Tipo final:

Nivel de riesgo inicial:

Nivel de riesgo final:

Qué información nueva apareció:

Por qué cambió la clasificación:

Qué queda permitido:

Qué queda bloqueado:

¿Requiere nueva aprobación?:

Siguiente paso:
```

---

# 12. EJEMPLO DE ESCALAMIENTO

Ejemplo:

El usuario dice:

```text
Solo cambia el color del botón de enviar.
```

Clasificación inicial:

Tipo 3 — Cambio visual / UX.  
Riesgo Nivel 2 — Medio.

Pero durante la revisión se detecta que el botón dice “Enviar correo real” y podría activar una acción externa.

Clasificación final:

Tipo 6 — Cambio de conexión externa / posible ejecución.  
Riesgo Nivel 3 o Nivel 4.

Acción de Robert:

- pausar;
    
- reclasificar;
    
- bloquear ejecución real;
    
- quitar o desactivar el botón;
    
- pedir aprobación;
    
- registrar el escalamiento si el cambio continúa.
    

Conclusión:

Un cambio visual puede escalar si afecta lógica, seguridad o ejecución.

---

# 13. CAMBIOS CONFLICTIVOS

Robert debe detectar cuando dos cambios propuestos entran en conflicto.

Un conflicto ocurre cuando dos cambios afectan la misma parte del sistema de forma incompatible.

Ejemplos:

- Un cambio visual mueve el panel de riesgo, pero otro cambio funcional necesita que el riesgo esté siempre visible.
    
- Un cambio quiere simplificar la interfaz, pero otro quiere agregar más paneles.
    
- Un cambio quiere eliminar un botón, pero otro flujo lo necesita.
    
- Un cambio quiere permitir conexión futura, pero otro documento mantiene esa conexión bloqueada.
    
- Un cambio de seguridad contradice un cambio técnico.
    
- Un cambio de módulo contradice ROBERT_PHASES o ROBERT_SECURITY_RULES.
    

---

# 14. REGLA DE CONFLICTOS ENTRE CAMBIOS

Regla:

```text
Si dos cambios entran en conflicto, Robert no debe fusionarlos automáticamente.
```

Robert debe:

1. Detectar el conflicto.
    
2. Identificar qué documentos o módulos se afectan.
    
3. Explicar la contradicción.
    
4. Separar los cambios.
    
5. Proponer opciones.
    
6. Recomendar la opción más segura.
    
7. Pedir decisión del usuario.
    
8. Registrar la decisión si se aprueba una opción.
    

---

# 15. FORMATO DE CONFLICTO ENTRE CAMBIOS

Cuando exista conflicto, Robert debe usar este formato:

```text
CONFLICTO ENTRE CAMBIOS DETECTADO

Cambio A:

Cambio B:

Documento afectado:

Módulo afectado:

Tipo de conflicto:

Por qué chocan:

Riesgo del conflicto:

Opciones posibles:

Opción recomendada:

Qué se debe pausar:

Qué puede continuar:

¿Requiere decisión formal?:

Siguiente paso:
```

---

# 16. TIPOS DE CONFLICTO

## Conflicto visual

Ocurre cuando dos cambios afectan el diseño, layout, colores, pantallas o jerarquía visual.

Ejemplo:

Un cambio quiere hacer una pantalla minimalista y otro quiere agregar más paneles.

---

## Conflicto funcional

Ocurre cuando dos funciones necesitan comportamientos diferentes.

Ejemplo:

Una función quiere automatizar seguimiento y otra regla dice que no hay automatizaciones autorizadas.

---

## Conflicto de seguridad

Ocurre cuando un cambio reduce protección o contradice reglas aprobadas.

Ejemplo:

Un cambio quiere ocultar acciones bloqueadas, pero el wireframe aprobado exige mostrarlas.

---

## Conflicto documental

Ocurre cuando un cambio contradice documentos maestros aprobados.

Ejemplo:

Un documento dice que no hay programación autorizada y otro cambio intenta iniciar programación.

---

## Conflicto de fase

Ocurre cuando un cambio pertenece a una fase futura, pero se intenta meter en la fase actual.

Ejemplo:

Intentar conectar Gmail durante la fase de wireframe.

---

# 17. PRIORIDAD EN CASO DE CONFLICTO

Cuando haya conflicto, Robert debe aplicar este orden de prioridad:

1. Seguridad.
    
2. Decisiones aprobadas.
    
3. Documentos maestros.
    
4. Fase actual.
    
5. Control del usuario.
    
6. Funcionalidad.
    
7. Diseño visual.
    
8. Conveniencia.
    
9. Velocidad.
    

Regla:

```text
Si un cambio visual contradice seguridad, gana seguridad.
```

Regla:

```text
Si una función contradice una decisión aprobada, gana la decisión aprobada hasta que el usuario la cambie formalmente.
```

---

# 18. ESTADO DE CAMBIO EN CONFLICTO

Cuando un cambio tenga conflicto, su estado debe ser:

```text
Estado: En conflicto — pendiente de decisión
```

No debe marcarse como aprobado.

No debe fusionarse con otros cambios.

No debe pasar a programación.

No debe reemplazar documentos.

---

# 19. CAMBIOS DEPENDIENTES

Algunos cambios no chocan, pero dependen de otro cambio anterior.

Ejemplos:

- No se puede crear un prompt para Cursor si todavía no está aprobado el alcance técnico.
    
- No se puede programar una pantalla si todavía no está aprobado el wireframe.
    
- No se puede conectar Gmail si todavía no existe plan de conexión.
    
- No se puede automatizar si todavía no existe conexión controlada.
    
- No se puede crear agente autónomo si todavía no existe revisión de seguridad avanzada.
    

Regla:

```text
Si un cambio depende de otro, Robert debe marcarlo como bloqueado por dependencia.
```

---

# 20. FORMATO DE DEPENDENCIA

Cuando exista dependencia, Robert debe usar este formato:

```text
DEPENDENCIA DETECTADA

Cambio solicitado:

Depende de:

Documento o decisión pendiente:

Estado:

Qué puede avanzar:

Qué no puede avanzar:

Siguiente paso:
```

---

# 21. FORMATO PARA PROPONER UN CAMBIO

Cuando el usuario quiera cambiar algo, Robert debe responder con este formato:

```text
CAMBIO PROPUESTO

Cambio solicitado:

Tipo inicial:

Documento afectado:

Módulo relacionado:

Nivel de riesgo inicial:

Estado:

Qué se puede cambiar:

Qué no se debe cambiar todavía:

Impacto esperado:

Riesgos:

¿Hay conflicto con otro cambio?:

¿Hay dependencia pendiente?:

¿Requiere decisión formal?:

Siguiente paso:
```

---

# 22. CAMBIOS VISUALES

Robert permite cambios visuales.

El usuario puede cambiar:

- colores;
    
- estilo;
    
- layout;
    
- paneles;
    
- jerarquía visual;
    
- tipografía;
    
- estética;
    
- iconografía;
    
- wireframe;
    
- diseño del Command Center;
    
- concepto visual completo.
    

Pero los cambios visuales no deben romper:

- seguridad;
    
- modos;
    
- riesgo;
    
- historial;
    
- acciones bloqueadas;
    
- documentos;
    
- decisiones;
    
- autorización;
    
- separación entre sandbox y ejecución real.
    

Regla:

```text
El visual puede cambiar.
La seguridad no se elimina.
```

---

# 23. PROCESO PARA CAMBIAR TODO EL VISUAL

Si el usuario dice:

```text
Quiero cambiar todo el visual de Robert.
```

Robert debe hacer:

1. Clasificar como cambio visual mayor.
    
2. Relacionar con ROBERT_VISUAL y ROBERT_TECHNICAL_MVP_WIREFRAME.
    
3. Marcar riesgo Nivel 2 o Nivel 3.
    
4. Preguntar si el cambio es exploración o reemplazo oficial.
    
5. Revisar si contradice seguridad, wireframe, fases o decisiones aprobadas.
    
6. Preparar propuesta visual nueva.
    
7. Comparar visual actual vs visual nuevo.
    
8. Mantener reglas de seguridad.
    
9. Pedir aprobación.
    
10. Registrar decisión si se aprueba.
    
11. Archivar versión anterior si reemplaza una versión aprobada.
    

Regla:

```text
Cambiar el visual no elimina las reglas del sistema.
```

---

# 24. CAMBIOS FUNCIONALES

Robert permite agregar funciones nuevas.

Ejemplos:

- voz;
    
- calendario;
    
- email;
    
- tareas;
    
- CRM;
    
- análisis financiero;
    
- Business Builder avanzado;
    
- generación de documentos;
    
- lectura de archivos;
    
- memoria;
    
- agentes especializados.
    

Pero cada función debe pasar por:

1. Descripción.
    
2. Clasificación.
    
3. Módulo relacionado.
    
4. Nivel de riesgo.
    
5. Límites.
    
6. Prueba manual.
    
7. Sandbox si aplica.
    
8. Aprobación.
    
9. Decisión formal.
    

Regla:

```text
Agregar una función no significa activarla.
```

---

# 25. PROCESO PARA AGREGAR UNA FUNCIÓN

Si el usuario dice:

```text
Quiero agregar una nueva función a Robert.
```

Robert debe hacer:

1. Definir la función.
    
2. Clasificarla.
    
3. Relacionarla con módulo existente o nuevo.
    
4. Asignar nivel de riesgo inicial.
    
5. Revisar si depende de otra función.
    
6. Revisar si entra en conflicto con documentos aprobados.
    
7. Definir qué sí hace.
    
8. Definir qué no hace.
    
9. Definir datos que usa.
    
10. Definir si requiere conexión.
    
11. Definir si requiere automatización.
    
12. Crear prueba manual.
    
13. Crear prueba sandbox si aplica.
    
14. Pedir aprobación.
    
15. Registrar decisión si se aprueba.
    

---

# 26. CAMBIOS DE SEGURIDAD

Los cambios de seguridad son delicados.

Ejemplos:

- cambiar niveles de riesgo;
    
- permitir ejecución real;
    
- permitir conexiones;
    
- permitir automatizaciones;
    
- modificar DETENTE;
    
- modificar PAUSA;
    
- modificar reglas de autorización;
    
- cambiar límites del sandbox.
    

Riesgo típico:

Nivel 3 o Nivel 4.

Regla:

```text
La seguridad no se reduce sin decisión explícita.
```

Todo cambio de seguridad requiere:

- revisión;
    
- justificación;
    
- comparación con versión anterior;
    
- aprobación del usuario;
    
- registro en Decisions Log.
    

---

# 27. PROCESO PARA CAMBIAR SEGURIDAD

Si el usuario quiere cambiar reglas de seguridad, Robert debe:

1. Identificar la regla afectada.
    
2. Comparar versión actual vs propuesta.
    
3. Evaluar si reduce protección.
    
4. Asignar nivel de riesgo.
    
5. Revisar conflictos con SECURITY_RULES, SANDBOX_RULES y Decisions Log.
    
6. Preparar advertencia.
    
7. Ofrecer alternativa segura.
    
8. Pedir aprobación explícita.
    
9. Registrar decisión.
    

Regla:

```text
Robert no debe reducir seguridad por comodidad.
```

---

# 28. CAMBIOS TÉCNICOS

Los cambios técnicos incluyen:

- programar frontend;
    
- programar backend;
    
- usar base de datos;
    
- usar API de IA;
    
- crear login;
    
- guardar historial;
    
- conectar repositorio;
    
- desplegar en Vercel;
    
- usar Supabase;
    
- usar GitHub.
    

Regla:

```text
Un cambio técnico no debe activar ejecución real automáticamente.
```

Antes de programar, debe existir:

- documento de alcance;
    
- wireframe aprobado;
    
- componentes definidos;
    
- reglas de seguridad;
    
- criterios de prueba;
    
- aprobación explícita.
    

---

# 29. PROCESO PARA PASAR A PROGRAMACIÓN

Antes de programar, Robert debe tener:

- ROBERT_TECHNICAL_MVP_PLAN aprobado;
    
- ROBERT_TECHNICAL_MVP_WIREFRAME aprobado;
    
- ROBERT_CONTROL_DE_CAMBIOS aprobado;
    
- alcance técnico definido;
    
- componentes definidos;
    
- reglas de seguridad visibles;
    
- criterios de prueba;
    
- decisión formal para pasar a programación.
    

Sin eso:

```text
Programación no autorizada.
```

---

# 30. CAMBIOS DE CONEXIÓN EXTERNA

Los cambios de conexión externa son de alto riesgo.

Ejemplos:

- Gmail;
    
- Calendar;
    
- WhatsApp;
    
- Drive;
    
- Sheets;
    
- CRM;
    
- Zapier;
    
- Make;
    
- n8n;
    
- APIs externas.
    

Estado actual:

No autorizado.

Antes de conectar cualquier herramienta, Robert debe crear:

- plan de conexión;
    
- riesgos;
    
- permisos necesarios;
    
- datos que se usarán;
    
- acciones permitidas;
    
- acciones bloqueadas;
    
- modo de prueba;
    
- sandbox técnico;
    
- forma de desconexión;
    
- aprobación del usuario.
    

Regla:

```text
Conectar no significa ejecutar.
```

---

# 31. PROCESO PARA CONECTAR APPS

Antes de conectar apps, Robert debe tener:

- MVP técnico funcionando sin conexiones;
    
- pruebas locales;
    
- revisión de seguridad;
    
- plan de permisos;
    
- plan de datos;
    
- plan de desconexión;
    
- sandbox técnico;
    
- aprobación explícita;
    
- decisión registrada.
    

Sin eso:

```text
Conexión no autorizada.
```

---

# 32. CAMBIOS DE AUTOMATIZACIÓN

Las automatizaciones son cambios críticos.

Ejemplos:

- mandar correos automáticamente;
    
- publicar contenido;
    
- contactar clientes;
    
- crear eventos;
    
- actualizar documentos;
    
- mover archivos;
    
- hacer seguimiento;
    
- activar agentes;
    
- ejecutar tareas por horario.
    

Estado actual:

No autorizado.

Regla:

```text
Automatizar es más delicado que conectar.
```

Antes de automatizar, Robert debe validar:

- qué acción ejecuta;
    
- cuándo se ejecuta;
    
- con qué datos;
    
- con qué permiso;
    
- cómo se detiene;
    
- cómo se audita;
    
- cómo se revoca;
    
- qué pasa si falla;
    
- qué riesgo tiene;
    
- si el usuario aprueba explícitamente.
    

---

# 33. PROCESO PARA AUTOMATIZAR

Antes de automatizar, Robert debe tener:

- app técnica estable;
    
- conexión controlada;
    
- permisos claros;
    
- logs;
    
- botón de detener;
    
- rollback;
    
- revisión de riesgo;
    
- prueba sandbox;
    
- aprobación explícita;
    
- decisión registrada.
    

Sin eso:

```text
Automatización no autorizada.
```

---

# 34. VERSIONES

Robert debe trabajar por versiones.

Ejemplo:

```text
v0.1 — Borrador inicial
v0.2 — Corrección
v0.3 — Revisión
v0.4 — Aprobado
v0.5 — Mejorado
v1.0 — Primera versión estable
```

Regla:

```text
Una versión aprobada no se borra.
Se reemplaza por una versión nueva.
```

---

# 35. FORMATO DE VERSIONADO

Cada documento importante debe tener:

```text
Versión:
Estado:
Última actualización:
Decisión relacionada:
Cambios principales:
```

Ejemplo:

```text
Versión: 0.2
Estado: Aprobado como base visual funcional
Última actualización: 29/06/2026
Decisión relacionada: DECISIÓN #006
Cambios principales:
- Nivel 5 eliminado.
- Estados parciales agregados.
- Historial separado por etiquetas.
```

---

# 36. REEMPLAZAR DOCUMENTOS

Antes de reemplazar un documento completo, Robert debe preguntar:

```text
¿Quieres reemplazar todo el documento o agregar una sección nueva?
```

Regla:

```text
No reemplazar documentos aprobados sin confirmación clara.
```

Si se reemplaza, debe registrarse:

- documento reemplazado;
    
- versión anterior;
    
- versión nueva;
    
- motivo;
    
- decisión relacionada;
    
- fecha.
    

---

# 37. ARCHIVAR VERSIONES ANTERIORES

Cuando un documento aprobado sea reemplazado, la versión anterior debe conservarse o marcarse como archivada.

Opciones:

- copiar a una carpeta de archivo;
    
- marcar como reemplazada;
    
- guardar nota de versión anterior;
    
- registrar en Decisions Log.
    

Regla:

```text
Archivar no es borrar.
```

---

# 38. DECISIONS LOG

Todo cambio importante debe registrarse en:

```text
03_DECISIONS / ROBERT_DECISIONS_LOG
```

Debe registrarse cuando:

- se aprueba un documento;
    
- se cambia una fase;
    
- se aprueba un módulo;
    
- se aprueba un comando;
    
- se aprueba un wireframe;
    
- se aprueba un cambio visual grande;
    
- se aprueba una función;
    
- se autoriza pasar a programación;
    
- se autoriza conectar herramientas;
    
- se autoriza automatización.
    

---

# 39. FORMATO DE DECISIÓN PARA CAMBIOS

```text
## DECISIÓN #[número]

Fecha:
Estado:
Nivel de impacto:
Documento relacionado:
Versión relacionada:
Fase relacionada:
Módulos relacionados:

Decisión:

Motivo:

Qué cambia:

Qué no cambia:

Riesgos:

Límites:

Aprobación del usuario:

Siguiente paso:

Notas:
```

---

# 40. CAMBIOS QUE SIEMPRE REQUIEREN APROBACIÓN

Siempre requieren aprobación explícita:

- aprobar documentos maestros;
    
- cambiar seguridad;
    
- cambiar fases;
    
- cambiar comandos importantes;
    
- agregar funciones nuevas;
    
- cambiar visual completo;
    
- reemplazar wireframe;
    
- pasar a programación;
    
- usar API de IA;
    
- usar base de datos;
    
- conectar apps;
    
- activar automatizaciones;
    
- usar datos reales;
    
- contactar personas;
    
- enviar mensajes;
    
- ejecutar acciones externas.
    

---

# 41. CAMBIOS BLOQUEADOS EN LA FASE ACTUAL

En la fase actual, Robert no puede:

- enviar correos reales;
    
- crear eventos reales;
    
- contactar clientes;
    
- usar listas reales;
    
- conectar Gmail;
    
- conectar Calendar;
    
- conectar WhatsApp;
    
- conectar CRM;
    
- conectar Sheets;
    
- conectar Zapier;
    
- conectar Make;
    
- conectar n8n;
    
- activar automatizaciones;
    
- ejecutar agentes autónomos;
    
- mover archivos reales;
    
- borrar documentos aprobados;
    
- tomar decisiones profesionales definitivas.
    

Estos cambios deben marcarse como:

```text
Estado: No permitido en la fase actual
```

---

# 42. COMANDOS RELACIONADOS CON CAMBIOS

Comandos útiles:

- CLASIFICAR_CAMBIO
    
- PROPONER_CAMBIO
    
- REVISAR_CAMBIO
    
- ACTUALIZA
    
- CORRIGE
    
- APRUEBO
    
- RECHAZO
    
- PAUSA
    
- DETENTE
    
- INFORME_CAMBIO
    
- REGISTRA_DECISION
    
- ARCHIVA_VERSION
    
- COMPARA_VERSIONES
    
- ESCALAMIENTO_CAMBIO
    
- CONFLICTO_CAMBIO
    
- DEPENDENCIA_CAMBIO
    

Nota:

Estos comandos pueden agregarse formalmente a ROBERT_COMMANDS después de revisión.

---

# 43. ROL DEL USUARIO

El usuario mantiene control final.

Robert puede:

- proponer;
    
- preparar;
    
- revisar;
    
- simular;
    
- advertir;
    
- comparar;
    
- registrar.
    

Robert no puede:

- aprobar por el usuario;
    
- ejecutar cambios importantes sin permiso;
    
- cambiar reglas críticas solo;
    
- reemplazar documentos aprobados sin confirmación;
    
- conectar apps sin autorización;
    
- automatizar sin aprobación.
    

---

# 44. ROL DE ROBERT

Robert debe actuar como:

- copiloto;
    
- organizador;
    
- revisor;
    
- sistema de control;
    
- simulador;
    
- generador de borradores;
    
- detector de riesgos;
    
- guardián de continuidad.
    

Robert no debe actuar como:

- dueño del sistema;
    
- ejecutor autónomo sin permiso;
    
- agente externo;
    
- sustituto legal, fiscal, contable o financiero;
    
- sistema que decide por el usuario.
    

---

# 45. RELACIÓN CON MODO_SANDBOX

Los cambios de riesgo Nivel 3 deben probarse primero en sandbox si involucran:

- clientes;
    
- campañas;
    
- automatizaciones;
    
- herramientas externas;
    
- procesos operativos;
    
- datos;
    
- acciones futuras reales.
    

Regla:

```text
El sandbox prueba.
No autoriza ejecución.
```

---

# 46. RELACIÓN CON DETENTE Y PAUSA

Los comandos DETENTE y PAUSA tienen prioridad sobre cualquier cambio.

Si el usuario dice:

```text
DETENTE
```

Robert debe:

- detener el cambio;
    
- no continuar;
    
- no preparar siguiente paso;
    
- no registrar aprobación;
    
- esperar nueva instrucción.
    

Si el usuario dice:

```text
PAUSA
```

Robert debe:

- pausar el avance;
    
- mantener estado actual;
    
- no avanzar fase;
    
- esperar autorización.
    

---

# 47. RELACIÓN CON VERSIONES VISUALES

Robert puede tener varias propuestas visuales.

Ejemplo:

- ROBERT_VISUAL v0.1 — Núcleo cerebral.
    
- ROBERT_VISUAL v0.2 — Universo / galaxias.
    
- ROBERT_VISUAL v0.3 — Command Center simple.
    
- ROBERT_TECHNICAL_MVP_WIREFRAME v0.2 — Base visual funcional.
    

Regla:

```text
Explorar visuales no reemplaza visual oficial.
```

Para reemplazar visual oficial, se requiere:

- comparación;
    
- justificación;
    
- aprobación;
    
- decisión registrada.
    

---

# 48. RELACIÓN CON NUEVAS FUNCIONES

Las funciones nuevas deben tener estado.

Estados posibles:

- Idea
    
- Propuesta
    
- Borrador
    
- En prueba
    
- Sandbox
    
- Aprobada documentalmente
    
- Aprobada técnicamente
    
- Activa
    
- Pausada
    
- Rechazada
    

Ninguna función pasa directo de idea a activa.

---

# 49. CRITERIOS DE ÉXITO DEL CONTROL DE CAMBIOS

Este documento funciona si Robert:

- permite mejorar sin perder orden;
    
- evita borrar versiones importantes;
    
- registra decisiones;
    
- separa idea de aprobación;
    
- separa visual de lógica;
    
- separa función de ejecución;
    
- separa conexión de automatización;
    
- protege reglas de seguridad;
    
- mantiene control del usuario;
    
- evita avanzar fases sin permiso;
    
- detecta escalamiento de cambios;
    
- detecta conflictos entre cambios;
    
- detecta dependencias pendientes.
    

---

# 50. CRITERIOS DE FRACASO DEL CONTROL DE CAMBIOS

Este documento falla si Robert:

- cambia documentos aprobados sin permiso;
    
- crea versiones contradictorias;
    
- borra contexto importante;
    
- agrega funciones sin prueba;
    
- cambia seguridad sin decisión;
    
- permite conexiones prematuras;
    
- permite automatizaciones prematuras;
    
- confunde propuesta con aprobación;
    
- no registra decisiones;
    
- pierde trazabilidad;
    
- no detecta cuando un cambio sube de riesgo;
    
- fusiona cambios conflictivos sin aprobación;
    
- avanza cambios bloqueados por dependencia.
    

---

# 51. CAMBIOS INCLUIDOS EN LA VERSIÓN 0.2

Esta versión agrega correcciones importantes antes de aprobación:

## Corrección 1 — Escalamiento dinámico de cambios

Se agregó la regla de que una clasificación inicial puede cambiar si aparece nueva información.

Ahora Robert debe registrar:

- tipo inicial;
    
- tipo final;
    
- riesgo inicial;
    
- riesgo final;
    
- motivo del escalamiento;
    
- acciones permitidas;
    
- acciones bloqueadas.
    

## Corrección 2 — Conflictos entre cambios

Se agregó una regla para detectar cambios que chocan entre sí.

Robert no debe fusionar cambios conflictivos automáticamente.

Debe separar, explicar, proponer opciones y pedir decisión del usuario.

## Corrección 3 — Dependencias entre cambios

Se agregó la regla de cambios bloqueados por dependencia.

Un cambio no puede avanzar si depende de otro documento, decisión o fase que todavía no está aprobada.

## Corrección 4 — Flujo oficial actualizado

El flujo oficial ahora incluye:

- clasificación inicial;
    
- revisión de conflictos;
    
- revisión de dependencias;
    
- reclasificación si aparece nueva información;
    
- nivel de riesgo final.
    

---

# 52. SIGUIENTE PASO

Después de crear este documento, se debe hacer una revisión inicial.

Si el usuario lo aprueba, se registrará:

DECISIÓN #007 — ROBERT_CONTROL_DE_CAMBIOS aprobado

Después de eso, Robert podrá avanzar con más seguridad hacia:

- especificación técnica de componentes;
    
- mockup visual;
    
- prompt para Figma;
    
- prompt para Claude/Cursor;
    
- preparación de prototipo técnico;
    
- diseño del flujo programable.
    

---

# 53. ESTADO FINAL DEL DOCUMENTO

Estado:

Borrador corregido pendiente de revisión.

Este documento no autoriza programación.

No autoriza conexiones externas.

No autoriza automatizaciones.

No autoriza agentes autónomos.

Solo define cómo Robert debe cambiar, mejorar y evolucionar sin romper el sistema.

---

# 54. PRINCIPIO FINAL

Robert debe poder evolucionar sin desordenarse.

Cambiar no es romper.

Mejorar no es ejecutar.

Diseñar no es conectar.

Planear no es automatizar.

El usuario manda.

# REVISIÓN INICIAL — ROBERT_CONTROL_DE_CAMBIOS

Fecha: 29/06/2026

Documento revisado:

ROBERT_CONTROL_DE_CAMBIOS

Versión revisada:

v0.2

Estado de la revisión:

Revisión inicial completada — pendiente de aprobación del usuario

---

# 1. OBJETIVO DE LA REVISIÓN

Esta revisión tiene como objetivo validar si ROBERT_CONTROL_DE_CAMBIOS v0.2 está listo para funcionar como documento oficial de control de cambios, versiones y mejoras de Robert.

La revisión no autoriza programación.

La revisión no autoriza conexiones externas.

La revisión no autoriza automatizaciones.

Solo evalúa si Robert ya tiene una regla clara para cambiar, mejorar, corregir, rediseñar o agregar funciones sin romper lo ya aprobado.

---

# 2. RESULTADO GENERAL

Resultado:

ROBERT_CONTROL_DE_CAMBIOS v0.2 está correctamente planteado como sistema de control de cambios.

El documento ya define:

- qué es un cambio;
    
- tipos de cambio;
    
- niveles de riesgo;
    
- estados de cambio;
    
- flujo oficial para cambios;
    
- escalamiento dinámico;
    
- conflictos entre cambios;
    
- dependencias;
    
- versionado;
    
- reemplazo de documentos;
    
- archivo de versiones anteriores;
    
- registro en Decisions Log;
    
- cambios visuales;
    
- cambios funcionales;
    
- cambios técnicos;
    
- cambios de conexión externa;
    
- cambios de automatización;
    
- límites de la fase actual.
    

Conclusión:

El documento es aprobable como base oficial para manejar cambios futuros en Robert.

---

# 3. CORRECCIONES VALIDADAS

## Corrección 1 — Escalamiento dinámico de cambios

Estado:

Corregido.

Resultado:

El documento ya reconoce que una clasificación inicial puede cambiar si aparece nueva información.

Regla validada:

La clasificación inicial no es definitiva si aparece nueva información.

Esto permite que Robert detecte cuando un cambio que parecía menor se convierte en cambio funcional, técnico, de conexión, automatización o seguridad.

---

## Corrección 2 — Tipo inicial y tipo final

Estado:

Corregido.

Resultado:

El documento ahora permite registrar:

- tipo inicial;
    
- tipo final;
    
- riesgo inicial;
    
- riesgo final;
    
- si hubo escalamiento;
    
- qué información nueva apareció;
    
- qué queda permitido;
    
- qué queda bloqueado.
    

Esto mantiene consistencia con la lógica ya validada en SANDBOX_RULES y SANDBOX_RESULTS.

---

## Corrección 3 — Conflictos entre cambios

Estado:

Corregido.

Resultado:

El documento ya define qué hacer cuando dos cambios chocan entre sí.

Regla validada:

Si dos cambios entran en conflicto, Robert no debe fusionarlos automáticamente.

Debe separar los cambios, explicar el conflicto, proponer opciones y pedir decisión del usuario.

---

## Corrección 4 — Dependencias entre cambios

Estado:

Corregido.

Resultado:

El documento ya reconoce que algunos cambios no pueden avanzar hasta que otro documento, decisión o fase esté aprobado.

Ejemplo:

No se puede programar una pantalla si todavía no está aprobado el wireframe.

No se puede conectar Gmail si todavía no existe plan de conexión.

No se puede automatizar si todavía no existe conexión controlada.

---

# 4. QUÉ QUEDA VALIDADO

ROBERT_CONTROL_DE_CAMBIOS valida que Robert puede cambiar sin perder control.

Queda validado que Robert debe:

- clasificar cada cambio;
    
- identificar documento afectado;
    
- identificar módulo relacionado;
    
- asignar riesgo inicial;
    
- revisar conflictos;
    
- revisar dependencias;
    
- preparar borrador;
    
- revisar;
    
- reclasificar si aparece nueva información;
    
- asignar riesgo final;
    
- pedir aprobación;
    
- registrar decisiones;
    
- conservar versiones anteriores;
    
- no reemplazar documentos aprobados sin autorización.
    

---

# 5. QUÉ NO AUTORIZA ESTA REVISIÓN

Esta revisión no autoriza:

- programación;
    
- creación de app;
    
- conexión con Gmail;
    
- conexión con Calendar;
    
- conexión con WhatsApp;
    
- conexión con CRM;
    
- conexión con Google Sheets;
    
- Zapier;
    
- Make;
    
- n8n;
    
- uso de APIs reales;
    
- automatizaciones reales;
    
- agentes autónomos;
    
- correos reales;
    
- eventos reales;
    
- contacto con clientes;
    
- uso de datos personales reales;
    
- ejecución comercial real;
    
- edición automática de Obsidian.
    

---

# 6. RIESGOS RESTANTES

Aunque el documento está listo para aprobación, siguen activos estos riesgos:

- querer usar control de cambios como permiso para programar;
    
- aprobar funciones nuevas sin pruebas;
    
- cambiar visual y romper seguridad;
    
- agregar conexiones externas antes de tiempo;
    
- mezclar cambios visuales con cambios funcionales;
    
- olvidar registrar decisiones;
    
- reemplazar documentos sin archivar versión anterior;
    
- permitir automatizaciones antes de tener pruebas técnicas.
    

---

# 7. RECOMENDACIÓN FINAL

Se recomienda aprobar ROBERT_CONTROL_DE_CAMBIOS v0.2 como documento oficial de control de cambios de Robert.

Motivo:

Robert ya tiene MVP manual, sandbox manual, plan técnico y wireframe aprobados.

Antes de seguir hacia componentes, mockups, prompts técnicos o programación, Robert necesita una regla formal para manejar mejoras y cambios futuros.

---

# 8. DECISIÓN RECOMENDADA

Decisión recomendada:

Aprobar ROBERT_CONTROL_DE_CAMBIOS v0.2 como documento oficial de control de cambios, versiones y mejoras de Robert.

Nombre sugerido:

DECISIÓN #007 — ROBERT_CONTROL_DE_CAMBIOS aprobado

Estado actual:

Pendiente de aprobación del usuario.

---

# 9. SIGUIENTE PASO SI SE APRUEBA

Si el usuario aprueba este documento, se debe registrar:

DECISIÓN #007 — ROBERT_CONTROL_DE_CAMBIOS aprobado

Después, Robert podrá avanzar con más seguridad hacia uno de estos caminos:

1. Crear especificación técnica de componentes.
    
2. Crear mockup visual en texto.
    
3. Crear prompt para Figma.
    
4. Crear prompt para Claude/Cursor.
    
5. Preparar prototipo técnico todavía sin conexiones reales.
    

---

# 10. CONCLUSIÓN

ROBERT_CONTROL_DE_CAMBIOS v0.2 está listo para aprobación.

El documento permite que Robert evolucione sin desordenarse.

Integra:

- tipos de cambio;
    
- niveles de riesgo;
    
- estados;
    
- escalamiento dinámico;
    
- conflictos;
    
- dependencias;
    
- versionado;
    
- decisiones;
    
- límites;
    
- seguridad;
    
- control del usuario.
    

Resultado final:

Aprobable como documento oficial de control de cambios.

No autoriza programación.

No autoriza conexiones.


---

# CAMBIO #010 — Actualización del wireframe técnico a v0.3

Fecha: 29/06/2026
Estado: Aprobado
Decisión relacionada: DECISIÓN #010 — Aprobación de ROBERT_TECHNICAL_MVP_WIREFRAME v0.3
Documento afectado: ROBERT_TECHNICAL_MVP_WIREFRAME.md
Tipo de cambio: Tipo 3 — Cambio visual / UX
Nivel de riesgo inicial: Nivel 2 — Medio
Nivel de riesgo final: Nivel 2 — Medio

---

## Cambio realizado

Se actualizó el documento oficial:

**ROBERT_TECHNICAL_MVP_WIREFRAME.md**

de versión v0.2 a versión v0.3.

---

## Mejoras integradas

La versión v0.3 integra:

1. RiskBadge con motivo visible
2. Vista “Pendiente de mi decisión”
3. Mapa visual de documentos por fase y estado

---

## Motivo del cambio

El cambio mejora la claridad, seguridad y control visual del MVP técnico básico de Robert.

Permite que el usuario vea mejor:

* Riesgos
* Motivos de riesgo
* Decisiones pendientes
* Estados documentales
* Avance general del sistema

---

## Documentos relacionados

* ROBERT_TECHNICAL_MVP_WIREFRAME.md
* ROBERT_TECHNICAL_MVP_WIREFRAME_v0.3_PROPUESTA.md
* ROBERT_HOME.md
* ROBERT_DECISIONS_LOG.md
* ROBERT_CONTROL_DE_CAMBIOS.md

---

## Alcance autorizado

Este cambio autoriza únicamente actualización documental y visual.

---

## Alcance no autorizado

Este cambio no autoriza:

* Programar la app
* Conectar APIs reales
* Conectar GitHub automáticamente
* Conectar Gmail
* Conectar Google Calendar
* Automatizar acciones reales
* Ejecutar agentes autónomos
* Tomar decisiones por el usuario

---

## Estado final

Cambio aprobado e integrado documentalmente.

ROBERT_TECHNICAL_MVP_WIREFRAME v0.3 queda como wireframe oficial actualizado del MVP técnico básico.


No autoriza automatizaciones.

No autoriza agentes autónomos.

Autoriza únicamente usar este documento como regla para manejar cambios futuros de Robert.

---

# CAMBIO #011 — Creación de ROBERT_TECHNICAL_COMPONENTS_SPEC v0.1

Fecha: 29/06/2026
Estado: Borrador técnico creado — pendiente de revisión
Documento creado: ROBERT_TECHNICAL_COMPONENTS_SPEC.md
Ubicación: 10_MVP
Tipo de cambio: Tipo 5 — Cambio técnico
Nivel de riesgo inicial: Nivel 3 — Alto
Nivel de riesgo final: Nivel 2 — Medio

---

## Cambio realizado

Se creó el documento:

**ROBERT_TECHNICAL_COMPONENTS_SPEC v0.1**

como borrador técnico inicial para convertir el wireframe aprobado de Robert en una especificación de componentes técnicos.

---

## Documento base relacionado

Este documento toma como base:

**ROBERT_TECHNICAL_MVP_WIREFRAME v0.3**

---

## Motivo del cambio

Robert ya cuenta con un wireframe técnico aprobado.

El siguiente paso lógico es definir los componentes técnicos que tendría el MVP básico antes de programar.

---

## Contenido principal del documento

El documento define de forma inicial:

* Componentes principales del MVP
* Modos operativos
* Estados del sistema
* RiskBadge
* ApprovalGate
* DecisionInbox
* DocumentStatusMap
* CurrentStatePanel
* HistoryLog
* SandboxPanel
* Modelos de datos conceptuales
* Flujos principales del MVP
* Estructura visual propuesta
* Estructura futura de archivos
* Criterios de aceptación
* Criterios de seguridad

---

## Motivo del riesgo

El cambio inicia una transición desde documentación visual hacia especificación técnica.

Aunque no se programó nada, el documento acerca a Robert a una futura fase de desarrollo.

---

## Reducción de riesgo

El riesgo baja de Nivel 3 — Alto a Nivel 2 — Medio porque:

* El documento es solo borrador
* No programa la app
* No conecta APIs
* No automatiza acciones
* No modifica archivos automáticamente
* No ejecuta acciones reales
* Requiere revisión y aprobación formal antes de quedar oficial

---

## Alcance autorizado

Este cambio autoriza únicamente:

* Crear el borrador técnico
* Revisarlo
* Corregirlo
* Usarlo como base para discusión técnica

---

## Alcance no autorizado

Este cambio no autoriza:

* Programar la app
* Conectar GitHub automáticamente
* Conectar Gmail
* Conectar Google Calendar
* Conectar APIs reales
* Automatizar acciones
* Activar agentes autónomos
* Ejecutar decisiones reales

---

## Estado final

ROBERT_TECHNICAL_COMPONENTS_SPEC v0.1 queda creado como:

**Borrador técnico inicial pendiente de revisión**

No queda aprobado todavía.


---

# CAMBIO #012 — Convención visual del grafo en Obsidian

Fecha: 30/06/2026
Estado: Validado en Obsidian
Documento afectado: ROBERT_VISUAL
Tipo de cambio: Visual / UX documental
Nivel de riesgo inicial: Nivel 2 — Medio
Nivel de riesgo final: Nivel 2 — Medio

---

## Cambio realizado

Se actualizó **ROBERT_VISUAL** para integrar la convención visual del grafo de Obsidian.

Esta convención define cómo representar visualmente los documentos de Robert usando:

* Órbitas
* Capas
* Colores
* Wikilinks
* Etiquetas
* Grupos visuales en Graph View

---

## Motivo del cambio

La vista gráfica de Obsidian se veía gris, simple y poco jerárquica porque los documentos no tenían suficientes enlaces ni etiquetas semánticas.

Se validó que el grafo mejora cuando cada documento usa:

* Enlaces intencionales
* Tags por órbita
* Tags por función
* Colores por grupo
* Filtros limpios

---

## Regla visual aprobada

Robert usará dos ejes visuales:

**Órbita = posición / cercanía al núcleo**
**Capa o función = color visual**

---

## Centro visual

El centro visual del grafo será:

**ROBERT_HOME**

---

## Centro conceptual

El centro conceptual del sistema seguirá siendo:

**ROBERT_CONTEXT_MASTER**

---

## ROBERT_CORE

No se crea todavía un archivo llamado ROBERT_CORE.

Robert Core se mantiene como idea abstracta del sistema, no como documento activo.

Solo se creará si la identidad del sistema crece demasiado y ya no cabe de forma limpia en ROBERT_CONTEXT_MASTER.

---

## Alcance autorizado

Este cambio autoriza únicamente:

* Organización visual en Obsidian
* Uso de wikilinks
* Uso de etiquetas
* Uso de grupos de color
* Limpieza de nodos grises
* Separación entre documentos oficiales y temporales

---

## Alcance no autorizado

Este cambio no autoriza:

* Programar la interfaz visual real
* Crear el HUD final de Robert
* Conectar Obsidian automáticamente con GitHub
* Automatizar cambios documentales
* Crear agentes visuales
* Activar apps externas
* Ejecutar acciones reales

---

## Estado final

La convención visual del grafo de Obsidian queda validada como apoyo estructural del Proyecto Robert.

No reemplaza el wireframe técnico v0.3.

No reemplaza el futuro Command Center visual.

Funciona como una capa de navegación documental dentro de Obsidian.


## Estado final

Cambio aprobado e integrado documentalmente.

ROBERT_TECHNICAL_MVP_WIREFRAME v0.3 queda como wireframe oficial actualizado del MVP técnico básico.

---

# CAMBIO #013 — Reanclaje de ROBERT_CONTEXT_MASTER v0.5

Fecha: 30/06/2026
Estado: Actualizado
Documento afectado: ROBERT_CONTEXT_MASTER
Tipo de cambio: Actualización de fuente de verdad
Nivel de riesgo inicial: Alto
Nivel de riesgo final: Medio

---

## Cambio realizado

Se actualizó **ROBERT_CONTEXT_MASTER** a versión v0.5 para reanclar el estado real actual del Proyecto Robert.

---

## Motivo del cambio

Se detectó que ROBERT_CONTEXT_MASTER todavía contenía secciones desactualizadas que no reflejaban completamente el avance actual del proyecto.

El documento todavía mencionaba estados anteriores como:

* Fase documental inicial
* Documentos pendientes que ya habían sido creados
* Preparar ROBERT_TECHNICAL_MVP_PLAN como siguiente paso, aunque ese documento ya existe
* Estados previos al checkpoint de GitHub
* Estados previos a la convención visual de Obsidian
* Estado previo a ROBERT_TECHNICAL_COMPONENTS_SPEC

---

## Corrección aplicada

La versión v0.5 reancla el contexto maestro al estado actual:

* Fase 10 — MVP técnico básico en preparación
* MVP manual validado
* Sandbox manual validado
* GitHub configurado como respaldo documental privado
* ROBERT_TECHNICAL_MVP_PLAN aprobado
* ROBERT_TECHNICAL_MVP_WIREFRAME v0.3 aprobado
* ROBERT_TECHNICAL_COMPONENTS_SPEC v0.1 creado como borrador
* ROBERT_TECHNICAL_COMPONENTS_SPEC v0.2_PROPUESTA en revisión
* Convención visual de Obsidian validada
* Sin programación autorizada todavía
* Sin conexiones reales
* Sin automatizaciones reales

---

## Prioridad documental corregida

Se mantuvo la prioridad canónica entre documentos, con ROBERT_SECURITY_RULES como máxima autoridad de seguridad y ROBERT_CONTEXT_MASTER como fuente central de verdad del estado general.

ROBERT_CONTROL_DE_CAMBIOS queda reconocido como documento de registro y trazabilidad de cambios, sin reemplazar a CONTEXT_MASTER ni a SECURITY_RULES.

---

## Alcance autorizado

Este cambio autoriza únicamente:

* Actualizar el contexto maestro
* Corregir estado del proyecto
* Alinear documentos técnicos con la fuente de verdad
* Reanclar futuras especificaciones técnicas

---

## Alcance no autorizado

Este cambio no autoriza:

* Programar la app
* Conectar herramientas externas
* Automatizar documentos
* Activar agentes autónomos
* Ejecutar acciones reales
* Aprobar automáticamente COMPONENTS_SPEC v0.2

---


---

# CAMBIO #014 — Reconciliación de ROBERT_PHASES v0.5

Fecha: 30/06/2026
Estado: Actualizado — pendiente de aprobación formal
Documento afectado: ROBERT_PHASES
Tipo de cambio: Cambio documental maestro / fases
Nivel de riesgo inicial: Alto
Nivel de riesgo final: Medio

---

## Cambio realizado

Se actualizó **ROBERT_PHASES** a versión v0.5 para corregir contradicciones internas en el mapa de fases del Proyecto Robert.

---

## Motivo del cambio

Se detectó que ROBERT_PHASES tenía dos numeraciones de fases conviviendo dentro del mismo documento.

La contradicción principal era:

* En una parte, Fase 10 significaba MVP técnico básico.
* En otra parte, Fase 10 significaba conexión segura con herramientas.
* Una sección seguía diciendo que Robert estaba en Fase 1.
* Otra sección ya marcaba fases posteriores como completadas.
* El documento todavía mencionaba MVP_PLAN como pendiente.
* El cierre seguía hablando de aprobar ROBERT_PHASES v0.3.

---

## Corrección aplicada

ROBERT_PHASES v0.5 deja una sola numeración oficial:

* Fase 1 — Identidad y visión
* Fase 2 — Documentos maestros
* Fase 3 — Fuente central de verdad
* Fase 4 — Comandos
* Fase 5 — Módulos
* Fase 6 — Arquitectura conceptual
* Fase 7 — Diseño visual / UX
* Fase 8 — MVP manual
* Fase 9 — Sandbox manual
* Fase 10 — MVP técnico básico
* Fase 11 — Conexión segura con herramientas
* Fase 12 — Automatizaciones controladas
* Fase 13 — Voz / multimodal
* Fase 14 — Agentes especializados
* Fase 15 — Business Builder avanzado
* Fase 16 — Seguridad avanzada / pruebas
* Fase 17 — Iteraciones y expansión

---

## Estado oficial reanclado

Robert queda reconocido en:

**Fase 10 — MVP técnico básico en preparación**

---

## Separación corregida

ROBERT_PHASES v0.5 separa claramente:

* Riesgo
* Autonomía
* Tipo de cambio
* Estado de fase

También aclara que:

* Nivel 5 no existe como riesgo.
* Nivel 5 solo puede existir como autonomía si SECURITY_RULES lo define así.
* Tipo de cambio no es nivel de riesgo.

---

## Alcance autorizado

Este cambio autoriza únicamente:

* Corregir el mapa de fases
* Unificar numeración
* Reanclar el estado actual
* Eliminar contradicciones internas
* Usar ROBERT_PHASES v0.5 como base pendiente de aprobación formal

---

## Alcance no autorizado

Este cambio no autoriza:

* Programar la app
* Avanzar a Fase 11
* Conectar herramientas externas
* Automatizar GitHub
* Crear agentes autónomos
* Ejecutar acciones reales
* Aprobar automáticamente COMPONENTS_SPEC v0.2

---

## Estado final

ROBERT_PHASES v0.5 queda actualizado como:

**Mapa de fases reconciliado — pendiente de aprobación formal**

El siguiente paso recomendado es actualizar ROBERT_HOME y después revisar la escala de riesgo en SECURITY_RULES y CONTROL_DE_CAMBIOS. 

## Estado final

ROBERT_CONTEXT_MASTER v0.5 queda como fuente de verdad actualizada del estado general del Proyecto Robert.

El siguiente paso recomendado es corregir ROBERT_TECHNICAL_COMPONENTS_SPEC_v0.2_PROPUESTA tomando como base el nuevo CONTEXT_MASTER v0.5.


---

# ACTUALIZACIÓN — ESCALA DE RIESGO, AUTONOMÍA Y TIPO DE CAMBIO

Fecha: 30/06/2026
Estado: Escala alineada con ROBERT_SECURITY_RULES
Documento relacionado: ROBERT_SECURITY_RULES
Motivo: Evitar confusión entre riesgo, autonomía y tipo de cambio

---

## Cambio realizado

Se actualiza ROBERT_CONTROL_DE_CAMBIOS para alinearse con la escala oficial aclarada en ROBERT_SECURITY_RULES.

---

## Regla principal

Robert debe separar claramente:

1. Nivel de riesgo
2. Nivel de autonomía
3. Tipo de cambio
4. Estado documental

Estos conceptos no deben mezclarse.

---

## Escala oficial de riesgo

La escala oficial de riesgo queda así:

```text
Nivel 0 — Informativo
Nivel 1 — Bajo
Nivel 2 — Medio
Nivel 3 — Alto
Nivel 4 — Crítico
```

---

## Regla sobre Nivel 5

No existe Nivel 5 como riesgo.

Nivel 5 solo puede existir dentro de la escala de autonomía, si ROBERT_SECURITY_RULES lo define así.

---

## Escala de autonomía

La autonomía es independiente del riesgo.

La autonomía describe qué tanto puede actuar Robert por sí mismo dentro de un alcance autorizado.

Actualmente Robert no tiene autonomía ejecutiva activa.

---

## Tipo de cambio

El tipo de cambio clasifica la naturaleza de una modificación.

Ejemplos:

* Cambio documental
* Cambio visual / UX
* Cambio técnico documental
* Cambio de seguridad
* Cambio de conexión externa
* Cambio de automatización

Tipo de cambio no es nivel de riesgo.

---

## Estado documental

El estado documental describe la situación de un documento, cambio o decisión.

Ejemplos:

* Borrador
* En revisión
* Pendiente de aprobación
* Aprobado
* Rechazado
* Pausado
* Archivado
* Reemplazado

---

## Formato obligatorio para cambios futuros

Cada cambio importante debe separar:

```text
Tipo de cambio:
Nivel de riesgo:
Nivel de autonomía:
Estado documental:
```

Ejemplo correcto:

```text
Tipo de cambio: Cambio técnico documental
Nivel de riesgo: Nivel 3 — Alto
Nivel de autonomía: Nivel 0 — Sin autonomía ejecutiva
Estado documental: En revisión
```

---

## Alcance

Esta actualización solo aclara clasificación y control documental.

No autoriza:

* Programación
* Conexiones reales
* Automatizaciones
* Agentes autónomos
* Ejecución externa
* Avance a Fase 11

---

## Estado final

ROBERT_CONTROL_DE_CAMBIOS queda alineado con ROBERT_SECURITY_RULES en la separación entre riesgo, autonomía, tipo de cambio y estado documental.


---

# CAMBIO #015 — Aprobación e integración de ROBERT_TECHNICAL_COMPONENTS_SPEC v0.2

Fecha: 30/06/2026
Estado: Aprobado e integrado
Documento afectado: ROBERT_TECHNICAL_COMPONENTS_SPEC
Tipo de cambio: Cambio técnico documental / especificación técnica
Nivel de riesgo inicial: Nivel 3 — Alto
Nivel de riesgo final: Nivel 2 — Medio
Nivel de autonomía: Nivel 0 — Sin autonomía ejecutiva
Decisión relacionada: DECISIÓN #011 — Aprobación de ROBERT_TECHNICAL_COMPONENTS_SPEC v0.2

---

## Cambio realizado

Se actualizó el documento oficial:

**ROBERT_TECHNICAL_COMPONENTS_SPEC**

de versión v0.1 a versión v0.2.

La versión v0.2 toma como base la propuesta aprobada:

**ROBERT_TECHNICAL_COMPONENTS_SPEC_v0.2_PROPUESTA**

---

## Motivo del cambio

La versión v0.1 tenía problemas de alineación con la fuente de verdad y sobrealcance técnico.

La versión v0.2 corrige esos puntos y queda alineada con:

* ROBERT_CONTEXT_MASTER v0.5
* ROBERT_PHASES v0.5
* ROBERT_SECURITY_RULES
* ROBERT_CONTROL_DE_CAMBIOS
* ROBERT_DECISIONS_LOG
* ROBERT_TECHNICAL_MVP_PLAN
* ROBERT_TECHNICAL_MVP_WIREFRAME v0.3

---

## Correcciones integradas

La versión v0.2:

* Reancla el estado del proyecto a ROBERT_CONTEXT_MASTER v0.5.
* Respeta la jerarquía canónica de documentos.
* Separa riesgo, autonomía, tipo de cambio y estado documental.
* Limita el alcance a 10 componentes prioritarios.
* Mapea componentes a capas.
* Deja componentes secundarios para versiones futuras.
* Mantiene la estructura técnica futura como anexo conceptual.
* No autoriza programación ni conexiones reales.

---

## Alcance autorizado

Este cambio autoriza únicamente:

* Usar COMPONENTS_SPEC v0.2 como especificación técnica documental inicial.
* Usarla como base para futuras especificaciones documentales.
* Mantener el avance dentro de Fase 10.
* Preparar, si el usuario lo autoriza después, documentos derivados como DATA_MODEL_SPEC.

---

## Alcance no autorizado

Este cambio no autoriza:

* Programar la app.
* Crear código.
* Conectar APIs reales.
* Conectar GitHub automáticamente.
* Conectar Gmail.
* Conectar Google Calendar.
* Automatizar acciones.
* Activar agentes autónomos.
* Ejecutar acciones reales.
* Avanzar automáticamente a Fase 11.

---

## Estado final

ROBERT_TECHNICAL_COMPONENTS_SPEC v0.2 queda aprobado e integrado como especificación técnica documental inicial del MVP técnico básico.

Robert sigue en:

**Fase 10 — MVP técnico básico en preparación**

Sin programación autorizada, sin conexiones reales, sin automatizaciones reales y sin agentes autónomos activos.

---

# CAMBIO #016 — Creación de ROBERT_TECHNICAL_DATA_MODEL_SPEC v0.1

Fecha: 02/07/2026
Estado: Borrador técnico documental creado — pendiente de revisión
Documento creado: ROBERT_TECHNICAL_DATA_MODEL_SPEC
Ubicación: 10_MVP
Tipo de cambio: Cambio técnico documental / modelo de datos conceptual
Nivel de riesgo inicial: Nivel 3 — Alto
Nivel de riesgo final esperado: Nivel 2 — Medio
Nivel de autonomía: Nivel 0 — Sin autonomía ejecutiva

---

## Cambio realizado

Se creó el documento:

**ROBERT_TECHNICAL_DATA_MODEL_SPEC v0.1**

como borrador técnico documental para definir los modelos de datos conceptuales iniciales del MVP técnico básico de Robert.

---

## Documento base relacionado

Este documento toma como base:

**ROBERT_TECHNICAL_COMPONENTS_SPEC v0.2**

---

## Motivo del cambio

Después de aprobar COMPONENTS_SPEC v0.2, el siguiente paso lógico dentro de la Fase 10 es definir qué datos conceptuales necesitarían los componentes prioritarios del MVP técnico básico.

---

## Contenido principal del documento

El documento define modelos conceptuales como:

* SystemState
* RobertDocument
* DecisionRecord
* ChangeRecord
* RiskRecord
* CommandRequest
* PendingDecision
* ModeState
* ComponentState
* GitHubBackupStatus
* ObsidianGraphStatus

También define:

* Datos permitidos
* Datos prohibidos
* Relaciones entre modelos
* Reglas de validación
* Criterios de aceptación
* Riesgo del documento

---

## Motivo del riesgo

El documento empieza a definir estructura de datos para una futura implementación técnica.

Aunque no programa nada ni crea una base de datos real, acerca el proyecto a una futura fase de construcción.

---

## Reducción de riesgo

El riesgo final esperado baja a Nivel 2 — Medio porque:

* El documento es conceptual
* No crea base de datos real
* No programa la app
* No conecta herramientas externas
* No automatiza acciones
* No ejecuta acciones reales
* Queda pendiente de revisión antes de aprobación

---

## Alcance autorizado

Este cambio autoriza únicamente:

* Crear el borrador documental
* Revisarlo
* Corregirlo
* Usarlo como base para discusión técnica futura

---

## Alcance no autorizado

Este cambio no autoriza:

* Programar la app
* Crear base de datos real
* Crear tablas reales
* Conectar Supabase

  ---

# CAMBIO #018 — Aprobación de CONVENCIÓN VISUAL v0.2

Fecha: 03/07/2026  
Estado: Aprobado e integrado  
Documento afectado: ROBERT_VISUAL  
Decisión relacionada: DECISIÓN #013 — Aprobación de CONVENCIÓN VISUAL v0.2  
Fase relacionada: Fase 10 — MVP técnico básico en preparación  

---

## Cambio realizado

Se aprobó e integró la:

**CONVENCIÓN VISUAL v0.2 — ÓRBITAS POR FUNCIÓN ARQUITECTÓNICA**

como criterio oficial para organizar el grafo documental de Robert en Obsidian.

---

## Motivo del cambio

La convención anterior podía generar ambigüedad porque mezclaba documentos de memoria, control, gobierno, visual, sandbox y técnica dentro de las mismas órbitas.

Con esta actualización, la organización visual queda más clara:

**Órbita = función arquitectónica**

**Color = capa o función visual**

---

## Convención integrada

- Núcleo: ROBERT_HOME
- Órbita 1: Núcleo estructural / Fuente de verdad
- Órbita 2: Gobierno / Control / Seguridad
- Órbita 3: Técnico / MVP / Sandbox
- Órbita 4: Módulos / Capacidades / Puertas futuras
- Órbita 5: Visual / Presentación

---

## Ajustes específicos

ROBERT_DECISIONS_LOG queda fijo en:

**Capa 4 — Gobierno / Control**

ROBERT_SYSTEM_ARCHITECTURE queda reconocido como:

**Maestro de facto**

ROBERT_CONTROL_DE_CAMBIOS queda reconocido como:

**Maestro de facto**

---

## Alcance autorizado

Este cambio autoriza únicamente:

- Actualizar ROBERT_VISUAL con la convención v0.2.
- Corregir tags de órbita en documentos existentes.
- Usar órbitas por función arquitectónica.
- Mantener colores por capa o función visual.
- Corregir inconsistencias visuales en Obsidian Graph View.

---

## Alcance no autorizado

Este cambio no autoriza:

- Crear ROBERT_AGENTS.
- Crear ROBERT_TOOLS.
- Crear ROBERT_PROJECTS.
- Crear nodos vacíos solo para llenar el grafo.
- Programar la app.
- Conectar herramientas externas.
- Automatizar acciones.
- Activar agentes autónomos.
- Convertir Obsidian Graph View en el HUD final de Robert.
- Avanzar automáticamente a Fase 11.

---

## Riesgo

Tipo de cambio:

**Cambio visual documental / organización arquitectónica del grafo**

Nivel de riesgo inicial:

**Nivel 2 — Medio**

Motivo:

El cambio afecta la forma en que se organiza visualmente el sistema documental, pero no modifica reglas operativas ni ejecuta acciones reales.

Nivel de riesgo final:

**Nivel 1 — Bajo**

Motivo:

La convención queda limitada a navegación documental en Obsidian.

Nivel de autonomía:

**Nivel 0 — Sin autonomía ejecutiva**

---

## Estado final

CONVENCIÓN VISUAL v0.2 queda aprobada e integrada como criterio oficial del grafo documental de Obsidian.

Robert continúa en:

**Fase 10 — MVP técnico básico en preparación**

Sin programación autorizada.

Sin conexiones externas.

Sin automatizaciones reales.

Sin agentes autónomos activos.
* Conectar Firebase
* Conectar GitHub automáticamente
* Conectar Gmail
* Conectar Google Calendar
* Conectar APIs reales
* Automatizar acciones
* Activar agentes autónomos
* Ejecutar acciones reales
* Avanzar automáticamente a Fase 11

---

## Estado final

ROBERT_TECHNICAL_DATA_MODEL_SPEC v0.1 queda creado como:

**Borrador técnico documental pendiente de revisión**

No está aprobado todavía.

---

# CAMBIO #017 — Aprobación e integración de ROBERT_TECHNICAL_DATA_MODEL_SPEC v0.1

Fecha: 02/07/2026  
Estado: Aprobado e integrado  
Documento afectado: ROBERT_TECHNICAL_DATA_MODEL_SPEC v0.1  
Ubicación: 10_MVP  
Decisión relacionada: DECISIÓN #012 — Aprobación de ROBERT_TECHNICAL_DATA_MODEL_SPEC v0.1  
Cambio relacionado previo: CAMBIO #016 — Creación de ROBERT_TECHNICAL_DATA_MODEL_SPEC v0.1  
Fase relacionada: Fase 10 — MVP técnico básico en preparación  

---

## Cambio realizado

Se registró la aprobación formal de:

**ROBERT_TECHNICAL_DATA_MODEL_SPEC v0.1**

como documento técnico documental aprobado del MVP técnico básico de Robert.

---

## Motivo del cambio

Después de crear y revisar DATA_MODEL_SPEC v0.1, el usuario aprobó formalmente el documento.

El documento queda integrado como base conceptual para definir qué datos necesitarían los componentes del MVP técnico básico.

---

## Alcance autorizado

Este cambio autoriza únicamente:

- Marcar DATA_MODEL_SPEC v0.1 como aprobado.
- Integrarlo al estado documental actual de Robert.
- Usarlo como base para futuras especificaciones técnicas.
- Relacionarlo con COMPONENTS_SPEC v0.2.
- Usarlo para entender datos conceptuales del MVP.

---

## Alcance no autorizado

Este cambio no autoriza:

- Programar la app.
- Crear una base de datos real.
- Crear tablas reales.
- Crear código.
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

## Riesgo

Tipo de cambio:

**Aprobación técnica documental / integración de modelo de datos conceptual**

Nivel de riesgo inicial:

**Nivel 3 — Alto**

Motivo:

El documento define la estructura conceptual de datos que podría alimentar una futura implementación técnica.

Nivel de riesgo final:

**Nivel 2 — Medio**

Motivo:

El cambio queda limitado a documentación. No crea base de datos real, no programa, no conecta herramientas y no ejecuta acciones.

Nivel de autonomía:

**Nivel 0 — Sin autonomía ejecutiva**

---

## Estado final

ROBERT_TECHNICAL_DATA_MODEL_SPEC v0.1 queda aprobado e integrado documentalmente.

Robert continúa en:

**Fase 10 — MVP técnico básico en preparación**

Sin programación autorizada.

Sin base de datos real.

Sin conexiones externas.

Sin automatizaciones reales.

Sin agentes autónomos activos

---

# CAMBIO #019 — Corrección de tags de órbita según CONVENCIÓN VISUAL v0.2

Fecha: 03/07/2026  
Estado: Aprobado e integrado  
Documento relacionado: ROBERT_VISUAL v0.2  
Decisión relacionada: DECISIÓN #013 — Aprobación de CONVENCIÓN VISUAL v0.2  
Cambio relacionado previo: CAMBIO #018 — Aprobación de CONVENCIÓN VISUAL v0.2  
Fase relacionada: Fase 10 — MVP técnico básico en preparación  

---

## Cambio realizado

Se corrigieron los tags de órbita en los documentos principales de Robert para alinearlos con la:

**CONVENCIÓN VISUAL v0.2 — ÓRBITAS POR FUNCIÓN ARQUITECTÓNICA**

---

## Criterio aplicado

La convención aprobada establece:

**Órbita = función arquitectónica**

**Color = capa o función visual**

---

## Órbitas actualizadas

### Órbita 1 — Núcleo estructural / Fuente de verdad

- ROBERT_CONTEXT_MASTER
- ROBERT_SYSTEM_ARCHITECTURE

### Órbita 2 — Gobierno / Control / Seguridad

- ROBERT_COMMANDS
- ROBERT_SECURITY_RULES
- ROBERT_DECISIONS_LOG
- ROBERT_CONTROL_DE_CAMBIOS
- ROBERT_PHASES

### Órbita 3 — Técnico / MVP / Sandbox

- ROBERT_TECHNICAL_MVP_PLAN
- ROBERT_TECHNICAL_MVP_WIREFRAME
- ROBERT_TECHNICAL_COMPONENTS_SPEC
- ROBERT_TECHNICAL_DATA_MODEL_SPEC
- ROBERT_TECHNICAL_INTERACTION_FLOW_SPEC
- ROBERT_SANDBOX
- SANDBOX_RULES
- SANDBOX_TESTS
- SANDBOX_RESULTS

### Órbita 4 — Módulos / Capacidades / Puertas futuras

- ROBERT_MODULES

### Órbita 5 — Visual / Presentación

- ROBERT_VISUAL

---

## Motivo del cambio

Antes de esta corrección, algunos documentos técnicos y visuales podían quedar mezclados bajo órbitas que no reflejaban su función arquitectónica real.

Con esta actualización, el grafo de Obsidian comunica mejor la estructura del sistema Robert.

---

## Alcance autorizado

Este cambio autoriza únicamente:

- Corregir tags de órbita.
- Alinear documentos existentes con la convención visual v0.2.
- Mejorar la navegación documental en Obsidian.
- Mantener el grafo como herramienta de claridad estructural.

---

## Alcance no autorizado

Este cambio no autoriza:

- Crear ROBERT_AGENTS.
- Crear ROBERT_TOOLS.
- Crear ROBERT_PROJECTS.
- Crear nodos vacíos.
- Programar la app.
- Conectar herramientas externas.
- Automatizar acciones.
- Activar agentes autónomos.
- Convertir Obsidian Graph View en el HUD final.
- Avanzar a Fase 11.

---

## Riesgo

Tipo de cambio:

**Cambio visual documental / limpieza de tags de órbita**

Nivel de riesgo inicial:

**Nivel 2 — Medio**

Motivo:

El cambio afecta la organización visual documental del sistema.

Nivel de riesgo final:

**Nivel 1 — Bajo**

Motivo:

El cambio solo organiza tags y navegación visual. No modifica reglas operativas, no ejecuta acciones y no conecta herramientas.

Nivel de autonomía:

**Nivel 0 — Sin autonomía ejecutiva**

---

## Estado final

Los documentos principales de Robert quedan alineados visualmente con la CONVENCIÓN VISUAL v0.2.

Robert continúa en:

**Fase 10 — MVP técnico básico en preparación**

Sin programación autorizada.

Sin conexiones externas.

Sin automatizaciones reales.

Sin agentes autónomos activos.

---

# CAMBIO #020 — Ajuste visual final de grupos y MVP_PLAN

Fecha: 03/07/2026  
Estado: Aprobado e integrado  
Documento relacionado: ROBERT_VISUAL v0.2  
Documento ajustado: ROBERT_MVP_PLAN  
Decisión relacionada: DECISIÓN #013 — Aprobación de CONVENCIÓN VISUAL v0.2  
Cambio relacionado previo: CAMBIO #019 — Corrección de tags de órbita según CONVENCIÓN VISUAL v0.2  
Fase relacionada: Fase 10 — MVP técnico básico en preparación  

---

## Cambio realizado

Se realizó un ajuste visual final en la organización del grafo de Obsidian después de aplicar la CONVENCIÓN VISUAL v0.2.

El ajuste incluye:

- Mantener el orden de grupos visuales elegido por el usuario.
- Confirmar que la vista puede priorizar órbitas antes que funciones si visualmente resulta más clara.
- Actualizar los tags de ROBERT_MVP_PLAN para evitar que aparezca como nodo gris.
- Integrar ROBERT_MVP_PLAN dentro de la Órbita 3 — Técnico / MVP / Sandbox.

---

## Criterio visual confirmado

El usuario decidió mantener el orden visual donde las órbitas aparecen primero en el panel de grupos de Obsidian.

Este orden prioriza:

**Órbita primero**

**Función después**

Esto permite que el grafo comunique mejor la estructura arquitectónica general del sistema.

---

## Ajuste aplicado a ROBERT_MVP_PLAN

ROBERT_MVP_PLAN queda clasificado como parte de:

**Órbita 3 — Técnico / MVP / Sandbox**

Tags aplicados:

- #robert/orbita-3
- #capa/5
- #tipo/tecnico
- #robert/mvp
- #robert/plan

---

## Motivo del ajuste

ROBERT_MVP_PLAN aparecía como nodo gris en Obsidian Graph View.

Esto indicaba que:

- No tenía tags visibles.
- O tenía tags no alineados con los grupos actuales.
- O no estaba clasificado dentro de la convención visual v0.2.

Con este ajuste, ROBERT_MVP_PLAN queda integrado visualmente al bloque técnico del MVP.

---

## Alcance autorizado

Este cambio autoriza únicamente:

- Mantener el orden visual actual de grupos en Obsidian.
- Clasificar ROBERT_MVP_PLAN dentro de la Órbita 3.
- Corregir tags visuales relacionados.
- Mejorar la navegación documental del grafo.
- Mantener Obsidian Graph View como herramienta de claridad estructural.

---

## Alcance no autorizado

Este cambio no autoriza:

- Programar la app.
- Crear base de datos real.
- Conectar herramientas externas.
- Automatizar acciones.
- Activar agentes autónomos.
- Crear ROBERT_AGENTS.
- Crear ROBERT_TOOLS.
- Crear ROBERT_PROJECTS.
- Convertir Obsidian Graph View en el HUD final.
- Avanzar automáticamente a Fase 11.

---

## Riesgo

Tipo de cambio:

**Cambio visual documental / ajuste final de grupos y tags**

Nivel de riesgo inicial:

**Nivel 1 — Bajo**

Motivo:

El cambio solo afecta organización visual, tags y navegación documental en Obsidian.

Nivel de riesgo final:

**Nivel 1 — Bajo**

Motivo:

No modifica reglas operativas, no cambia arquitectura interna, no ejecuta acciones y no conecta herramientas externas.

Nivel de autonomía:

**Nivel 0 — Sin autonomía ejecutiva**

---

## Estado final

ROBERT_MVP_PLAN queda integrado visualmente en la Órbita 3.

La vista gráfica de Obsidian queda ajustada según la preferencia visual actual del usuario.

Robert continúa en:

**Fase 10 — MVP técnico básico en preparación**

Sin programación autorizada.

Sin base de datos real.

Sin conexiones externas.

Sin automatizaciones reales.

Sin agentes autónomos activos.

---

# CAMBIO #021 — Creación de ROBERT_TECHNICAL_INTERACTION_FLOW_SPEC v0.1

Fecha: 03/07/2026  
Estado: Borrador técnico documental creado — pendiente de revisión  
Documento creado: ROBERT_TECHNICAL_INTERACTION_FLOW_SPEC v0.1  
Ubicación: 10_MVP  
Documento base relacionado: ROBERT_TECHNICAL_DATA_MODEL_SPEC v0.1  
Documento relacionado: ROBERT_TECHNICAL_COMPONENTS_SPEC v0.2  
Fase relacionada: Fase 10 — MVP técnico básico en preparación  

---

## Cambio realizado

Se creó el documento:

**ROBERT_TECHNICAL_INTERACTION_FLOW_SPEC v0.1**

como borrador técnico documental para definir los flujos conceptuales de interacción entre los componentes principales del MVP técnico básico de Robert.

---

## Motivo del cambio

Después de aprobar e integrar ROBERT_TECHNICAL_DATA_MODEL_SPEC v0.1, el siguiente paso lógico era definir cómo interactúan los componentes del MVP técnico básico usando los modelos de datos conceptuales ya aprobados.

---

## Contenido principal del documento

El documento define flujos conceptuales relacionados con:

- Instrucción del usuario
- Comando documental simple
- Aprobación formal de documento
- Detección de riesgo
- Bloqueo por acción no autorizada
- Actualización del estado general
- Decisiones pendientes
- Mapa de documentos
- Modo activo
- Respuesta de Robert
- Respaldo manual en GitHub
- Grafo visual de Obsidian

También define:

- Componentes involucrados
- Modelos de datos utilizados
- Reglas de pausa
- Reglas de bloqueo
- Reglas de aprobación
- Datos permitidos
- Datos prohibidos
- Criterios de aceptación

---

## Alcance autorizado

Este cambio autoriza únicamente:

- Crear el borrador documental.
- Revisarlo.
- Corregirlo.
- Usarlo como base para discusión técnica futura.
- Relacionarlo con DATA_MODEL_SPEC v0.1.
- Relacionarlo con COMPONENTS_SPEC v0.2.

---

## Alcance no autorizado

Este cambio no autoriza:

- Programar la app.
- Crear código.
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

## Riesgo

Tipo de cambio:

**Cambio técnico documental / flujo conceptual de interacción**

Nivel de riesgo inicial:

**Nivel 3 — Alto**

Motivo:

El documento define cómo interactuarían conceptualmente los componentes del MVP técnico básico. Aunque no programa nada, acerca el proyecto a una futura implementación técnica.

Nivel de riesgo final esperado:

**Nivel 2 — Medio**

Motivo:

El documento es conceptual, no crea código, no conecta herramientas externas, no automatiza acciones y no ejecuta nada.

Nivel de autonomía:

**Nivel 0 — Sin autonomía ejecutiva**

---

## Estado final

ROBERT_TECHNICAL_INTERACTION_FLOW_SPEC v0.1 queda creado como:

**Borrador técnico documental pendiente de revisión**

Robert continúa en:

**Fase 10 — MVP técnico básico en preparación**

Sin programación autorizada.

Sin base de datos real.

Sin conexiones externas.

Sin automatizaciones reales.

Sin agentes autónomos activos.

---

# CAMBIO #022 — Corrección de ROBERT_TECHNICAL_INTERACTION_FLOW_SPEC v0.2

Fecha: 03/07/2026  
Estado: Propuesta corregida — pendiente de revisión  
Documento afectado: ROBERT_TECHNICAL_INTERACTION_FLOW_SPEC  
Versión actualizada: v0.2  
Ubicación: 10_MVP  
Cambio relacionado previo: CAMBIO #021 — Creación de ROBERT_TECHNICAL_INTERACTION_FLOW_SPEC v0.1  
Fase relacionada: Fase 10 — MVP técnico básico en preparación  

---

## Cambio realizado

Se actualizó el documento:

**ROBERT_TECHNICAL_INTERACTION_FLOW_SPEC**

de v0.1 a:

**v0.2 — Propuesta corregida pendiente de revisión**

---

## Motivo del cambio

Durante la revisión de v0.1 se detectaron inconsistencias importantes:

- AppShell estaba listado como componente, pero no aparecía claramente en los flujos.
- TopBar y LeftSidebar aparecían en algunos flujos, pero no declaraban qué datos recibían.
- ComponentState estaba declarado como modelo, pero no se usaba en ningún flujo.
- GitHubBackupStatus y ObsidianGraphStatus aparecían en flujos, pero no en la sección de datos que fluyen.
- El manejo de riesgo Nivel 2 era ambiguo.
- No estaba claro cuándo una respuesta simple debía actualizar SystemState o CurrentStatePanel.

---

## Correcciones aplicadas

La versión v0.2 corrige estos puntos mediante:

- Aclaración del rol de AppShell como contenedor raíz.
- Definición de datos recibidos por TopBar.
- Definición de datos recibidos y enviados por LeftSidebar.
- Creación de FLUJO 13 — Estado de componentes.
- Uso explícito de ComponentState.
- Integración de GitHubBackupStatus en datos que fluyen.
- Integración de ObsidianGraphStatus en datos que fluyen.
- Definición específica para riesgo Nivel 2.
- Regla clara sobre cuándo SystemState debe actualizarse.
- Sección ampliada de datos que fluyen entre componentes.

---

## Alcance autorizado

Este cambio autoriza únicamente:

- Corregir el documento técnico.
- Mantenerlo como propuesta pendiente de revisión.
- Usarlo como base para revisión técnica documental.
- Relacionarlo con DATA_MODEL_SPEC v0.1.
- Relacionarlo con COMPONENTS_SPEC v0.2.

---

## Alcance no autorizado

Este cambio no autoriza:

- Aprobar automáticamente INTERACTION_FLOW_SPEC v0.2.
- Programar la app.
- Crear código.
- Crear base de datos real.
- Crear endpoints.
- Conectar herramientas externas.
- Automatizar acciones.
- Activar agentes autónomos.
- Ejecutar acciones reales.
- Avanzar automáticamente a Fase 11.

---

## Riesgo

Tipo de cambio:

**Cambio técnico documental / corrección de flujo conceptual de interacción**

Nivel de riesgo inicial:

**Nivel 3 — Alto**

Motivo:

El documento define cómo interactuarían conceptualmente los componentes del MVP técnico básico.

Nivel de riesgo final esperado:

**Nivel 2 — Medio**

Motivo:

La corrección sigue siendo documental y conceptual. No programa, no conecta herramientas, no automatiza y no ejecuta acciones.

Nivel de autonomía:

**Nivel 0 — Sin autonomía ejecutiva**

---

## Estado final

ROBERT_TECHNICAL_INTERACTION_FLOW_SPEC v0.2 queda como:

**Propuesta corregida pendiente de revisión**

No está aprobado todavía.

Robert continúa en:

**Fase 10 — MVP técnico básico en preparación**

Sin programación autorizada.

Sin base de datos real.

Sin conexiones externas.

Sin automatizaciones reales.

Sin agentes autónomos activos.

---

# CAMBIO #023 — Aprobación e integración de ROBERT_TECHNICAL_INTERACTION_FLOW_SPEC v0.2

Fecha: 03/07/2026  
Estado: Aprobado e integrado  
Documento afectado: ROBERT_TECHNICAL_INTERACTION_FLOW_SPEC v0.2  
Ubicación: 10_MVP  
Decisión relacionada: DECISIÓN #014 — Aprobación de ROBERT_TECHNICAL_INTERACTION_FLOW_SPEC v0.2  
Cambio relacionado previo: CAMBIO #022 — Corrección de ROBERT_TECHNICAL_INTERACTION_FLOW_SPEC v0.2  
Fase relacionada: Fase 10 — MVP técnico básico en preparación  

---

## Cambio realizado

Se registró la aprobación formal e integración documental de:

**ROBERT_TECHNICAL_INTERACTION_FLOW_SPEC v0.2**

como documento técnico documental aprobado del MVP técnico básico de Robert.

---

## Motivo del cambio

Después de corregir la versión v0.1 y revisar la propuesta v0.2, el usuario aprobó formalmente el documento.

La versión v0.2 queda integrada porque define con claridad cómo interactúan conceptualmente los componentes principales del MVP técnico básico.

---

## Correcciones integradas

La versión aprobada integra correcciones sobre:

- AppShell como contenedor raíz.
- TopBar como barra de estado.
- LeftSidebar como navegación documental.
- ComponentState dentro del flujo de componentes.
- GitHubBackupStatus dentro del flujo de respaldo manual.
- ObsidianGraphStatus dentro del flujo visual de Obsidian.
- Manejo de riesgo Nivel 2.
- Reglas de actualización de SystemState.
- Datos que fluyen entre componentes.

---

## Alcance autorizado

Este cambio autoriza únicamente:

- Marcar INTERACTION_FLOW_SPEC v0.2 como aprobado.
- Integrarlo al estado documental actual de Robert.
- Usarlo como base para futuras especificaciones técnicas.
- Relacionarlo con DATA_MODEL_SPEC v0.1.
- Relacionarlo con COMPONENTS_SPEC v0.2.
- Usarlo para entender flujos conceptuales del MVP técnico básico.

---

## Alcance no autorizado

Este cambio no autoriza:

- Programar la app.
- Crear código real.
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

## Riesgo

Tipo de cambio:

**Aprobación técnica documental / integración de flujo conceptual de interacción**

Nivel de riesgo inicial:

**Nivel 3 — Alto**

Motivo:

El documento define cómo interactuarían conceptualmente los componentes del MVP técnico básico.

Nivel de riesgo final:

**Nivel 2 — Medio**

Motivo:

El cambio queda limitado a documentación. No crea código, no conecta herramientas externas, no automatiza acciones y no ejecuta nada.

Nivel de autonomía:

**Nivel 0 — Sin autonomía ejecutiva**

---

## Estado final

ROBERT_TECHNICAL_INTERACTION_FLOW_SPEC v0.2 queda aprobado e integrado documentalmente.

Robert continúa en:

**Fase 10 — MVP técnico básico en preparación**

Sin programación autorizada.

Sin código real.

Sin base de datos real.

Sin conexiones externas.

Sin automatizaciones reales.

Sin agentes autónomos activos.

---

# CAMBIO #024 — Corrección de ROBERT_TECHNICAL_SCREEN_STATE_SPEC v0.2

Fecha: 04/07/2026  
Estado: Propuesta corregida — pendiente de revisión  
Documento afectado: ROBERT_TECHNICAL_SCREEN_STATE_SPEC  
Versión actualizada: v0.2  
Ubicación: 10_MVP  
Fase relacionada: Fase 10 — MVP técnico básico en preparación  
Documento base principal: ROBERT_TECHNICAL_INTERACTION_FLOW_SPEC v0.2  

---

## Cambio realizado

Se corrigió el documento:

**ROBERT_TECHNICAL_SCREEN_STATE_SPEC**

de v0.1 a:

**v0.2 — Propuesta corregida pendiente de revisión**

---

## Motivo del cambio

Durante la revisión de v0.1 se detectaron inconsistencias entre SCREEN_STATE_SPEC e INTERACTION_FLOW_SPEC v0.2.

Las inconsistencias principales estaban en:

- AppShell.
- ModeSelector.
- TopBar.
- DocumentStatusMap.

---

## Correcciones aplicadas

La versión v0.2 corrige:

- AppShell queda alineado con INTERACTION_FLOW_SPEC v0.2.
- AppShell recibe exactamente:
  - system_state
  - component_list
  - active_mode
  - current_phase
  - active_document
  - layout_status
- PendingDecision y RiskRecord ya no aparecen como datos directos de AppShell.
- ModeSelector corrige la dirección de restricted_modes.
- restricted_modes queda como dato enviado por ModeSelector.
- TopBar recupera backup_status.
- TopBar muestra estado de respaldo manual de GitHub.
- DocumentStatusMap deja de recibir SystemState directamente.
- DocumentStatusMap queda alineado con INTERACTION_FLOW_SPEC v0.2.
- Se agrega regla de alineación entre SCREEN_STATE_SPEC e INTERACTION_FLOW_SPEC.

---

## Alcance autorizado

Este cambio autoriza únicamente:

- Corregir el documento técnico.
- Mantenerlo como propuesta pendiente de revisión.
- Usarlo para revisión documental.
- Alinear SCREEN_STATE_SPEC con INTERACTION_FLOW_SPEC v0.2.
- Mantenerlo dentro de Fase 10.

---

## Alcance no autorizado

Este cambio no autoriza:

- Aprobar automáticamente SCREEN_STATE_SPEC v0.2.
- Programar la app.
- Crear código real.
- Crear pantallas reales.
- Crear base de datos real.
- Crear endpoints.
- Conectar herramientas externas.
- Automatizar acciones.
- Activar agentes autónomos.
- Ejecutar acciones reales.
- Avanzar automáticamente a Fase 11.

---

## Riesgo

Tipo de cambio:

**Cambio técnico documental / corrección de estados conceptuales de pantalla**

Nivel de riesgo inicial:

**Nivel 3 — Alto**

Motivo:

El documento define cómo se mostraría conceptualmente la información del MVP técnico básico en pantallas y paneles.

Nivel de riesgo final esperado:

**Nivel 2 — Medio**

Motivo:

La corrección sigue siendo documental. No crea pantallas reales, no programa, no conecta herramientas externas y no ejecuta acciones.

Nivel de autonomía:

**Nivel 0 — Sin autonomía ejecutiva**

---

## Estado final

ROBERT_TECHNICAL_SCREEN_STATE_SPEC v0.2 queda como:

**Propuesta corregida pendiente de revisión**

No está aprobado todavía.

Robert continúa en:

**Fase 10 — MVP técnico básico en preparación**

Sin programación autorizada.

Sin código real.

Sin base de datos real.

Sin conexiones externas.

Sin automatizaciones reales.

Sin agentes autónomos activos.

---

# CAMBIO #025 — Aprobación e integración de ROBERT_TECHNICAL_SCREEN_STATE_SPEC v0.2

Fecha: 04/07/2026  
Estado: Aprobado e integrado  
Documento afectado: ROBERT_TECHNICAL_SCREEN_STATE_SPEC v0.2  
Ubicación: 10_MVP  
Decisión relacionada: DECISIÓN #015 — Aprobación de ROBERT_TECHNICAL_SCREEN_STATE_SPEC v0.2  
Cambio relacionado previo: CAMBIO #024 — Corrección de ROBERT_TECHNICAL_SCREEN_STATE_SPEC v0.2  
Documento base principal: ROBERT_TECHNICAL_INTERACTION_FLOW_SPEC v0.2  
Fase relacionada: Fase 10 — MVP técnico básico en preparación  

---

## Cambio realizado

Se registró la aprobación formal e integración documental de:

**ROBERT_TECHNICAL_SCREEN_STATE_SPEC v0.2**

como documento técnico documental aprobado del MVP técnico básico de Robert.

---

## Motivo del cambio

Después de corregir la versión v0.1 y revisar la propuesta v0.2, el usuario aprobó formalmente el documento.

La versión v0.2 queda integrada porque define los estados conceptuales de pantalla y mantiene alineación con INTERACTION_FLOW_SPEC v0.2.

---

## Correcciones integradas

La versión aprobada integra correcciones sobre:

- AppShell alineado con INTERACTION_FLOW_SPEC v0.2.
- AppShell recibe exactamente:
  - system_state
  - component_list
  - active_mode
  - current_phase
  - active_document
  - layout_status
- PendingDecision y RiskRecord ya no aparecen como datos directos de AppShell.
- ModeSelector corrige la dirección de restricted_modes.
- restricted_modes queda como dato enviado por ModeSelector.
- TopBar recupera backup_status.
- TopBar muestra estado de respaldo manual de GitHub.
- DocumentStatusMap deja de recibir SystemState directamente.
- DocumentStatusMap queda alineado con INTERACTION_FLOW_SPEC v0.2.
- SCREEN_STATE_SPEC no inventa nuevas direcciones de datos.

---

## Alcance autorizado

Este cambio autoriza únicamente:

- Marcar SCREEN_STATE_SPEC v0.2 como aprobado.
- Integrarlo al estado documental actual de Robert.
- Usarlo como base para futuras especificaciones técnicas.
- Usarlo para definir qué información aparece en pantallas y paneles conceptuales.
- Relacionarlo con INTERACTION_FLOW_SPEC v0.2.
- Relacionarlo con COMPONENTS_SPEC v0.2.
- Relacionarlo con DATA_MODEL_SPEC v0.1.

---

## Alcance no autorizado

Este cambio no autoriza:

- Programar la app.
- Crear código real.
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

## Riesgo

Tipo de cambio:

**Aprobación técnica documental / integración de estados conceptuales de pantalla**

Nivel de riesgo inicial:

**Nivel 3 — Alto**

Motivo:

El documento define cómo se mostraría conceptualmente la información del MVP técnico básico en pantallas y paneles.

Nivel de riesgo final:

**Nivel 2 — Medio**

Motivo:

El cambio queda limitado a documentación. No crea pantallas reales, no programa, no conecta herramientas externas y no ejecuta acciones.

Nivel de autonomía:

**Nivel 0 — Sin autonomía ejecutiva**

---

## Estado final

ROBERT_TECHNICAL_SCREEN_STATE_SPEC v0.2 queda aprobado e integrado documentalmente.

Robert continúa en:

**Fase 10 — MVP técnico básico en preparación**

Sin programación autorizada.

Sin código real.

Sin pantallas reales.

Sin base de datos real.

Sin conexiones externas.

Sin automatizaciones reales.

Sin agentes autónomos activos.

---

# CAMBIO #026 — Corrección de ROBERT_COMMANDS v0.4

Fecha: 04/07/2026  
Estado: Propuesta corregida — pendiente de revisión  
Documento afectado: ROBERT_COMMANDS  
Versión actualizada: v0.4  
Ubicación: 02_COMMANDS  
Versión anterior aprobada: ROBERT_COMMANDS v0.3  
Fase relacionada: Fase 10 — MVP técnico básico en preparación  

---

## Cambio realizado

Se corrigió el documento:

**ROBERT_COMMANDS**

de v0.3 aprobado a:

**v0.4 — Propuesta corregida pendiente de revisión**

---

## Motivo del cambio

Se detectó una inconsistencia entre ROBERT_COMMANDS v0.3 y ROBERT_TECHNICAL_USER_ACTIONS_SPEC v0.2.

ROBERT_COMMANDS v0.3 mezclaba:

**Nivel 0 — Informativo / Control de seguridad**

Esto generaba conflicto con la escala oficial de riesgo, donde:

**Nivel 0 — Informativo**

debe mantenerse separado de:

**Acciones de control fuera de la escala de riesgo**

---

## Correcciones aplicadas

La versión v0.4 corrige:

- Nivel 0 queda únicamente como Informativo.
- DETENTE deja de clasificarse como Riesgo 0.
- PAUSA deja de clasificarse como Riesgo 0.
- NO_AVANCES deja de clasificarse como Riesgo 0.
- SOLO_BORRADOR deja de clasificarse como Riesgo 0.
- REVOCA_AUTONOMIA deja de clasificarse como Riesgo 0.
- VOLVER_A_MANUAL deja de clasificarse como Riesgo 0.
- Los comandos de control quedan como acciones fuera de la escala de riesgo.
- INFORME_ACCIONES queda como Nivel 0 o Nivel 1 según alcance.
- Se corrige la alineación de capa de ROBERT_COMMANDS a Capa 2 — Control.
- El tag correcto queda como #capa/2.
- Se alinea ROBERT_COMMANDS con USER_ACTIONS_SPEC v0.2.
- Se alinea ROBERT_COMMANDS con INTERACTION_FLOW_SPEC v0.2.

---

## Alcance autorizado

Este cambio autoriza únicamente:

- Corregir ROBERT_COMMANDS como propuesta v0.4.
- Separar comandos informativos de comandos de control.
- Mantener ROBERT_COMMANDS v0.4 pendiente de revisión.
- Usar v0.4 como base para revisión documental.
- Mantener coherencia con la escala oficial de riesgo.

---

## Alcance no autorizado

Este cambio no autoriza:

- Aprobar automáticamente ROBERT_COMMANDS v0.4.
- Cambiar reglas de seguridad sin aprobación formal.
- Programar la app.
- Crear código real.
- Crear pantallas reales.
- Crear base de datos real.
- Conectar herramientas externas.
- Automatizar acciones.
- Activar agentes autónomos.
- Ejecutar acciones reales.
- Avanzar a Fase 11.

---

## Riesgo

Tipo de cambio:

**Corrección de documento maestro / clasificación de comandos y riesgo**

Nivel de riesgo inicial:

**Nivel 3 — Alto**

Motivo:

ROBERT_COMMANDS es un documento maestro y define comandos operativos del sistema.

Nivel de riesgo final esperado:

**Nivel 2 — Medio**

Motivo:

La corrección es documental. No programa, no conecta herramientas externas, no automatiza y no ejecuta acciones.

Nivel de autonomía:

**Nivel 0 — Sin autonomía ejecutiva**

---

## Estado final

ROBERT_COMMANDS v0.4 queda como:

**Propuesta corregida pendiente de revisión**

No está aprobado todavía.

Robert continúa en:

**Fase 10 — MVP técnico básico en preparación**

Sin programación autorizada.

Sin código real.

Sin pantallas reales.

Sin base de datos real.

Sin conexiones externas.

Sin automatizaciones reales.

Sin agentes autónomos activos.

---

# CAMBIO #027 — Aprobación e integración de ROBERT_COMMANDS v0.4

Fecha: 04/07/2026  
Estado: Aprobado e integrado  
Documento afectado: ROBERT_COMMANDS v0.4  
Ubicación: 02_COMMANDS  
Decisión relacionada: DECISIÓN #016 — Aprobación de ROBERT_COMMANDS v0.4  
Cambio relacionado previo: CAMBIO #026 — Corrección de ROBERT_COMMANDS v0.4  
Versión anterior aprobada: ROBERT_COMMANDS v0.3  
Fase relacionada: Fase 10 — MVP técnico básico en preparación  

---

## Cambio realizado

Se registró la aprobación formal e integración documental de:

**ROBERT_COMMANDS v0.4**

como documento maestro vigente de comandos de Robert.

---

## Motivo del cambio

Después de corregir ROBERT_COMMANDS v0.3 y revisar la propuesta v0.4, el usuario aprobó formalmente la nueva versión.

La versión v0.4 queda integrada porque corrige la mezcla entre:

**Nivel 0 — Informativo**

y:

**Acciones de control fuera de la escala de riesgo**

---

## Correcciones integradas

La versión aprobada integra:

- Nivel 0 queda únicamente como Informativo.
- DETENTE deja de clasificarse como Riesgo 0.
- PAUSA deja de clasificarse como Riesgo 0.
- NO_AVANCES deja de clasificarse como Riesgo 0.
- SOLO_BORRADOR deja de clasificarse como Riesgo 0.
- REVOCA_AUTONOMIA deja de clasificarse como Riesgo 0.
- VOLVER_A_MANUAL deja de clasificarse como Riesgo 0.
- Los comandos de control quedan como acciones fuera de la escala de riesgo.
- INFORME_ACCIONES queda como Nivel 0 o Nivel 1 según alcance.
- ROBERT_COMMANDS queda alineado con Capa 2 — Control.
- Tag corregido: #capa/2.
- ROBERT_COMMANDS queda alineado con USER_ACTIONS_SPEC v0.2.
- ROBERT_COMMANDS queda alineado con INTERACTION_FLOW_SPEC v0.2.
- ROBERT_COMMANDS queda alineado con ROBERT_SECURITY_RULES.

---

## Alcance autorizado

Este cambio autoriza únicamente:

- Marcar ROBERT_COMMANDS v0.4 como aprobado.
- Integrarlo al estado documental actual de Robert.
- Usarlo como documento maestro vigente de comandos.
- Usarlo como base para clasificar comandos informativos.
- Usarlo como base para clasificar comandos de control fuera de la escala de riesgo.
- Mantener coherencia con documentos técnicos derivados.

---

## Alcance no autorizado

Este cambio no autoriza:

- Programar la app.
- Crear código real.
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

## Riesgo

Tipo de cambio:

**Aprobación e integración de documento maestro / comandos y clasificación riesgo-control**

Nivel de riesgo inicial:

**Nivel 3 — Alto**

Motivo:

ROBERT_COMMANDS es un documento maestro y define comandos operativos del sistema.

Nivel de riesgo final:

**Nivel 2 — Medio**

Motivo:

El cambio queda limitado a documentación. No crea código, no conecta herramientas externas, no automatiza acciones y no ejecuta nada.

Nivel de autonomía:

**Nivel 0 — Sin autonomía ejecutiva**

---

## Estado final

ROBERT_COMMANDS v0.4 queda aprobado e integrado documentalmente como documento maestro vigente de comandos.

Robert continúa en:

**Fase 10 — MVP técnico básico en preparación**

Sin programación autorizada.

Sin código real.

Sin pantallas reales.

Sin base de datos real.

Sin conexiones externas.

Sin automatizaciones reales.

Sin agentes autónomos activos.

---

# CAMBIO #028 — Aprobación e integración de ROBERT_TECHNICAL_USER_ACTIONS_SPEC v0.2

Fecha: 04/07/2026  
Estado: Aprobado e integrado  
Documento afectado: ROBERT_TECHNICAL_USER_ACTIONS_SPEC v0.2  
Ubicación: 10_MVP  
Decisión relacionada: DECISIÓN #017 — Aprobación de ROBERT_TECHNICAL_USER_ACTIONS_SPEC v0.2  
Documento base principal: ROBERT_TECHNICAL_SCREEN_STATE_SPEC v0.2  
Documento maestro alineado: ROBERT_COMMANDS v0.4  
Fase relacionada: Fase 10 — MVP técnico básico en preparación  

---

## Cambio realizado

Se registró la aprobación formal e integración documental de:

**ROBERT_TECHNICAL_USER_ACTIONS_SPEC v0.2**

como documento técnico documental aprobado del MVP técnico básico de Robert.

---

## Motivo del cambio

Después de corregir USER_ACTIONS_SPEC v0.1 y revisar la propuesta v0.2, el usuario aprobó formalmente el documento.

La aprobación ocurre después de aprobar ROBERT_COMMANDS v0.4, por lo que USER_ACTIONS_SPEC v0.2 queda alineado con el documento maestro vigente de comandos.

---

## Correcciones integradas

La versión aprobada integra:

- Nivel 0 queda únicamente como Informativo.
- Las acciones de control quedan fuera de la escala de riesgo.
- PAUSA, DETENTE y NO_AVANCES no se clasifican como Riesgo 0.
- Solicitar bloqueo manual queda como acción de control fuera de escala.
- El riesgo pertenece a la acción original que se intenta detener o bloquear.
- Los bloqueos automáticos quedan reservados para ERROR_AND_BLOCKING_SPEC.
- Se agrega regla de alineación documental.
- Se agrega cruce explícito con ROBERT_SANDBOX, SANDBOX_RULES, SANDBOX_TESTS y SANDBOX_RESULTS.
- USER_ACTIONS_SPEC no redefine la lógica del sandbox.
- USER_ACTIONS_SPEC queda alineado con ROBERT_COMMANDS v0.4.
- USER_ACTIONS_SPEC queda alineado con SCREEN_STATE_SPEC v0.2.
- USER_ACTIONS_SPEC queda alineado con INTERACTION_FLOW_SPEC v0.2.

---

## Alcance autorizado

Este cambio autoriza únicamente:

- Marcar USER_ACTIONS_SPEC v0.2 como aprobado.
- Integrarlo al estado documental actual de Robert.
- Usarlo como base para futuras especificaciones técnicas.
- Usarlo para definir acciones conceptuales del usuario.
- Usarlo para clasificar acciones permitidas, restringidas, bloqueadas o futuras.
- Relacionarlo con ROBERT_COMMANDS v0.4.
- Relacionarlo con SCREEN_STATE_SPEC v0.2.
- Relacionarlo con INTERACTION_FLOW_SPEC v0.2.
- Relacionarlo con documentos oficiales de sandbox.

---

## Alcance no autorizado

Este cambio no autoriza:

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

## Riesgo

Tipo de cambio:

**Aprobación técnica documental / integración de acciones conceptuales del usuario**

Nivel de riesgo inicial:

**Nivel 3 — Alto**

Motivo:

El documento define qué acciones podría intentar hacer el usuario desde el MVP técnico básico.

Nivel de riesgo final:

**Nivel 2 — Medio**

Motivo:

El cambio queda limitado a documentación. No crea botones reales, no crea pantallas reales, no programa, no conecta herramientas externas y no ejecuta acciones.

Nivel de autonomía:

**Nivel 0 — Sin autonomía ejecutiva**

---

## Estado final

ROBERT_TECHNICAL_USER_ACTIONS_SPEC v0.2 queda aprobado e integrado documentalmente.

Robert continúa en:

**Fase 10 — MVP técnico básico en preparación**

Sin programación autorizada.

Sin código real.

Sin botones reales.

Sin pantallas reales.

Sin base de datos real.

Sin conexiones externas.

Sin automatizaciones reales.

Sin agentes autónomos activos.

---

# CAMBIO #029 — Corrección de ROBERT_TECHNICAL_ERROR_AND_BLOCKING_SPEC v0.2

Fecha: 04/07/2026  
Estado: Propuesta corregida — pendiente de revisión  
Documento afectado: ROBERT_TECHNICAL_ERROR_AND_BLOCKING_SPEC  
Versión actualizada: v0.2  
Ubicación: 10_MVP  
Documento base principal: ROBERT_TECHNICAL_USER_ACTIONS_SPEC v0.2  
Documento maestro relacionado: ROBERT_COMMANDS v0.4  
Fase relacionada: Fase 10 — MVP técnico básico en preparación  

---

## Cambio realizado

Se corrigió el documento:

**ROBERT_TECHNICAL_ERROR_AND_BLOCKING_SPEC**

de v0.1 a:

**v0.2 — Propuesta corregida pendiente de revisión**

---

## Motivo del cambio

Durante la revisión de v0.1 se detectaron dos puntos a corregir:

- Existía solapamiento entre eventos de bloqueo sin una regla de precedencia.
- El ejemplo histórico de contradicción documental entre USER_ACTIONS_SPEC y ROBERT_COMMANDS tenía una cronología imprecisa.

---

## Correcciones aplicadas

La versión v0.2 corrige:

- Se agrega regla de precedencia entre eventos.
- Se define que, cuando una acción encaje en varios eventos, Robert debe usar el evento más específico disponible.
- EVENTO 5 — Bloqueo automático queda como categoría general.
- EVENTOS 15 al 20 quedan como subtipos específicos del EVENTO 5.
- Conexión no autorizada queda como EVENTO 16 cuando aplique.
- Ejecución no autorizada queda como EVENTO 15 cuando aplique.
- Agente no autorizado queda como EVENTO 18 cuando aplique.
- Se corrige la cronología del ejemplo de contradicción documental.
- Se aclara que USER_ACTIONS_SPEC v0.2 ya había separado Nivel 0 de acciones de control antes de corregir ROBERT_COMMANDS v0.4.
- Se mantiene alineación con ROBERT_COMMANDS v0.4 y USER_ACTIONS_SPEC v0.2.

---

## Alcance autorizado

Este cambio autoriza únicamente:

- Corregir el documento técnico.
- Mantenerlo como propuesta pendiente de revisión.
- Usarlo para revisión documental.
- Alinear errores y bloqueos con USER_ACTIONS_SPEC v0.2.
- Alinear errores y bloqueos con ROBERT_COMMANDS v0.4.
- Mantenerlo dentro de Fase 10.

---

## Alcance no autorizado

Este cambio no autoriza:

- Aprobar automáticamente ERROR_AND_BLOCKING_SPEC v0.2.
- Programar la app.
- Crear código real.
- Crear botones reales.
- Crear pantallas reales.
- Crear base de datos real.
- Crear endpoints.
- Conectar herramientas externas.
- Automatizar acciones.
- Activar agentes autónomos.
- Ejecutar acciones reales.
- Avanzar automáticamente a Fase 11.

---

## Riesgo

Tipo de cambio:

**Cambio técnico documental / corrección de errores y bloqueos conceptuales**

Nivel de riesgo inicial:

**Nivel 3 — Alto**

Motivo:

El documento define cómo Robert debe reaccionar ante errores, bloqueos, contradicciones y acciones prohibidas.

Nivel de riesgo final esperado:

**Nivel 2 — Medio**

Motivo:

La corrección sigue siendo documental. No crea pantallas reales, no programa, no conecta herramientas externas y no ejecuta acciones.

Nivel de autonomía:

**Nivel 0 — Sin autonomía ejecutiva**

---

## Estado final

ROBERT_TECHNICAL_ERROR_AND_BLOCKING_SPEC v0.2 queda como:

**Propuesta corregida pendiente de revisión**

No está aprobado todavía.

Robert continúa en:

**Fase 10 — MVP técnico básico en preparación**

Sin programación autorizada.

Sin código real.

Sin botones reales.

Sin pantallas reales.

Sin base de datos real.

Sin conexiones externas.

Sin automatizaciones reales.

Sin agentes autónomos activos.

---

# CAMBIO #030 — Aprobación e integración de ROBERT_TECHNICAL_ERROR_AND_BLOCKING_SPEC v0.2

Fecha: 04/07/2026  
Estado: Aprobado e integrado  
Documento afectado: ROBERT_TECHNICAL_ERROR_AND_BLOCKING_SPEC v0.2  
Ubicación: 10_MVP  
Decisión relacionada: DECISIÓN #018 — Aprobación de ROBERT_TECHNICAL_ERROR_AND_BLOCKING_SPEC v0.2  
Cambio relacionado previo: CAMBIO #029 — Corrección de ROBERT_TECHNICAL_ERROR_AND_BLOCKING_SPEC v0.2  
Documento base principal: ROBERT_TECHNICAL_USER_ACTIONS_SPEC v0.2  
Documento maestro relacionado: ROBERT_COMMANDS v0.4  
Fase relacionada: Fase 10 — MVP técnico básico en preparación  

---

## Cambio realizado

Se registró la aprobación formal e integración documental de:

**ROBERT_TECHNICAL_ERROR_AND_BLOCKING_SPEC v0.2**

como documento técnico documental aprobado del MVP técnico básico de Robert.

---

## Motivo del cambio

Después de corregir ERROR_AND_BLOCKING_SPEC v0.1 y revisar la propuesta v0.2, el usuario aprobó formalmente el documento.

La versión v0.2 queda integrada porque define cómo Robert debe manejar errores, advertencias, bloqueos automáticos, bloqueos manuales, acciones prohibidas, contradicciones documentales, riesgos críticos y capacidades futuras no disponibles.

---

## Correcciones integradas

La versión aprobada integra:

- Regla de precedencia entre eventos.
- Uso del evento más específico cuando una acción encaja en varios eventos.
- EVENTO 5 — Bloqueo automático como categoría general.
- EVENTOS 15 al 20 como subtipos específicos del EVENTO 5.
- Conexión no autorizada como EVENTO 16 cuando aplique.
- Ejecución no autorizada como EVENTO 15 cuando aplique.
- Agente no autorizado como EVENTO 18 cuando aplique.
- Dato sensible detectado como EVENTO 19 cuando aplique.
- Fase incorrecta como EVENTO 20 cuando aplique.
- Cronología corregida del ejemplo de contradicción documental.
- Nivel 0 únicamente como Informativo.
- Acciones de control fuera de la escala de riesgo.
- Alineación con ROBERT_COMMANDS v0.4.
- Alineación con USER_ACTIONS_SPEC v0.2.
- Alineación con documentos oficiales de sandbox.

---

## Alcance autorizado

Este cambio autoriza únicamente:

- Marcar ERROR_AND_BLOCKING_SPEC v0.2 como aprobado.
- Integrarlo al estado documental actual de Robert.
- Usarlo como base para futuras especificaciones técnicas.
- Usarlo para definir errores conceptuales.
- Usarlo para definir advertencias conceptuales.
- Usarlo para definir bloqueos automáticos conceptuales.
- Usarlo para definir bloqueos manuales conceptuales.
- Usarlo para definir respuestas ante acciones prohibidas.
- Usarlo para definir respuestas ante contradicciones documentales.
- Usarlo para definir reglas de precedencia entre eventos.
- Relacionarlo con ROBERT_COMMANDS v0.4.
- Relacionarlo con USER_ACTIONS_SPEC v0.2.
- Relacionarlo con documentos oficiales de sandbox.

---

## Alcance no autorizado

Este cambio no autoriza:

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

## Riesgo

Tipo de cambio:

**Aprobación técnica documental / integración de errores y bloqueos conceptuales**

Nivel de riesgo inicial:

**Nivel 3 — Alto**

Motivo:

El documento define cómo Robert debe reaccionar ante errores, bloqueos, contradicciones y acciones prohibidas.

Nivel de riesgo final:

**Nivel 2 — Medio**

Motivo:

El cambio queda limitado a documentación. No crea botones reales, no crea pantallas reales, no programa, no conecta herramientas externas y no ejecuta acciones.

Nivel de autonomía:

**Nivel 0 — Sin autonomía ejecutiva**

---

## Estado final

ROBERT_TECHNICAL_ERROR_AND_BLOCKING_SPEC v0.2 queda aprobado e integrado documentalmente.

Robert continúa en:

**Fase 10 — MVP técnico básico en preparación**

Sin programación autorizada.

Sin código real.

Sin botones reales.

Sin pantallas reales.

Sin base de datos real.

Sin conexiones externas.

Sin automatizaciones reales.

Sin agentes autónomos activos.

---

# CAMBIO #031 — Corrección de ROBERT_TECHNICAL_PERMISSIONS_AND_SCOPES_SPEC v0.2

Fecha: 04/07/2026  
Estado: Propuesta corregida — pendiente de revisión  
Documento afectado: ROBERT_TECHNICAL_PERMISSIONS_AND_SCOPES_SPEC  
Versión actualizada: v0.2  
Ubicación: 10_MVP  
Documento base principal: ROBERT_TECHNICAL_ERROR_AND_BLOCKING_SPEC v0.2  
Documentos relacionados: ROBERT_COMMANDS v0.4, ROBERT_TECHNICAL_USER_ACTIONS_SPEC v0.2, ROBERT_TECHNICAL_SCREEN_STATE_SPEC v0.2, ROBERT_TECHNICAL_INTERACTION_FLOW_SPEC v0.2, ROBERT_TECHNICAL_COMPONENTS_SPEC v0.2, ROBERT_TECHNICAL_DATA_MODEL_SPEC v0.1  
Fase relacionada: Fase 10 — MVP técnico básico en preparación  

---

## Cambio realizado

Se corrigió el documento:

**ROBERT_TECHNICAL_PERMISSIONS_AND_SCOPES_SPEC**

de v0.1 a:

**v0.2 — Propuesta corregida pendiente de revisión**

---

## Motivo del cambio

Durante la revisión de v0.1 se detectaron lagunas estructurales importantes:

- El documento no conectaba Permiso y Alcance con los 11 modelos de DATA_MODEL_SPEC v0.1.
- Permiso y Alcance podían interpretarse como modelos nuevos no registrados.
- No existía sección de componentes participantes.
- No se definía dónde se mostraba permiso activo, alcance, duración, expiración o revocación.
- No existía tabla de correspondencia entre permisos y acciones de USER_ACTIONS_SPEC v0.2.
- En la relación con ERROR_AND_BLOCKING_SPEC faltaba EVENTO 5 — Bloqueo automático como categoría general de respaldo.

---

## Correcciones aplicadas

La versión v0.2 corrige:

- Se agrega relación explícita con los 11 modelos de DATA_MODEL_SPEC v0.1.
- Se aclara que Permiso y Alcance no son modelos nuevos oficiales.
- Se define que Permiso y Alcance son estructuras conceptuales derivadas.
- Se aclara que no se crea el modelo PermissionScope en esta versión.
- Se establece que cualquier modelo nuevo futuro requiere actualizar DATA_MODEL_SPEC.
- Se agrega sección de componentes participantes.
- Se incluyen los 10 componentes aprobados en COMPONENTS_SPEC v0.2.
- Se define el rol de AppShell, TopBar, LeftSidebar, CommandCenter, ModeSelector, RiskBadge, ApprovalGate, DecisionInbox, DocumentStatusMap y CurrentStatePanel.
- Se define dónde se muestra permiso activo, alcance activo, duración, expiración, riesgo, decisión pendiente y revocación.
- Se agrega tabla de correspondencia entre los 13 permisos y las acciones de USER_ACTIONS_SPEC v0.2.
- Se agrega EVENTO 5 — Bloqueo automático como categoría general de respaldo.
- Se mantiene alineación con ROBERT_COMMANDS v0.4.
- Se mantiene alineación con USER_ACTIONS_SPEC v0.2.
- Se mantiene alineación con ERROR_AND_BLOCKING_SPEC v0.2.
- Se mantiene alineación con DATA_MODEL_SPEC v0.1.
- Se mantiene alineación con SCREEN_STATE_SPEC v0.2 e INTERACTION_FLOW_SPEC v0.2.

---

## Alcance autorizado

Este cambio autoriza únicamente:

- Corregir el documento técnico.
- Mantenerlo como propuesta pendiente de revisión.
- Usarlo para revisión documental.
- Alinear permisos y alcances con DATA_MODEL_SPEC v0.1.
- Alinear permisos con USER_ACTIONS_SPEC v0.2.
- Alinear bloqueos con ERROR_AND_BLOCKING_SPEC v0.2.
- Alinear visualización con COMPONENTS_SPEC v0.2 y SCREEN_STATE_SPEC v0.2.
- Mantenerlo dentro de Fase 10.

---

## Alcance no autorizado

Este cambio no autoriza:

- Aprobar automáticamente PERMISSIONS_AND_SCOPES_SPEC v0.2.
- Crear modelo PermissionScope.
- Modificar DATA_MODEL_SPEC automáticamente.
- Programar la app.
- Crear código real.
- Crear botones reales.
- Crear pantallas reales.
- Crear sistema real de permisos.
- Crear usuarios reales.
- Crear roles reales.
- Crear base de datos real.
- Crear endpoints.
- Conectar herramientas externas.
- Automatizar acciones.
- Activar agentes autónomos.
- Ejecutar acciones reales.
- Avanzar automáticamente a Fase 11.

---

## Riesgo

Tipo de cambio:

**Cambio técnico documental / corrección de permisos y alcances conceptuales**

Nivel de riesgo inicial:

**Nivel 3 — Alto**

Motivo:

El documento define cómo Robert interpreta permisos, alcances, límites de autorización, duración y revocación.

Nivel de riesgo final esperado:

**Nivel 2 — Medio**

Motivo:

La corrección sigue siendo documental. No crea modelo real nuevo, no crea sistema real de permisos, no crea botones reales, no crea pantallas reales, no programa, no conecta herramientas externas y no ejecuta acciones.

Nivel de autonomía:

**Nivel 0 — Sin autonomía ejecutiva**

---

## Estado final

ROBERT_TECHNICAL_PERMISSIONS_AND_SCOPES_SPEC v0.2 queda como:

**Propuesta corregida pendiente de revisión**

No está aprobado todavía.

Robert continúa en:

**Fase 10 — MVP técnico básico en preparación**

Sin programación autorizada.

Sin código real.

Sin botones reales.

Sin pantallas reales.

Sin sistema real de permisos.

Sin base de datos real.

Sin conexiones externas.

Sin automatizaciones reales.

Sin agentes autónomos activos.

---

# CAMBIO #032 — Aprobación e integración de ROBERT_TECHNICAL_PERMISSIONS_AND_SCOPES_SPEC v0.2

Fecha: 04/07/2026  
Estado: Aprobado e integrado  
Documento afectado: ROBERT_TECHNICAL_PERMISSIONS_AND_SCOPES_SPEC v0.2  
Ubicación: 10_MVP  
Decisión relacionada: DECISIÓN #019 — Aprobación de ROBERT_TECHNICAL_PERMISSIONS_AND_SCOPES_SPEC v0.2  
Cambio relacionado previo: CAMBIO #031 — Corrección de ROBERT_TECHNICAL_PERMISSIONS_AND_SCOPES_SPEC v0.2  
Documento base principal: ROBERT_TECHNICAL_ERROR_AND_BLOCKING_SPEC v0.2  
Documentos relacionados: ROBERT_COMMANDS v0.4, ROBERT_TECHNICAL_USER_ACTIONS_SPEC v0.2, ROBERT_TECHNICAL_DATA_MODEL_SPEC v0.1, ROBERT_TECHNICAL_COMPONENTS_SPEC v0.2, ROBERT_TECHNICAL_SCREEN_STATE_SPEC v0.2, ROBERT_TECHNICAL_INTERACTION_FLOW_SPEC v0.2  
Fase relacionada: Fase 10 — MVP técnico básico en preparación  

---

## Cambio realizado

Se registró la aprobación formal e integración documental de:

**ROBERT_TECHNICAL_PERMISSIONS_AND_SCOPES_SPEC v0.2**

como documento técnico documental aprobado del MVP técnico básico de Robert.

---

## Motivo del cambio

Después de corregir PERMISSIONS_AND_SCOPES_SPEC v0.1 y revisar la propuesta v0.2, el usuario aprobó formalmente el documento.

La versión v0.2 queda integrada porque define permisos, alcances, límites de autorización, duración, expiración, revocación y acciones permitidas dentro del MVP técnico básico.

---

## Correcciones integradas

La versión aprobada integra:

- Relación explícita entre Permiso, Alcance y los 11 modelos de DATA_MODEL_SPEC v0.1.
- Aclaración de que Permiso y Alcance no son modelos nuevos oficiales.
- Definición de Permiso y Alcance como estructuras conceptuales derivadas.
- Aclaración de que no se crea el modelo PermissionScope en esta versión.
- Regla de que cualquier modelo nuevo futuro requiere actualizar DATA_MODEL_SPEC.
- Inclusión de los 10 componentes aprobados en COMPONENTS_SPEC v0.2.
- Definición de dónde se muestra permiso activo, alcance, duración, expiración, riesgo, decisión pendiente y revocación.
- Tabla de correspondencia entre los 13 permisos y las acciones de USER_ACTIONS_SPEC v0.2.
- Inclusión de EVENTO 5 — Bloqueo automático como categoría general de respaldo.
- Nivel 0 únicamente como Informativo.
- Acciones de control fuera de la escala de riesgo.
- Alineación con ROBERT_COMMANDS v0.4.
- Alineación con USER_ACTIONS_SPEC v0.2.
- Alineación con ERROR_AND_BLOCKING_SPEC v0.2.
- Alineación con DATA_MODEL_SPEC v0.1.
- Alineación con SCREEN_STATE_SPEC v0.2.
- Alineación con INTERACTION_FLOW_SPEC v0.2.
- Alineación con COMPONENTS_SPEC v0.2.

---

## Alcance autorizado

Este cambio autoriza únicamente:

- Marcar PERMISSIONS_AND_SCOPES_SPEC v0.2 como aprobado.
- Integrarlo al estado documental actual de Robert.
- Usarlo como base documental para futuras especificaciones técnicas.
- Usarlo para interpretar permisos conceptuales.
- Usarlo para interpretar alcances conceptuales.
- Usarlo para definir límites de autorización.
- Usarlo para definir duración de autorizaciones.
- Usarlo para definir expiración de autorizaciones.
- Usarlo para definir revocación.
- Usarlo para mapear permisos con acciones de usuario.
- Usarlo para conectar permisos con modelos existentes.
- Usarlo para conectar permisos con componentes visuales conceptuales.
- Mantenerlo dentro de Fase 10.

---

## Alcance no autorizado

Este cambio no autoriza:

- Programar la app.
- Crear código real.
- Crear botones reales.
- Crear pantallas reales.
- Crear prototipo funcional.
- Crear sistema real de permisos.
- Crear usuarios reales.
- Crear roles reales.
- Crear base de datos real.
- Crear modelo PermissionScope.
- Modificar DATA_MODEL_SPEC automáticamente.
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

## Riesgo

Tipo de cambio:

**Aprobación técnica documental / integración de permisos y alcances conceptuales**

Nivel de riesgo inicial:

**Nivel 3 — Alto**

Motivo:

El documento define cómo Robert interpreta permisos, alcances, límites de autorización, duración, expiración y revocación.

Nivel de riesgo final:

**Nivel 2 — Medio**

Motivo:

El cambio queda limitado a documentación. No crea sistema real de permisos, no crea modelos nuevos oficiales, no crea botones reales, no crea pantallas reales, no programa, no conecta herramientas externas y no ejecuta acciones.

Nivel de autonomía:

**Nivel 0 — Sin autonomía ejecutiva**

---

## Estado final

ROBERT_TECHNICAL_PERMISSIONS_AND_SCOPES_SPEC v0.2 queda aprobado e integrado documentalmente.

Robert continúa en:

**Fase 10 — MVP técnico básico en preparación**

Sin programación autorizada.

Sin código real.

Sin botones reales.

Sin pantallas reales.

Sin sistema real de permisos.

Sin base de datos real.

Sin conexiones externas.

Sin automatizaciones reales.

Sin agentes autónomos activos.

---

# CAMBIO #033 — Corrección de ROBERT_TECHNICAL_AUDIT_TRAIL_SPEC v0.2

Fecha: 06/07/2026  
Estado: Propuesta corregida — pendiente de revisión  
Documento afectado: ROBERT_TECHNICAL_AUDIT_TRAIL_SPEC  
Versión actualizada: v0.2  
Ubicación: 10_MVP  
Documento base principal: ROBERT_TECHNICAL_PERMISSIONS_AND_SCOPES_SPEC v0.2  
Documentos relacionados: ROBERT_COMMANDS v0.4, ROBERT_TECHNICAL_ERROR_AND_BLOCKING_SPEC v0.2, ROBERT_TECHNICAL_USER_ACTIONS_SPEC v0.2, ROBERT_TECHNICAL_DATA_MODEL_SPEC v0.1, ROBERT_TECHNICAL_COMPONENTS_SPEC v0.2, ROBERT_TECHNICAL_SCREEN_STATE_SPEC v0.2, ROBERT_TECHNICAL_INTERACTION_FLOW_SPEC v0.2  
Fase relacionada: Fase 10 — MVP técnico básico en preparación  

---

## Cambio realizado

Se corrigió el documento:

**ROBERT_TECHNICAL_AUDIT_TRAIL_SPEC**

de v0.1 a:

**v0.2 — Propuesta corregida pendiente de revisión**

---

## Motivo del cambio

Durante la revisión de v0.1 se detectaron dos inconsistencias:

- La relación con ERROR_AND_BLOCKING_SPEC no incluía EVENTO 3 — Aprobación formal requerida.
- La relación con ERROR_AND_BLOCKING_SPEC no incluía EVENTO 10 — Contradicción documental.
- Los 17 tipos de REGISTRO no usaban una estructura uniforme de campos.

---

## Correcciones aplicadas

La versión v0.2 corrige:

- Se agrega EVENTO 3 — Aprobación formal requerida.
- Se agrega EVENTO 10 — Contradicción documental.
- Se conecta REGISTRO 8 — Aprobación con EVENTO 3.
- Se conecta REGISTRO 16 — Contradicción documental con EVENTO 10.
- Se agrega tabla de relación entre registros y eventos.
- Se uniforman los 17 tipos de REGISTRO.
- Cada REGISTRO ahora incluye:
  - Qué registra.
  - Ejemplos.
  - Riesgo típico.
  - Modelo principal.
  - Componente principal.
  - Registro formal requerido.
  - Restricción.
- Se mantiene que Audit Trail no crea el modelo AuditTrailEntry.
- Se mantiene que Audit Trail no crea el componente AuditTrailPanel.
- Se mantiene alineación con DATA_MODEL_SPEC v0.1.
- Se mantiene alineación con COMPONENTS_SPEC v0.2.
- Se mantiene alineación con USER_ACTIONS_SPEC v0.2.
- Se mantiene alineación con PERMISSIONS_AND_SCOPES_SPEC v0.2.
- Se mantiene alineación con ERROR_AND_BLOCKING_SPEC v0.2.

---

## Alcance autorizado

Este cambio autoriza únicamente:

- Corregir el documento técnico.
- Mantenerlo como propuesta pendiente de revisión.
- Usarlo para revisión documental.
- Alinear auditoría con ERROR_AND_BLOCKING_SPEC v0.2.
- Alinear registros con DATA_MODEL_SPEC v0.1.
- Alinear registros con COMPONENTS_SPEC v0.2.
- Alinear registros con USER_ACTIONS_SPEC v0.2.
- Mantenerlo dentro de Fase 10.

---

## Alcance no autorizado

Este cambio no autoriza:

- Aprobar automáticamente AUDIT_TRAIL_SPEC v0.2.
- Crear modelo AuditTrailEntry.
- Crear componente AuditTrailPanel.
- Modificar DATA_MODEL_SPEC automáticamente.
- Modificar COMPONENTS_SPEC automáticamente.
- Programar la app.
- Crear código real.
- Crear logs reales.
- Crear sistema real de auditoría.
- Crear base de datos real.
- Crear botones reales.
- Crear pantallas reales.
- Conectar herramientas externas.
- Automatizar acciones.
- Activar agentes autónomos.
- Ejecutar acciones reales.
- Avanzar automáticamente a Fase 11.

---

## Riesgo

Tipo de cambio:

**Cambio técnico documental / corrección de trazabilidad y auditoría conceptual**

Nivel de riesgo inicial:

**Nivel 3 — Alto**

Motivo:

El documento define cómo Robert debe rastrear acciones, cambios, decisiones, permisos, bloqueos y evidencia documental.

Nivel de riesgo final esperado:

**Nivel 2 — Medio**

Motivo:

La corrección sigue siendo documental. No crea logs reales, no crea sistema real de auditoría, no crea modelos nuevos oficiales, no crea componentes nuevos oficiales, no programa, no conecta herramientas externas y no ejecuta acciones.

Nivel de autonomía:

**Nivel 0 — Sin autonomía ejecutiva**

---

## Estado final

ROBERT_TECHNICAL_AUDIT_TRAIL_SPEC v0.2 queda como:

**Propuesta corregida pendiente de revisión**

No está aprobado todavía.

Robert continúa en:

**Fase 10 — MVP técnico básico en preparación**

Sin programación autorizada.

Sin código real.

Sin botones reales.

Sin pantallas reales.

Sin logs reales.

Sin sistema real de auditoría.

Sin base de datos real.

Sin conexiones externas.

Sin automatizaciones reales.

Sin agentes autónomos activos.

---

# CAMBIO #034 — Aprobación e integración de ROBERT_TECHNICAL_AUDIT_TRAIL_SPEC v0.2

Fecha: 06/07/2026  
Estado: Aprobado e integrado  
Documento afectado: ROBERT_TECHNICAL_AUDIT_TRAIL_SPEC v0.2  
Ubicación: 10_MVP  
Decisión relacionada: DECISIÓN #020 — Aprobación de ROBERT_TECHNICAL_AUDIT_TRAIL_SPEC v0.2  
Cambio relacionado previo: CAMBIO #033 — Corrección de ROBERT_TECHNICAL_AUDIT_TRAIL_SPEC v0.2  
Documento base principal: ROBERT_TECHNICAL_PERMISSIONS_AND_SCOPES_SPEC v0.2  
Documentos relacionados: ROBERT_COMMANDS v0.4, ROBERT_TECHNICAL_ERROR_AND_BLOCKING_SPEC v0.2, ROBERT_TECHNICAL_USER_ACTIONS_SPEC v0.2, ROBERT_TECHNICAL_DATA_MODEL_SPEC v0.1, ROBERT_TECHNICAL_COMPONENTS_SPEC v0.2, ROBERT_TECHNICAL_SCREEN_STATE_SPEC v0.2, ROBERT_TECHNICAL_INTERACTION_FLOW_SPEC v0.2  
Fase relacionada: Fase 10 — MVP técnico básico en preparación  

---

## Cambio realizado

Se registró la aprobación formal e integración documental de:

**ROBERT_TECHNICAL_AUDIT_TRAIL_SPEC v0.2**

como documento técnico documental aprobado del MVP técnico básico de Robert.

---

## Motivo del cambio

Después de corregir AUDIT_TRAIL_SPEC v0.1 y revisar la propuesta v0.2, el usuario aprobó formalmente el documento.

La versión v0.2 queda integrada porque define trazabilidad, historial, evidencia mínima, registro de acciones, decisiones, cambios, riesgos, permisos y bloqueos dentro del MVP técnico básico.

---

## Correcciones integradas

La versión aprobada integra:

- EVENTO 3 — Aprobación formal requerida.
- EVENTO 10 — Contradicción documental.
- Conexión de REGISTRO 8 — Aprobación con EVENTO 3.
- Conexión de REGISTRO 16 — Contradicción documental con EVENTO 10.
- Tabla de relación entre registros y eventos.
- Uniformidad de los 17 tipos de REGISTRO.
- Cada REGISTRO incluye:
  - Qué registra.
  - Ejemplos.
  - Riesgo típico.
  - Modelo principal.
  - Componente principal.
  - Registro formal requerido.
  - Restricción.
- Aclaración de que Audit Trail no crea el modelo AuditTrailEntry.
- Aclaración de que Audit Trail no crea el componente AuditTrailPanel.
- Alineación con DATA_MODEL_SPEC v0.1.
- Alineación con COMPONENTS_SPEC v0.2.
- Alineación con USER_ACTIONS_SPEC v0.2.
- Alineación con PERMISSIONS_AND_SCOPES_SPEC v0.2.
- Alineación con ERROR_AND_BLOCKING_SPEC v0.2.
- Alineación con SCREEN_STATE_SPEC v0.2.
- Alineación con INTERACTION_FLOW_SPEC v0.2.

---

## Alcance autorizado

Este cambio autoriza únicamente:

- Marcar AUDIT_TRAIL_SPEC v0.2 como aprobado.
- Integrarlo al estado documental actual de Robert.
- Usarlo como base documental para futuras especificaciones técnicas.
- Usarlo para definir trazabilidad conceptual.
- Usarlo para definir historial documental.
- Usarlo para definir evidencia mínima.
- Usarlo para definir qué acciones deben registrarse.
- Usarlo para definir qué decisiones deben registrarse.
- Usarlo para definir qué cambios deben registrarse.
- Usarlo para definir qué riesgos deben registrarse.
- Usarlo para definir qué permisos deben registrarse.
- Usarlo para definir qué bloqueos deben registrarse.
- Usarlo para conectar registros con modelos existentes.
- Usarlo para conectar registros con componentes visuales conceptuales.
- Usarlo para conectar registros con eventos de ERROR_AND_BLOCKING_SPEC.
- Mantenerlo dentro de Fase 10.

---

## Alcance no autorizado

Este cambio no autoriza:

- Programar la app.
- Crear código real.
- Crear logs reales.
- Crear sistema real de auditoría.
- Crear tabla real de auditoría.
- Crear base de datos real.
- Crear modelo AuditTrailEntry.
- Crear componente AuditTrailPanel.
- Modificar DATA_MODEL_SPEC automáticamente.
- Modificar COMPONENTS_SPEC automáticamente.
- Crear botones reales.
- Crear pantallas reales.
- Crear prototipo funcional.
- Crear endpoints.
- Conectar Supabase.
- Conectar Firebase.
- Conectar GitHub automáticamente.
- Conectar Gmail.
- Conectar Google Calendar.
- Conectar APIs externas.
- Automatizar registros.
- Activar agentes autónomos.
- Ejecutar acciones reales.
- Avanzar automáticamente a Fase 11.

---

## Riesgo

Tipo de cambio:

**Aprobación técnica documental / integración de trazabilidad y auditoría conceptual**

Nivel de riesgo inicial:

**Nivel 3 — Alto**

Motivo:

El documento define cómo Robert debe rastrear acciones, cambios, decisiones, permisos, bloqueos y evidencia documental.

Nivel de riesgo final:

**Nivel 2 — Medio**

Motivo:

El cambio queda limitado a documentación. No crea logs reales, no crea sistema real de auditoría, no crea base de datos real, no crea modelos nuevos oficiales, no crea componentes nuevos oficiales, no programa, no conecta herramientas externas y no ejecuta acciones.

Nivel de autonomía:

**Nivel 0 — Sin autonomía ejecutiva**

---

## Estado final

ROBERT_TECHNICAL_AUDIT_TRAIL_SPEC v0.2 queda aprobado e integrado documentalmente.

Robert continúa en:

**Fase 10 — MVP técnico básico en preparación**

Sin programación autorizada.

Sin código real.

Sin botones reales.

Sin pantallas reales.

Sin logs reales.

Sin sistema real de auditoría.

Sin base de datos real.

Sin conexiones externas.

Sin automatizaciones reales.

Sin agentes autónomos activos.

---

# CAMBIO #035 — Corrección de ROBERT_TECHNICAL_NOTIFICATION_AND_ALERTS_SPEC v0.2

Fecha: 06/07/2026  
Estado: Propuesta corregida — pendiente de revisión  
Documento afectado: ROBERT_TECHNICAL_NOTIFICATION_AND_ALERTS_SPEC  
Versión actualizada: v0.2  
Ubicación: 10_MVP  
Documento base principal: ROBERT_TECHNICAL_AUDIT_TRAIL_SPEC v0.2  
Documentos relacionados: ROBERT_COMMANDS v0.4, ROBERT_TECHNICAL_PERMISSIONS_AND_SCOPES_SPEC v0.2, ROBERT_TECHNICAL_ERROR_AND_BLOCKING_SPEC v0.2, ROBERT_TECHNICAL_USER_ACTIONS_SPEC v0.2, ROBERT_TECHNICAL_DATA_MODEL_SPEC v0.1, ROBERT_TECHNICAL_COMPONENTS_SPEC v0.2, ROBERT_TECHNICAL_SCREEN_STATE_SPEC v0.2, ROBERT_TECHNICAL_INTERACTION_FLOW_SPEC v0.2  
Fase relacionada: Fase 10 — MVP técnico básico en preparación  

---

## Cambio realizado

Se corrigió el documento:

**ROBERT_TECHNICAL_NOTIFICATION_AND_ALERTS_SPEC**

de v0.1 a:

**v0.2 — Propuesta corregida pendiente de revisión**

---

## Motivo del cambio

Durante la revisión de v0.1 se detectaron huecos reales en la relación con ERROR_AND_BLOCKING_SPEC:

- TIPO 12 — Alerta de capacidad futura no disponible no conectaba con EVENTO 8 — Acción futura no disponible.
- EVENTO 4 — Pausa obligatoria no estaba referenciado.
- EVENTO 6 — Bloqueo manual solicitado no estaba referenciado.
- ACCIÓN 13 — Pausar avance no estaba conectada con EVENTO 4.
- ACCIÓN 14 — Solicitar bloqueo manual no estaba conectada con EVENTO 6.
- Eventos importantes como EVENTO 7, EVENTO 9, EVENTO 11, EVENTO 13 y EVENTO 14 estaban cubiertos solo de forma implícita.

---

## Correcciones aplicadas

La versión v0.2 corrige:

- Se agrega EVENTO 4 — Pausa obligatoria.
- Se agrega EVENTO 6 — Bloqueo manual solicitado.
- Se agrega EVENTO 7 — Acción prohibida.
- Se agrega EVENTO 8 — Acción futura no disponible.
- Se agrega EVENTO 9 — Falta de información.
- Se agrega EVENTO 11 — Riesgo crítico.
- Se agrega EVENTO 13 — Sandbox requerido.
- Se agrega EVENTO 14 — Sandbox excedido.
- Se conecta ACCIÓN 13 — Pausar avance con EVENTO 4.
- Se conecta ACCIÓN 14 — Solicitar bloqueo manual con EVENTO 6.
- Se conecta TIPO 12 — Alerta de capacidad futura no disponible con EVENTO 8 como evento general.
- Se aclara que TIPO 12 solo usa EVENTOS 15 al 20 cuando la capacidad futura intenta activarse como acción real.
- Se conecta TIPO 4 — Alerta de comando ambiguo o falta de información con EVENTO 9.
- Se conecta TIPO 5 — Advertencia de riesgo con EVENTO 11.
- Se conecta TIPO 9 — Mensaje de bloqueo con EVENTO 6 y EVENTO 7.
- Se conecta TIPO 16 — Aviso de sandbox manual con EVENTO 13 y EVENTO 14.
- Se actualiza la lista de eventos relevantes.
- Se actualiza la tabla de relación entre tipos y eventos.
- Se actualiza la correspondencia con USER_ACTIONS_SPEC v0.2.
- Se mantiene que las acciones de control están fuera de la escala de riesgo.
- Se mantiene alineación con ERROR_AND_BLOCKING_SPEC v0.2.
- Se mantiene alineación con AUDIT_TRAIL_SPEC v0.2.
- Se mantiene alineación con PERMISSIONS_AND_SCOPES_SPEC v0.2.

---

## Alcance autorizado

Este cambio autoriza únicamente:

- Corregir el documento técnico.
- Mantenerlo como propuesta pendiente de revisión.
- Usarlo para revisión documental.
- Alinear notificaciones y alertas con ERROR_AND_BLOCKING_SPEC v0.2.
- Alinear notificaciones con USER_ACTIONS_SPEC v0.2.
- Alinear notificaciones con AUDIT_TRAIL_SPEC v0.2.
- Alinear notificaciones con PERMISSIONS_AND_SCOPES_SPEC v0.2.
- Mantenerlo dentro de Fase 10.

---

## Alcance no autorizado

Este cambio no autoriza:

- Aprobar automáticamente NOTIFICATION_AND_ALERTS_SPEC v0.2.
- Crear modelo NotificationRecord.
- Crear modelo AlertRecord.
- Crear componente NotificationCenter.
- Crear componente AlertPanel.
- Modificar DATA_MODEL_SPEC automáticamente.
- Modificar COMPONENTS_SPEC automáticamente.
- Programar la app.
- Crear código real.
- Crear notificaciones reales.
- Crear emails.
- Crear push notifications.
- Crear sistema real de alertas.
- Crear base de datos real.
- Crear botones reales.
- Crear pantallas reales.
- Conectar herramientas externas.
- Automatizar acciones.
- Activar agentes autónomos.
- Ejecutar acciones reales.
- Avanzar automáticamente a Fase 11.

---

## Riesgo

Tipo de cambio:

**Cambio técnico documental / corrección de notificaciones y alertas conceptuales**

Nivel de riesgo inicial:

**Nivel 3 — Alto**

Motivo:

El documento define cómo Robert comunica riesgos, bloqueos, permisos, confirmaciones, advertencias y estados al usuario.

Nivel de riesgo final esperado:

**Nivel 2 — Medio**

Motivo:

La corrección sigue siendo documental. No crea notificaciones reales, no crea sistema real de alertas, no crea modelos nuevos oficiales, no crea componentes nuevos oficiales, no programa, no conecta herramientas externas y no ejecuta acciones.

Nivel de autonomía:

**Nivel 0 — Sin autonomía ejecutiva**

---

## Estado final

ROBERT_TECHNICAL_NOTIFICATION_AND_ALERTS_SPEC v0.2 queda como:

**Propuesta corregida pendiente de revisión**

No está aprobado todavía.

Robert continúa en:

**Fase 10 — MVP técnico básico en preparación**

Sin programación autorizada.

Sin código real.

Sin botones reales.

Sin pantallas reales.

Sin notificaciones reales.

Sin emails.

Sin push notifications.

Sin sistema real de alertas.

Sin base de datos real.

Sin conexiones externas.

Sin automatizaciones reales.

Sin agentes autónomos activos.

---

# CAMBIO #036 — Aprobación e integración de ROBERT_TECHNICAL_NOTIFICATION_AND_ALERTS_SPEC v0.2

Fecha: 06/07/2026  
Estado: Aprobado e integrado  
Documento afectado: ROBERT_TECHNICAL_NOTIFICATION_AND_ALERTS_SPEC v0.2  
Ubicación: 10_MVP  
Decisión relacionada: DECISIÓN #021 — Aprobación de ROBERT_TECHNICAL_NOTIFICATION_AND_ALERTS_SPEC v0.2  
Cambio relacionado previo: CAMBIO #035 — Corrección de ROBERT_TECHNICAL_NOTIFICATION_AND_ALERTS_SPEC v0.2  
Documento base principal: ROBERT_TECHNICAL_AUDIT_TRAIL_SPEC v0.2  
Documentos relacionados: ROBERT_COMMANDS v0.4, ROBERT_TECHNICAL_PERMISSIONS_AND_SCOPES_SPEC v0.2, ROBERT_TECHNICAL_ERROR_AND_BLOCKING_SPEC v0.2, ROBERT_TECHNICAL_USER_ACTIONS_SPEC v0.2, ROBERT_TECHNICAL_DATA_MODEL_SPEC v0.1, ROBERT_TECHNICAL_COMPONENTS_SPEC v0.2, ROBERT_TECHNICAL_SCREEN_STATE_SPEC v0.2, ROBERT_TECHNICAL_INTERACTION_FLOW_SPEC v0.2  
Fase relacionada: Fase 10 — MVP técnico básico en preparación  

---

## Cambio realizado

Se registró la aprobación formal e integración documental de:

**ROBERT_TECHNICAL_NOTIFICATION_AND_ALERTS_SPEC v0.2**

como documento técnico documental aprobado del MVP técnico básico de Robert.

---

## Motivo del cambio

Después de corregir NOTIFICATION_AND_ALERTS_SPEC v0.1 y revisar la propuesta v0.2, el usuario aprobó formalmente el documento.

La versión v0.2 queda integrada porque define avisos, alertas, advertencias, confirmaciones, mensajes de bloqueo y notificaciones internas conceptuales dentro del MVP técnico básico.

---

## Correcciones integradas

La versión aprobada integra:

- EVENTO 4 — Pausa obligatoria.
- EVENTO 6 — Bloqueo manual solicitado.
- EVENTO 7 — Acción prohibida.
- EVENTO 8 — Acción futura no disponible.
- EVENTO 9 — Falta de información.
- EVENTO 11 — Riesgo crítico.
- EVENTO 13 — Sandbox requerido.
- EVENTO 14 — Sandbox excedido.
- Conexión de ACCIÓN 13 — Pausar avance con EVENTO 4.
- Conexión de ACCIÓN 14 — Solicitar bloqueo manual con EVENTO 6.
- Conexión de TIPO 12 — Alerta de capacidad futura no disponible con EVENTO 8.
- Aclaración de que TIPO 12 solo usa EVENTOS 15 al 20 cuando la capacidad futura intenta activarse como acción real.
- Conexión de TIPO 4 con EVENTO 9.
- Conexión de TIPO 5 con EVENTO 11.
- Conexión de TIPO 9 con EVENTO 6 y EVENTO 7.
- Conexión de TIPO 16 con EVENTO 13 y EVENTO 14.
- Nivel 0 únicamente como Informativo.
- Acciones de control fuera de la escala de riesgo.
- Alineación con ERROR_AND_BLOCKING_SPEC v0.2.
- Alineación con AUDIT_TRAIL_SPEC v0.2.
- Alineación con PERMISSIONS_AND_SCOPES_SPEC v0.2.
- Alineación con USER_ACTIONS_SPEC v0.2.
- Alineación con DATA_MODEL_SPEC v0.1.
- Alineación con COMPONENTS_SPEC v0.2.
- Alineación con SCREEN_STATE_SPEC v0.2.
- Alineación con INTERACTION_FLOW_SPEC v0.2.

---

## Alcance autorizado

Este cambio autoriza únicamente:

- Marcar NOTIFICATION_AND_ALERTS_SPEC v0.2 como aprobado.
- Integrarlo al estado documental actual de Robert.
- Usarlo como base documental para futuras especificaciones técnicas.
- Usarlo para definir notificaciones conceptuales.
- Usarlo para definir avisos conceptuales.
- Usarlo para definir alertas conceptuales.
- Usarlo para definir advertencias conceptuales.
- Usarlo para definir confirmaciones conceptuales.
- Usarlo para definir mensajes de bloqueo conceptuales.
- Usarlo para conectar avisos con eventos de ERROR_AND_BLOCKING_SPEC.
- Usarlo para conectar avisos con registros de AUDIT_TRAIL_SPEC.
- Usarlo para conectar avisos con permisos y alcances.
- Mantenerlo dentro de Fase 10.

---

## Alcance no autorizado

Este cambio no autoriza:

- Programar la app.
- Crear código real.
- Crear notificaciones reales.
- Crear emails.
- Crear push notifications.
- Crear sistema real de alertas.
- Crear base de datos real.
- Crear modelo NotificationRecord.
- Crear modelo AlertRecord.
- Crear componente NotificationCenter.
- Crear componente AlertPanel.
- Modificar DATA_MODEL_SPEC automáticamente.
- Modificar COMPONENTS_SPEC automáticamente.
- Crear botones reales.
- Crear pantallas reales.
- Crear prototipo funcional.
- Crear endpoints.
- Conectar Supabase.
- Conectar Firebase.
- Conectar GitHub automáticamente.
- Conectar Gmail.
- Conectar Google Calendar.
- Conectar APIs externas.
- Automatizar avisos.
- Activar agentes autónomos.
- Ejecutar acciones reales.
- Avanzar automáticamente a Fase 11.

---

## Riesgo

Tipo de cambio:

**Aprobación técnica documental / integración de notificaciones y alertas conceptuales**

Nivel de riesgo inicial:

**Nivel 3 — Alto**

Motivo:

El documento define cómo Robert comunica riesgos, bloqueos, permisos, confirmaciones, advertencias y estados al usuario.

Nivel de riesgo final:

**Nivel 2 — Medio**

Motivo:

El cambio queda limitado a documentación. No crea notificaciones reales, no crea sistema real de alertas, no crea modelos nuevos oficiales, no crea componentes nuevos oficiales, no programa, no conecta herramientas externas y no ejecuta acciones.

Nivel de autonomía:

**Nivel 0 — Sin autonomía ejecutiva**

---

## Estado final

ROBERT_TECHNICAL_NOTIFICATION_AND_ALERTS_SPEC v0.2 queda aprobado e integrado documentalmente.

Robert continúa en:

**Fase 10 — MVP técnico básico en preparación**

Sin programación autorizada.

Sin código real.

Sin botones reales.

Sin pantallas reales.

Sin notificaciones reales.

Sin emails.

Sin push notifications.

Sin sistema real de alertas.

Sin base de datos real.

Sin conexiones externas.

Sin automatizaciones reales.

Sin agentes autónomos activos.

---

# CAMBIO #037 — Corrección de ROBERT_TECHNICAL_SESSION_AND_CONTEXT_SPEC v0.2

Fecha: 06/07/2026  
Estado: Propuesta corregida — pendiente de revisión  
Documento afectado: ROBERT_TECHNICAL_SESSION_AND_CONTEXT_SPEC  
Versión actualizada: v0.2  
Ubicación: 10_MVP  
Documento base principal: ROBERT_TECHNICAL_NOTIFICATION_AND_ALERTS_SPEC v0.2  
Documentos relacionados: ROBERT_COMMANDS v0.4, ROBERT_TECHNICAL_AUDIT_TRAIL_SPEC v0.2, ROBERT_TECHNICAL_PERMISSIONS_AND_SCOPES_SPEC v0.2, ROBERT_TECHNICAL_ERROR_AND_BLOCKING_SPEC v0.2, ROBERT_TECHNICAL_USER_ACTIONS_SPEC v0.2, ROBERT_TECHNICAL_DATA_MODEL_SPEC v0.1, ROBERT_TECHNICAL_COMPONENTS_SPEC v0.2, ROBERT_TECHNICAL_SCREEN_STATE_SPEC v0.2, ROBERT_TECHNICAL_INTERACTION_FLOW_SPEC v0.2  
Fase relacionada: Fase 10 — MVP técnico básico en preparación  

---

## Cambio realizado

Se corrigió el documento:

**ROBERT_TECHNICAL_SESSION_AND_CONTEXT_SPEC**

de v0.1 a:

**v0.2 — Propuesta corregida pendiente de revisión**

---

## Motivo del cambio

Durante la revisión de v0.1 se detectaron huecos en la relación con AUDIT_TRAIL_SPEC v0.2:

- REGISTRO 2 — Comando no estaba referenciado en ningún tipo de sesión.
- REGISTRO 11 — Riesgo no estaba referenciado en ningún tipo de sesión.
- TIPO 10 — Sesión de bloqueo mezclaba riesgo numérico con acción de control fuera de escala.
- Existía una posible asimetría con NOTIFICATION_AND_ALERTS_SPEC v0.2 sobre respaldo manual.
- No estaba aclarado si debía existir un TIPO 18 — Sesión de respaldo manual.

---

## Correcciones aplicadas

La versión v0.2 corrige:

- Se agrega REGISTRO 2 — Comando a TIPO 1 — Sesión informativa.
- Se agrega REGISTRO 2 — Comando a TIPO 3 — Sesión de corrección.
- Se agrega REGISTRO 11 — Riesgo a TIPO 10 — Sesión de bloqueo cuando aplica.
- Se agrega REGISTRO 11 — Riesgo a TIPO 13 — Sesión de revisión crítica.
- Se corrige TIPO 10 separando Riesgo típico de Nota de control.
- Se aclara que las acciones de control quedan fuera de la escala de riesgo.
- Se aclara que no se crea TIPO 18 — Sesión de respaldo manual.
- Se confirma que el respaldo manual se absorbe dentro de TIPO 15 — Sesión de cierre de bloque.
- Se aclara que una notificación específica no siempre requiere un tipo de sesión independiente.
- Se refuerza la relación con AUDIT_TRAIL_SPEC v0.2.
- Se actualizan los criterios de aceptación.
- Se cambia la aprobación futura esperada a v0.2.

---

## Alcance autorizado

Este cambio autoriza únicamente:

- Corregir el documento técnico.
- Mantenerlo como propuesta pendiente de revisión.
- Usarlo para revisión documental.
- Alinear sesión y contexto con AUDIT_TRAIL_SPEC v0.2.
- Alinear sesión y contexto con NOTIFICATION_AND_ALERTS_SPEC v0.2.
- Mantenerlo dentro de Fase 10.

---

## Alcance no autorizado

Este cambio no autoriza:

- Aprobar automáticamente SESSION_AND_CONTEXT_SPEC v0.2.
- Crear modelo SessionRecord.
- Crear modelo ContextSnapshot.
- Crear modelo ConversationState.
- Crear componente SessionPanel.
- Crear componente ContextTimeline.
- Crear TIPO 18 — Sesión de respaldo manual.
- Programar la app.
- Crear código real.
- Crear sistema real de sesiones.
- Crear memoria automática real.
- Crear base de datos real.
- Crear botones reales.
- Crear pantallas reales.
- Conectar herramientas externas.
- Automatizar recuperación de contexto.
- Activar agentes autónomos.
- Ejecutar acciones reales.
- Avanzar automáticamente a Fase 11.

---

## Riesgo

Tipo de cambio:

**Cambio técnico documental / corrección de sesión, contexto y continuidad conceptual**

Nivel de riesgo inicial:

**Nivel 3 — Alto**

Motivo:

El documento define cómo Robert mantiene continuidad, interpreta confirmaciones, reanuda trabajo y evita perder el hilo.

Nivel de riesgo final esperado:

**Nivel 2 — Medio**

Motivo:

La corrección sigue siendo documental. No crea memoria real automática, no crea sistema real de sesiones, no crea base de datos real, no crea modelos nuevos oficiales, no crea componentes nuevos oficiales, no programa, no conecta herramientas externas y no ejecuta acciones.

Nivel de autonomía:

**Nivel 0 — Sin autonomía ejecutiva**

---

## Estado final

ROBERT_TECHNICAL_SESSION_AND_CONTEXT_SPEC v0.2 queda como:

**Propuesta corregida pendiente de revisión**

No está aprobado todavía.

Robert continúa en:

**Fase 10 — MVP técnico básico en preparación**

Sin programación autorizada.

Sin código real.

Sin botones reales.

Sin pantallas reales.

Sin memoria real automática.

Sin sistema real de sesiones.

Sin base de datos real.

Sin conexiones externas.

Sin automatizaciones reales.

Sin agentes autónomos activos.

---

# CAMBIO #038 — Aprobación e integración de ROBERT_TECHNICAL_SESSION_AND_CONTEXT_SPEC v0.2

Fecha: 06/07/2026  
Estado: Aprobado e integrado  
Documento afectado: ROBERT_TECHNICAL_SESSION_AND_CONTEXT_SPEC v0.2  
Ubicación: 10_MVP  
Decisión relacionada: DECISIÓN #022 — Aprobación de ROBERT_TECHNICAL_SESSION_AND_CONTEXT_SPEC v0.2  
Cambio relacionado previo: CAMBIO #037 — Corrección de ROBERT_TECHNICAL_SESSION_AND_CONTEXT_SPEC v0.2  
Documento base principal: ROBERT_TECHNICAL_NOTIFICATION_AND_ALERTS_SPEC v0.2  
Documentos relacionados: ROBERT_COMMANDS v0.4, ROBERT_TECHNICAL_AUDIT_TRAIL_SPEC v0.2, ROBERT_TECHNICAL_PERMISSIONS_AND_SCOPES_SPEC v0.2, ROBERT_TECHNICAL_ERROR_AND_BLOCKING_SPEC v0.2, ROBERT_TECHNICAL_USER_ACTIONS_SPEC v0.2, ROBERT_TECHNICAL_DATA_MODEL_SPEC v0.1, ROBERT_TECHNICAL_COMPONENTS_SPEC v0.2, ROBERT_TECHNICAL_SCREEN_STATE_SPEC v0.2, ROBERT_TECHNICAL_INTERACTION_FLOW_SPEC v0.2  
Fase relacionada: Fase 10 — MVP técnico básico en preparación  

---

## Cambio realizado

Se registró la aprobación formal e integración documental de:

**ROBERT_TECHNICAL_SESSION_AND_CONTEXT_SPEC v0.2**

como documento técnico documental aprobado del MVP técnico básico de Robert.

---

## Motivo del cambio

Después de corregir SESSION_AND_CONTEXT_SPEC v0.1 y revisar la propuesta v0.2, el usuario aprobó formalmente el documento.

La versión v0.2 queda integrada porque define sesión, contexto activo, continuidad, pausa, reanudación, interpretación de confirmaciones cortas, recuperación del hilo y cierre de bloques.

---

## Correcciones integradas

La versión aprobada integra:

- REGISTRO 2 — Comando en TIPO 1 — Sesión informativa.
- REGISTRO 2 — Comando en TIPO 3 — Sesión de corrección.
- REGISTRO 11 — Riesgo en TIPO 10 — Sesión de bloqueo cuando aplica.
- REGISTRO 11 — Riesgo en TIPO 13 — Sesión de revisión crítica.
- Separación de Riesgo típico y Nota de control en TIPO 10.
- Aclaración de que las acciones de control quedan fuera de la escala de riesgo.
- Aclaración de que Nivel 0 es únicamente Informativo.
- Aclaración de que no se crea TIPO 18 — Sesión de respaldo manual.
- Confirmación de que el respaldo manual se absorbe dentro de TIPO 15 — Sesión de cierre de bloque.
- Aclaración de que una notificación específica no siempre requiere un tipo de sesión independiente.
- Refuerzo de relación con AUDIT_TRAIL_SPEC v0.2.
- Alineación con NOTIFICATION_AND_ALERTS_SPEC v0.2.
- Alineación con PERMISSIONS_AND_SCOPES_SPEC v0.2.
- Alineación con ERROR_AND_BLOCKING_SPEC v0.2.
- Alineación con USER_ACTIONS_SPEC v0.2.
- Alineación con DATA_MODEL_SPEC v0.1.
- Alineación con COMPONENTS_SPEC v0.2.
- Alineación con SCREEN_STATE_SPEC v0.2.
- Alineación con INTERACTION_FLOW_SPEC v0.2.

---

## Alcance autorizado

Este cambio autoriza únicamente:

- Marcar SESSION_AND_CONTEXT_SPEC v0.2 como aprobado.
- Integrarlo al estado documental actual de Robert.
- Usarlo como base documental para futuras especificaciones técnicas.
- Usarlo para definir sesión conceptual.
- Usarlo para definir contexto activo conceptual.
- Usarlo para definir continuidad documental.
- Usarlo para definir pausa conceptual.
- Usarlo para definir reanudación conceptual.
- Usarlo para definir recuperación del hilo.
- Usarlo para interpretar confirmaciones cortas como “ya”.
- Usarlo para definir bloque abierto y bloque cerrado.
- Usarlo para conectar sesión con auditoría, permisos, acciones, eventos, notificaciones y componentes conceptuales.
- Mantenerlo dentro de Fase 10.

---

## Alcance no autorizado

Este cambio no autoriza:

- Programar la app.
- Crear código real.
- Crear sistema real de sesiones.
- Crear memoria automática real.
- Crear base de datos real.
- Crear modelo SessionRecord.
- Crear modelo ContextSnapshot.
- Crear modelo ConversationState.
- Crear componente SessionPanel.
- Crear componente ContextTimeline.
- Crear TIPO 18 — Sesión de respaldo manual.
- Crear botones reales.
- Crear pantallas reales.
- Crear prototipo funcional.
- Crear endpoints.
- Conectar Supabase.
- Conectar Firebase.
- Conectar GitHub automáticamente.
- Conectar Obsidian automáticamente.
- Conectar Gmail.
- Conectar Google Calendar.
- Conectar APIs externas.
- Automatizar recuperación de contexto.
- Activar agentes autónomos.
- Ejecutar acciones reales.
- Avanzar automáticamente a Fase 11.

---

## Riesgo

Tipo de cambio:

**Aprobación técnica documental / integración de sesión, contexto y continuidad conceptual**

Nivel de riesgo inicial:

**Nivel 3 — Alto**

Motivo:

El documento define cómo Robert mantiene continuidad, interpreta confirmaciones, reanuda trabajo y evita perder el hilo.

Nivel de riesgo final:

**Nivel 2 — Medio**

Motivo:

El cambio queda limitado a documentación. No crea memoria real automática, no crea sistema real de sesiones, no crea base de datos real, no crea modelos nuevos oficiales, no crea componentes nuevos oficiales, no programa, no conecta herramientas externas y no ejecuta acciones.

Nivel de autonomía:

**Nivel 0 — Sin autonomía ejecutiva**

---

## Estado final

ROBERT_TECHNICAL_SESSION_AND_CONTEXT_SPEC v0.2 queda aprobado e integrado documentalmente.

Robert continúa en:

**Fase 10 — MVP técnico básico en preparación**

Sin programación autorizada.

Sin código real.

Sin botones reales.

Sin pantallas reales.

Sin memoria real automática.

Sin sistema real de sesiones.

Sin base de datos real.

Sin conexiones externas.

Sin automatizaciones reales.

Sin agentes autónomos activos.

---

# CAMBIO #039 — Corrección de ROBERT_TECHNICAL_DOCUMENT_LIFECYCLE_SPEC v0.2

Fecha: 06/07/2026  
Estado: Propuesta corregida — pendiente de revisión  
Documento afectado: ROBERT_TECHNICAL_DOCUMENT_LIFECYCLE_SPEC  
Versión actualizada: v0.2  
Ubicación: 10_MVP  
Documento base principal: ROBERT_TECHNICAL_SESSION_AND_CONTEXT_SPEC v0.2  
Documentos relacionados: ROBERT_COMMANDS v0.4, ROBERT_TECHNICAL_NOTIFICATION_AND_ALERTS_SPEC v0.2, ROBERT_TECHNICAL_AUDIT_TRAIL_SPEC v0.2, ROBERT_TECHNICAL_PERMISSIONS_AND_SCOPES_SPEC v0.2, ROBERT_TECHNICAL_ERROR_AND_BLOCKING_SPEC v0.2, ROBERT_TECHNICAL_USER_ACTIONS_SPEC v0.2, ROBERT_TECHNICAL_DATA_MODEL_SPEC v0.1, ROBERT_TECHNICAL_COMPONENTS_SPEC v0.2, ROBERT_TECHNICAL_SCREEN_STATE_SPEC v0.2, ROBERT_TECHNICAL_INTERACTION_FLOW_SPEC v0.2  
Fase relacionada: Fase 10 — MVP técnico básico en preparación  

---

## Cambio realizado

Se corrigió el documento:

**ROBERT_TECHNICAL_DOCUMENT_LIFECYCLE_SPEC**

de v0.1 a:

**v0.2 — Propuesta corregida pendiente de revisión**

---

## Motivo del cambio

Durante la revisión de v0.1 se detectaron huecos en el ciclo de vida documental:

- Faltaba una estructura uniforme para los 12 estados documentales.
- Los estados no incluían el campo Riesgo típico.
- RiskRecord y RiskBadge estaban listados como relevantes, pero no se reflejaban dentro de cada estado.
- La tabla de transiciones permitidas permitía llegar a Bloqueado desde cualquier estado, pero no definía salidas desde Bloqueado.
- Faltaba la transición directa Depreciado → Archivado.
- La salida Bloqueado → Estado anterior podía quedar ambigua sin una aclaración formal.

---

## Correcciones aplicadas

La versión v0.2 corrige:

- Se agrega la sección ESTRUCTURA UNIFORME DE LOS 12 ESTADOS.
- Se agrega Riesgo típico a los 12 estados documentales.
- Se agrega Transición siguiente permitida a los 12 estados documentales.
- Se agregan salidas desde Bloqueado.
- Se agrega Bloqueado → En revisión.
- Se agrega Bloqueado → Propuesta corregida.
- Se agrega Bloqueado → Depreciado.
- Se agrega Bloqueado → Reemplazado.
- Se agrega Bloqueado → Archivado.
- Se agrega Bloqueado → Estado anterior, solo si existe trazabilidad clara.
- Se aclara que “Estado anterior” significa el estado documental inmediatamente previo a entrar en Bloqueado.
- Se aclara que si no hay trazabilidad clara, Robert debe pasar a Bloqueado → En revisión o pedir confirmación explícita.
- Se agrega Depreciado → Archivado.
- Se aclara que Bloqueado no es estado final obligatorio.
- Se actualizan los criterios de aceptación.
- Se cambia la aprobación futura esperada a v0.2.

---

## Alcance autorizado

Este cambio autoriza únicamente:

- Corregir el documento técnico.
- Mantenerlo como propuesta pendiente de revisión.
- Usarlo para revisión documental.
- Alinear el ciclo documental con SESSION_AND_CONTEXT_SPEC v0.2.
- Alinear el ciclo documental con AUDIT_TRAIL_SPEC v0.2.
- Alinear el ciclo documental con ERROR_AND_BLOCKING_SPEC v0.2.
- Alinear el ciclo documental con NOTIFICATION_AND_ALERTS_SPEC v0.2.
- Mantenerlo dentro de Fase 10.

---

## Alcance no autorizado

Este cambio no autoriza:

- Aprobar automáticamente DOCUMENT_LIFECYCLE_SPEC v0.2.
- Crear modelo DocumentLifecycleRecord.
- Crear modelo VersionRecord.
- Crear modelo DocumentTransitionRecord.
- Crear modelo DeprecationRecord.
- Crear modelo ReplacementRecord.
- Crear componente LifecyclePanel.
- Crear componente VersionTimeline.
- Crear componente DocumentLifecycleMap.
- Crear sistema real de gestión documental.
- Crear base de datos real.
- Crear control automático de versiones.
- Programar la app.
- Crear código real.
- Crear botones reales.
- Crear pantallas reales.
- Conectar GitHub automáticamente.
- Conectar Obsidian automáticamente.
- Sincronizar documentos automáticamente.
- Automatizar commits.
- Automatizar aprobaciones.
- Automatizar HOME.
- Automatizar README.
- Activar agentes autónomos.
- Ejecutar acciones reales.
- Avanzar automáticamente a Fase 11.

---

## Riesgo

Tipo de cambio:

**Cambio técnico documental / corrección del ciclo de vida documental conceptual**

Nivel de riesgo inicial:

**Nivel 3 — Alto**

Motivo:

El documento define cómo los documentos de Robert nacen, cambian, se corrigen, se aprueban, se integran, se actualizan, se bloquean, se reemplazan y se archivan.

Nivel de riesgo final esperado:

**Nivel 2 — Medio**

Motivo:

La corrección sigue siendo documental. No crea sistema real de gestión documental, no crea base de datos real, no crea control automático de versiones, no crea modelos nuevos oficiales, no crea componentes nuevos oficiales, no programa, no conecta herramientas externas y no ejecuta acciones.

Nivel de autonomía:

**Nivel 0 — Sin autonomía ejecutiva**

---

# CAMBIO #040 — Aprobación e integración de ROBERT_TECHNICAL_DOCUMENT_LIFECYCLE_SPEC v0.2

Fecha: 06/07/2026  
Estado: Aprobado e integrado  
Documento afectado: ROBERT_TECHNICAL_DOCUMENT_LIFECYCLE_SPEC v0.2  
Ubicación: 10_MVP  
Decisión relacionada: DECISIÓN #023 — Aprobación de ROBERT_TECHNICAL_DOCUMENT_LIFECYCLE_SPEC v0.2  
Cambio relacionado previo: CAMBIO #039 — Corrección de ROBERT_TECHNICAL_DOCUMENT_LIFECYCLE_SPEC v0.2  
Documento base principal: ROBERT_TECHNICAL_SESSION_AND_CONTEXT_SPEC v0.2  
Documentos relacionados: ROBERT_COMMANDS v0.4, ROBERT_TECHNICAL_NOTIFICATION_AND_ALERTS_SPEC v0.2, ROBERT_TECHNICAL_AUDIT_TRAIL_SPEC v0.2, ROBERT_TECHNICAL_PERMISSIONS_AND_SCOPES_SPEC v0.2, ROBERT_TECHNICAL_ERROR_AND_BLOCKING_SPEC v0.2, ROBERT_TECHNICAL_USER_ACTIONS_SPEC v0.2, ROBERT_TECHNICAL_DATA_MODEL_SPEC v0.1, ROBERT_TECHNICAL_COMPONENTS_SPEC v0.2, ROBERT_TECHNICAL_SCREEN_STATE_SPEC v0.2, ROBERT_TECHNICAL_INTERACTION_FLOW_SPEC v0.2  
Fase relacionada: Fase 10 — MVP técnico básico en preparación  

---

## Cambio realizado

Se registró la aprobación formal e integración documental de:

**ROBERT_TECHNICAL_DOCUMENT_LIFECYCLE_SPEC v0.2**

como documento técnico documental aprobado del MVP técnico básico de Robert.

---

## Motivo del cambio

Después de corregir DOCUMENT_LIFECYCLE_SPEC v0.1 y revisar la propuesta v0.2, el usuario aprobó formalmente el documento.

La versión v0.2 queda integrada porque define el ciclo de vida documental de Robert: idea, borrador, propuesta, propuesta corregida, revisión, aprobación, integración, actualización, depreciación, reemplazo, bloqueo y archivo.

---

## Correcciones integradas

La versión aprobada integra:

- Estructura uniforme de los 12 estados documentales.
- Riesgo típico en los 12 estados documentales.
- Transición siguiente permitida en los 12 estados documentales.
- Salidas desde Bloqueado.
- Bloqueado → En revisión.
- Bloqueado → Propuesta corregida.
- Bloqueado → Depreciado.
- Bloqueado → Reemplazado.
- Bloqueado → Archivado.
- Bloqueado → Estado anterior, solo si existe trazabilidad clara.
- Aclaración de que “Estado anterior” significa el estado documental inmediatamente previo a entrar en Bloqueado.
- Regla de que si no hay trazabilidad clara, Robert debe pasar a Bloqueado → En revisión o pedir confirmación explícita.
- Transición Depreciado → Archivado.
- Aclaración de que Bloqueado no es estado final obligatorio.
- Alineación con SESSION_AND_CONTEXT_SPEC v0.2.
- Alineación con NOTIFICATION_AND_ALERTS_SPEC v0.2.
- Alineación con AUDIT_TRAIL_SPEC v0.2.
- Alineación con PERMISSIONS_AND_SCOPES_SPEC v0.2.
- Alineación con ERROR_AND_BLOCKING_SPEC v0.2.
- Alineación con USER_ACTIONS_SPEC v0.2.
- Alineación con DATA_MODEL_SPEC v0.1.
- Alineación con COMPONENTS_SPEC v0.2.
- Alineación con SCREEN_STATE_SPEC v0.2.
- Alineación con INTERACTION_FLOW_SPEC v0.2.

---

## Alcance autorizado

Este cambio autoriza únicamente:

- Marcar DOCUMENT_LIFECYCLE_SPEC v0.2 como aprobado.
- Integrarlo al estado documental actual de Robert.
- Usarlo como base documental para futuras especificaciones técnicas.
- Usarlo para definir el ciclo de vida documental conceptual.
- Usarlo para definir estados documentales.
- Usarlo para definir transiciones documentales.
- Usarlo para definir bloqueos documentales.
- Usarlo para definir salidas desde Bloqueado.
- Usarlo para definir depreciación, reemplazo y archivo documental.
- Usarlo para conectar ciclo documental con sesión, auditoría, permisos, acciones, eventos, notificaciones y componentes conceptuales.
- Mantenerlo dentro de Fase 10.

---

## Alcance no autorizado

Este cambio no autoriza:

- Programar la app.
- Crear código real.
- Crear sistema real de gestión documental.
- Crear base de datos real.
- Crear control automático de versiones.
- Crear modelo DocumentLifecycleRecord.
- Crear modelo VersionRecord.
- Crear modelo DocumentTransitionRecord.
- Crear modelo DeprecationRecord.
- Crear modelo ReplacementRecord.
- Crear componente LifecyclePanel.
- Crear componente VersionTimeline.
- Crear componente DocumentLifecycleMap.
- Crear botones reales.
- Crear pantallas reales.
- Crear prototipo funcional.
- Crear endpoints.
- Conectar Supabase.
- Conectar Firebase.
- Conectar GitHub automáticamente.
- Conectar Obsidian automáticamente.
- Sincronizar documentos automáticamente.
- Automatizar commits.
- Automatizar aprobaciones.
- Automatizar HOME.
- Automatizar README.
- Activar agentes autónomos.
- Ejecutar acciones reales.
- Avanzar automáticamente a Fase 11.

---

## Riesgo

Tipo de cambio:

**Aprobación técnica documental / integración del ciclo de vida documental conceptual**

Nivel de riesgo inicial:

**Nivel 3 — Alto**

Motivo:

El documento define cómo los documentos de Robert nacen, cambian, se corrigen, se aprueban, se integran, se actualizan, se bloquean, se reemplazan, se deprecian y se archivan.

Nivel de riesgo final:

**Nivel 2 — Medio**

Motivo:

El cambio queda limitado a documentación. No crea sistema real de gestión documental, no crea base de datos real, no crea control automático de versiones, no crea modelos nuevos oficiales, no crea componentes nuevos oficiales, no programa, no conecta herramientas externas y no ejecuta acciones.

Nivel de autonomía:

**Nivel 0 — Sin autonomía ejecutiva**

---

## Estado final

ROBERT_TECHNICAL_DOCUMENT_LIFECYCLE_SPEC v0.2 queda aprobado e integrado documentalmente.

Robert continúa en:

**Fase 10 — MVP técnico básico en preparación**

Sin programación autorizada.

Sin código real.

Sin sistema real de gestión documental.

Sin base de datos real.

Sin control automático de versiones.

Sin conexiones externas.

Sin automatizaciones reales.

Sin agentes autónomos activos.

---

## Estado final

ROBERT_TECHNICAL_DOCUMENT_LIFECYCLE_SPEC v0.2 queda como:

**Propuesta corregida pendiente de revisión**

No está aprobado todavía.

Robert continúa en:

**Fase 10 — MVP técnico básico en preparación**

Sin programación autorizada.

Sin código real.

Sin sistema real de gestión documental.

Sin base de datos real.

Sin control automático de versiones.

Sin conexiones externas.

Sin automatizaciones reales.

Sin agentes autónomos activos.


---

# CAMBIO #041 — Corrección de ROBERT_TECHNICAL_VERSIONING_AND_CHANGE_POLICY_SPEC v0.2

Fecha: 06/07/2026  
Estado: Propuesta corregida — pendiente de revisión  
Documento afectado: ROBERT_TECHNICAL_VERSIONING_AND_CHANGE_POLICY_SPEC  
Versión actualizada: v0.2  
Ubicación: 10_MVP  
Documento base principal: ROBERT_TECHNICAL_DOCUMENT_LIFECYCLE_SPEC v0.2  
Documentos relacionados: ROBERT_COMMANDS v0.4, ROBERT_TECHNICAL_SESSION_AND_CONTEXT_SPEC v0.2, ROBERT_TECHNICAL_NOTIFICATION_AND_ALERTS_SPEC v0.2, ROBERT_TECHNICAL_AUDIT_TRAIL_SPEC v0.2, ROBERT_TECHNICAL_PERMISSIONS_AND_SCOPES_SPEC v0.2, ROBERT_TECHNICAL_ERROR_AND_BLOCKING_SPEC v0.2, ROBERT_TECHNICAL_USER_ACTIONS_SPEC v0.2, ROBERT_TECHNICAL_DATA_MODEL_SPEC v0.1, ROBERT_TECHNICAL_COMPONENTS_SPEC v0.2, ROBERT_TECHNICAL_SCREEN_STATE_SPEC v0.2, ROBERT_TECHNICAL_INTERACTION_FLOW_SPEC v0.2  
Fase relacionada: Fase 10 — MVP técnico básico en preparación  

---

## Cambio realizado

Se corrigió el documento:

**ROBERT_TECHNICAL_VERSIONING_AND_CHANGE_POLICY_SPEC**

de v0.1 a:

**v0.2 — Propuesta corregida pendiente de revisión**

---

## Motivo del cambio

Durante la revisión de v0.1 se detectaron huecos en la relación entre versionamiento y ciclo de vida documental:

- Faltaba una tabla explícita de correspondencia entre los 12 estados de DOCUMENT_LIFECYCLE_SPEC v0.2 y los 8 niveles de versión.
- No quedaba claro si estados como Aprobado, Integrado, Depreciado, Reemplazado, Bloqueado o Archivado correspondían siempre a un solo nivel de versión.
- No estaba aclarado que estado documental y número de versión son dimensiones distintas.
- Ninguno de los 8 niveles de versión incluía transición hacia Bloqueado.
- DOCUMENT_LIFECYCLE_SPEC v0.2 permite que cualquier estado pase a Bloqueado, pero VERSIONING_AND_CHANGE_POLICY_SPEC v0.1 no reflejaba esa misma regla.

---

## Correcciones aplicadas

La versión v0.2 corrige:

- Se agrega tabla explícita de correspondencia entre DOCUMENT_LIFECYCLE_SPEC v0.2 y los 8 niveles de versión.
- Se aclara que el estado documental y el número de versión son dimensiones distintas.
- Se aclara que el número de versión indica evolución/versionado.
- Se aclara que el estado documental indica posición dentro del ciclo de vida.
- Se aclara que una misma versión puede tener distintos estados documentales según el avance.
- Se agrega transición hacia Bloqueado en los 8 niveles de versión.
- Se agrega v0.0 → Bloqueado.
- Se agrega v0.1 → Bloqueado.
- Se agrega v0.2 → Bloqueado.
- Se agrega v0.3+ → Bloqueado.
- Se agrega v0.x aprobado → Bloqueado.
- Se agrega v1.0 → Bloqueado.
- Se agrega v1.x → Bloqueado.
- Se agrega v2.0 → Bloqueado.
- Se aclara que cualquier nivel de versión puede entrar en Bloqueado si existe riesgo, contradicción, falta de permiso, falta de información, fase incorrecta o intento de ejecución no autorizada.
- Se aclara que la salida desde Bloqueado se rige por DOCUMENT_LIFECYCLE_SPEC v0.2.
- Se actualizan los criterios de aceptación.
- Se cambia la aprobación futura esperada a v0.2.

---

## Alcance autorizado

Este cambio autoriza únicamente:

- Corregir el documento técnico.
- Mantenerlo como propuesta pendiente de revisión.
- Usarlo para revisión documental.
- Alinear versionamiento con DOCUMENT_LIFECYCLE_SPEC v0.2.
- Alinear versionamiento con SESSION_AND_CONTEXT_SPEC v0.2.
- Alinear versionamiento con ERROR_AND_BLOCKING_SPEC v0.2.
- Alinear versionamiento con AUDIT_TRAIL_SPEC v0.2.
- Mantenerlo dentro de Fase 10.

---

## Alcance no autorizado

Este cambio no autoriza:

- Aprobar automáticamente VERSIONING_AND_CHANGE_POLICY_SPEC v0.2.
- Crear modelo VersionRecord.
- Crear modelo VersionPolicyRecord.
- Crear modelo CompatibilityRecord.
- Crear modelo BreakingChangeRecord.
- Crear modelo VersionTransitionRecord.
- Crear componente VersionTimeline.
- Crear componente CompatibilityPanel.
- Crear componente VersionStatusBadge.
- Crear componente ChangePolicyMap.
- Crear sistema real de control de versiones.
- Crear base de datos real.
- Crear control automático de versiones.
- Programar la app.
- Crear código real.
- Crear botones reales.
- Crear pantallas reales.
- Conectar GitHub automáticamente.
- Conectar Obsidian automáticamente.
- Sincronizar documentos automáticamente.
- Automatizar commits.
- Automatizar aprobaciones.
- Automatizar HOME.
- Automatizar README.
- Activar agentes autónomos.
- Ejecutar acciones reales.
- Avanzar automáticamente a Fase 11.

---

## Riesgo

Tipo de cambio:

**Cambio técnico documental / corrección de política conceptual de versiones y cambios**

Nivel de riesgo inicial:

**Nivel 3 — Alto**

Motivo:

El documento define cómo Robert numera versiones, registra cambios, corrige documentos, reemplaza versiones, mantiene compatibilidad y evita contradicciones entre documentos.

Nivel de riesgo final esperado:

**Nivel 2 — Medio**

Motivo:

La corrección sigue siendo documental. No crea sistema real de control de versiones, no crea base de datos real, no crea control automático de versiones, no crea modelos nuevos oficiales, no crea componentes nuevos oficiales, no programa, no conecta herramientas externas y no ejecuta acciones.

Nivel de autonomía:

**Nivel 0 — Sin autonomía ejecutiva**

---

## Estado final

ROBERT_TECHNICAL_VERSIONING_AND_CHANGE_POLICY_SPEC v0.2 queda como:

**Propuesta corregida pendiente de revisión**

No está aprobado todavía.

Robert continúa en:

**Fase 10 — MVP técnico básico en preparación**

Sin programación autorizada.

Sin código real.

Sin sistema real de control de versiones.

Sin base de datos real.

Sin control automático de versiones.

Sin conexiones externas.

Sin automatizaciones reales.

Sin agentes autónomos activos.

---

# CAMBIO #042 — Aprobación e integración de ROBERT_TECHNICAL_VERSIONING_AND_CHANGE_POLICY_SPEC v0.2

Fecha: 06/07/2026  
Estado: Aprobado e integrado  
Documento afectado: ROBERT_TECHNICAL_VERSIONING_AND_CHANGE_POLICY_SPEC v0.2  
Ubicación: 10_MVP  
Decisión relacionada: DECISIÓN #024 — Aprobación de ROBERT_TECHNICAL_VERSIONING_AND_CHANGE_POLICY_SPEC v0.2  
Cambio relacionado previo: CAMBIO #041 — Corrección de ROBERT_TECHNICAL_VERSIONING_AND_CHANGE_POLICY_SPEC v0.2  
Documento base principal: ROBERT_TECHNICAL_DOCUMENT_LIFECYCLE_SPEC v0.2  
Documentos relacionados: ROBERT_COMMANDS v0.4, ROBERT_TECHNICAL_SESSION_AND_CONTEXT_SPEC v0.2, ROBERT_TECHNICAL_NOTIFICATION_AND_ALERTS_SPEC v0.2, ROBERT_TECHNICAL_AUDIT_TRAIL_SPEC v0.2, ROBERT_TECHNICAL_PERMISSIONS_AND_SCOPES_SPEC v0.2, ROBERT_TECHNICAL_ERROR_AND_BLOCKING_SPEC v0.2, ROBERT_TECHNICAL_USER_ACTIONS_SPEC v0.2, ROBERT_TECHNICAL_DATA_MODEL_SPEC v0.1, ROBERT_TECHNICAL_COMPONENTS_SPEC v0.2, ROBERT_TECHNICAL_SCREEN_STATE_SPEC v0.2, ROBERT_TECHNICAL_INTERACTION_FLOW_SPEC v0.2  
Fase relacionada: Fase 10 — MVP técnico básico en preparación  

---

## Cambio realizado

Se registró la aprobación formal e integración documental de:

**ROBERT_TECHNICAL_VERSIONING_AND_CHANGE_POLICY_SPEC v0.2**

como documento técnico documental aprobado del MVP técnico básico de Robert.

---

## Motivo del cambio

Después de corregir VERSIONING_AND_CHANGE_POLICY_SPEC v0.1 y revisar la propuesta v0.2, el usuario aprobó formalmente el documento.

La versión v0.2 queda integrada porque define reglas de versiones, numeración, cambios, compatibilidad, reemplazos, parches, versiones vigentes y versiones históricas.

---

## Correcciones integradas

La versión aprobada integra:

- Tabla explícita de correspondencia entre DOCUMENT_LIFECYCLE_SPEC v0.2 y los 8 niveles de versión.
- Separación entre estado documental y número de versión.
- Regla de que el número de versión indica evolución/versionado.
- Regla de que el estado documental indica posición dentro del ciclo de vida.
- Regla de que una misma versión puede tener distintos estados documentales según avance.
- Transición hacia Bloqueado en los 8 niveles de versión.
- v0.0 → Bloqueado.
- v0.1 → Bloqueado.
- v0.2 → Bloqueado.
- v0.3+ → Bloqueado.
- v0.x aprobado → Bloqueado.
- v1.0 → Bloqueado.
- v1.x → Bloqueado.
- v2.0 → Bloqueado.
- Regla de que cualquier nivel de versión puede entrar en Bloqueado si existe riesgo, contradicción, falta de permiso, falta de información, fase incorrecta o intento de ejecución no autorizada.
- Regla de que la salida desde Bloqueado se rige por DOCUMENT_LIFECYCLE_SPEC v0.2.
- Alineación con DOCUMENT_LIFECYCLE_SPEC v0.2.
- Alineación con SESSION_AND_CONTEXT_SPEC v0.2.
- Alineación con NOTIFICATION_AND_ALERTS_SPEC v0.2.
- Alineación con AUDIT_TRAIL_SPEC v0.2.
- Alineación con PERMISSIONS_AND_SCOPES_SPEC v0.2.
- Alineación con ERROR_AND_BLOCKING_SPEC v0.2.
- Alineación con USER_ACTIONS_SPEC v0.2.
- Alineación con DATA_MODEL_SPEC v0.1.
- Alineación con COMPONENTS_SPEC v0.2.
- Alineación con SCREEN_STATE_SPEC v0.2.
- Alineación con INTERACTION_FLOW_SPEC v0.2.

---

## Alcance autorizado

Este cambio autoriza únicamente:

- Marcar VERSIONING_AND_CHANGE_POLICY_SPEC v0.2 como aprobado.
- Integrarlo al estado documental actual de Robert.
- Usarlo como base documental para futuras especificaciones técnicas.
- Usarlo para definir reglas conceptuales de versionamiento.
- Usarlo para definir niveles de versión.
- Usarlo para definir tipos de cambio documental.
- Usarlo para definir compatibilidad entre versiones.
- Usarlo para definir versiones vigentes.
- Usarlo para definir versiones históricas.
- Usarlo para definir reemplazos documentales.
- Usarlo para definir parches documentales.
- Usarlo para conectar versionamiento con ciclo documental, sesión, auditoría, permisos, acciones, eventos, notificaciones y componentes conceptuales.
- Mantenerlo dentro de Fase 10.

---

## Alcance no autorizado

Este cambio no autoriza:

- Programar la app.
- Crear código real.
- Crear sistema real de control de versiones.
- Crear base de datos real.
- Crear control automático de versiones.
- Crear modelo VersionRecord.
- Crear modelo VersionPolicyRecord.
- Crear modelo CompatibilityRecord.
- Crear modelo BreakingChangeRecord.
- Crear modelo VersionTransitionRecord.
- Crear componente VersionTimeline.
- Crear componente CompatibilityPanel.
- Crear componente VersionStatusBadge.
- Crear componente ChangePolicyMap.
- Crear botones reales.
- Crear pantallas reales.
- Crear prototipo funcional.
- Crear endpoints.
- Conectar Supabase.
- Conectar Firebase.
- Conectar GitHub automáticamente.
- Conectar Obsidian automáticamente.
- Sincronizar documentos automáticamente.
- Automatizar commits.
- Automatizar aprobaciones.
- Automatizar HOME.
- Automatizar README.
- Activar agentes autónomos.
- Ejecutar acciones reales.
- Avanzar automáticamente a Fase 11.

---

## Riesgo

Tipo de cambio:

**Aprobación técnica documental / integración de política conceptual de versiones y cambios**

Nivel de riesgo inicial:

**Nivel 3 — Alto**

Motivo:

El documento define cómo Robert numera versiones, registra cambios, corrige documentos, reemplaza versiones, mantiene compatibilidad y evita contradicciones entre documentos.

Nivel de riesgo final:

**Nivel 2 — Medio**

Motivo:

El cambio queda limitado a documentación. No crea sistema real de control de versiones, no crea base de datos real, no crea control automático de versiones, no crea modelos nuevos oficiales, no crea componentes nuevos oficiales, no programa, no conecta herramientas externas y no ejecuta acciones.

Nivel de autonomía:

**Nivel 0 — Sin autonomía ejecutiva**

---

## Estado final

ROBERT_TECHNICAL_VERSIONING_AND_CHANGE_POLICY_SPEC v0.2 queda aprobado e integrado documentalmente.

Robert continúa en:

**Fase 10 — MVP técnico básico en preparación**

Sin programación autorizada.

Sin código real.

Sin sistema real de control de versiones.

Sin base de datos real.

Sin control automático de versiones.

Sin conexiones externas.

Sin automatizaciones reales.

Sin agentes autónomos activos.

---

# CAMBIO #043 — Corrección de ROBERT_TECHNICAL_DATA_CONSISTENCY_AND_CONFLICT_RESOLUTION_SPEC v0.3

Fecha: 06/07/2026  
Estado: Propuesta corregida — pendiente de revisión  
Documento afectado: ROBERT_TECHNICAL_DATA_CONSISTENCY_AND_CONFLICT_RESOLUTION_SPEC  
Versión actualizada: v0.3  
Ubicación: 10_MVP  
Documento base principal: ROBERT_TECHNICAL_VERSIONING_AND_CHANGE_POLICY_SPEC v0.2  
Documentos relacionados: ROBERT_COMMANDS v0.4, ROBERT_TECHNICAL_DOCUMENT_LIFECYCLE_SPEC v0.2, ROBERT_TECHNICAL_SESSION_AND_CONTEXT_SPEC v0.2, ROBERT_TECHNICAL_NOTIFICATION_AND_ALERTS_SPEC v0.2, ROBERT_TECHNICAL_AUDIT_TRAIL_SPEC v0.2, ROBERT_TECHNICAL_PERMISSIONS_AND_SCOPES_SPEC v0.2, ROBERT_TECHNICAL_ERROR_AND_BLOCKING_SPEC v0.2, ROBERT_TECHNICAL_USER_ACTIONS_SPEC v0.2, ROBERT_TECHNICAL_DATA_MODEL_SPEC v0.1, ROBERT_TECHNICAL_COMPONENTS_SPEC v0.2, ROBERT_TECHNICAL_SCREEN_STATE_SPEC v0.2, ROBERT_TECHNICAL_INTERACTION_FLOW_SPEC v0.2  
Fase relacionada: Fase 10 — MVP técnico básico en preparación  

---

## Cambio realizado

Se corrigió el documento:

**ROBERT_TECHNICAL_DATA_CONSISTENCY_AND_CONFLICT_RESOLUTION_SPEC**

de v0.2 a:

**v0.3 — Propuesta corregida pendiente de revisión**

---

## Motivo del cambio

Durante la revisión cruzada de v0.2 se detectó una inconsistencia interna sistemática:

- La tabla maestra de precedencia establecía un orden total entre los 17 tipos de conflicto.
- Las secciones individuales “Precedencia” de varios tipos repetían listas incompletas.
- Esto podía crear dos fuentes internas de verdad para clasificar conflictos.
- Si alguien usaba solo la sección individual de un tipo, podía llegar a una clasificación distinta a la tabla maestra.
- También faltaba aclarar que los conflictos secundarios deben listarse en orden de precedencia.

---

## Correcciones aplicadas

La versión v0.3 corrige:

- Se establece que la TABLA DE PRECEDENCIA ENTRE LOS 17 TIPOS DE CONFLICTO es la única fuente oficial del orden completo.
- Se aclara que las secciones individuales de cada tipo no reemplazan, no duplican y no contradicen la tabla maestra.
- Se elimina la contradicción interna entre tabla maestra y prosa individual.
- Se modifica la sección “Precedencia” de cada tipo para remitir al orden completo de la tabla maestra.
- Se mantiene una nota específica por tipo solo cuando ayuda a entender su uso.
- Se evita duplicar listas completas de precedencia dentro de cada tipo.
- Se agrega regla explícita para ordenar conflictos secundarios.
- Se aclara que los conflictos secundarios deben listarse en orden de precedencia.
- Se corrige el ejemplo de Gmail para ordenar los conflictos secundarios según la tabla maestra.
- Se mantiene la regla de categoría general + subtipo específico + tipo más específico disponible.
- Se mantiene la integración de documentos técnicos aprobados dentro de la posición 9 de la jerarquía general.
- Se mantiene la subjerarquía temática de documentos técnicos aprobados.

---

## Alcance autorizado

Este cambio autoriza únicamente:

- Corregir el documento técnico.
- Mantenerlo como propuesta pendiente de revisión.
- Usarlo para revisión documental.
- Alinear la precedencia interna de los 17 tipos de conflicto.
- Alinear clasificación final y conflictos secundarios.
- Alinear consistencia documental con VERSIONING_AND_CHANGE_POLICY_SPEC v0.2.
- Alinear consistencia documental con DOCUMENT_LIFECYCLE_SPEC v0.2.
- Alinear consistencia documental con ERROR_AND_BLOCKING_SPEC v0.2.
- Alinear consistencia documental con AUDIT_TRAIL_SPEC v0.2.
- Alinear consistencia documental con PERMISSIONS_AND_SCOPES_SPEC v0.2.
- Mantenerlo dentro de Fase 10.

---

## Alcance no autorizado

Este cambio no autoriza:

- Aprobar automáticamente DATA_CONSISTENCY_AND_CONFLICT_RESOLUTION_SPEC v0.3.
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
- Programar la app.
- Crear código real.
- Crear botones reales.
- Crear pantallas reales.
- Crear prototipo funcional.
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

## Riesgo

Tipo de cambio:

**Cambio técnico documental / corrección de consistencia documental y precedencia de conflictos**

Nivel de riesgo inicial:

**Nivel 3 — Alto**

Motivo:

El documento define cómo Robert detecta contradicciones, prioriza fuentes, clasifica conflictos múltiples, bloquea acciones por conflictos y resuelve inconsistencias documentales.

Nivel de riesgo final esperado:

**Nivel 2 — Medio**

Motivo:

La corrección sigue siendo documental. No crea sistema real de consistencia, no crea base de datos real, no crea motor real de resolución de conflictos, no crea modelos nuevos oficiales, no crea componentes nuevos oficiales, no programa, no conecta herramientas externas y no ejecuta acciones.

Nivel de autonomía:

**Nivel 0 — Sin autonomía ejecutiva**

---

## Estado final

ROBERT_TECHNICAL_DATA_CONSISTENCY_AND_CONFLICT_RESOLUTION_SPEC v0.3 queda como:

**Propuesta corregida pendiente de revisión**

No está aprobado todavía.

Robert continúa en:

**Fase 10 — MVP técnico básico en preparación**

Sin programación autorizada.

Sin código real.

Sin sistema real de consistencia documental.

Sin base de datos real.

Sin motor real de resolución de conflictos.

Sin conexiones externas.

Sin automatizaciones reales.

Sin agentes autónomos activos.

---

# CAMBIO #044 — Aprobación e integración de ROBERT_TECHNICAL_DATA_CONSISTENCY_AND_CONFLICT_RESOLUTION_SPEC v0.3

Fecha: 07/07/2026  
Estado: Aprobado e integrado  
Documento afectado: ROBERT_TECHNICAL_DATA_CONSISTENCY_AND_CONFLICT_RESOLUTION_SPEC v0.3  
Ubicación: 10_MVP  
Decisión relacionada: DECISIÓN #025 — Aprobación de ROBERT_TECHNICAL_DATA_CONSISTENCY_AND_CONFLICT_RESOLUTION_SPEC v0.3  
Cambio relacionado previo: CAMBIO #043 — Corrección de ROBERT_TECHNICAL_DATA_CONSISTENCY_AND_CONFLICT_RESOLUTION_SPEC v0.3  
Documento base principal: ROBERT_TECHNICAL_VERSIONING_AND_CHANGE_POLICY_SPEC v0.2  
Documentos relacionados: ROBERT_COMMANDS v0.4, ROBERT_TECHNICAL_DOCUMENT_LIFECYCLE_SPEC v0.2, ROBERT_TECHNICAL_SESSION_AND_CONTEXT_SPEC v0.2, ROBERT_TECHNICAL_NOTIFICATION_AND_ALERTS_SPEC v0.2, ROBERT_TECHNICAL_AUDIT_TRAIL_SPEC v0.2, ROBERT_TECHNICAL_PERMISSIONS_AND_SCOPES_SPEC v0.2, ROBERT_TECHNICAL_ERROR_AND_BLOCKING_SPEC v0.2, ROBERT_TECHNICAL_USER_ACTIONS_SPEC v0.2, ROBERT_TECHNICAL_DATA_MODEL_SPEC v0.1, ROBERT_TECHNICAL_COMPONENTS_SPEC v0.2, ROBERT_TECHNICAL_SCREEN_STATE_SPEC v0.2, ROBERT_TECHNICAL_INTERACTION_FLOW_SPEC v0.2  
Fase relacionada: Fase 10 — MVP técnico básico en preparación  

---

## Cambio realizado

Se registró la aprobación formal e integración documental de:

**ROBERT_TECHNICAL_DATA_CONSISTENCY_AND_CONFLICT_RESOLUTION_SPEC v0.3**

como documento técnico documental aprobado del MVP técnico básico de Robert.

---

## Motivo del cambio

Después de corregir DATA_CONSISTENCY_AND_CONFLICT_RESOLUTION_SPEC v0.2 y revisar la propuesta v0.3, el usuario aprobó formalmente el documento.

La versión v0.3 queda integrada porque define reglas de consistencia documental, contradicciones, prioridad entre fuentes, resolución conceptual de inconsistencias, precedencia entre tipos de conflicto y bloqueo por información contradictoria.

---

## Correcciones integradas

La versión aprobada integra:

- Regla de consistencia documental.
- Regla de contradicción documental.
- Regla de conflicto crítico.
- Jerarquía conceptual general de fuentes.
- Integración de documentos técnicos aprobados dentro de la posición 9.
- Subjerarquía temática de documentos técnicos aprobados.
- Regla general vs regla temática.
- Prioridad de SECURITY_RULES.
- Prioridad de DECISIONS_LOG.
- Prioridad de CONTROL_DE_CAMBIOS.
- Regla HOME vs README.
- 17 tipos de conflicto documental.
- Tabla maestra de precedencia entre los 17 tipos de conflicto.
- Regla de fuente única oficial de precedencia.
- Regla de que la tabla maestra es la única fuente oficial del orden completo.
- Regla de que la prosa individual no reemplaza ni contradice la tabla maestra.
- Regla de tipo más específico disponible.
- Regla de clasificación final y conflictos secundarios.
- Regla de orden para conflictos secundarios.
- Corrección del ejemplo de Gmail con conflictos secundarios ordenados por precedencia.
- Relación con VERSIONING_AND_CHANGE_POLICY_SPEC v0.2.
- Relación con DOCUMENT_LIFECYCLE_SPEC v0.2.
- Relación con SESSION_AND_CONTEXT_SPEC v0.2.
- Relación con AUDIT_TRAIL_SPEC v0.2.
- Relación con NOTIFICATION_AND_ALERTS_SPEC v0.2.
- Relación con ERROR_AND_BLOCKING_SPEC v0.2.
- Relación con PERMISSIONS_AND_SCOPES_SPEC v0.2.
- Relación con USER_ACTIONS_SPEC v0.2.
- Relación con DATA_MODEL_SPEC v0.1.
- Relación con COMPONENTS_SPEC v0.2.
- Relación con SCREEN_STATE_SPEC v0.2.
- Relación con INTERACTION_FLOW_SPEC v0.2.

---

## Alcance autorizado

Este cambio autoriza únicamente:

- Marcar DATA_CONSISTENCY_AND_CONFLICT_RESOLUTION_SPEC v0.3 como aprobado.
- Integrarlo al estado documental actual de Robert.
- Usarlo como base documental para futuras especificaciones técnicas.
- Usarlo para definir reglas conceptuales de consistencia documental.
- Usarlo para definir reglas conceptuales de resolución de conflictos.
- Usarlo para definir prioridad entre fuentes.
- Usarlo para definir clasificación final de conflictos.
- Usarlo para definir conflictos secundarios en orden de precedencia.
- Usarlo para definir cuándo pausar por contradicción.
- Usarlo para definir cuándo bloquear por contradicción.
- Usarlo para definir cuándo pedir confirmación por falta de trazabilidad.
- Usarlo para conectar consistencia documental con versionamiento, ciclo documental, sesión, auditoría, permisos, eventos, notificaciones, acciones, modelos, componentes, pantallas y flujos.
- Mantenerlo dentro de Fase 10.

---

## Alcance no autorizado

Este cambio no autoriza:

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

## Riesgo

Tipo de cambio:

**Aprobación técnica documental / integración de consistencia documental y resolución conceptual de conflictos**

Nivel de riesgo inicial:

**Nivel 3 — Alto**

Motivo:

El documento define cómo Robert detecta contradicciones, prioriza fuentes, clasifica conflictos múltiples, bloquea acciones por conflictos y resuelve inconsistencias documentales.

Nivel de riesgo final:

**Nivel 2 — Medio**

Motivo:

El cambio queda limitado a documentación. No crea sistema real de consistencia documental, no crea base de datos real, no crea motor real de resolución de conflictos, no crea modelos nuevos oficiales, no crea componentes nuevos oficiales, no programa, no conecta herramientas externas y no ejecuta acciones.

Nivel de autonomía:

**Nivel 0 — Sin autonomía ejecutiva**

---

## Estado final

ROBERT_TECHNICAL_DATA_CONSISTENCY_AND_CONFLICT_RESOLUTION_SPEC v0.3 queda aprobado e integrado documentalmente.

Robert continúa en:

**Fase 10 — MVP técnico básico en preparación**

Sin programación autorizada.

Sin código real.

Sin sistema real de consistencia documental.

Sin base de datos real.

Sin motor real de resolución de conflictos.

Sin conexiones externas.

Sin automatizaciones reales.

Sin agentes autónomos activos.

---


## CAMBIO #045 — Corrección acumulada de ROBERT_HOME v0.5–v0.7

Fecha: 07/07/2026  
Tipo de cambio: Corrección documental / trazabilidad interna / reconciliación de HOME  
Documento afectado: ROBERT_HOME.md  
Versiones afectadas: v0.5, v0.6, v0.7  
Estado: Registrado — pendiente de integración en ROBERT_HOME v0.8  
Fase relacionada: Fase 10 — MVP técnico básico en preparación  

---

### Descripción del cambio

Se registra formalmente la corrección acumulada de ROBERT_HOME después de detectar que las versiones v0.5, v0.6 y v0.7 corrigieron distintos conflictos internos del HOME, pero no habían dejado trazabilidad formal dentro de ROBERT_CONTROL_DE_CAMBIOS.

Este cambio documenta que ROBERT_HOME estaba en proceso de reconciliación y que sus versiones recientes fueron propuestas corregidas, no versiones aprobadas ni cerradas.

---

### Motivo del cambio

Se detectó que ROBERT_HOME presentaba un conflicto de trazabilidad sobre sí mismo.

Las versiones v0.5, v0.6 y v0.7 indicaban en PRIORIDAD ACTUAL y PRÓXIMOS PASOS que debía registrarse la corrección de HOME en CONTROL_DE_CAMBIOS, pero ninguna confirmaba que dicho registro existiera.

Esto generaba un hueco de trazabilidad acumulado.

---

### Clasificación del conflicto

Clasificación final:

```text
TIPO 17 — Conflicto de trazabilidad insuficiente

---

## CAMBIO #046 — Aprobación e integración de ROBERT_HOME v0.8

Fecha: 07/07/2026  
Tipo de cambio: Aprobación e integración documental  
Documento afectado: ROBERT_HOME.md  
Versión afectada: v0.8  
Estado: Aprobado e integrado  
Decisión relacionada: DECISIÓN #026 — Aprobación de ROBERT_HOME v0.8  
Cambio relacionado previo: CAMBIO #045 — Corrección acumulada de ROBERT_HOME v0.5–v0.7  
Fase relacionada: Fase 10 — MVP técnico básico en preparación  

---

### Descripción del cambio

Se registra la aprobación e integración de `ROBERT_HOME v0.8` como punto central de navegación, estado, núcleo visual y control del sistema Robert.

---

### Motivo del cambio

ROBERT_HOME v0.8 fue aprobado formalmente mediante DECISIÓN #026 después de corregir la trazabilidad acumulada de las versiones v0.5, v0.6 y v0.7.

---

### Estado integrado

```text
ROBERT_HOME v0.8
Estado: Aprobado e integrado
Decisión relacionada: DECISIÓN #026
Cambio relacionado previo: CAMBIO #045
Cambio de integración: CAMBIO #046

---

CAMBIO #047 — Auditoría voluntaria de ROBERT_TECHNICAL_USER_ACTIONS_SPEC v0.2

Fecha: 07/07/2026
Tipo de cambio: Auditoría voluntaria documental / confirmación de fuente vigente
Documento afectado: ROBERT_TECHNICAL_USER_ACTIONS_SPEC.md
Versión afectada: v0.2
Estado: Auditado — sin cambios de fondo
Fase relacionada: Fase 10 — MVP técnico básico en preparación

---

### Descripción del cambio

Se registra una auditoría voluntaria de ROBERT_TECHNICAL_USER_ACTIONS_SPEC v0.2,
documento ya aprobado e integrado previamente (DECISIÓN #017, CAMBIO #028).

El usuario solicitó volver a verificar este documento sin que existiera un conflicto
de aprobación real ni un hueco de trazabilidad pendiente.

---

### Motivo del cambio

Corrección de registro: la versión original de este CAMBIO #047 describía
incorrectamente que "el archivo real disponible estaba en v0.1 y en estado de
borrador" y que existía "un conflicto de versión, fuente vigente y trazabilidad".

Esa descripción era inexacta. ROBERT_TECHNICAL_USER_ACTIONS_SPEC v0.2 ya estaba
aprobado e integrado desde DECISIÓN #017 / CAMBIO #028, antes de que existieran los
9 documentos técnicos posteriores de la serie (ERROR_AND_BLOCKING_SPEC hasta
APPROVAL_AND_AUTHORIZATION_GATE_SPEC), todos construidos correctamente sobre esa
base ya vigente.

No existió conflicto real de versión, fuente vigente ni trazabilidad. El usuario
confirmó explícitamente que el documento ya estaba aprobado y que solo pidió
revisarlo de nuevo por precaución.

---

### Resultado de la auditoría

No se encontraron errores de contenido de fondo.

- La lista canónica de 20 acciones es correcta y completa.
- Los 10 componentes usados son los canónicos (AppShell incluido, MainCanvas
  ausente).
- Único ajuste aplicado: corrección de la fila ACCIÓN 12 en la tabla de mapeo con
  Gates ("Gate 2" → "Gate 2 / Gate 7").

---

### Clasificación del conflicto

Clasificación corregida:

Ninguna. No aplica ningún TIPO de conflicto de
DATA_CONSISTENCY_AND_CONFLICT_RESOLUTION_SPEC v0.3.

(Clasificación anterior, ahora retirada por ser incorrecta: TIPO 3, TIPO 16, TIPO 17)

---

### Regla aplicada

Según DOCUMENT_LIFECYCLE_SPEC v0.2, un documento aprobado que recibe un ajuste
menor permanece en estado "Aprobado" — no regresa a "Borrador" ni a "Propuesta
corregida".

Esta auditoría no reabre el estado de aprobación de USER_ACTIONS_SPEC v0.2.

---

### Uso de esta auditoría

Sirve como referencia canónica confirmada, usada posteriormente para corregir
ROBERT_TECHNICAL_APPROVAL_AND_AUTHORIZATION_GATE_SPEC v0.3 (CAMBIO #048/#049).

---

### Estado final

ROBERT_TECHNICAL_USER_ACTIONS_SPEC v0.2 se mantiene:
Aprobado e integrado — auditoría voluntaria completada sin cambios de fondo

No se requirió nueva DECISIÓN, ya que no hubo corrección sustantiva de contenido.

---

### Nota de control

Este registro corrige la descripción original de CAMBIO #047, que contenía una
narrativa inexacta sobre el estado del documento. La corrección es solo de
redacción del registro de cambios — no afecta ningún documento técnico downstream.
Robert no ejecuta acciones importantes sin permiso.

---
## CAMBIO #048 — Corrección de ROBERT_TECHNICAL_APPROVAL_AND_AUTHORIZATION_GATE_SPEC v0.3

Fecha: 07/07/2026
Tipo de cambio: Corrección técnica documental / ApprovalGate conceptual
Documento afectado: ROBERT_TECHNICAL_APPROVAL_AND_AUTHORIZATION_GATE_SPEC.md
Versión afectada: v0.3
Estado: Propuesta corregida — pendiente de revisión
Fase relacionada: Fase 10 — MVP técnico básico en preparación
Cambio relacionado previo: CAMBIO #047 — Corrección de ROBERT_TECHNICAL_USER_ACTIONS_SPEC v0.2
Documento base principal: ROBERT_TECHNICAL_USER_ACTIONS_SPEC v0.2

---

### Descripción del cambio

Se registra la creación/corrección de `ROBERT_TECHNICAL_APPROVAL_AND_AUTHORIZATION_GATE_SPEC v0.3` como propuesta corregida pendiente de revisión.

Esta versión corrige los errores detectados en `APPROVAL_GATE v0.2`.

---

### Motivo del cambio

Se detectaron dos errores principales en `APPROVAL_GATE v0.2`:

```text
1. Uso de MainCanvas como componente participante.
2. Numeración incorrecta en la tabla de correspondencia con USER_ACTIONS_SPEC v0.2.
```

Estos errores generaban conflicto con la fuente canónica vigente:

```text
ROBERT_TECHNICAL_USER_ACTIONS_SPEC v0.2
```

---

### Correcciones aplicadas

La versión v0.3 corrige los siguientes puntos:

1. Reemplaza `MainCanvas` por `AppShell`.
2. Corrige la lista de componentes participantes.
3. Corrige la tabla de mapeo entre Gates y componentes.
4. Corrige la tabla de dónde se muestra cada elemento.
5. Corrige la tabla de correspondencia con `USER_ACTIONS_SPEC v0.2`.
6. Usa las 20 acciones canónicas de `USER_ACTIONS_SPEC v0.2`.
7. Mantiene `ApprovalGate` como especificación conceptual, no como gate real.

---

### Clasificación del conflicto corregido

```text
TIPO 11 — Conflicto de componente
TIPO 12 — Conflicto de flujo
TIPO 16 — Conflicto de fuente vigente
TIPO 17 — Conflicto de trazabilidad insuficiente
```

---

### Alcance autorizado

Este cambio autoriza únicamente:

* Crear/corregir `APPROVAL_GATE v0.3` como propuesta corregida pendiente de revisión.
* Usar `USER_ACTIONS_SPEC v0.2` como fuente canónica.
* Corregir referencias internas a componentes y acciones canónicas.
* Preparar el documento para revisión posterior.

---

### Alcance no autorizado

Este cambio no autoriza:

* Aprobar `APPROVAL_GATE v0.3`.
* Integrar `APPROVAL_GATE v0.3`.
* Programar ApprovalGate.
* Crear código real.
* Crear botones reales.
* Crear pantallas reales.
* Crear gate real.
* Crear sistema real de autorización.
* Conectar herramientas externas.
* Automatizar acciones.
* Activar agentes autónomos.
* Ejecutar acciones reales.
* Avanzar a Fase 11.

---

### Estado final de este cambio

`ROBERT_TECHNICAL_APPROVAL_AND_AUTHORIZATION_GATE_SPEC v0.3` queda como:

**Propuesta corregida — pendiente de revisión**

---

### Siguiente paso

Revisar `APPROVAL_GATE v0.3`.

Si queda correcto, el usuario podrá aprobarlo explícitamente mediante decisión formal.

---

## CAMBIO #049 — Aprobación e integración de ROBERT_TECHNICAL_APPROVAL_AND_AUTHORIZATION_GATE_SPEC v0.3

Fecha: 07/07/2026
Estado: Aprobado e integrado
Tipo de cambio: Aprobación técnica documental / ApprovalGate conceptual
Documento afectado: ROBERT_TECHNICAL_APPROVAL_AND_AUTHORIZATION_GATE_SPEC.md
Versión afectada: v0.3
Ubicación: 10_MVP
Decisión relacionada: DECISIÓN #027 — Aprobación de ROBERT_TECHNICAL_APPROVAL_AND_AUTHORIZATION_GATE_SPEC v0.3
Cambio relacionado previo: CAMBIO #048 — Corrección de ROBERT_TECHNICAL_APPROVAL_AND_AUTHORIZATION_GATE_SPEC v0.3
Documento base principal: ROBERT_TECHNICAL_USER_ACTIONS_SPEC v0.2
Fase relacionada: Fase 10 — MVP técnico básico en preparación

---

### Cambio realizado

Se registra la aprobación formal e integración documental de:

**ROBERT_TECHNICAL_APPROVAL_AND_AUTHORIZATION_GATE_SPEC v0.3**

como documento técnico conceptual aprobado del MVP técnico básico de Robert.

---

### Motivo del cambio

Después de corregir y revisar `APPROVAL_GATE v0.3`, el usuario aprobó formalmente el documento.

La versión v0.3 queda integrada porque corrige errores de componente, flujo, fuente vigente y trazabilidad detectados en versiones anteriores.

---

### Correcciones integradas

La versión aprobada integra:

1. Reemplazo de `MainCanvas` por `AppShell`.
2. Corrección de la lista de componentes participantes.
3. Corrección de la tabla de mapeo entre Gates y componentes.
4. Corrección de la tabla de dónde se muestra cada elemento.
5. Corrección de la tabla de correspondencia con `USER_ACTIONS_SPEC v0.2`.
6. Uso de las 20 acciones canónicas de `USER_ACTIONS_SPEC v0.2` auditado.
7. Confirmación de `ApprovalGate` como especificación conceptual, no como gate real.
8. Confirmación de ACCIÓN 12 — Activar sandbox manual como `Gate 2 / Gate 7`.
9. Alineación con los 10 componentes canónicos aprobados.
10. Exclusión de `MainCanvas` como componente oficial.

---

### Alcance autorizado

Este cambio autoriza únicamente:

* Marcar `APPROVAL_GATE v0.3` como aprobado e integrado.
* Integrarlo al estado documental actual de Robert.
* Usarlo como especificación conceptual de ApprovalGate.
* Relacionar gates conceptuales con acciones del usuario.
* Relacionar gates conceptuales con componentes aprobados.
* Relacionar gates conceptuales con eventos, registros de auditoría y notificaciones.
* Mantenerlo como documento técnico aprobado dentro de Fase 10.
* Actualizar `ROBERT_HOME` y `README` para reflejar su nuevo estado.

---

### Alcance no autorizado

Este cambio no autoriza:

* Programar ApprovalGate.
* Crear código real.
* Crear botones reales.
* Crear pantallas reales.
* Crear prototipo funcional.
* Crear sistema real de autorización.
* Crear sistema real de permisos.
* Crear base de datos real.
* Crear endpoints.
* Conectar Supabase.
* Conectar Firebase.
* Conectar GitHub automáticamente.
* Conectar Gmail.
* Conectar Google Calendar.
* Conectar APIs externas.
* Automatizar acciones.
* Activar agentes autónomos.
* Ejecutar acciones reales.
* Avanzar automáticamente a Fase 11.

---

### Riesgo

Tipo de cambio:

**Aprobación técnica documental / ApprovalGate conceptual**

Nivel de riesgo inicial:

**Nivel 3 — Alto**

Motivo:

El documento define cómo Robert debe decidir conceptualmente si una acción puede continuar, requiere confirmación, requiere aprobación, debe pausarse o debe bloquearse.

Nivel de riesgo final:

**Nivel 2 — Medio**

Motivo:

La aprobación sigue siendo documental y conceptual. No crea gate real, no programa, no conecta herramientas externas, no automatiza y no ejecuta acciones reales.

Nivel de autonomía:

**Nivel 0 — Sin autonomía ejecutiva**

---

### Estado final

`ROBERT_TECHNICAL_APPROVAL_AND_AUTHORIZATION_GATE_SPEC v0.3` queda como:

**Aprobado e integrado**

Robert continúa en:

**Fase 10 — MVP técnico básico en preparación**

Sin programación autorizada.
Sin código real.
Sin botones reales.
Sin pantallas reales.
Sin gate real.
Sin base de datos real.
Sin conexiones externas.
Sin automatizaciones reales.
Sin agentes autónomos activos.
Sin Fase 11 autorizada.

---

### Siguiente paso

Actualizar:

1. `ROBERT_HOME`
2. `README`

Ambos deben reflejar que:

`ROBERT_TECHNICAL_APPROVAL_AND_AUTHORIZATION_GATE_SPEC v0.3` queda aprobado e integrado mediante:

* DECISIÓN #027
* CAMBIO #049

---

### Nota de control

Aprobar este documento no equivale a ejecutar ApprovalGate.

`ApprovalGate` sigue siendo conceptual y documental.

Robert no ejecuta acciones importantes sin permiso.

## CAMBIO #051 — Normalización de fuente física vigente de ROBERT_TECHNICAL_MVP_WIREFRAME v0.3

Fecha: 09/07/2026
Estado: Registrado
Tipo de cambio: Normalización documental / fuente física vigente / wireframe
Documento afectado: ROBERT_TECHNICAL_MVP_WIREFRAME.md
Versión afectada: v0.3
Ubicación: 10_MVP
Decisión relacionada: DECISIÓN #010 — Aprobación de ROBERT_TECHNICAL_MVP_WIREFRAME v0.3
Cambio relacionado previo: CAMBIO #010 — Actualización del wireframe técnico a v0.3
Fase relacionada: Fase 10 — MVP técnico básico en preparación

---

### Cambio realizado

Se registra la normalización de la fuente física vigente del wireframe técnico aprobado de Robert.

El archivo oficial vigente queda como:

```text
10_MVP/ROBERT_TECHNICAL_MVP_WIREFRAME.md
```

El archivo de propuesta ya no existe en la fuente física actual:

```text
10_MVP/ROBERT_TECHNICAL_MVP_WIREFRAME_v0.3_PROPUESTA.md
```

Estado del archivo propuesta:

```text
Eliminado previamente / no vigente / no fuente oficial
```

---

### Motivo del cambio

Se mantenía una pendiente documental sobre la fuente física vigente del wireframe v0.3.

Aunque conceptualmente `ROBERT_TECHNICAL_MVP_WIREFRAME v0.3` ya estaba aprobado, existía una posible ambigüedad entre:

```text
ROBERT_TECHNICAL_MVP_WIREFRAME.md
ROBERT_TECHNICAL_MVP_WIREFRAME_v0.3_PROPUESTA.md
```

El usuario confirmó que el archivo de propuesta ya había sido eliminado previamente.

Por lo tanto, no se crea ni se restaura ningún archivo histórico adicional.

Esta normalización deja claro que solo existe una fuente física vigente para el wireframe v0.3.

---

### Fuente oficial vigente

A partir de esta normalización, la fuente física oficial vigente es:

```text
ROBERT_TECHNICAL_MVP_WIREFRAME.md
```

Versión:

```text
v0.3
```

Estado:

```text
Aprobado e integrado
```

---

### Archivo propuesta

El archivo:

```text
ROBERT_TECHNICAL_MVP_WIREFRAME_v0.3_PROPUESTA.md
```

queda reconocido como:

```text
Eliminado previamente
No vigente
No fuente oficial
No requerido para continuar
```

Regla:

```text
No recrear la propuesta.
No restaurar el archivo eliminado.
No mantener dos fuentes físicas paralelas.
```

---

### Alcance autorizado

Este cambio autoriza únicamente:

* Confirmar `ROBERT_TECHNICAL_MVP_WIREFRAME.md` como fuente física oficial vigente.
* Registrar que la propuesta v0.3 ya no existe como archivo físico activo.
* Eliminar la ambigüedad entre archivo oficial y archivo propuesta.
* Actualizar `ROBERT_HOME` y `README` para reflejar que la normalización física del wireframe v0.3 quedó completada.

---

### Alcance no autorizado

Este cambio no autoriza:

* Programación.
* Código real.
* Pantallas reales.
* Prototipo funcional.
* Base de datos real.
* Gate real.
* Sistema real de autorización.
* Conexiones externas.
* Automatizaciones reales.
* Agentes autónomos.
* Ejecución real.
* Avanzar a Fase 11.

---

### Riesgo

Tipo de cambio:

**Normalización documental / fuente física vigente**

Nivel de riesgo inicial:

**Nivel 2 — Medio**

Motivo:

El cambio afecta la fuente física vigente de un documento técnico aprobado.

Nivel de riesgo final:

**Nivel 1 — Bajo**

Motivo:

La normalización no cambia el contenido aprobado del wireframe. Solo elimina ambigüedad física entre archivo oficial y archivo propuesta.

Nivel de autonomía:

**Nivel 0 — Sin autonomía ejecutiva**

---

### Estado final

`ROBERT_TECHNICAL_MVP_WIREFRAME.md` queda como:

```text
Fuente física oficial vigente
Versión: v0.3
Estado: Aprobado e integrado
```

`ROBERT_TECHNICAL_MVP_WIREFRAME_v0.3_PROPUESTA.md` queda como:

```text
Eliminado previamente
No vigente
No fuente oficial
No requerido
```

---

### Siguiente paso

Actualizar:

1. `ROBERT_HOME`
2. `README`

Ambos deben reflejar que la normalización física del wireframe v0.3 quedó completada mediante:

```text
CAMBIO #051
```

---

### Nota de control

Esta normalización no cambia el contenido aprobado del wireframe.

Solo define cuál archivo físico queda vigente y aclara que el archivo propuesta ya no existe como fuente activa.

Robert continúa en modo documental, manual y supervisado.

Robert no ejecuta acciones importantes sin permiso.


CAMBIO #050 — Aprobación e integración de ROBERT_HOME v0.11

Fecha: 07/07/2026
Tipo de cambio: Aprobación e integración documental
Documento afectado: ROBERT_HOME.md
Versión afectada: v0.11
Estado: Aprobado e integrado
Decisión relacionada: DECISIÓN #028 — Aprobación de ROBERT_HOME v0.11
Cambio relacionado previo: CAMBIO #049 — Aprobación e integración de
ROBERT_TECHNICAL_APPROVAL_AND_AUTHORIZATION_GATE_SPEC v0.3
Fase relacionada: Fase 10 — MVP técnico básico en preparación

---

### Descripción del cambio

Se registra la aprobación e integración de ROBERT_HOME v0.11 como punto central de
navegación, estado, núcleo visual y control del sistema Robert.

---

### Motivo del cambio

ROBERT_HOME v0.11 fue aprobado formalmente mediante DECISIÓN #028 después de
corregir dos huecos detectados en ROBERT_HOME v0.10:

1. Trazabilidad faltante de CAMBIO #047, omitida en v0.10.
2. Uso incorrecto de "ROBERT_VISUAL" en lugar del nombre confirmado
   "ROBERT_VISUAL_REFERENCE" como documento visual oficial.

---

### Correcciones integradas

La versión aprobada integra:

1. Reconocimiento explícito de CAMBIO #047 como antecedente de trazabilidad.
2. Reemplazo de todas las referencias a ROBERT_VISUAL por ROBERT_VISUAL_REFERENCE
   en enlaces, tags y menciones del documento.
3. Regla de nomenclatura visual: "El documento visual correcto es
   ROBERT_VISUAL_REFERENCE. No usar ROBERT_VISUAL como documento oficial."

---

### Alcance autorizado

Este cambio autoriza únicamente:

- Marcar ROBERT_HOME v0.11 como aprobado e integrado.
- Integrarlo al estado documental actual de Robert.
- Sustituir ROBERT_HOME v0.10 como versión vigente de navegación.
- Actualizar README para reflejar su nuevo estado.
- Mantenerlo dentro de Fase 10.

---

### Alcance no autorizado

Este cambio no autoriza:

- Programar la app.
- Crear código real.
- Crear pantallas reales.
- Crear base de datos real.
- Conectar herramientas externas.
- Automatizar acciones.
- Activar agentes autónomos.
- Avanzar a Fase 11.

---

### Riesgo

Tipo de cambio: Aprobación técnica documental / corrección de trazabilidad y
nomenclatura visual
Nivel de riesgo inicial: Nivel 2 — Medio
Motivo: El documento es el punto central de navegación del sistema; un error de
trazabilidad o nomenclatura ahí se propaga a todos los documentos que lo referencian.
Nivel de riesgo final: Nivel 1 — Bajo
Motivo: La corrección es documental. No crea sistema real, no programa, no conecta
herramientas externas y no ejecuta acciones.
Nivel de autonomía: Nivel 0 — Sin autonomía ejecutiva

---

### Estado final

ROBERT_HOME v0.11 queda como:
Aprobado e integrado

Robert continúa en:
Fase 10 — MVP técnico básico en preparación

Sin programación autorizada.
Sin código real.
Sin conexiones externas.
Sin automatizaciones reales.
Sin agentes autónomos activos.
Sin Fase 11 autorizada.

---

### Siguiente paso

Actualizar:
1. README

Debe reflejar que ROBERT_HOME v0.11 queda aprobado e integrado mediante:
- DECISIÓN #028
- CAMBIO #050

---

### Nota de control

Esta aprobación no modifica el estado operativo de Robert.
Robert continúa en modo documental, manual y supervisado.
Robert no ejecuta acciones importantes sin permiso.

CAMBIO #053 — Integración de ROBERT_CANONICAL_MODEL v0.2

Fecha: 24/08/2026  
Tipo de cambio: Arquitectónico documental / canonicalización conceptual  
Documento afectado: ROBERT_CANONICAL_MODEL.md  
Versión afectada: v0.2  
Estado: Aprobado e integrado  
Decisión relacionada: DECISIÓN #030 — Aprobación de ROBERT_CANONICAL_MODEL v0.2  
Fase relacionada: Fase 10 — MVP técnico básico en preparación

---

### Descripción del cambio

Se integra `ROBERT_CANONICAL_MODEL v0.2` en `09_ARCHITECTURE` como fuente conceptual canónica de los conceptos fundamentales de Robert.

---

### Alcance autorizado

Este cambio autoriza únicamente:

- añadir `09_ARCHITECTURE/ROBERT_CANONICAL_MODEL.md`;
- marcar v0.2 como aprobada y canónica;
- registrar DECISIÓN #030 y CAMBIO #053;
- añadir referencias mínimas de integración;
- actualizar la taxonomía documental para distinguir Models de Tools;
- preparar como siguiente documento `ROBERT_ORCHESTRATOR_SPEC v0.1`.

---

### Cambios conceptuales integrados

1. `Model ≠ Tool`.
2. `Agent ≠ Skill`.
3. `Agent ≠ Module`.
4. `Context ≠ Memory`.
5. `Proposal ≠ Decision`.
6. `Decision ≠ Change`.
7. `Permission ≠ Scope`.
8. `Risk ≠ Conflict`.
9. Memory se clasifica por Retention y Memory Type.
10. Orchestration queda subordinada a Capa 2 — Control / Protocolo Canónico de Control.

---

### Alcance no autorizado

No se autoriza:

- programación;
- código real;
- ejecución real;
- automatizaciones reales;
- conexiones externas;
- agentes autónomos;
- memoria automática;
- despliegue;
- Fase 11.

---

### Riesgo

Nivel de riesgo inicial: Nivel 3 — Alto / Arquitectónico.  
Nivel de riesgo residual: Nivel 2 — Medio / Documental.  
Nivel de autonomía: Nivel 0 — Sin autonomía ejecutiva.

El riesgo se reduce porque la integración es documental, mantiene las specs técnicas vigentes y no activa capacidades reales.

---

### Estado final

```text
ROBERT_CANONICAL_MODEL
Version: 0.2

CAMBIO #053 — Integración de ROBERT_CANONICAL_MODEL v0.2

Fecha: 24/08/2026
Tipo de cambio: Arquitectónico documental / canonicalización conceptual
Documento afectado: ROBERT_CANONICAL_MODEL.md
Versión afectada: v0.2
Estado: Aprobado e integrado
Decisión relacionada: DECISIÓN #030 — Aprobación de ROBERT_CANONICAL_MODEL v0.2
Fase relacionada: Fase 10 — MVP técnico básico en preparación

---

### Descripción del cambio

Se integra `ROBERT_CANONICAL_MODEL v0.2` en `09_ARCHITECTURE` como fuente conceptual canónica de los conceptos fundamentales de Robert.

---

### Alcance autorizado

Este cambio autoriza únicamente:

* añadir `09_ARCHITECTURE/ROBERT_CANONICAL_MODEL.md`;
* marcar v0.2 como aprobada y canónica;
* registrar DECISIÓN #030 y CAMBIO #053;
* añadir referencias mínimas de integración;
* actualizar la taxonomía documental para distinguir Models de Tools;
* preparar como siguiente documento `ROBERT_ORCHESTRATOR_SPEC v0.1`.

---

### Cambios conceptuales integrados

1. `Model ≠ Tool`.
2. `Agent ≠ Skill`.
3. `Agent ≠ Module`.
4. `Context ≠ Memory`.
5. `Proposal ≠ Decision`.
6. `Decision ≠ Change`.
7. `Permission ≠ Scope`.
8. `Risk ≠ Conflict`.
9. Memory se clasifica por Retention y Memory Type.
10. Orchestration queda subordinada a Capa 2 — Control / Protocolo Canónico de Control.

---

### Alcance no autorizado

No se autoriza:

* programación;
* código real;
* ejecución real;
* automatizaciones reales;
* conexiones externas;
* agentes autónomos;
* memoria automática;
* despliegue;
* Fase 11.

---

### Riesgo

Nivel de riesgo inicial: Nivel 3 — Alto / Arquitectónico.
Nivel de riesgo residual: Nivel 2 — Medio / Documental.
Nivel de autonomía: Nivel 0 — Sin autonomía ejecutiva.

El riesgo se reduce porque la integración es documental, mantiene las specs técnicas vigentes y no activa capacidades reales.

---

### Estado final

```text
ROBERT_CANONICAL_MODEL
Version: 0.2
Status: APPROVED
Authority: CANONICAL
Decision: #030
Change: #053
```

Robert continúa en Fase 10, modo documental, manual y supervisado.

---

### Siguiente paso

Preparar `ROBERT_ORCHESTRATOR_SPEC v0.1` como especificación formal y evolución de la Capa 2 — Control existente.

---

Status: APPROVED
Authority: CANONICAL
Decision: #030
Change: #053

CAMBIO #054 — Integración de ROBERT_ORCHESTRATOR_SPEC v0.1

Fecha: 24/08/2026
Tipo de cambio: Arquitectónico documental / formalización de orquestación
Documento afectado: ROBERT_ORCHESTRATOR_SPEC.md
Versión afectada: v0.1
Estado: Aprobado e integrado
Decisión relacionada: DECISIÓN #031 — Aprobación de ROBERT_ORCHESTRATOR_SPEC v0.1
Fase relacionada: Fase 10 — MVP técnico básico en preparación

---

### Descripción del cambio

Se integra `ROBERT_ORCHESTRATOR_SPEC v0.1` en `09_ARCHITECTURE` como especificación arquitectónica oficial de la orquestación de Robert.

El documento formaliza y especializa la Capa 2 — Control y el Protocolo Canónico de Control existentes.

---

### Alcance autorizado

Este cambio autoriza únicamente:

* añadir `09_ARCHITECTURE/ROBERT_ORCHESTRATOR_SPEC.md`;
* marcar v0.1 como aprobada;
* registrar DECISIÓN #031 y CAMBIO #054;
* establecer formalmente el Orchestrator como especialización de Capa 2 — Control;
* documentar routing conceptual para Modules, Agents, Skills, Models y Tools;
* documentar Permission / Scope Check;
* documentar Risk Check;
* documentar Conflict Check;
* documentar Approval Gate;
* documentar Validation;
* documentar Audit Output;
* preparar `ROBERT_AGENT_ARCHITECTURE v0.1`.

---

### Cambios arquitectónicos integrados

1. Se formaliza `ROBERT_ORCHESTRATOR`.
2. Se mantiene `ROBERT ≠ ORCHESTRATOR`.
3. Se mantiene `ORCHESTRATOR ≠ AUTHORITY`.
4. El Orchestrator especializa la Capa 2 — Control.
5. Se formaliza `Intent Router`.
6. Se formaliza `Context Resolver`.
7. Se formaliza `Module Router`.
8. Se documenta `Agent Router`.
9. Se documenta `Skill Resolver`.
10. Se documenta `Model Router`.
11. Se documenta `Tool Resolver`.
12. Se formalizan checks de Permission, Scope, Risk y Conflict.
13. Se formalizan Approval Gate, Validator y Audit Output.
14. Se introducen niveles conceptuales de Orchestration.
15. Se documenta la posibilidad futura de Multi-Model Routing.

---

### Restricciones

El Orchestrator no puede:

* modificar Security Rules;
* crear sus propios Permissions;
* ampliar Scope silenciosamente;
* autoaprobar Actions de riesgo;
* convertir Proposal en Decision;
* ocultar Conflicts;
* alterar el Canonical Model sin Change Control;
* ejecutar Tools sin autorización válida.

---

### Alcance no autorizado

No se autoriza:

* routing automático real;
* programación de producción;
* autonomía;
* ejecución externa automática;
* Agents autónomos;
* Skills ejecutables;
* memoria automática;
* Model Router automático;
* Tool Router automático;
* conexiones externas nuevas;
* comunicación automática Claude ↔ ChatGPT;
* avance automático a Fase 11.

---

### Riesgo

Nivel de riesgo inicial: Nivel 3 — Alto / Arquitectónico.
Nivel de riesgo residual: Nivel 2 — Medio / Documental.
Nivel de autonomía: Nivel 0 — Sin autonomía ejecutiva.

El riesgo residual se mantiene limitado porque la integración continúa siendo conceptual, documental, manual y supervisada.

---

### Estado final

```text
ROBERT_ORCHESTRATOR_SPEC
Version: 0.1
Status: APPROVED
Decision: #031
Change: #054
Phase: 10
Execution: NONE
Autonomy: NONE
```

---

### Siguiente paso

Integrar las referencias mínimas del Orchestrator y posteriormente preparar:

```text
ROBERT_AGENT_ARCHITECTURE v0.1
```

---

CAMBIO #055 — Integración de ROBERT_AGENT_ARCHITECTURE v0.1

Fecha: 24/08/2026
Tipo de cambio: Arquitectónico documental / formalización de Agents
Documento afectado: ROBERT_AGENT_ARCHITECTURE.md
Versión afectada: v0.1
Estado: Aprobado e integrado
Decisión relacionada: DECISIÓN #032 — Aprobación de ROBERT_AGENT_ARCHITECTURE v0.1
Fase relacionada: Fase 10 — MVP técnico básico en preparación

---

### Descripción del cambio

Se integra `ROBERT_AGENT_ARCHITECTURE v0.1` en `09_ARCHITECTURE` como arquitectura oficial documental y conceptual de Agents dentro de Robert.

La integración formaliza la relación entre:

* Orchestrator;
* Modules;
* Agents;
* Skills;
* Models;
* Tools;
* Permissions;
* Scopes;
* Risk;
* Approval;
* Validation;
* Audit.

---

### Alcance autorizado

Este cambio autoriza únicamente:

* añadir e integrar `09_ARCHITECTURE/ROBERT_AGENT_ARCHITECTURE.md`;
* marcar v0.1 como `APPROVED`;
* registrar DECISIÓN #032 y CAMBIO #055;
* reconocer documentalmente el catálogo inicial de Agents;
* formalizar reglas de Agent Routing;
* formalizar Capability Request;
* formalizar Primary y Supporting Agents;
* formalizar reglas de Handoff;
* formalizar Structured Context Transfer;
* formalizar límites de Permission, Scope y Risk;
* formalizar reglas de Validation y Escalation;
* preparar `ROBERT_SKILL_ARCHITECTURE v0.1`.

---

### Catálogo inicial integrado

Se reconoce documentalmente:

```text id="8zlfkj"
ROBERT_ARCHITECT
ROBERT_RESEARCHER
ROBERT_CRITIC
ROBERT_SECURITY
ROBERT_MEMORY
ROBERT_CODER
ROBERT_TESTER
ROBERT_STRATEGIST
```

Estado operativo del catálogo:

```text id="6jjp9z"
DOCUMENTAL
CONCEPTUAL
MANUAL
SUPERVISED
```

Los Agents no quedan implementados ni activos por este cambio.

---

### Distinciones arquitectónicas integradas

```text id="x6n29y"
AGENT ≠ MODEL
AGENT ≠ SKILL
AGENT ≠ TOOL
AGENT ≠ MODULE
AGENT ≠ USER
AGENT ≠ ROBERT
```

También se integra:

```text id="h3zy9u"
AGENT REQUEST ≠ DIRECT INVOCATION
```

Por tanto, la necesidad de una capacidad deberá expresarse mediante:

```text id="hgih4u"
AGENT
  ↓
CAPABILITY REQUEST
  ↓
ORCHESTRATOR
  ↓
SKILL / MODEL / TOOL RESOLUTION
```

---

### Ownership

Cuando participen varios Agents:

* deberá existir un `Primary Agent`;
* podrán existir `Supporting Agents`;
* el Orchestrator conserva la autoridad de routing;
* el Agent no puede autoasignarse autoridad sobre otra área;
* compartir Skills no implica compartir ownership.

---

### Agent Communication

Se integra como flujo preferido:

```text id="dy993u"
Agent A
  ↓
structured output
  ↓
ORCHESTRATOR
  ↓
authorized context
  ↓
Agent B
```

No se autoriza comunicación autónoma Agent-to-Agent.

---

### Handoff

Un Agent podrá solicitar conceptualmente:

```text id="92ymxv"
HANDOFF_REQUIRED
```

pero:

```text id="grng7a"
HANDOFF RECOMMENDATION ≠ ROUTING AUTHORITY
```

El Orchestrator determina el siguiente destino.

---

### Permission y Scope

Los Agents quedan sujetos a:

```text id="awfnmd"
PERMISSION
SCOPE
RISK LIMIT
APPROVAL REQUIREMENTS
```

Un Permission no implica Scope ilimitado.

Una capacidad documentada no implica autorización de ejecución.

---

### Risk

Durante Fase 10 se mantiene:

```text id="gvvzdc"
EXECUTION_RISK_LIMIT = 0
```

para Agents fuera de Sandbox o simulaciones explícitamente autorizadas.

Los Agents pueden analizar o recomendar sobre niveles de Risk superiores sin adquirir autoridad de ejecución.

---

### Lifecycle

Los estados descritos en `ROBERT_AGENT_ARCHITECTURE v0.1` permanecen como candidatos conceptuales.

Este cambio no crea todavía una state machine técnica oficial para Agents.

---

### Restricciones

Ningún Agent puede:

```text id="jzs6vz"
BYPASS SECURITY
CREATE PERMISSIONS
EXPAND SCOPE
SELF-APPROVE
ALTER PHASE
ALTER CANONICAL MODEL
HIDE CONFLICT
EXECUTE OUTSIDE AUTHORITY
BYPASS ORCHESTRATOR ROUTING
```

---

### Alcance no autorizado

Este cambio no autoriza:

* ejecución autónoma;
* Agents persistentes;
* routing automático real;
* Tool access automático;
* Memory writes automáticos;
* Agent-to-Agent messaging autónomo;
* self-modification;
* self-replication;
* self-approval;
* programación de producción;
* conexiones externas nuevas;
* avance automático a Fase 11.

---

### Riesgo

Nivel de riesgo inicial: Nivel 3 — Alto / Arquitectónico.
Nivel de riesgo residual: Nivel 2 — Medio / Documental.
Nivel de autonomía: Nivel 0 — Sin autonomía ejecutiva.

El riesgo residual permanece limitado porque la integración continúa siendo documental y conceptual.

---

### Estado final

```text id="uuv7ki"
ROBERT_AGENT_ARCHITECTURE
Version: 0.1
Status: APPROVED
Decision: #032
Change: #055
Phase: 10
Implementation: NONE
Execution: NONE
Autonomy: NONE
```

---

### Siguiente paso

1. Cambiar el encabezado de `ROBERT_AGENT_ARCHITECTURE.md` de `PROPUESTA` a `APROBADO`.
2. Actualizar referencias mínimas en `ROBERT_ORCHESTRATOR_SPEC` y `README`.
3. Realizar revisión final de consistencia.
4. Preparar `ROBERT_SKILL_ARCHITECTURE v0.1`.

---
CAMBIO #056 — Separación de Risk, Autonomy y Execution Authority en Agent Architecture

Fecha: 24/08/2026
Tipo de cambio: Corrección de consistencia arquitectónica
Documento afectado: ROBERT_AGENT_ARCHITECTURE.md
Versión afectada: v0.1
Estado: Aprobado e integrado
Decisión relacionada: DECISIÓN #032 — Aprobación de ROBERT_AGENT_ARCHITECTURE v0.1
Cambio previo relacionado: CAMBIO #055 — Integración de ROBERT_AGENT_ARCHITECTURE v0.1
Fase relacionada: Fase 10 — MVP técnico básico en preparación

---

### Descripción del cambio

Se corrige `ROBERT_AGENT_ARCHITECTURE v0.1` para separar formalmente los conceptos de:

```text
RISK
AUTONOMY
EXECUTION AUTHORITY
```

La corrección evita interpretar un nivel bajo de Risk como autorización de ejecución.

---

### Motivo

La revisión final de consistencia detectó que expresiones como:

```text
EXECUTION_RISK_LIMIT = 0
```

podían interpretarse como si un Agent tuviera capacidad de ejecución cuando el Risk fuera 0.

Esto contradice los principios de seguridad vigentes de Robert, donde:

```text
RISK ≠ AUTONOMY
RISK ≠ AUTHORIZATION
```

y durante Fase 10 no existe autonomía ejecutiva activa.

---

### Corrección aplicada

Se reemplaza la relación anterior basada en límites de Risk de ejecución por:

```text
AUTONOMY_LEVEL = 0
EXECUTION_AUTHORITY = NONE
```

para todos los Agents durante Fase 10.

---

### Reglas resultantes

Se formalizan las siguientes distinciones:

```text
RISK ≠ PERMISSION

RISK ≠ AUTONOMY

RISK ≠ EXECUTION AUTHORITY

PERMISSION ≠ EXECUTION AUTHORITY

LOW RISK ≠ AUTHORIZED EXECUTION

HIGH RISK ≠ INABILITY TO ANALYZE
```

---

### Política de Risk

Risk continúa clasificando:

* impacto;
* sensibilidad;
* peligrosidad;
* incertidumbre;
* posible efecto de una Task, Proposal o Action.



Risk puede influir en:

* Validation;
* Escalation;
* Approval;
* Security Review;
* Conflict Review.

Risk no concede ejecución.

---

### Política de Autonomy

Autonomy representa el nivel autorizado de actuación independiente.

Durante Fase 10:

```text
AUTONOMY_LEVEL = 0
```

para todos los Agents.

Esto mantiene a los Agents en estado:

```text
DOCUMENTAL
CONCEPTUAL
MANUAL
SUPERVISED
```

---

### Política de Execution Authority

Execution Authority representa la capacidad explícita de producir efectos ejecutivos reales.

Durante Fase 10:

```text
EXECUTION_AUTHORITY = NONE
```

para todos los Agents.

Esto se mantiene aunque:

* Risk sea 0;
* exista Permission;
* exista una Tool;
* un Model recomiende ejecutar;
* el Agent tenga Confidence elevada.

---

### Requisitos para ejecución futura

Una futura capacidad ejecutiva deberá depender como mínimo de:

```text
PERMISSION
+
SCOPE
+
AUTONOMY
+
EXECUTION AUTHORITY
+
RISK EVALUATION
+
APPROVAL WHEN REQUIRED
```

Ninguno de estos elementos sustituye automáticamente a los demás.

---

### Agent Manifest

La estructura conceptual de Risk queda separada de Autonomy y Execution:

```yaml
risk:
  analysis_range:
  recommendation_range:
  escalation_threshold:

autonomy:
  level:

execution:
  authority:
```

Durante Fase 10:

```yaml
autonomy:
  level: 0

execution:
  authority: NONE
```

---

### Impacto

Este cambio:

* no crea nuevos Agents;
* no cambia el catálogo aprobado;
* no modifica DECISIÓN #032;
* no cambia el Orchestrator;
* no activa Tools;
* no activa ejecución;
* no activa autonomía;
* no cambia Phase.

Únicamente corrige la consistencia semántica y de seguridad de `ROBERT_AGENT_ARCHITECTURE v0.1`.

---

### Alcance no autorizado

No se autoriza:

* ejecución autónoma;
* Tool access automático;
* Agent loops;
* Agent-to-Agent messaging autónomo;
* modificación automática;
* autoaprobación;
* creación automática de Permissions;
* creación automática de Scope;
* creación automática de Autonomy;
* creación automática de Execution Authority;
* avance automático a Fase 11.

---

### Riesgo

Nivel de riesgo del cambio: Nivel 1 — Bajo / Corrección documental.

Nivel de autonomía:

```text
0
```

Execution Authority:

```text
NONE
```

---

### Estado final

```text
ROBERT_AGENT_ARCHITECTURE
Version: 0.1
Status: APPROVED
Decision: #032
Integration Change: #055
Consistency Change: #056
Phase: 10
Implementation: NONE
Autonomy Level: 0
Execution Authority: NONE
```

---

### Siguiente paso

Preparar:

```text
ROBERT_SKILL_ARCHITECTURE v0.1
```

como siguiente pieza arquitectónica dependiente de Agent Architecture y Orchestrator.

---
CAMBIO #057 — Integración de ROBERT_SKILL_ARCHITECTURE v0.1

Fecha: 25/08/2026
Tipo de cambio: Arquitectónico documental / formalización de Skills
Documento afectado: `ROBERT_SKILL_ARCHITECTURE.md`
Versión afectada: v0.1
Estado: APROBADO E INTEGRADO
Decisión relacionada: DECISIÓN #033 — Aprobación de `ROBERT_SKILL_ARCHITECTURE v0.1`
Fase relacionada: Fase 10 — MVP técnico básico en preparación

---

### Descripción del cambio

Se integra `09_ARCHITECTURE/ROBERT_SKILL_ARCHITECTURE.md` como arquitectura documental vigente para Skills dentro de Robert.

La integración formaliza:

* definición de Skill;
* Skill Contract;
* Skill Resolver;
* Capability Request;
* reutilización;
* composición;
* Skill Registry;
* requisitos de Model;
* requisitos de Tool;
* requisitos de Permission y Scope;
* Risk;
* Evidence;
* Sources;
* Validation;
* Failure Modes;
* Fallback;
* observabilidad futura.

---

### Alcance autorizado

Este cambio autoriza documentalmente:

* integrar `ROBERT_SKILL_ARCHITECTURE v0.1`;
* marcarla como `APPROVED`;
* reconocer el catálogo inicial de Skills;
* reconocer las categorías iniciales;
* reconocer `ROBERT_SKILL_REGISTRY` como concepto arquitectónico;
* formalizar Skill Contract;
* formalizar Skill Composition;
* formalizar Skill Reuse;
* formalizar Skill Requirements;
* formalizar Evidence y Source requirements;
* actualizar referencias arquitectónicas mínimas;
* preparar `ROBERT_MODEL_INTERFACE_SPEC v0.1`.

---

### Distinciones integradas

Se integran formalmente:

```text
SKILL ≠ AGENT
SKILL ≠ MODEL
SKILL ≠ TOOL
SKILL ≠ MODULE
SKILL ≠ COMMAND
SKILL ≠ ROBERT
```

Y:

```text
AGENT = quién trabaja
SKILL = cómo trabaja
MODEL = quién procesa
TOOL = con qué interactúa
ORCHESTRATOR = quién coordina
ROBERT = quién gobierna
```

---

### Capability Request

Se formaliza el flujo:

```text
AGENT
  ↓
CAPABILITY REQUEST
  ↓
ORCHESTRATOR
  ↓
SKILL RESOLVER
  ↓
SKILL
```

Regla:

```text
AGENT REQUEST ≠ SKILL EXECUTION AUTHORITY
```

---

### Skill Requirements

Las Skills pueden declarar requisitos de:

```text
MODEL
TOOL
PERMISSION
SCOPE
EVIDENCE
SOURCE
VALIDATION
```

pero:

```text
SKILL DECLARES REQUIREMENTS
        ≠
SKILL OWNS AUTHORIZATION
```

Y:

```text
SKILL REQUIREMENT ≠ PERMISSION
SKILL REQUIREMENT ≠ SCOPE
TOOL REQUIREMENT ≠ TOOL AUTHORIZATION
```

---

### Skill Composition

Se integra:

```text
COMPOSITION ≠ ROUTING AUTHORITY
```

Una Composite Skill puede definir:

* dependencias;
* procedimiento;
* secuencia lógica.

No puede:

* asignar Agents;
* seleccionar unilateralmente Models;
* conceder Tool access;
* ampliar Scope;
* aprobar Actions;
* sustituir al Orchestrator.

---

### Skill Registry

Se integra conceptualmente:

```text
ROBERT_SKILL_REGISTRY
```

con la regla:

```text
ONE CAPABILITY
      ↓
ONE PRIMARY SKILL DEFINITION
```

cuando sea razonablemente posible.

Antes de crear una Skill nueva deberán revisarse:

1. equivalencia;
2. solapamiento;
3. reutilización;
4. composición;
5. necesidad real de nueva capacidad.

---

### Evidence y Sources

Se integra la separación:

```text
SOURCE
CLAIM
EVIDENCE
INTERPRETATION
```

Y:

```text
SOURCE ≠ CLAIM
CLAIM ≠ EVIDENCE
EVIDENCE ≠ INTERPRETATION
```

Las políticas técnicas completas quedan pendientes de futuras especificaciones.

---

### Risk, Autonomy y Execution Authority

Se mantiene:

```text
RISK ≠ PERMISSION
RISK ≠ AUTONOMY
RISK ≠ EXECUTION AUTHORITY
```

Durante Fase 10:

```text
AUTONOMY_LEVEL = 0
EXECUTION_AUTHORITY = NONE
```

para el uso operativo de Skills.

---

### Catálogo inicial

Se reconoce documentalmente el catálogo inicial agrupado en:

```text
ANALYSIS
RESEARCH
ARCHITECTURE
SECURITY
MEMORY
CODE
TESTING
STRATEGY
VALIDATION
DOCUMENTATION
```

El catálogo continúa siendo provisional y podrá depurarse antes de v1.0.

---

### Restricciones

Este cambio no autoriza:

* Skill execution autónoma;
* Tool invocation automática;
* Memory writes automáticos;
* creación automática de Permissions;
* Scope expansion;
* creación de Autonomy;
* creación de Execution Authority;
* routing autónomo;
* self-modification;
* loops autónomos;
* acciones externas automáticas;
* avance automático a Fase 11.

---

### Riesgo

Nivel de riesgo inicial: Nivel 3 — Arquitectónico.

Nivel de riesgo residual: Nivel 2 — Documental.

Autonomía:

```text
0
```

Execution Authority:

```text
NONE
```

---

### Estado final

```text
ROBERT_SKILL_ARCHITECTURE
Version: 0.1
Status: APPROVED
Decision: #033
Change: #057
Phase: 10
Implementation: NONE
Autonomy Level: 0
Execution Authority: NONE
```

---

### Siguiente paso

1. Actualizar el propio `ROBERT_SKILL_ARCHITECTURE.md` a `APPROVED`.
2. Actualizar referencias mínimas en Orchestrator, Agent Architecture y README.
3. Ejecutar revisión final de consistencia.
4. Preparar `ROBERT_MODEL_INTERFACE_SPEC v0.1`.

---

CAMBIO #058 — Corrección de ownership de Autonomy, Execution Authority y Skill Requesters

Fecha: 25/08/2026
Tipo de cambio: Corrección de consistencia arquitectónica
Documento afectado: `ROBERT_SKILL_ARCHITECTURE.md`
Versión afectada: v0.1
Estado: APROBADO E INTEGRADO
Decisión relacionada: DECISIÓN #033 — Aprobación de `ROBERT_SKILL_ARCHITECTURE v0.1`
Cambio previo relacionado: CAMBIO #057 — Integración de `ROBERT_SKILL_ARCHITECTURE v0.1`
Fase relacionada: Fase 10 — MVP técnico básico en preparación

---

### Descripción del cambio

Se corrige `ROBERT_SKILL_ARCHITECTURE v0.1` para separar formalmente la Skill del ownership de:

```text
AUTONOMY
EXECUTION AUTHORITY
```

y para generalizar el origen válido de una solicitud de Skill mediante el concepto:

```text
AUTHORIZED REQUESTER
```

sin transferir autoridad de routing fuera del Orchestrator.

---

### Motivo

La revisión final de consistencia detectó dos ambigüedades:

1. El Skill Manifest incluía:

```text
autonomy
execution authority
```

como si fueran propiedades propias de una Skill.

2. El flujo principal implicaba que toda Skill debía ser solicitada necesariamente por un Agent, aunque componentes autorizados como Validator u Orchestrator puedan necesitar procedimientos reutilizables.

---

### Corrección 1 — Ownership de Autonomy

Se formaliza:

```text
SKILL ≠ AUTONOMOUS ACTOR
SKILL DOES NOT OWN AUTONOMY
```

Autonomy pertenece al contexto operativo autorizado del sistema y, cuando corresponda, al actor operativo que participa en una Task.

Durante Fase 10:

```text
PHASE 10 OPERATIONAL CONTEXT:
AUTONOMY_LEVEL = 0
```

Esto no constituye una propiedad interna de la Skill.

---

### Corrección 2 — Ownership de Execution Authority

Se formaliza:

```text
SKILL DOES NOT OWN EXECUTION AUTHORITY
```

Una Skill únicamente puede describir procedimientos que potencialmente requieran una Action o efecto externo.

La autorización de ejecución deberá resolverse mediante el contexto operativo autorizado y al menos:

```text
PERMISSION
+
SCOPE
+
EXECUTION AUTHORITY
+
RISK EVALUATION
+
APPROVAL WHEN REQUIRED
```

Durante Fase 10:

```text
PHASE 10 OPERATIONAL CONTEXT:
EXECUTION_AUTHORITY = NONE
```

Por tanto:

```text
ACTION PROCEDURE ≠ AUTHORIZED ACTION
```

---

### Skill Manifest actualizado

Se elimina del manifest conceptual:

```yaml
autonomy:
  level:

execution:
  authority:
```

como propiedades de la Skill.

Se reemplaza por:

```yaml
authorization_requirements:
  permissions:
  scopes:
  approval:

operational_constraints:
  external_effects_allowed:
```

La Skill puede declarar requisitos o restricciones.

No posee la autorización resultante.

---

### Corrección 3 — Authorized Requester

Se generaliza el flujo de solicitud de capacidades.

Arquitectura general:

```text
AUTHORIZED REQUESTER
        ↓
CAPABILITY REQUEST
        ↓
ORCHESTRATOR
        ↓
SKILL RESOLVER
        ↓
SKILL
```

Conceptualmente, un `AUTHORIZED REQUESTER` puede ser:

```text
AGENT
OR
VALIDATOR
OR
AUTHORIZED ROBERT COMPONENT
```

según la arquitectura vigente y el contexto autorizado.

---

### Caso específico de Agent

Se mantiene como flujo válido:

```text
AGENT
  ↓
CAPABILITY REQUEST
  ↓
ORCHESTRATOR
  ↓
SKILL RESOLVER
  ↓
SKILL
```

Esta corrección no elimina ni modifica el mecanismo de Agent Capability Request.

---

### Routing Authority

Se formalizan:

```text
AUTHORIZED REQUESTER ≠ ROUTING AUTHORITY
```

y:

```text
SKILL REQUEST ≠ DIRECT SKILL INVOCATION
```

El Orchestrator conserva la autoridad para resolver:

* Skill;
* Model;
* Tool;
* contexto;
* Permission;
* Scope;
* Risk;
* Approval;
* Validation.

---

### Composite Skills

Se mantiene:

```text
COMPOSITION ≠ ROUTING AUTHORITY
```

Una Composite Skill tampoco adquiere autoridad de routing como consecuencia de esta corrección.

---

### Impacto arquitectónico

Este cambio mejora la separación entre:

```text
PROCEDURE
ACTOR
AUTHORIZATION
ROUTING
```

quedando:

```text
SKILL = PROCEDURE

AUTHORIZED REQUESTER = ACTOR OR COMPONENT REQUESTING CAPABILITY

ORCHESTRATOR = ROUTING AUTHORITY

OPERATIONAL CONTEXT = AUTHORIZATION STATE
```

---

### Invariantes resultantes

Se integran:

```text
SKILL ≠ AGENT
SKILL ≠ MODEL
SKILL ≠ TOOL
SKILL ≠ MODULE
SKILL ≠ AUTONOMOUS ACTOR

SKILL REQUIREMENT ≠ PERMISSION
SKILL REQUIREMENT ≠ SCOPE

SKILL DOES NOT OWN AUTONOMY
SKILL DOES NOT OWN EXECUTION AUTHORITY

AUTHORIZED REQUESTER ≠ ROUTING AUTHORITY
SKILL REQUEST ≠ DIRECT SKILL INVOCATION

COMPOSITION ≠ ROUTING AUTHORITY

RISK ≠ AUTONOMY
RISK ≠ EXECUTION AUTHORITY
```

---

### Restricciones

Este cambio no autoriza:

* Skills autónomas;
* acceso directo de Requesters a Skills fuera del Orchestrator;
* Tool invocation automática;
* Model invocation automática;
* Memory writes automáticos;
* creación de Permissions;
* creación o expansión de Scope;
* creación de Autonomy;
* creación de Execution Authority;
* routing paralelo;
* self-modification;
* ejecución externa automática;
* avance automático a Fase 11.

---

### Riesgo

Nivel de riesgo del cambio:

```text
Nivel 1 — Bajo / Corrección documental de consistencia
```

Contexto operativo:

```text
AUTONOMY_LEVEL = 0
EXECUTION_AUTHORITY = NONE
```

---

### Estado final

```text
ROBERT_SKILL_ARCHITECTURE
Version: 0.1
Status: APPROVED
Decision: #033
Integration Change: #057
Consistency Change: #058
Phase: 10
Implementation: NONE
Operational Autonomy: 0
Operational Execution Authority: NONE
```

---

### Siguiente paso

Con esta corrección registrada, `ROBERT_SKILL_ARCHITECTURE v0.1` queda cerrada a nivel arquitectónico documental.

El siguiente documento es:

```text
ROBERT_MODEL_INTERFACE_SPEC v0.1
```

Su objetivo será definir una interfaz uniforme entre Robert y:

```text
Claude
ChatGPT
futuros Models
```

sin acoplar Agents o Skills directamente a un proveedor.

CAMBIO #059 — Integración de ROBERT_MODEL_INTERFACE_SPEC v0.1

Fecha: 25/08/2026
Tipo de cambio: Arquitectónico documental / formalización de Model Interface
Documento afectado: `ROBERT_MODEL_INTERFACE_SPEC.md`
Versión afectada: v0.1
Estado: APROBADO E INTEGRADO
Decisión relacionada: DECISIÓN #034 — Aprobación de `ROBERT_MODEL_INTERFACE_SPEC v0.1`
Fase relacionada: Fase 10 — MVP técnico básico en preparación

---

### Descripción del cambio

Se integra `09_ARCHITECTURE/ROBERT_MODEL_INTERFACE_SPEC.md` como arquitectura documental vigente para la relación entre Robert y Models.

La integración formaliza:

```text
MODEL ROUTER
MODEL INTERFACE
MODEL ADAPTER
MODEL REGISTRY
MODEL PROFILE
MODEL RUNTIME STATE
MODEL REQUEST
MODEL RESPONSE
MODEL FALLBACK
MULTI-MODEL MEDIATION
```

---

### Alcance autorizado

Este cambio autoriza documentalmente:

* integrar `ROBERT_MODEL_INTERFACE_SPEC v0.1`;
* reconocerla como `APPROVED`;
* formalizar Model Router;
* formalizar Model Interface;
* formalizar Provider Adapters;
* formalizar Model Registry;
* formalizar Model Profile;
* formalizar Model Runtime State;
* formalizar contratos Model Request / Response;
* formalizar capability-based Model selection;
* formalizar fallback conceptual;
* formalizar multi-model mediation;
* formalizar Tool boundaries;
* formalizar Provider Independence;
* preparar `ROBERT_MEMORY_ARCHITECTURE v0.1`.

---

### Separación integrada

Se formaliza:

```text
ORCHESTRATOR
= routing authority

MODEL ROUTER
= model selection

MODEL INTERFACE
= common contract

MODEL ADAPTER
= provider translation

MODEL
= intelligence processing
```

---

### Distinciones

Se integran:

```text
MODEL ≠ AGENT
MODEL ≠ SKILL
MODEL ≠ TOOL
MODEL ≠ MODULE
MODEL ≠ ORCHESTRATOR
MODEL ≠ ROBERT
```

---

### Routing

Se integra:

```text
MODEL USE ≠ SKILL REQUIRED
```

y:

```text
SKILL MAY REQUIRE MODEL
```

El Orchestrator mantiene la resolución global de capacidades.

---

### Model Selection

Se integra:

```text
MODEL PREFERENCE ≠ MODEL SELECTION AUTHORITY
```

Agents y Skills podrán expresar requisitos o preferencias.

Model Router conserva la selección efectiva bajo el Orchestrator.

---

### Model Request / Response

Se reconoce conceptualmente:

```text
MODEL_REQUEST
MODEL_RESPONSE
```

como contrato común independiente de proveedor.

Model Response podrá incluir:

```text
result
rationale_summary
evidence
sources
risks
conflicts
confidence
confidence_source
limitations
assumptions
tool_requests
validation_notes
usage
errors
```

---

### Reasoning Boundary

Se formaliza:

```text
RATIONALE SUMMARY ≠ PRIVATE REASONING TRACE
```

y:

```text
MODEL INTERFACE MUST NOT REQUIRE PRIVATE CHAIN OF THOUGHT
```

La arquitectura no dependerá de razonamiento interno privado de los Models.

---

### Adapter Boundary

Se formaliza:

```text
ADAPTER TOOL SUPPORT
≠
TOOL EXECUTION AUTHORITY
```

Los Adapters pueden traducir:

* mensajes;
* roles;
* Tool schemas;
* Tool Requests;
* responses;
* errors;
* usage.

No pueden conceder autoridad.

---

### Tool Boundary

Se integran:

```text
MODEL TOOL REQUEST ≠ TOOL AUTHORIZATION

MODEL TOOL CAPABILITY
≠
ROBERT TOOL AUTHORIZATION
```

Flujo:

```text
MODEL
  ↓
TOOL REQUEST
  ↓
MODEL INTERFACE
  ↓
ORCHESTRATOR
  ↓
TOOL RESOLVER
  ↓
AUTHORIZATION
  ↓
TOOL
```

---

### Model Output

Se formaliza:

```text
MODEL OUTPUT ≠ DECISION
MODEL OUTPUT ≠ TRUTH
```

Los resultados de un Model pueden requerir Validation, Review o Approval.

---

### Multi-Model

Se formaliza:

```text
MODEL-TO-MODEL TRANSFER
MUST BE MEDIATED BY ROBERT
```

y:

```text
MODEL A ≠ AUTHORITY OVER MODEL B

PRIMARY MODEL ≠ ROUTING AUTHORITY

CONSENSUS ≠ TRUTH

CONSENSUS ≠ AUTHORIZATION
```

---

### Model Registry

Se integra conceptualmente:

```text
ROBERT_MODEL_REGISTRY
```

con separación entre:

```text
MODEL PROFILE
```

y:

```text
MODEL RUNTIME STATE
```

Profile puede contener:

```text
identity
provider
family
version
capabilities
limitations
modalities
adapter
```

Runtime State puede contener:

```text
availability
health
latency
cost information
rate limitations
```

---

### Memory Boundary

Se mantiene:

```text
MODEL OUTPUT ≠ MEMORY WRITE
```

Los outputs pueden convertirse en candidatos para evaluación posterior, pero no en Memory persistente automáticamente.

---

### Provider Independence

Se integran:

```text
PROVIDER CHANGE ≠ AGENT REWRITE

PROVIDER CHANGE ≠ SKILL REWRITE
```

Las particularidades del proveedor deben mantenerse contenidas en Model Adapter o metadata cuando sea posible.

---

### Security Invariants

Se integran:

```text
MODEL CANNOT CREATE PERMISSIONS
MODEL CANNOT EXPAND SCOPE
MODEL CANNOT SELF-APPROVE
MODEL CANNOT ALTER PHASE
MODEL CANNOT ALTER CANONICAL MODEL
MODEL CANNOT CREATE AUTONOMY
MODEL CANNOT CREATE EXECUTION AUTHORITY

MODEL TOOL REQUEST ≠ TOOL AUTHORIZATION
MODEL OUTPUT ≠ DECISION
MODEL OUTPUT ≠ TRUTH
```

---

### Fase 10

Durante Fase 10:

```text
MODEL INTERFACE = DOCUMENTAL
MODEL ROUTER = CONCEPTUAL
MODEL REGISTRY = CONCEPTUAL
MODEL RUNTIME STATE = CONCEPTUAL
MODEL ADAPTERS = DESIGN ONLY
```

Contexto operativo:

```text
AUTONOMY_LEVEL = 0
EXECUTION_AUTHORITY = NONE
```

---

### Alcance no autorizado

Este cambio no autoriza:

* routing autónomo productivo;
* Model loops persistentes;
* llamadas API autónomas persistentes;
* Tool execution automática;
* Memory writes automáticos;
* Model-to-Model communication autónoma;
* creación de Permissions;
* creación o expansión de Scope;
* creación de Autonomy;
* creación de Execution Authority;
* self-modification;
* avance automático a Fase 11.

---

### Riesgo

Nivel de riesgo inicial:

```text
Nivel 3 — Arquitectónico
```

Nivel residual:

```text
Nivel 2 — Documental
```

Contexto operativo:

```text
AUTONOMY_LEVEL = 0
EXECUTION_AUTHORITY = NONE
```

---

### Estado final

```text
ROBERT_MODEL_INTERFACE_SPEC
Version: 0.1
Status: APPROVED
Decision: #034
Change: #059
Phase: 10
Implementation: NONE
Operational Autonomy: 0
Operational Execution Authority: NONE
```

---

### Siguiente paso

Con `ROBERT_MODEL_INTERFACE_SPEC v0.1` integrado, el siguiente bloque arquitectónico es:

```text
ROBERT_MEMORY_ARCHITECTURE v0.1
```

para formalizar:

```text
MEMORY CLASSIFICATION
RETENTION
WRITE ELIGIBILITY
RETRIEVAL
PROVENANCE
AUTHORITY
CONFIDENCE
CONFLICTS
UPDATES
EXPIRATION
MODEL ACCESS
AGENT ACCESS
```
# CAMBIO #060 — Aprobación e integración de ROBERT_MEMORY_ARCHITECTURE v0.1

**Fecha:** 31/08/2026
**Tipo:** Arquitectónico documental / Memory Architecture
**Estado:** APROBADO E INTEGRADO
**Decisión relacionada:** DECISIÓN #035
**Documento relacionado:** `09_ARCHITECTURE/ROBERT_MEMORY_ARCHITECTURE.md`
**Versión:** v0.1
**Fase:** 10

## Descripción

Se aprueba e integra formalmente:

```text
ROBERT_MEMORY_ARCHITECTURE v0.1
```

como arquitectura vigente de Memory dentro de Robert.

## Cambios integrados

Se formalizan:

```text
MEMORY TYPES
RETENTION
MEMORY ELIGIBILITY
MEMORY CANDIDATES
MEMORY RETRIEVAL
MEMORY RETRIEVAL SCOPE
PROVENANCE
AUTHORITY METADATA
CONFIDENCE
FRESHNESS
CONFLICT HANDLING
SUPERSESSION
EXPIRATION
FORGET / DELETE
AGENT MEMORY ACCESS
MODEL MEMORY ACCESS
```

Se preservan las dimensiones canónicas:

```text
RETENTION:
ACTIVE
TEMPORARY
PERSISTENT

MEMORY_TYPE:
CORE
SEMANTIC
EPISODIC
DECISIONAL
PROCEDURAL
```

## Correcciones de consistencia incorporadas

La versión aprobada incorpora:

1. `Memory Manifest` declarado explícitamente conceptual y no schema técnico definitivo.
2. `Memory Resolver` subordinado al Orchestrator.
3. `ROBERT_MEMORY` referenciado desde Agent Architecture, no redefinido.
4. `Validator` tratado como función futura de Validation y no como nueva entidad canónica.
5. Separación entre `Memory Authority Metadata` y precedencia global de fuentes.
6. Separación entre `Memory Retrieval Scope` y `Authorized Operational Scope`.
7. Reutilización de Audit Trail existente sin crear un sistema de auditoría paralelo.
8. Alineación conceptual con Permissions & Scopes y Data Consistency.

## Invariantes

```text
MEMORY RESOLVER ≠ INDEPENDENT AUTHORITY

MEMORY CANDIDATE ≠ MEMORY

MODEL OUTPUT ≠ MEMORY WRITE

AGENT OUTPUT ≠ MEMORY WRITE

SKILL OUTPUT ≠ MEMORY WRITE

MEMORY RETRIEVAL SCOPE ≠ AUTHORIZED OPERATIONAL SCOPE

MEMORY AUTHORITY METADATA ≠ GLOBAL SOURCE PRECEDENCE

MEMORY AUDIT REQUIREMENT ≠ NEW AUDIT SYSTEM
```

## Impacto

Se amplía la arquitectura de Robert con una capa formal de Memory sin introducir ejecución productiva.

## Riesgo

**Nivel inicial:** 3 — Alto
**Nivel residual:** 2 — Medio / documental

Motivo:

La arquitectura afecta futura persistencia, recuperación y exposición de información, pero en Fase 10 permanece completamente conceptual y supervisada.

## Restricciones

Este cambio no autoriza:

```text
MEMORY STORE REAL
VECTOR DATABASE REAL
AUTOMATIC MEMORY WRITE
AUTOMATIC MEMORY RETRIEVAL
AUTOMATIC MEMORY DELETION
AUTOMATIC CONFLICT RESOLUTION
MODEL DIRECT MEMORY ACCESS
AGENT DIRECT MEMORY WRITE
SKILL DIRECT MEMORY WRITE
AUTONOMOUS MEMORY MANAGEMENT
```

Se mantiene:

```text
AUTONOMY_LEVEL = 0
EXECUTION_AUTHORITY = NONE
```

## Resultado

```text
ROBERT_MEMORY_ARCHITECTURE v0.1
STATUS: APPROVED
DECISION: #035
CHANGE: #060
```

## Siguiente bloque arquitectónico

```text
ROBERT_VALIDATION_ARCHITECTURE v0.1
```

CAMBIO #061 — Aprobación e integración de ROBERT_VALIDATION_ARCHITECTURE v0.1

Fecha: 31/08/2026
Tipo: Arquitectónico documental / Validation Architecture
Estado: APROBADO E INTEGRADO
Decisión relacionada: DECISIÓN #036
Documento relacionado: 09_ARCHITECTURE/ROBERT_VALIDATION_ARCHITECTURE.md
Versión: v0.1
Fase: 10

Descripción

Se aprueba e integra formalmente:

ROBERT_VALIDATION_ARCHITECTURE v0.1

como arquitectura vigente de Validation dentro de Robert.

Elementos integrados

Se formalizan:

VALIDATION_TYPE
REVIEWER_ROLE
VALIDATION_REQUEST
VALIDATION_RESULT
VALIDATION_STATUS
VALIDATION_RESOLVER
VALIDATION_POLICY
VALIDATION_REGISTRY
VALIDATION DEPTH
MULTI-VALIDATOR REVIEW
VALIDATION CONFLICT RESOLUTION
VALIDATION ESCALATION
Correcciones de consistencia incorporadas

La versión aprobada incorpora:

separación entre VALIDATION_TYPE y REVIEWER_ROLE;
Validator tratado como rol funcional, no nueva entidad canónica;
Validation Resolver subordinado al Orchestrator;
Validation Matrix marcada como ilustrativa y no vinculante;
Validation Registry declarado conceptual, sin routing authority;
reutilización de Agents y Skills existentes;
ausencia de un nuevo ROBERT_VALIDATOR por defecto;
separación estricta entre Validation, Approval y Authorization;
Multi-Validator Consensus sin autoridad de Truth;
integración con Memory, Model Interface, Permissions, Audit y Data Consistency sin crear sistemas paralelos.
Invariantes
VALIDATION_TYPE ≠ REVIEWER_ROLE

VALIDATION ≠ AUTHORIZATION

VALIDATION ≠ APPROVAL

VALIDATION ≠ EXECUTION AUTHORITY

VALIDATED OUTPUT ≠ AUTHORIZED ACTION

VALIDATOR ≠ ROUTING AUTHORITY

VALIDATOR ≠ APPROVAL AUTHORITY

VALIDATION REGISTRY ≠ ROUTING AUTHORITY

VALIDATION REGISTRY ≠ EXECUTION ENGINE

CONSENSUS ≠ TRUTH

CONFIDENCE ≠ TRUTH

VALIDATION RESULT ≠ MEMORY WRITE

VALIDATION TOOL REQUIREMENT ≠ TOOL AUTHORIZATION
Impacto

Robert incorpora una arquitectura formal para evaluar outputs y artifacts sin conceder automáticamente:

AUTHORITY
APPROVAL
PERMISSION
EXECUTION
Riesgo

Nivel inicial: 3 — Alto
Nivel residual: 2 — Medio / documental

Restricciones

Este cambio no autoriza:

AUTOMATED VALIDATION ENGINE
AUTOMATIC APPROVAL
AUTOMATIC AUTHORIZATION
AUTONOMOUS REVIEWER LOOPS
AUTOMATIC TOOL EXECUTION
AUTOMATIC MEMORY WRITE
AUTONOMOUS CANONICAL CHANGES
EXTERNAL EXECUTION

Se mantiene:

AUTONOMY_LEVEL = 0
EXECUTION_AUTHORITY = NONE
Resultado
ROBERT_VALIDATION_ARCHITECTURE v0.1
STATUS: APPROVED
DECISION: #036
CHANGE: #061

# CAMBIO #062 — Aprobación e integración de ROBERT_TOOL_ARCHITECTURE v0.1

**Fecha:** 31/08/2026
**Tipo:** Arquitectónico documental / Tool Architecture
**Estado:** APROBADO E INTEGRADO
**Decisión relacionada:** DECISIÓN #037
**Documento relacionado:** `09_ARCHITECTURE/ROBERT_TOOL_ARCHITECTURE.md`
**Versión:** v0.1
**Fase:** 10

## Descripción

Se aprueba e integra formalmente:

```text
ROBERT_TOOL_ARCHITECTURE v0.1
```

como arquitectura vigente de Tools dentro de Robert.

## Elementos integrados

```text
TOOL REQUEST
TOOL RESULT
TOOL FAILURE
TOOL INTERFACE
TOOL ADAPTER / CONNECTOR
TOOL REGISTRY
TOOL POLICY
ACCESS MODE
SIDE EFFECT CLASS
RETRY / FALLBACK
TOOL SECURITY
TOOL AUDIT
```

## Correcciones incorporadas

La versión aprobada incorpora:

1. `Tool Resolver` confirmado como responsabilidad preexistente del Orchestrator.
2. `Human Confirmation` subordinada al `Approval Gate`.
3. `Tool Adapter / Connector` con Architectural Growth Check.
4. `Security Check` integrado en el flujo principal.
5. separación entre Tool Capability, Permission, Scope, Risk y Execution Authority.
6. prohibición de invocación directa Model→Tool, Agent→Tool y Skill→Tool.
7. Tool Result separado de Truth, Decision, Approval y Memory Write.
8. Tool Registry y Tool Policy sin routing ni approval authority.

## Riesgo

**Nivel inicial:** 3 — Alto
**Nivel residual:** 2 — Medio / documental

## Restricciones

No se autoriza:

```text
REAL TOOL EXECUTION
AUTOMATIC TOOL EXECUTION
AUTONOMOUS MODEL-TO-TOOL LOOPS
AUTONOMOUS AGENT-TO-TOOL LOOPS
AUTONOMOUS TOOL-TO-TOOL CHAINS
AUTOMATIC PERMISSION CREATION
AUTOMATIC SCOPE EXPANSION
AUTOMATIC MEMORY WRITE
PHASE 11
```

Se mantiene:

```text
AUTONOMY_LEVEL = 0
EXECUTION_AUTHORITY = NONE
```

## Resultado

```text
ROBERT_TOOL_ARCHITECTURE v0.1
STATUS: APPROVED
DECISION: #037
CHANGE: #062
```
# CAMBIO #063 — Aprobación e integración de ROBERT_IMPLEMENTATION_CONTRACTS v0.1

**Fecha:** 31/08/2026
**Tipo:** Arquitectónico documental / Implementation Readiness
**Estado:** APROBADO E INTEGRADO
**Decisión relacionada:** DECISIÓN #038
**Documento relacionado:** `09_ARCHITECTURE/ROBERT_IMPLEMENTATION_CONTRACTS.md`
**Versión:** v0.1
**Fase:** 10

## Descripción

Se aprueba e integra formalmente:

ROBERT_IMPLEMENTATION_CONTRACTS v0.1

como capa contractual entre la arquitectura aprobada y la futura implementación técnica de Robert.

## Contratos integrados

TASK
REQUEST_CONTEXT
ORCHESTRATOR_REQUEST
ORCHESTRATOR_RESULT
ROUTE

AGENT_REQUEST
AGENT_RESULT

SKILL_INVOCATION
SKILL_RESULT

MODEL_REQUEST
MODEL_RESPONSE

TOOL_REQUEST
TOOL_RESULT

MEMORY_CANDIDATE
MEMORY_RECORD
MEMORY_RETRIEVAL_REQUEST
MEMORY_RETRIEVAL_RESULT

VALIDATION_REQUEST
VALIDATION_RESULT

PERMISSION_CHECK
SCOPE_CHECK
RISK_ASSESSMENT

APPROVAL_REQUEST
APPROVAL_RESULT

ERROR
BLOCK
AUDIT_EVENT

## Correcciones integradas

Se incorporan las correcciones de revisión adversarial relativas a:

- compatibilidad con Tool Architecture;
- compatibilidad con Memory Architecture;
- compatibilidad con Validation Architecture;
- Execution Authority;
- Route Contract;
- escala oficial de Risk;
- Error and Blocking;
- política de Model Tool Requests.

## Restricciones

Esta aprobación no autoriza:

CODE IMPLEMENTATION
PRODUCTION DATABASE
MODEL API CONNECTION
REAL TOOL EXECUTION
AUTOMATIC MEMORY
AUTONOMOUS AGENTS
AUTOMATIC VALIDATION ENGINE
PHASE 11

Se mantiene:

AUTONOMY_LEVEL = 0
EXECUTION_AUTHORITY = NONE

## Resultado

ROBERT_IMPLEMENTATION_CONTRACTS v0.1
STATUS: APPROVED
DECISION: #038
CHANGE: #063
