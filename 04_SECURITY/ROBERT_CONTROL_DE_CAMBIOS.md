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
