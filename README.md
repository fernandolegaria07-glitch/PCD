# PCD - Reportes de transito (seed: 55)

> **SEMILLA: 55**

## Confusio alguna vez dijo: Todos tenemos dos vidas y la segunda empieza cuando te das cuenta de que solo tienes una

Desarrollo de habilidades para la administración y procesamineto de datos con python

- Persona A: Fernando Legaria Mendoza
- Persona B: Hugo Hernandez Carrillo

Reportes de transito - Analisis de reportes de transito para la mejora en la gestion del trafico

## Estructura del repositorio

- `datos/` - Dataset sintetico compartido por todas las practicas
- `practica1/` a `practica6/` - Codigo y resultados de cada practica
- `proyecto/` - Proyecto final con datos reales

EQUIPO: the sea bros

TEMA: Reportes de Transito

Observaciones Repositorio:
1- No tiene requirements.txt
2- No tiene la carpeta datos/
3- No tiene las carpetas practica1 a practica6 (tiene una carpeta "codigos/" en su lugar)
4- No tiene la carpeta proyecto/
5- Tiene un archivo .DS_Store versionado; deberia estar en .gitignore

---

## Observaciones del profesor

### Práctica 2 — evaluación (27-oct-2026)

**Calificación: 85 / 100**

Entregada el **26-oct-2026 a las 20:29**, dentro del plazo (la entrega cerraba el lun 26-oct), así que no lleva penalización por retraso.

**Lo que destaca:** **Son los únicos que modelaron el problema con clases propias:** `Categorica` y `Numerica`, cada una con sus métodos. Es más de lo que pedía el enunciado (las clases eran opcionales) y es una buena estructura. También son de los que más commits hicieron sobre `practica2/` (9) y vienen de 68 en P1.

**Criterios cubiertos al 100 %:** Nombres exactos de los entregables; Requisitos de Git (3+ commits, rama integrada); Requisitos de código (5 funciones, `lambda`, `map`/`filter`); Encabezado del JSON: archivo, pareja, seed; `valores_unicos_categorica`; `conteo_por_categoria`; `categoria_mas_frecuente`; `top_3_categorias`.

**Observaciones:**

1. Están descartando los **valores negativos** de las columnas numéricas. Reportan `minimo` = 3.0 en `duracion_incidente_min` cuando el mínimo real es **−600.0**, y **97,616** valores válidos en vez de **98,877**. Los outliers negativos son parte del ruido del dataset a propósito y cuentan como válidos: solo se excluye lo vacío y lo no convertible. Eso arrastra el promedio (65.22 en vez de 63.73), la misma situación en `<numerica_2>`, el `promedio_por_categoria` (20 de 21 categorías fuera de tolerancia) y el filtrado (umbral 57.0 en vez de 56.0; 9,313 registros en vez de 9,832). Lo mismo pasa en `vehiculos_afectados`: reportan 1.0 de mínimo cuando el real es **−60.0**.
2. La causa está en `a_float()`, que devuelve **−1** cuando no puede convertir. Ese −1 es un valor numérico, así que entra al análisis como si fuera un dato real. El enunciado pide **descartar** esos valores con `filter()` antes del `map()`, no sustituirlos por un número.

**Desglose:**

| Criterio | Obtenido | Máximo |
|---|:---:|:---:|
| Nombres exactos de los entregables | 10 | 10 |
| Requisitos de Git (3+ commits, rama integrada) | 8 | 8 |
| Requisitos de código (5 funciones, `lambda`, `map`/`filter`) | 12 | 12 |
| Encabezado del JSON: archivo, pareja, seed | 6 | 6 |
| `valores_unicos_categorica` | 10 | 10 |
| `conteo_por_categoria` | 10 | 10 |
| `categoria_mas_frecuente` | 6 | 6 |
| `top_3_categorias` | 8 | 8 |
| `estadisticas_numerica_1` (con mediana) | 6 | 12 |
| `estadisticas_numerica_2` (con mediana) | 4 | 8 |
| `promedio_por_categoria` | 4 | 6 |
| `filtrado` (percentil 90) | 1 | 4 |
| **Total** | **85** | **100** |

### 13-oct-2026 — Correcciones de la Práctica 1

**Calificación de P1: 68 → 90 / 100.**

**Corrigieron sus cuatro observaciones** (commit del 8-oct), el mismo día que recibieron la
retroalimentación:

1. La semilla ya dice **55**.
2. Las primeras 5 filas ya van separadas con la barra con espacios a los lados.
3. La columna categórica ya es **`zona`**, y lo importante: ahora la toman por nombre en el
   código (`columnas.index("zona")`) en vez de detectarla automáticamente. Ese era el fondo
   de la observación, no solo el nombre en la salida.
4. La columna numérica ya es **`duracion_incidente_min`**: 98877 válidos, mínimo -600.0 y
   máximo 6360.0, exacto como la referencia.

De paso quitaron los acentos de los títulos de sección, con lo que el formato quedó igual al
de la solución de referencia.

