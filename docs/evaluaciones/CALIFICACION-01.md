# Retroalimentación — Laboratorio 01: Fundamentos, complejidad y recurrencias

**Estudiante:** Johan Sneider Garzón Salazar · **Laboratorio:** Laboratorio evaluativo 01 — Fundamentos, complejidad y recurrencias
**Fecha límite:** 2026-10-05 23:59 · **Versión revisada:** commit `c2b5ba9`

## Nota

| Criterio | Puntos |
|---|---|
| Corrección conceptual | 21 / 25 |
| Calidad de la explicación teórica | 20 / 25 |
| Corrección de la implementación | 10 / 20 |
| Calidad del análisis de las gráficas | 17 / 20 |
| Documentación y organización del informe | 9 / 10 |
| **Total** | **77 / 100** |
| **Nota (0–5)** | **3.85** |

## 1. Corrección conceptual (21 / 25)
**Lo que hizo bien:**
- Distingue bien entre ordenar correctamente y hacerlo a tiempo, y nombra la ventana de cuatro horas como lo que se incumple.
- Explica con números (60 veces más datos, unas 3.600 veces más trabajo) por qué un servidor más rápido no arregla el problema.
- Da dos perjuicios concretos (el paciente y el operador del centro de contacto) y dice quién asume el costo en el caso del paciente.
- Reconoce que el orden de la lista decide a quién se llama primero.

**Lo que puede mejorar:**
- El segundo ejemplo (catálogo de 40.000 productos) no dice qué tiempo máximo se esperaba; "varios segundos" es vago.
- La parte ambiental es solo cualitativa: faltó relacionar las horas de ejecución con el consumo de energía acumulado.
- Faltó decir claramente quién asume el costo en el caso del operador y de la Secretaría.

## 2. Calidad de la explicación teórica (20 / 25)
**Lo que hizo bien:**
- Define los tres casos, justifica el peor caso para la decisión y deja escrita la predicción antes de medir.
- Plantea `T(n) = 2T(n/2) + Θ(n)`, explica cada término y lo resuelve con el método maestro identificando `a`, `b` y `f(n)`.
- Presenta la tabla de complejidades.

**Lo que puede mejorar:**
- En las definiciones de los casos falta precisar sobre qué conjunto de entradas se toma el máximo, el mínimo y el promedio.
- En insertion sort describe qué hace cada línea, pero no da cuántas veces se ejecuta cada una ni suma los costos de todas.
- En el método maestro, escriba explícitamente la comparación de `f(n)` con `n^(log_b a)` como condición verificada.

## 3. Corrección de la implementación (10 / 20)
**Lo que hizo bien:**
- `insertion_sort` y `merge_sort` ordenan bien de mayor a menor, no cambian la lista original y cuentan comparaciones correctamente (n − 1 en el mejor caso, n(n − 1)/2 en el peor).
- `merge_sort` tiene su propia mezcla recursiva.
- Los generadores producen valores distintos, con semilla reproducible.

**Lo que puede mejorar:**
- En `datos.py`, el generador del escenario B usa `sorted()`. La guía prohíbe usar `sorted()` en el código entregado; aquí lo debía construir sin esa función (por ejemplo con `range`).
- Las funciones internas de `merge_sort` no tienen *docstring*.
- Los archivos no terminan con salto de línea y falta una línea en blanco antes de las importaciones (PEP 8).

## 4. Calidad del análisis de las gráficas (17 / 20)
**Lo que hizo bien:**
- Las tres gráficas existen, con título, ejes con unidades y leyenda, y los escenarios en los mismos ejes.
- Identifica con cifras que C es el peor caso, B el mejor y A cercano al promedio, y lo contrasta con la predicción.
- En la Parte 4 describe cada curva y la relaciona con las complejidades calculadas.
- El concepto técnico recomienda Merge Sort, estima las horas para 1.200.000 registros declarándolas como estimación, responde sobre el servidor doble con datos medidos y menciona la memoria extra.

**Lo que puede mejorar:**
- La estimación de Merge Sort (3,29 s) no tiene en cuenta otros costos reales; sería bueno advertirlo con más fuerza.
- Faltó explicar con más detalle qué se ve en la gráfica para los tamaños pequeños.
- Faltó indicar si repitió las mediciones y promedió.

## 5. Documentación y organización del informe (9 / 10)
**Lo que hizo bien:**
- La carpeta está en `laboratorios/lab1-fundamentos-complejidad-recurrencias/`, ubicación válida, con todos los archivos pedidos.
- El informe sigue el orden pedido, incrusta las gráficas con rutas que funcionan y enlaza el código.
- Hay instrucciones de reproducción claras y seis commits con mensajes descriptivos.

**Lo que puede mejorar:**
- Hay un `requirements.txt` adicional dentro de la carpeta del laboratorio que no estaba en el entregable.

## ¿El código funciona?
Sí. Los dos algoritmos ordenan bien en mis pruebas y los dos scripts corren sin errores y generan las gráficas.

## Para el próximo laboratorio
- Evite `sorted()` y `list.sort()` en todo el código, también en los generadores de datos.
- Agregue *docstring* a todas las funciones, incluidas las internas, y corrija los detalles de PEP 8.
- Cuando pida el conteo línea a línea, escriba cuántas veces se ejecuta cada línea y sume.
- Cuantifique las consecuencias ambientales (horas de ejecución por año) y cierre cada perjuicio diciendo quién asume el costo.
- Repita las mediciones y promedie para obtener curvas más estables.
