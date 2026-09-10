"""Experimento de la Parte 3: casos de Insertion Sort."""
import time
import matplotlib.pyplot as plt
from algoritmos import insertion_sort
from datos import generar_aleatorio, generar_casi_ordenado, generar_inverso


def ejecutar_experimento() -> None:
    """Mide tiempo y comparaciones de insertion sort en los tres escenarios."""
    tamanos = [100, 200, 400, 800, 1600, 3200, 6400]

    resultados = {
        "A (Aleatorio)": {"tiempos": [], "comparaciones": []},
        "B (Casi ordenado)": {"tiempos": [], "comparaciones": []},
        "C (Orden inverso)": {"tiempos": [], "comparaciones": []},
    }

    print("Ejecutando mediciones de Parte 3...")
    for n in tamanos:
        print(f"  Procesando n = {n}...")
        lote_a = generar_aleatorio(n)
        lote_b = generar_casi_ordenado(n)
        lote_c = generar_inverso(n)

        # Escenario A
        t0 = time.perf_counter()
        _, c_a = insertion_sort(lote_a)
        t_a = time.perf_counter() - t0
        resultados["A (Aleatorio)"]["tiempos"].append(t_a)
        resultados["A (Aleatorio)"]["comparaciones"].append(c_a)

        # Escenario B
        t0 = time.perf_counter()
        _, c_b = insertion_sort(lote_b)
        t_b = time.perf_counter() - t0
        resultados["B (Casi ordenado)"]["tiempos"].append(t_b)
        resultados["B (Casi ordenado)"]["comparaciones"].append(c_b)

        # Escenario C
        t0 = time.perf_counter()
        _, c_c = insertion_sort(lote_c)
        t_c = time.perf_counter() - t0
        resultados["C (Orden inverso)"]["tiempos"].append(t_c)
        resultados["C (Orden inverso)"]["comparaciones"].append(c_c)

    # 1. Grafica de comparaciones
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

    # 2. Grafica de tiempo
    plt.figure(figsize=(9, 5))
    for esc, datos in resultados.items():
        plt.plot(tamanos, datos["tiempos"], marker="o", label=esc)
    plt.title("Insertion Sort: Tiempo de ejecución vs. Tamaño (n)")
    plt.xlabel("Tamaño de la entrada (n)")
    plt.ylabel("Tiempo de ejecución (segundos)")
    plt.grid(True, linestyle="--", alpha=0.6)
    plt.legend()
    plt.tight_layout()
    plt.savefig("graficas/parte3_tiempo.png", dpi=300)
    plt.close()
    print("Gráficas guardadas con éxito en graficas/")


if __name__ == "__main__":
    ejecutar_experimento()