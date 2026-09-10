"""Experimento de la Parte 4: Comparativa Insertion Sort vs Merge Sort."""
import time
import matplotlib.pyplot as plt
from algoritmos import insertion_sort, merge_sort
from datos import generar_aleatorio


def ejecutar_comparacion() -> None:
    """Mide y compara el tiempo de ejecucion entre insertion sort y merge sort."""
    tamanos = [100, 200, 400, 800, 1600, 3200, 6400]
    tiempos_insertion = []
    tiempos_merge = []

    print("Ejecutando mediciones de Parte 4...")
    for n in tamanos:
        print(f"  Procesando n = {n}...")
        lote = generar_aleatorio(n)

        # Insertion sort
        t0 = time.perf_counter()
        insertion_sort(lote)
        t_ins = time.perf_counter() - t0
        tiempos_insertion.append(t_ins)

        # Merge sort
        t0 = time.perf_counter()
        merge_sort(lote)
        t_mrg = time.perf_counter() - t0
        tiempos_merge.append(t_mrg)

    # Grafica de tiempo comparativa
    plt.figure(figsize=(9, 5))
    plt.plot(tamanos, tiempos_insertion, marker="o", color="red", label="Insertion Sort")
    plt.plot(tamanos, tiempos_merge, marker="s", color="blue", label="Merge Sort")
    plt.title("Comparativa de Tiempo: Insertion Sort vs. Merge Sort (Escenario A)")
    plt.xlabel("Tamaño de la entrada (n)")
    plt.ylabel("Tiempo de ejecución (segundos)")
    plt.grid(True, linestyle="--", alpha=0.6)
    plt.legend()
    plt.tight_layout()
    plt.savefig("graficas/parte4_tiempo.png", dpi=300)
    plt.close()
    print("Gráfica guardada en graficas/parte4_tiempo.png")


if __name__ == "__main__":
    ejecutar_comparacion()