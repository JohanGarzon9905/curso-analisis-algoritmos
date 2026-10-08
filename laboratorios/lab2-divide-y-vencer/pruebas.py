import random
from subarreglo import subarreglo_fuerza_bruta, subarreglo_maximo

serie_guia = [-3.0, 5.0, -2.0, 8.0, -6.0, 3.0, 9.0, -4.0]
res_fb_guia = subarreglo_fuerza_bruta(serie_guia)
res_dv_guia = subarreglo_maximo(serie_guia, 0, len(serie_guia) - 1)
assert res_fb_guia[2] == 17.0
assert res_dv_guia[2] == 17.0

serie_un_elemento = [42.0]
res_fb_uno = subarreglo_fuerza_bruta(serie_un_elemento)
res_dv_uno = subarreglo_maximo(serie_un_elemento, 0, 0)
assert res_fb_uno == (0, 0, 42.0)
assert res_dv_uno == (0, 0, 42.0)

serie_negativos = [-15.0, -8.0, -23.0, -4.0, -12.0]
res_fb_neg = subarreglo_fuerza_bruta(serie_negativos)
res_dv_neg = subarreglo_maximo(serie_negativos, 0, len(serie_negativos) - 1)
assert res_fb_neg[2] == -4.0
assert res_dv_neg[2] == -4.0

serie_positivos = [5.0, 10.0, 15.0, 20.0, 25.0]
res_fb_pos = subarreglo_fuerza_bruta(serie_positivos)
res_dv_pos = subarreglo_maximo(serie_positivos, 0, len(serie_positivos) - 1)
assert res_fb_pos[2] == 75.0
assert res_dv_pos[2] == 75.0

serie_cruzada = [4.0, -10.0, 8.0, 7.0, -3.0, 12.0, -20.0, 5.0]
res_fb_cruz = subarreglo_fuerza_bruta(serie_cruzada)
res_dv_cruz = subarreglo_maximo(serie_cruzada, 0, len(serie_cruzada) - 1)
assert res_fb_cruz[2] == 24.0
assert res_dv_cruz[2] == 24.0
assert res_dv_cruz[0] <= 3 < res_dv_cruz[1]

random.seed(12345)
for iteracion in range(50):
    tamano = random.randint(2, 60)
    lista_aleatoria = [float(random.randint(-50, 50)) for _ in range(tamano)]
    suma_fb = subarreglo_fuerza_bruta(lista_aleatoria)[2]
    suma_dv = subarreglo_maximo(lista_aleatoria, 0, tamano - 1)[2]
    assert abs(suma_fb - suma_dv) < 1e-9

print("Todas las pruebas pasaron exitosamente (incluidas 50 listas aleatorias).")
