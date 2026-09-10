"""Generadores de lotes de registros para los escenarios de Tamiza."""
import random


def generar_aleatorio(n: int, semilla: int = 42) -> list[int]:
    """Genera un lote de n registros en orden aleatorio (escenario A).

    Args:
        n: cantidad de registros del lote.
        semilla: semilla del generador aleatorio, para que el
            experimento sea reproducible.

    Returns:
        Lista de n indices de riesgo enteros distintos, desordenada.
    """
    rng = random.Random(semilla)
    return rng.sample(range(max(n * 5, 2000)), n)


def generar_casi_ordenado(n: int, semilla: int = 42) -> list[int]:
    """Genera un lote casi ordenado: 98% ordenado y 2% al final (escenario B).

    Args:
        n: cantidad de registros del lote.
        semilla: semilla del generador aleatorio.

    Returns:
        Lista de n indices de riesgo enteros distintos, con el primer
        98% en el orden que el algoritmo produce y el 2% restante
        desordenado al final.
    """
    rng = random.Random(semilla)
    datos = rng.sample(range(max(n * 5, 2000)), n)
    n_ordenados = int(n * 0.98)

    # El 98% ya ordenado de mayor a menor
    parte_ordenada = sorted(datos[:n_ordenados], reverse=True)
    parte_desordenada = datos[n_ordenados:]
    return parte_ordenada + parte_desordenada


def generar_inverso(n: int) -> list[int]:
    """Genera un lote en el orden exactamente contrario (escenario C).

    Args:
        n: cantidad de registros del lote.

    Returns:
        Lista de n indices de riesgo enteros distintos, en el orden
        inverso al que el algoritmo debe producir (menor a mayor).
    """
    return list(range(n))