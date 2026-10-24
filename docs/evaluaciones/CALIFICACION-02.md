# Retroalimentación — Laboratorio 2: Dividir y vencer

**Estudiante:** Johan Sneider Garzón Salazar · **Laboratorio:** Laboratorio evaluativo 02 — Dividir y vencer
**Fecha límite:** 2026-10-21 23:59 · **Versión revisada:** commit `3bfc0a0`

Muy buen trabajo, completo y bien sustentado con sus propias mediciones.

## Nota

| Criterio | Puntos |
|---|---|
| Corrección conceptual | 19 / 20 |
| Calidad de la explicación teórica | 19 / 20 |
| Corrección de la implementación | 23 / 25 |
| Calidad del análisis de las gráficas | 25 / 25 |
| Documentación y organización del informe | 10 / 10 |
| **Total** | **96 / 100** |
| **Nota (0–5)** | **4.80** |

## 1. Corrección conceptual (19 / 20)
**Lo que hizo bien:**
- Identificó el cruce: con n = 10 gana la fuerza bruta, en n = 50 empatan y desde n = 100 gana divide y vencerás, y lo explicó por el costo de las llamadas recursivas.
- Comparó con el máximo de un arreglo: combinar cuesta Θ(1), por eso dividir no mejora.
- Recomendó divide y vencerás y estimó 1.000.000 de registros (unas 4.8 horas contra unos 2 segundos), declarándolo como estimación y sin regla de tres lineal.

**Lo que puede mejorar:**
- Al estimar divide y vencerás, aclare que el valor sale de una sola medición (n = 8000) y puede variar con el computador.

## 2. Calidad de la explicación teórica (19 / 20)
**Lo que hizo bien:**
- Planteó `T(n) = 2T(n/2) + Θ(n)` explicando cada término y la resolvió con el método maestro (caso 2), comparando `n^(log₂2)` con `f(n)`.
- Justificó el Θ(n²) de la fuerza bruta contando los pares (i, j).

**Lo que puede mejorar:**
- Al aplicar el método maestro, nombre de forma explícita la condición del caso 2 (f(n) = Θ(n^(log_b a))) y mencione que es el caso que se está verificando con su comparación.

## 3. Corrección de la implementación (23 / 25)
**Lo que hizo bien:**
- Las tres funciones dan resultados correctos, no modifican la lista, y `subarreglo_maximo` resuelve los tres casos sin usar la fuerza bruta.
- `pruebas.py` cubre todos los casos pedidos y 50 listas aleatorias.
- Funciones con *type hints* y *docstrings* en `subarreglo.py`.

**Lo que puede mejorar:**
- La función `ejecutar_experimento` de `medicion.py` no tiene *docstring* y el archivo no tiene descripción inicial.

## 4. Calidad del análisis de las gráficas (25 / 25)
**Lo que hizo bien:**
- La gráfica tiene título, ejes rotulados, leyenda, ambas curvas en los mismos ejes y 8 tamaños.
- Calculó los factores al duplicar n (3.89 y 4.01 para fuerza bruta; 2.10 y 2.20 para divide y vencerás) y los contrastó bien con la teoría. Los valores citados coinciden con la gráfica publicada.
- Incluyó una tabla con los tiempos medidos.

## 5. Documentación y organización del informe (10 / 10)
**Lo que hizo bien:**
- Estructura correcta (`laboratorios/lab2-divide-y-vencer/`), informe en el orden pedido, enlaces al código, gráfica visible, instrucciones de reproducción y commits descriptivos.

## ¿El código funciona?
Sí. Las pruebas pasan, ambos algoritmos coinciden en listas aleatorias y la medición genera la gráfica sin errores.

## Para el próximo laboratorio
- Agregue *docstrings* a todas las funciones, también a las de los scripts de medición.
- Mantenga dos líneas en blanco entre funciones y type hints en todas ellas.
- Indique siempre que las estimaciones salen de una medición y pueden variar entre equipos.
