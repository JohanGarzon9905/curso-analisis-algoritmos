"""Medicion experimental y generacion de graficas para listas y tablas hash."""

import os
import random
import time
import matplotlib.pyplot as plt
from estructuras import ListaEnlazada, TablaHash


def generar_guias_inexistentes(
    existentes: set[int], cantidad: int, semilla: int = 7
) -> list[int]:
    """Genera guias de diez digitos que no estan en la coleccion.

    Args:
        existentes: guias almacenadas en las estructuras.
        cantidad: cuantas guias inexistentes generar.
        semilla: semilla del generador, para reproducir la medicion.

    Returns:
        Una lista con cantidad guias que no pertenecen a existentes.
    """
    azar = random.Random(semilla)
    inexistentes: list[int] = []
    while len(inexistentes) < cantidad:
        guia = azar.randint(10**9, 10**10 - 1)
        if guia not in existentes:
            inexistentes.append(guia)
    return inexistentes


def ejecutar_experimento_a() -> tuple[list[int], list[float], list[float], list[int]]:
    """Mide el tiempo medio de busqueda infructuosa en lista frente a tabla hash.

    Returns:
        Tupla con valores n, tiempos medios de lista enlazada (s),
        tiempos medios de tabla hash (s) y valores de m empleados.
    """
    valores_n: list[int] = [100, 500, 1000, 5000, 20000, 50000]
    primos_m: list[int] = [53, 251, 503, 2503, 10007, 25013]
    estados: tuple[str, ...] = ("en bodega", "en reparto", "entregado")
    repeticiones: int = 5

    tiempos_lista: list[float] = []
    tiempos_tabla: list[float] = []

    azar_datos = random.Random(12345)

    print("=== Experimento A (Lista vs Tabla) ===")
    for n, m in zip(valores_n, primos_m):
        guias_set: set[int] = set()
        while len(guias_set) < n:
            guias_set.add(azar_datos.randint(10**9, 10**10 - 1))

        guias_lista = list(guias_set)

        lista = ListaEnlazada()
        tabla = TablaHash(m)

        for guia in guias_lista:
            estado = estados[guia % len(estados)]
            lista.insertar(guia, estado)
            tabla.insertar(guia, estado)

        for muestra in guias_lista[:10]:
            assert lista.buscar(muestra) == tabla.buscar(muestra)

        inexistentes = generar_guias_inexistentes(guias_set, 200, semilla=77)

        tiempos_rep_lista: list[float] = []
        tiempos_rep_tabla: list[float] = []

        for _ in range(repeticiones):
            t0 = time.perf_counter()
            for g in inexistentes:
                lista.buscar(g)
            t1 = time.perf_counter()
            tiempos_rep_lista.append((t1 - t0) / len(inexistentes))

            t0 = time.perf_counter()
            for g in inexistentes:
                tabla.buscar(g)
            t1 = time.perf_counter()
            tiempos_rep_tabla.append((t1 - t0) / len(inexistentes))

        t_medio_lista = sum(tiempos_rep_lista) / repeticiones
        t_medio_tabla = sum(tiempos_rep_tabla) / repeticiones

        tiempos_lista.append(t_medio_lista)
        tiempos_tabla.append(t_medio_tabla)

        print(
            f"n={n:5d} | m={m:5d} | alfa={tabla.factor_carga():.2f} | "
            f"Lista: {t_medio_lista * 1e6:8.2f} us | Tabla: {t_medio_tabla * 1e6:6.2f} us"
        )

    return valores_n, tiempos_lista, tiempos_tabla, primos_m


