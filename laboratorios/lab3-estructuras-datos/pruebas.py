import random
from estructuras import ListaEnlazada, TablaHash


def test_busqueda_basica() -> None:
    lista = ListaEnlazada()
    tabla = TablaHash(11)

    lista.insertar(1000000001, "en bodega")
    tabla.insertar(1000000001, "en bodega")

    assert lista.buscar(1000000001) == "en bodega"
    assert tabla.buscar(1000000001) == "en bodega"

    assert lista.buscar(9999999999) is None
    assert tabla.buscar(9999999999) is None


def test_colision_forzada() -> None:
    m = 7
    tabla = TablaHash(m)
    guias_colision = (10, 24, 17)

    for guia in guias_colision:
        assert tabla.hash(guia) == 3
        tabla.insertar(guia, f"estado_{guia}")

    for guia in guias_colision:
        assert tabla.buscar(guia) == f"estado_{guia}"

    assert tabla.buscar(99) is None
    assert tabla.casillas[3].tamano == 3
    assert tabla.factor_carga() == 3 / 7


def test_colecciones_aleatorias() -> None:
    azar = random.Random(42)
    estados = ("en bodega", "en reparto", "entregado", "cancelado")

    for _ in range(25):
        n = azar.randint(10, 100)
        m = azar.choice((7, 13, 19, 31, 53))

        lista = ListaEnlazada()
        tabla = TablaHash(m)

        guias_insertadas: list[int] = []
        for _ in range(n):
            guia = azar.randint(10**9, 10**10 - 1)
            estado = azar.choice(estados)
            lista.insertar(guia, estado)
            tabla.insertar(guia, estado)
            guias_insertadas.append(guia)

        assert lista.tamano == n
        assert tabla.tamano == n
        assert abs(tabla.factor_carga() - (n / m)) < 1e-9

        for guia in guias_insertadas:
            assert lista.buscar(guia) == tabla.buscar(guia)

        for _ in range(20):
            guia_inexistente = azar.randint(10**9, 10**10 - 1)
            if guia_inexistente not in guias_insertadas:
                assert lista.buscar(guia_inexistente) is None
                assert tabla.buscar(guia_inexistente) is None


if __name__ == "__main__":
    test_busqueda_basica()
    test_colision_forzada()
    test_colecciones_aleatorias()
    print("Todas las pruebas pasaron exitosamente.")
