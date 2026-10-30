# Retroalimentación — Laboratorio 02: Dividir y vencer

**Estudiante:** Johan Sneider Garzón Salazar · **Laboratorio:** Laboratorio evaluativo 02 — Dividir y vencer
**Fecha límite:** 2026-10-30 23:59 · **Versión revisada:** commit `9e8d428`

Muy buen trabajo, el laboratorio está completo y bien sustentado.

## Nota

| Criterio | Puntos |
|---|---|
| Corrección conceptual | 19 / 20 |
| Calidad de la explicación teórica | 19 / 20 |
| Corrección de la implementación | 23 / 25 |
| Calidad del análisis de las gráficas | 23 / 25 |
| Documentación y organización del informe | 10 / 10 |
| **Total** | **94 / 100** |
| **Nota (0–5)** | **4.70** |

## 1. Corrección conceptual (19 / 20)
**Lo que hizo bien:**
- Identificó el tamaño desde el cual divide y vencerás gana (entre n = 50 y n = 100) y explicó por qué antes no gana: el costo de las llamadas recursivas.
- Comparó con el máximo de un arreglo y justificó con el costo de combinar.
- Recomendó un algoritmo y declaró la cifra a 1.000.000 de registros como estimación, sin regla de tres lineal.

**Lo que puede mejorar (y cómo corregirlo):**
- En la pregunta 4 plantea la recurrencia del máximo pero no la resuelve; solo afirma el resultado.
  → *Cómo corregirlo:* aplique el método maestro a esa recurrencia, identificando `a`, `b`, `f(n)` y el caso que corresponde, como hizo en la pregunta 1.

## 2. Calidad de la explicación teórica (19 / 20)
**Lo que hizo bien:**
- Planteó `T(n) = 2T(n/2) + Θ(n)`, explicó cada término y verificó la condición del caso 2 del método maestro.
- Justificó el `Θ(n²)` de la fuerza bruta contando los pares de días.

**Lo que puede mejorar (y cómo corregirlo):**
- Falta decir por qué la recursión tiene profundidad `log n`, que es lo que da el factor `log n` en el resultado.
  → *Cómo corregirlo:* agregue una frase sobre cuántas veces se puede partir `n` a la mitad hasta llegar a tamaño 1.

## 3. Corrección de la implementación (23 / 25)
**Lo que hizo bien:**
- Las tres funciones dan resultados correctos en todos los casos pedidos y coinciden entre sí en 50 listas aleatorias.
- `subarreglo_maximo` resuelve los tres casos sin llamar a la fuerza bruta y no modifica la lista recibida.
- Tiene type hints y docstrings con `Args` y `Returns` en `subarreglo.py`.

**Lo que puede mejorar (y cómo corregirlo):**
- La función `ejecutar_experimento` de `medicion.py` tiene docstring, pero sin la sección `Returns`.
  → *Cómo corregirlo:* agregue `Returns:` (aunque sea "None") siguiendo el estilo Google usado en `subarreglo.py`.

## 4. Calidad del análisis de las gráficas (23 / 25)
**Lo que hizo bien:**
- La gráfica tiene título, ejes rotulados, leyenda y ambas curvas en los mismos ejes, con 8 tamaños.
- Calculó los factores de crecimiento al duplicar `n` para ambos algoritmos (cerca de 4 y cerca de 2.2) y los contrastó con `Θ(n²)` y `Θ(n log n)`.
- Sus cifras coinciden con la gráfica publicada (fuerza bruta cerca de 1.1 s en n = 8000).

**Lo que puede mejorar (y cómo corregirlo):**
- El análisis se apoya sobre todo en la tabla y casi no en lo que se ve en la gráfica; en escala lineal la curva de divide y vencerás queda pegada al eje.
  → *Cómo corregirlo:* cite también valores leídos de la gráfica (por ejemplo, a qué altura está cada curva en n = 4000 y n = 8000).

## 5. Documentación y organización del informe (10 / 10)
**Lo que hizo bien:**
- El laboratorio está en `laboratorios/lab2-divide-y-vencer/`, una ubicación válida, con todos los archivos del entregable.
- El informe sigue el orden pedido, enlaza el código en cada parte, incrusta la gráfica con ruta que funciona e incluye instrucciones de reproducción.
- Hay cuatro commits descriptivos del laboratorio.

## ¿El código funciona?
Sí. Las pruebas pasan, ambos algoritmos dan siempre la misma suma máxima y `medicion.py` corre y genera la gráfica.
