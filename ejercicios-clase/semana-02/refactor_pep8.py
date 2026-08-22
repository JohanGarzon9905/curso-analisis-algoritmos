"""Módulo para el cálculo de promedios numéricos."""


def calcular_promedio(lista_numeros: list[int | float]) -> float:
    """Calcula el promedio aritmético de una lista de números.

    Args:
        lista_numeros: Lista de enteros o flotantes a promediar.

    Returns:
        El promedio aritmético de los valores ingresados.
    """
    suma_total: float = 0.0
    for numero in lista_numeros:
        suma_total += numero
    return suma_total / len(lista_numeros)


def main() -> None:
    """Punto de entrada principal del script."""
    numeros_ejemplo: list[int] = [1, 2, 3, 4, 5]
    promedio: float = calcular_promedio(numeros_ejemplo)
    print(promedio)


if __name__ == "__main__":
    main()