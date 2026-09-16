import random

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

from tp1 import juego_monedas

random.seed(12345)


def generar(n, centro, dispersion):
    monedas = []
    for j in range(n):
        monedas.append(random.randint(centro - dispersion, centro + dispersion))
    return monedas


def experimento():
    print("Variabilidad de los valores contra el margen de victoria del greedy")
    print()

    # n fijo y par, que es el caso donde puede haber empate.
    # probe tambien con 1000 y la curva da igual.
    n = 200
    centro = 1000
    dispersiones = [0, 1, 2, 5, 10, 50, 100, 300, 600, 999]
    repeticiones = 100

    desvios = []
    margenes = []
    ultima_con_empates = None

    print("   %10s %10s %10s %9s" % ("dispersion", "desvio", "margen", "empates"))
    for dispersion in dispersiones:
        suma_desvios = 0.0
        suma_margen = 0.0
        empates = 0
        # una sola instancia es ruido, promedio varias
        for prueba in range(repeticiones):
            monedas = generar(n, centro, dispersion)
            suma_sophia, suma_mateo, _, _, _ = juego_monedas(monedas)
            suma_desvios += float(np.std(monedas))
            suma_margen += suma_sophia / (suma_sophia + suma_mateo)
            if suma_sophia == suma_mateo:
                empates += 1

        desvios.append(suma_desvios / repeticiones)
        margenes.append(suma_margen / repeticiones)
        if empates > 0:
            ultima_con_empates = dispersion

        print("   %10d %10.1f %10.4f %8.0f%%" % (
            dispersion, desvios[-1], margenes[-1], 100.0 * empates / repeticiones))

    print()
    print("   el margen de Sophia pasa de %.3f a %.3f" % (margenes[0], margenes[-1]))
    print("   hubo empates solo hasta dispersion %d" % ultima_con_empates)

    figura, eje = plt.subplots(figsize=(8, 5))
    eje.plot(desvios, margenes, "o-", color="blue")
    eje.axhline(0.5, color="gray", linestyle="--", label="empate")
    eje.set_ylim(0.45, 0.75)
    eje.set_title("Margen de Sophia segun la varianza de los valores (n = %d)" % n)
    eje.set_xlabel("desvio estandar de los valores")
    eje.set_ylabel("ganancia de Sophia / total")
    eje.legend()
    eje.grid(alpha=0.3)
    figura.savefig("grafico_d.png", dpi=150, bbox_inches="tight")
    print("   grafico_d.png")


if __name__ == "__main__":
    experimento()
