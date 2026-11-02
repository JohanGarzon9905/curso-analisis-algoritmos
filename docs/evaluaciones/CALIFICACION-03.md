# Retroalimentación — Laboratorio 03: Estructuras de datos

**Estudiante:** Johan Sneider Garzon Salazar · **Laboratorio:** Laboratorio evaluativo 03 — Estructuras de datos
**Fecha límite:** 2026-11-01 23:59 · **Versión revisada:** commit `554e85b`

Muy buen trabajo: implementación limpia, pruebas completas e informe bien organizado.

## Nota

| Criterio | Puntos |
|---|---|
| Corrección conceptual | 19 / 20 |
| Calidad de la explicación teórica | 20 / 20 |
| Corrección de la implementación | 24 / 25 |
| Calidad del análisis de las gráficas | 23 / 25 |
| Documentación y organización del informe | 10 / 10 |
| **Total** | **96 / 100** |
| **Nota (0–5)** | **4.80** |

## 1. Corrección conceptual (19 / 20)
**Lo que hizo bien:**
- Explica bien qué es una colisión, por qué ocurre aunque sobren casillas, y compara encadenamiento con direccionamiento abierto usando el ejemplo de 10, 24 y 17 con m = 7.
- Justifica por qué la tabla hash no sirve para rangos y por qué el árbol sí.
- Da altura y comparaciones del árbol degenerado (400.000) frente al equilibrado (~19), y recomienda una combinación de tabla hash y árbol.
- Declara que el valor para 5.000.000 de envíos es una estimación.

**Lo que puede mejorar (y cómo corregirlo):**
- Para el árbol degenerado solo cuenta las comparaciones de una búsqueda; no estima las comparaciones totales de insertar las 400.000 guías una a una.
  → *Cómo corregirlo:* piense cuántos nodos debe recorrer cada guía nueva al insertarse y sume esos recorridos para todas las guías.
- En la estimación de la lista, dice que "superará de 1 a 2 segundos" por fallos de caché, pero ese valor no sale de sus mediciones. Además, su propia gráfica muestra que de n = 20.000 a n = 50.000 el tiempo creció más rápido que n.
  → *Cómo corregirlo:* apoye la estimación en la razón entre dos de sus mediciones consecutivas y explique la forma de la curva, en vez de añadir un rango sin respaldo. Lo mismo vale para el "1 a 2 µs" de la tabla.

## 2. Calidad de la explicación teórica (20 / 20)
**Lo que hizo bien:**
- Justifica el Θ(n) de la lista y el Θ(1 + α) de la tabla, nombra el supuesto de dispersión uniforme y explica que, si todas las guías caen en una casilla, la tabla se vuelve una lista de tamaño n.

## 3. Corrección de la implementación (24 / 25)
**Lo que hizo bien:**
- Ambas estructuras devuelven lo correcto en búsquedas exitosas e infructuosas; la colisión forzada con m = 7 y `factor_carga` (3/7) funcionan.
- La tabla reutiliza `ListaEnlazada` sin `dict`, `set` ni `hash()`; `buscar` es iterativa.
- Hay 25 colecciones aleatorias comparando lista y tabla, con guías existentes e inexistentes.
- Todas las funciones de `estructuras.py` y `medicion.py` tienen docstrings con `Args` y `Returns` y type hints.

**Lo que puede mejorar (y cómo corregirlo):**
- En `medicion.py`, la verificación de que lista y tabla coinciden usa solo 10 guías existentes; es una muestra pequeña.
  → *Cómo corregirlo:* aumente la muestra o recorra todas las guías insertadas.

## 4. Calidad del análisis de las gráficas (23 / 25)
**Lo que hizo bien:**
- Ambas gráficas existen, con título, ejes rotulados y leyenda; la primera tiene seis valores de n con las dos curvas en los mismos ejes y la segunda cinco valores de α.
- Calcula el factor de 1,99 entre n = 500 y n = 1000 para la lista y lo contrasta con Θ(n). Las cifras del informe coinciden con lo que muestran las gráficas.

**Lo que puede mejorar (y cómo corregirlo):**
- Para la tabla dice "plana", pero en su tabla de datos pasa de 0,19 a 0,91 µs; no calcula el factor de crecimiento de la tabla ni explica esa diferencia.
  → *Cómo corregirlo:* calcule también la razón entre dos n consecutivos para la tabla y comente si es cercana a 1 o qué podría explicar el aumento.
- En la segunda gráfica no calcula cuánto se multiplica el tiempo cuando α crece, y afirma que sube "linealmente" sin cuantificarlo.
  → *Cómo corregirlo:* compare dos valores de α (por ejemplo, uno y su doble) con los tiempos que lee en la gráfica y vea si el cambio es coherente con 1 + α.
- No comenta que entre n = 20.000 y n = 50.000 la lista creció más de lo que predice una recta.
  → *Cómo corregirlo:* calcule ese factor y compárelo con el crecimiento de n.

## 5. Documentación y organización del informe (10 / 10)
**Lo que hizo bien:**
- Carpeta `laboratorios/lab3-estructuras-datos/` (ubicación válida) con todos los archivos y las dos gráficas; las imágenes están incrustadas con ruta relativa que funciona.
- El README tiene su nombre, instrucciones de reproducción, el orden pedido y enlaces al código en cada parte.
- Tres commits con mensajes descriptivos.

## ¿El código funciona?
Sí. Las pruebas pasan, ambas estructuras buscan bien, y `medicion.py` corre y genera las dos gráficas.
