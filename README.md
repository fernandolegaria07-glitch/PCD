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
### 22-sep-2026

**Estatus:** 4/6 de la estructura esperada.

Buen avance: agregaron `requirements.txt`, reemplazaron `codigos/` por `datos/`, y crearon las 6 carpetas `practica1` a `practica6` más `proyecto/`. Les falta llenar cada una con sus subcarpetas `src/` y `resultados/` (y `proyecto/` también necesita `datos/`) — por ahora están vacías. También resolvieron el `.DS_Store` que tenían versionado, bien hecho. Ya les dejamos su dataset (`reportes_transito-ruido_100.csv` y `_100000.csv`) dentro de `datos/`.

### 23-sep-2026

**Estatus:** 4/6 de la estructura esperada.

Sigue igual: `practica1` a `practica6` y `proyecto/` siguen vacías, les falta llenarlas con sus subcarpetas `src/` y `resultados/` (`proyecto/` también necesita `datos/`). También notamos una carpeta extra `mi_primer_proyecto/` en la raíz que no forma parte de la estructura esperada.

📖 **Práctica 1 ya está disponible.** La encontrarán en `labs/P1/P1_setup_reconocimiento.md`, dentro del repositorio del profesor: https://github.com/ESCOMLCD/pcd202701/blob/main/labs/P1/P1_setup_reconocimiento.md — léanla completa antes de empezar a programar, ahí está todo lo que deben hacer, el formato exacto de `resumen.txt` y la fecha de entrega (mar 6-oct).

### 26-sep-2026

**Estatus:** 5/6 de la estructura esperada.

Buen avance: completaron `src/` y `resultados/` en las 6 carpetas `practicaN/` (antes estaban vacías). Sigue pendiente terminar `proyecto/`: por ahora solo tiene `datos/`, les falta agregar `src/` y `resultados/` dentro. También sigue la carpeta extra `mi_primer_proyecto/` en la raíz que no forma parte de la estructura esperada.
