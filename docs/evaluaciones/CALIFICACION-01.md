# Retroalimentación — Laboratorio 01: Fundamentos, complejidad y recurrencias

**Estudiante:** Johan Sneider Garzón Salazar · **Laboratorio:** Laboratorio evaluativo 01 — Fundamentos, complejidad y recurrencias
**Fecha límite:** 2026-10-06 23:59 · **Versión revisada:** commit `50f52ea`

Muy buen trabajo: el informe es completo y apoyado en sus propias mediciones.

## Nota

| Criterio | Puntos |
|---|---|
| Corrección conceptual | 23 / 25 |
| Calidad de la explicación teórica | 24 / 25 |
| Corrección de la implementación | 19 / 20 |
| Calidad del análisis de las gráficas | 17 / 20 |
| Documentación y organización del informe | 10 / 10 |
| **Total** | **93 / 100** |
| **Nota (0–5)** | **4.65** |

## 1. Corrección conceptual (23 / 25)
**Lo que hizo bien:**
- Distingue entre ordenar bien y ordenar a tiempo, y nombra la ventana de cuatro horas como la restricción que se incumple.
- Explica con números (60 veces más datos, unas 3.600 veces más trabajo) por qué un servidor el doble de rápido no resuelve el problema.
- El segundo ejemplo (buscador de una tienda con 40.000 productos) dice qué se procesa y cuál es el tiempo máximo esperado (menos de medio segundo).
- Calcula el consumo de energía anual (kWh) del proceso nocturno y lo compara con merge sort.
- Da tres perjuicios (paciente, operadores y Secretaría) y dice quién asume el costo en cada uno.
- Reconoce que el orden de la lista decide a quién se llama primero.

**Lo que puede mejorar:**
- La obligación que impone ese orden quedó en una sola frase: faltó desarrollar qué debe garantizarse sobre la corrección del ordenamiento, más allá del tiempo.
- Las horas diarias que usa para el cálculo de energía (8 h) son un supuesto; convendría decir de dónde sale.

## 2. Calidad de la explicación teórica (24 / 25)
**Lo que hizo bien:**
- Define peor, mejor y caso promedio indicando sobre qué entradas se toma el máximo, el mínimo y el promedio, justifica usar el peor caso y deja la predicción escrita antes de medir.
- Plantea `T(n) = 2T(n/2) + Θ(n)`, explica cada término y lo resuelve con el método maestro verificando la condición del caso 2.
- Hace el conteo línea a línea de insertion sort con el número de veces que se ejecuta cada línea y llega a `Θ(n²)`.
- Presenta la tabla de complejidades por caso.

**Lo que puede mejorar:**
- En las definiciones, aclare que el tamaño `n` se mantiene fijo al tomar el máximo, el mínimo o el promedio.
- El conteo línea a línea se hace solo para el peor caso; agregue también el mejor caso para ver de dónde sale `Θ(n)`.

## 3. Corrección de la implementación (19 / 20)
**Lo que hizo bien:**
- `insertion_sort` y `merge_sort` ordenan bien de mayor a menor en mis pruebas con listas aleatorias y pequeñas, no cambian la lista recibida y cuentan solo comparaciones entre elementos (n − 1 en el mejor caso, n(n − 1)/2 en el peor).
- `merge_sort` tiene su propia mezcla recursiva y no se usa `sorted()` ni `list.sort()` en ningún archivo.
- Los tres generadores producen valores distintos del tamaño pedido, con semilla reproducible; el escenario B deja el 98 % ordenado y el 2 % desordenado al final.
- Todas las funciones tienen *type hints* y *docstring*.

**Lo que puede mejorar:**
- Las estructuras de resultados en los scripts de medición podrían llevar anotación de tipos.

## 4. Calidad del análisis de las gráficas (17 / 20)
**Lo que hizo bien:**
- Las tres gráficas existen, con título, ejes rotulados, leyenda y las curvas pedidas en los mismos ejes.
- Identifica con cifras que C es el peor caso, B el mejor y A cercano al promedio, y lo contrasta con su predicción.
- En la Parte 4 describe qué hace cada curva, explica por qué merge sort no gana en tamaños muy pequeños y mide la diferencia en n = 6.400.
- El concepto técnico recomienda merge sort, extrapola a 1.200.000 registros declarándolo como proyección, responde sobre el servidor doble con datos medidos y discute memoria y otros costos reales.

**Lo que puede mejorar:**
- En 3.2 el informe dice que en n = 6.400 el escenario A tardó 1,35 s y C 2,34 s, pero las gráficas publicadas muestran cerca de 0,90 s y 1,65 s. Los datos del texto deben coincidir con los de la gráfica.
- En 4.2 diga explícitamente que lo observado coincide con `Θ(n log n)` frente a `Θ(n²)` calculados en 4.1.
- En 4.3 cite la gráfica de la que toma el dato del servidor doble.

## 5. Documentación y organización del informe (10 / 10)
**Lo que hizo bien:**
- La carpeta está en `laboratorios/lab1-fundamentos-complejidad-recurrencias/`, ubicación válida, con todos los archivos y gráficas pedidos.
- El informe sigue el orden pedido, incrusta las gráficas con rutas que funcionan y enlaza el código de cada parte.
- Las instrucciones de reproducción son claras y el `requirements.txt` de la raíz se conserva, así que se puede instalar `matplotlib` como indican.
- Hay siete commits con mensajes descriptivos sobre el laboratorio.

## ¿El código funciona?
Sí. Los dos algoritmos ordenan bien y cuentan las comparaciones correctamente, y los dos scripts corren sin errores y generan las gráficas.

## Para el próximo laboratorio
- Verifique que las cifras del informe coincidan con las gráficas publicadas antes de entregar.
- Desarrolle más las obligaciones éticas que se desprenden del caso, no solo el costo para cada afectado.
- Contraste siempre lo medido con la complejidad calculada, diciéndolo de forma explícita.
