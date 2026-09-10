"""Algoritmos de ordenamiento instrumentados para el Laboratorio 1."""


def insertion_sort(datos: list[int]) -> tuple[list[int], int]:
    """Ordena una lista de indices de riesgo con el metodo de insercion.

    Ordena de mayor a menor riesgo. No modifica la lista recibida:
    trabaja sobre una copia.

    Args:
        datos: lista de indices de riesgo a ordenar.

    Returns:
        Una tupla con la lista ordenada y el numero total de
        comparaciones entre elementos realizadas durante el proceso.
    """
    arr = datos.copy()
    comparaciones = 0
    n = len(arr)

    for i in range(1, n):
        clave = arr[i]
        j = i - 1
        while j >= 0:
            comparaciones += 1
            if arr[j] < clave:
                arr[j + 1] = arr[j]
                j -= 1
            else:
                break
        arr[j + 1] = clave

    return arr, comparaciones


def merge_sort(datos: list[int]) -> tuple[list[int], int]:
    """Ordena una lista de indices de riesgo con el metodo de mezcla.

    Ordena de mayor a menor riesgo. No modifica la lista recibida:
    trabaja sobre una copia.

    Args:
        datos: lista de indices de riesgo a ordenar.

    Returns:
        Una tupla con la lista ordenada y el numero total de
        comparaciones entre elementos realizadas durante el proceso.
    """
    arr = datos.copy()

    def _merge_sort_rec(lista: list[int]) -> tuple[list[int], int]:
        if len(lista) <= 1:
            return lista, 0

        medio = len(lista) // 2
        izq, comp_izq = _merge_sort_rec(lista[:medio])
        der, comp_der = _merge_sort_rec(lista[medio:])

        mezclada, comp_merge = _merge(izq, der)
        return mezclada, comp_izq + comp_der + comp_merge

    def _merge(izq: list[int], der: list[int]) -> tuple[list[int], int]:
        resultado: list[int] = []
        i = j = 0
        comp = 0

        while i < len(izq) and j < len(der):
            comp += 1
            if izq[i] >= der[j]:
                resultado.append(izq[i])
                i += 1
            else:
                resultado.append(der[j])
                j += 1

        resultado.extend(izq[i:])
        resultado.extend(der[j:])
        return resultado, comp

    return _merge_sort_rec(arr)