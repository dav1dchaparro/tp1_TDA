import math
import random

import matplotlib.pyplot as plt

from tp1 import juego_monedas

random.seed(12345)


def generar_monedas(n, centro, dispersion):
    monedas = []
    for i in range(n):
        monedas.append(random.randint(centro - dispersion, centro + dispersion))
    return monedas


def desvio_estandar(valores):
    promedio = sum(valores) / len(valores)
    suma = 0
    for valor in valores:
        suma += (valor - promedio) ** 2
    return math.sqrt(suma / len(valores))


n = 200
centro = 1000
dispersiones = [0, 1, 2, 5, 10, 50, 100, 300, 600, 999]
repeticiones = 100

desvios = []
margenes = []
ultima_con_empates = 0

print("Variabilidad de los valores contra el margen de victoria del greedy")
print()
print("   %10s %10s %10s %9s" % ("dispersion", "desvio", "margen", "empates"))

for dispersion in dispersiones:
    suma_desvios = 0
    suma_margenes = 0
    empates = 0

    # con una sola fila de monedas sale cualquier cosa, por eso repito y promedio
    for prueba in range(repeticiones):
        monedas = generar_monedas(n, centro, dispersion)
        ganancia_sophia, ganancia_mateo, movimientos, monedas_sophia, monedas_mateo = juego_monedas(monedas)
        suma_desvios += desvio_estandar(monedas)
        suma_margenes += ganancia_sophia / (ganancia_sophia + ganancia_mateo)
        if ganancia_sophia == ganancia_mateo:
            empates += 1

    desvios.append(suma_desvios / repeticiones)
    margenes.append(suma_margenes / repeticiones)
    if empates > 0:
        ultima_con_empates = dispersion

    print("   %10d %10.1f %10.4f %8.0f%%" % (
        dispersion, desvios[-1], margenes[-1], 100 * empates / repeticiones))

print()
print("   el margen de Sophia pasa de %.3f a %.3f" % (margenes[0], margenes[-1]))
print("   hubo empates solo hasta dispersion %d" % ultima_con_empates)

plt.plot(desvios, margenes, "o-")
plt.axhline(0.5, color="gray", linestyle="--", label="empate")
plt.ylim(0.45, 0.75)
plt.title("Margen de Sophia segun la varianza de los valores (n = %d)" % n)
plt.xlabel("desvio estandar de los valores")
plt.ylabel("ganancia de Sophia / total")
plt.legend()
plt.grid()
plt.savefig("grafico_d.png")
print("   grafico_d.png")