Su conteo de la columna categórica sigue distinto (14 valores únicos y `Periferico` con
14127, contra 21 y 13831 de la referencia), pero **no se les descuenta**: viene de que en
`resumen.py:51` hacen `.lower().title()` sin `.strip()`, y ese tipo de normalización se dio
por válida para todo el grupo porque el enunciado de P1 no decía cómo normalizar. Ténganlo
presente para P4 y P5.

**Cómo se aplicó el reconocimiento.** Nueve de los diez equipos que tenían observaciones las atendieron entre el 8 y el 12 de octubre. A quien corrigió y tenía 90 o más, su práctica queda en **99**; a quien tenía menos de 90, en **90**. El 100 se reserva para quien entregó bien desde la primera vez. En la tabla de calificaciones del curso su celda aparece como `anterior/vigente`: el primer número es la entrega original y **el segundo es el que cuenta**.

### Práctica 1 — evaluación (8-oct-2026, 00:51 h)

**Calificación: 68 / 100**

Entregada el **6-oct-2026 a las 14:19**, dentro del plazo (la entrega cerraba el mar 6-oct), así que no lleva penalización por retraso.

**Criterios cubiertos al 100%:** Estructura del monorepo (6/6); Nombres exactos de los entregables; Requisitos de Git (3+ commits, rama mergeada); Python puro (sin `csv` ni `pandas`, lectura con `open`); Formato del `resumen.txt` (encabezado y secciones); Dimensiones: filas, columnas, nombres; Calidad de datos (celdas vacías).

**Observaciones:**

1. La semilla reportada es incorrecta: pusieron `Seed: ?` y su semilla es **55**.
2. Las primeras 5 filas deben ir separadas con ` | ` (barra con espacios a los lados), no con `|` pegado.
3. La columna categórica de su tema es **`zona`** (viene en la tabla de referencia del enunciado), no `telefono`. Por el número de valores únicos que reportan, parece que la están detectando automáticamente (la columna con más valores distintos) en vez de tomarla de la tabla.
4. La columna numérica que pide P1 es la `numerica_1` de su tema, **`duracion_incidente_min`**, no `descripcion_incidente`.

**Desglose:**

| Criterio | Obtenido | Máximo |
|---|:---:|:---:|
| Estructura del monorepo (6/6) | 8 | 8 |
| Nombres exactos de los entregables | 10 | 10 |
| Requisitos de Git (3+ commits, rama mergeada) | 10 | 10 |
| Python puro (sin `csv` ni `pandas`, lectura con `open`) | 8 | 8 |
| Formato del `resumen.txt` (encabezado y secciones) | 9 | 9 |
| Encabezado: Archivo, Pareja, Seed | 5 | 10 |
| Dimensiones: filas, columnas, nombres | 10 | 10 |
| Primeras 5 filas (separadas con barra y espacios) | 3 | 5 |
| Columna categórica (nombre, únicos, más frecuente) | 0 | 12 |
| Columna numérica_1 (nombre, válidos, mín, máx) | 0 | 13 |
| Calidad de datos (celdas vacías) | 5 | 5 |
| **Total** | **68** | **100** |

### 26-sep-2026

**Estatus:** 5/6 de la estructura esperada.

Buen avance: completaron `src/` y `resultados/` en las 6 carpetas `practicaN/` (antes estaban vacías). Sigue pendiente terminar `proyecto/`: por ahora solo tiene `datos/`, les falta agregar `src/` y `resultados/` dentro. También sigue la carpeta extra `mi_primer_proyecto/` en la raíz que no forma parte de la estructura esperada.

### 23-sep-2026

**Estatus:** 4/6 de la estructura esperada.

Sigue igual: `practica1` a `practica6` y `proyecto/` siguen vacías, les falta llenarlas con sus subcarpetas `src/` y `resultados/` (`proyecto/` también necesita `datos/`). También notamos una carpeta extra `mi_primer_proyecto/` en la raíz que no forma parte de la estructura esperada.

📖 **Práctica 1 ya está disponible.** La encontrarán en `labs/P1/P1_setup_reconocimiento.md`, dentro del repositorio del profesor: https://github.com/ESCOMLCD/pcd202701/blob/main/labs/P1/P1_setup_reconocimiento.md — léanla completa antes de empezar a programar, ahí está todo lo que deben hacer, el formato exacto de `resumen.txt` y la fecha de entrega (mar 6-oct).

### 22-sep-2026

**Estatus:** 4/6 de la estructura esperada.

Buen avance: agregaron `requirements.txt`, reemplazaron `codigos/` por `datos/`, y crearon las 6 carpetas `practica1` a `practica6` más `proyecto/`. Les falta llenar cada una con sus subcarpetas `src/` y `resultados/` (y `proyecto/` también necesita `datos/`) — por ahora están vacías. También resolvieron el `.DS_Store` que tenían versionado, bien hecho. Ya les dejamos su dataset (`reportes_transito-ruido_100.csv` y `_100000.csv`) dentro de `datos/`.