def ejecutar_experimento_b() -> tuple[list[float], list[float], list[int]]:
    """Mide el tiempo medio de busqueda infructuosa variando el factor de carga alfa.

    Returns:
        Tupla con factores de carga reales alfa, tiempos medios de tabla hash (s)
        y valores m empleados.
    """
    n: int = 20000
    configuraciones_m: list[int] = [40009, 20011, 10007, 5003, 2003]
    estados: tuple[str, ...] = ("en bodega", "en reparto", "entregado")
    repeticiones: int = 5

    azar_datos = random.Random(54321)
    guias_set: set[int] = set()
    while len(guias_set) < n:
        guias_set.add(azar_datos.randint(10**9, 10**10 - 1))
    guias_lista = list(guias_set)

    inexistentes = generar_guias_inexistentes(guias_set, 200, semilla=99)

    alfas_reales: list[float] = []
    tiempos_tabla_alfa: list[float] = []

    print("\n=== Experimento B (Efecto de alfa con n=20000) ===")
    for m in configuraciones_m:
        tabla = TablaHash(m)
        for guia in guias_lista:
            estado = estados[guia % len(estados)]
            tabla.insertar(guia, estado)

        alfa = tabla.factor_carga()
        alfas_reales.append(alfa)

        tiempos_rep: list[float] = []
        for _ in range(repeticiones):
            t0 = time.perf_counter()
            for g in inexistentes:
                tabla.buscar(g)
            t1 = time.perf_counter()
            tiempos_rep.append((t1 - t0) / len(inexistentes))

        t_medio = sum(tiempos_rep) / repeticiones
        tiempos_tabla_alfa.append(t_medio)

        print(f"m={m:5d} | alfa={alfa:5.2f} | Tiempo medio: {t_medio * 1e6:6.2f} us")

    return alfas_reales, tiempos_tabla_alfa, configuraciones_m


def graficar_experimentos(
    valores_n: list[int],
    tiempos_lista: list[float],
    tiempos_tabla: list[float],
    alfas: list[float],
    tiempos_alfa: list[float],
    directorio_graficas: str,
) -> None:
    """Genera y guarda en disco las figuras de los dos experimentos.

    Args:
        valores_n: tamanos de coleccion evaluados en el experimento A.
        tiempos_lista: tiempos medios de busqueda en lista para cada n.
        tiempos_tabla: tiempos medios de busqueda en tabla para cada n.
        alfas: factores de carga evaluados en el experimento B.
        tiempos_alfa: tiempos medios de busqueda para cada alfa.
        directorio_graficas: ruta del directorio donde se guardaran los archivos PNG.
    """
    os.makedirs(directorio_graficas, exist_ok=True)

    t_lista_us = [t * 1e6 for t in tiempos_lista]
    t_tabla_us = [t * 1e6 for t in tiempos_tabla]

    plt.figure(figsize=(9, 5.5))
    plt.plot(valores_n, t_lista_us, "o-", color="#d62728", label="Lista Enlazada (Θ(n))", linewidth=2)
    plt.plot(valores_n, t_tabla_us, "s-", color="#1f77b4", label="Tabla Hash (Θ(1 + α), α ≈ 2)", linewidth=2)
    plt.title("Tiempo Medio de Búsqueda Infructuosa: Lista Enlazada vs Tabla Hash", fontsize=12, pad=12)
    plt.xlabel("Número de Guías Almacenadas (n)", fontsize=11)
    plt.ylabel("Tiempo Medio por Búsqueda (microsegundos, µs)", fontsize=11)
    plt.grid(True, linestyle="--", alpha=0.6)
    plt.legend(fontsize=10)
    plt.tight_layout()
    ruta_exp_a = os.path.join(directorio_graficas, "lista_vs_tabla.png")
    plt.savefig(ruta_exp_a, dpi=300)
    plt.close()
    print(f"\nGrafica A guardada en: {ruta_exp_a}")

    t_alfa_us = [t * 1e6 for t in tiempos_alfa]

    plt.figure(figsize=(9, 5.5))
    plt.plot(alfas, t_alfa_us, "d-", color="#2ca02c", linewidth=2, label="Tabla Hash (n = 20.000)")
    plt.title("Efecto del Factor de Carga (α) en el Tiempo de Búsqueda Infructuosa", fontsize=12, pad=12)
    plt.xlabel("Factor de Carga (α = n / m)", fontsize=11)
    plt.ylabel("Tiempo Medio por Búsqueda (microsegundos, µs)", fontsize=11)
    plt.grid(True, linestyle="--", alpha=0.6)
    plt.legend(fontsize=10)
    plt.tight_layout()
    ruta_exp_b = os.path.join(directorio_graficas, "tiempo_vs_alfa.png")
    plt.savefig(ruta_exp_b, dpi=300)
    plt.close()
    print(f"Grafica B guardada en: {ruta_exp_b}")


if __name__ == "__main__":
    dir_graficas = os.path.join(os.path.dirname(__file__), "graficas")
    val_n, t_lis, t_tab, m_a = ejecutar_experimento_a()
    val_alfa, t_alf, m_b = ejecutar_experimento_b()
    graficar_experimentos(val_n, t_lis, t_tab, val_alfa, t_alf, dir_graficas)
