"""Experimento de la Parte 3: casos de Insertion Sort."""

import time
import matplotlib.pyplot as plt
from algoritmos import insertion_sort
from datos import generar_aleatorio, generar_casi_ordenado, generar_inverso


def ejecutar_experimento() -> None:
    """Mide tiempo y comparaciones de insertion sort en los tres escenarios."""
    tamanos = [100, 200, 400, 800, 1600, 3200, 6400]
    num_repeticiones = 5

    resultados = {
        "A (Aleatorio)": {"tiempos": [], "comparaciones": []},
        "B (Casi ordenado)": {"tiempos": [], "comparaciones": []},
        "C (Orden inverso)": {"tiempos": [], "comparaciones": []},
    }

    print("Ejecutando mediciones de Parte 3...")
    for n in tamanos:
        print(f"  Procesando n = {n}...")
        tiempos_a, comp_a = [], []
        tiempos_b, comp_b = [], []
        tiempos_c, comp_c = [], []

        for rep in range(num_repeticiones):
            semilla = 42 + rep
            lote_a = generar_aleatorio(n, semilla=semilla)
            lote_b = generar_casi_ordenado(n, semilla=semilla)
            lote_c = generar_inverso(n)

            t0 = time.perf_counter()
            _, c_a = insertion_sort(lote_a)
            tiempos_a.append(time.perf_counter() - t0)
            comp_a.append(c_a)

            t0 = time.perf_counter()
            _, c_b = insertion_sort(lote_b)
            tiempos_b.append(time.perf_counter() - t0)
            comp_b.append(c_b)

            t0 = time.perf_counter()
            _, c_c = insertion_sort(lote_c)
            tiempos_c.append(time.perf_counter() - t0)
            comp_c.append(c_c)

        resultados["A (Aleatorio)"]["tiempos"].append(sum(tiempos_a) / num_repeticiones)
        resultados["A (Aleatorio)"]["comparaciones"].append(sum(comp_a) / num_repeticiones)

        resultados["B (Casi ordenado)"]["tiempos"].append(sum(tiempos_b) / num_repeticiones)
        resultados["B (Casi ordenado)"]["comparaciones"].append(sum(comp_b) / num_repeticiones)

        resultados["C (Orden inverso)"]["tiempos"].append(sum(tiempos_c) / num_repeticiones)
        resultados["C (Orden inverso)"]["comparaciones"].append(sum(comp_c) / num_repeticiones)

    plt.figure(figsize=(9, 5))
    for esc, datos in resultados.items():
        plt.plot(tamanos, datos["comparaciones"], marker="o", label=esc)
    plt.title("Insertion Sort: Comparaciones entre elementos vs. Tamaño (n)")
    plt.xlabel("Tamaño de la entrada (n)")
    plt.ylabel("Número de comparaciones")
    plt.grid(True, linestyle="--", alpha=0.6)
    plt.legend()
    plt.tight_layout()
    plt.savefig("graficas/parte3_comparaciones.png", dpi=300)
    plt.close()

    plt.figure(figsize=(9, 5))
    for esc, datos in resultados.items():
        plt.plot(tamanos, datos["tiempos"], marker="o", label=esc)
    plt.title("Insertion Sort: Tiempo de ejecución vs. Tamaño (n)")
    plt.xlabel("Tamaño de la entrada (n)")
    plt.ylabel("Tiempo de ejecución promedio (segundos)")
    plt.grid(True, linestyle="--", alpha=0.6)
    plt.legend()
    plt.tight_layout()
    plt.savefig("graficas/parte3_tiempo.png", dpi=300)
    plt.close()
    print("Gráficas guardadas con éxito en graficas/")


if __name__ == "__main__":
    ejecutar_experimento()
