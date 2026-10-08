import os
import random
import time
import matplotlib.pyplot as plt
from subarreglo import subarreglo_fuerza_bruta, subarreglo_maximo


def ejecutar_experimento() -> None:
    tamanos: list[int] = [10, 50, 100, 500, 1000, 2000, 4000, 8000]
    repeticiones: int = 5
    semilla_base: int = 42

    tiempos_fb_promedio: list[float] = []
    tiempos_dv_promedio: list[float] = []

    print(f"{'n':>6} | {'FB Promedio (s)':>15} | {'DV Promedio (s)':>15} | {'Suma Validada':>15}")
    print("-" * 60)

    for n in tamanos:
        tiempos_fb_iter: list[float] = []
        tiempos_dv_iter: list[float] = []

        for rep in range(repeticiones):
            random.seed(semilla_base + n + rep)
            datos: list[float] = [float(random.randint(-100, 100)) for _ in range(n)]

            t0_fb = time.perf_counter()
            res_fb = subarreglo_fuerza_bruta(datos)
            t1_fb = time.perf_counter()
            tiempos_fb_iter.append(t1_fb - t0_fb)

            t0_dv = time.perf_counter()
            res_dv = subarreglo_maximo(datos, 0, n - 1)
            t1_dv = time.perf_counter()
            tiempos_dv_iter.append(t1_dv - t0_dv)

            assert abs(res_fb[2] - res_dv[2]) < 1e-9

        prom_fb = sum(tiempos_fb_iter) / repeticiones
        prom_dv = sum(tiempos_dv_iter) / repeticiones
        tiempos_fb_promedio.append(prom_fb)
        tiempos_dv_promedio.append(prom_dv)

        print(f"{n:>6} | {prom_fb:>15.6f} | {prom_dv:>15.6f} | {res_fb[2]:>15.1f}")

    os.makedirs("graficas", exist_ok=True)
    ruta_grafica = os.path.join("graficas", "tiempo_vs_n.png")

    fig, ax = plt.subplots(figsize=(10, 6), dpi=300)
    ax.plot(
        tamanos,
        tiempos_fb_promedio,
        marker="o",
        color="#d9534f",
        linewidth=2,
        label=r"Fuerza Bruta $\Theta(n^2)$",
    )
    ax.plot(
        tamanos,
        tiempos_dv_promedio,
        marker="s",
        color="#0275d8",
        linewidth=2,
        label=r"Divide y Vencerás $\Theta(n \log n)$",
    )

    ax.set_title(
        "Comparación Experimental de Rendimiento: Subarreglo Máximo\nFuerza Bruta vs. Divide y Vencerás",
        fontsize=13,
        pad=15,
        fontweight="bold",
    )
    ax.set_xlabel("Tamaño de la entrada ($n$ elementos)", fontsize=11)
    ax.set_ylabel("Tiempo de ejecución promedio (segundos)", fontsize=11)
    ax.grid(True, linestyle="--", alpha=0.6)
    ax.legend(fontsize=11, loc="upper left")

    plt.tight_layout()
    plt.savefig(ruta_grafica)
    plt.close()
    print(f"\nGráfica guardada exitosamente en: {ruta_grafica}")


if __name__ == "__main__":
    ejecutar_experimento()
