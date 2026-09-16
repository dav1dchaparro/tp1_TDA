import random
import time

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

from tp1 import juego_monedas

random.seed(12345)


def medir(monedas):
    tiempos = []
    for prueba in range(10):
        desde = time.perf_counter()
        juego_monedas(monedas)
        hasta = time.perf_counter()
        tiempos.append((hasta - desde) * 1000)
    return min(tiempos)


def lineal(n):
    return n


def n_log_n(n):
    return n * np.log2(n)


def cuadratico(n):
    return n * n


def ajustar(tamanios, tiempos, modelo):
    n = np.array(tamanios, dtype=float)
    A = np.column_stack([modelo(n), np.ones(len(n))])
    b = np.array(tiempos, dtype=float)
    coeficientes = np.linalg.lstsq(A, b, rcond=None)[0]
    error = float(np.sum((b - A @ coeficientes) ** 2))
    return coeficientes, error


def experimento_a():
    print("A) tiempo segun la cantidad de monedas")

    tamanios = list(range(10000, 260000, 10000))

    orden = list(tamanios)
    random.shuffle(orden)
    medidos = {}
    for n in orden:
        monedas = list(range(1, n + 1))
        random.shuffle(monedas)
        medidos[n] = medir(monedas)

    tiempos = []
    for n in tamanios:
        tiempos.append(medidos[n])

    modelos = [("lineal", lineal), ("n log n", n_log_n), ("cuadratico", cuadratico)]

    print()
    for nombre, modelo in modelos:
        coeficientes, error = ajustar(tamanios, tiempos, modelo)
        print("   %-12s error = %9.3f" % (nombre, error))

    coeficientes, error = ajustar(tamanios, tiempos, lineal)
    print()
    print("   recta ajustada: t(n) = %.3e * n + %.3e ms" % (coeficientes[0], coeficientes[1]))
    print("   costo por moneda: %.1f ns" % (coeficientes[0] * 1000000))

    primeros = tiempos[0] / tamanios[0]
    ultimos = tiempos[-1] / tamanios[-1]
    print("   t/n crecio %.1f %% (n log n pediria %.1f %%)" % (
        (ultimos / primeros - 1) * 100,
        (np.log2(tamanios[-1]) / np.log2(tamanios[0]) - 1) * 100))

    figura, eje = plt.subplots(figsize=(8, 5))
    eje.plot(tamanios, tiempos, "o", color="blue", label="mediciones")
    n = np.array(tamanios, dtype=float)
    for nombre, modelo in modelos:
        coeficientes, error = ajustar(tamanios, tiempos, modelo)
        A = np.column_stack([modelo(n), np.ones(len(n))])
        eje.plot(n, A @ coeficientes, "-", label="%s (error %.2f)" % (nombre, error))
    eje.set_title("Tiempo de ejecucion segun la cantidad de monedas")
    eje.set_xlabel("cantidad de monedas n")
    eje.set_ylabel("tiempo [ms]")
    eje.legend()
    eje.grid(alpha=0.3)
    figura.savefig("grafico_a_tiempo_vs_n.png", dpi=150, bbox_inches="tight")
    print("   grafico_a_tiempo_vs_n.png")


def experimento_b():
    print()
    print("B) tiempo segun la varianza de los valores, con n fijo")
    print()

    n = 150000
    centro = 500000
    dispersiones = [0, 1, 100, 10000, 100000, 499999]

    desvios = []
    tiempos = []
    for dispersion in dispersiones:
        monedas = []
        for j in range(n):
            monedas.append(random.randint(centro - dispersion, centro + dispersion))
        desvios.append(float(np.std(monedas)))
        tiempos.append(medir(monedas))
        print("   dispersion +-%6d   desvio %9.1f   t = %7.3f ms" % (
            dispersion, desvios[-1], tiempos[-1]))

    print()
    print("   los tiempos varian %.1f %%" % (
        (max(tiempos) - min(tiempos)) / np.mean(tiempos) * 100))

    figura, eje = plt.subplots(figsize=(8, 5))
    eje.plot(desvios, tiempos, "o-", color="green")
    eje.set_ylim(0, max(tiempos) * 1.4)
    eje.set_title("Tiempo segun la varianza de los valores (n = %d)" % n)
    eje.set_xlabel("desvio estandar de los valores")
    eje.set_ylabel("tiempo [ms]")
    eje.grid(alpha=0.3)
    figura.savefig("grafico_b_tiempo_vs_varianza.png", dpi=150, bbox_inches="tight")
    print("   grafico_b_tiempo_vs_varianza.png")


def experimento_c():
    print()
    print("C) tiempo segun la magnitud de los valores, con n fijo")
    print()

    n = 120000
    exponentes = [3, 9, 15, 19, 30, 60, 150, 300, 600]

    orden = list(exponentes)
    random.shuffle(orden)
    medidos = {}
    for exponente in orden:
        monedas = []
        for j in range(n):
            monedas.append(random.randint(10 ** exponente, 10 ** (exponente + 1)))
        medidos[exponente] = medir(monedas)

    bits = []
    tiempos = []
    for exponente in exponentes:
        bits.append((10 ** exponente).bit_length())
        tiempos.append(medidos[exponente])
        print("   valores ~ 10^%-3d (%5d bits)   t = %7.3f ms" % (
            exponente, bits[-1], tiempos[-1]))

    print()
    print("   de %d bits a %d bits: %.2f veces mas lento" % (
        bits[0], bits[-1], tiempos[-1] / tiempos[0]))

    figura, eje = plt.subplots(figsize=(8, 5))
    eje.plot(bits, tiempos, "o-", color="red")
    eje.set_xscale("log", base=2)
    eje.set_title("Tiempo segun la magnitud de los valores (n = %d)" % n)
    eje.set_xlabel("tamano de los valores [bits]")
    eje.set_ylabel("tiempo [ms]")
    eje.grid(alpha=0.3)
    figura.savefig("grafico_c_tiempo_vs_magnitud.png", dpi=150, bbox_inches="tight")
    print("   grafico_c_tiempo_vs_magnitud.png")


if __name__ == "__main__":
    experimento_a()
    experimento_b()
    experimento_c()
