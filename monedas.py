import sys


def juego_monedas(monedas):
    i = 0
    k = len(monedas) - 1
    suma_sofia = 0
    suma_mateo = 0
    movimientos = []
    monedas_sofia = []
    monedas_mateo = []
    turno_de_sophia = True
    while i <= k:
        if turno_de_sophia:
            if monedas[i] > monedas[k]:
                suma_sofia += monedas[i]
                monedas_sofia.append(monedas[i])
                movimientos.append("Primera moneda para Sophia")
                i += 1
            else:
                suma_sofia += monedas[k]
                monedas_sofia.append(monedas[k])
                movimientos.append("Última moneda para Sophia")
                k -= 1
        else:
            if monedas[i] < monedas[k]:
                suma_mateo += monedas[i]
                monedas_mateo.append(monedas[i])
                movimientos.append("Primera moneda para Mateo")
                i += 1
            else:
                suma_mateo += monedas[k]
                monedas_mateo.append(monedas[k])
                movimientos.append("Última moneda para Mateo")
                k -= 1
        turno_de_sophia = not turno_de_sophia
    return suma_sofia, suma_mateo, movimientos, monedas_sofia, monedas_mateo


def leer_monedas(nombre_archivo):
    monedas = []
    with open(nombre_archivo, encoding="utf-8") as archivo:
        for linea in archivo:
            if linea.startswith("#"):
                continue
            for parte in linea.split(";"):
                if parte.strip() != "":
                    monedas.append(int(parte))
    return monedas


if __name__ == "__main__":
    for nombre_archivo in sys.argv[1:]:
        monedas = leer_monedas(nombre_archivo)
        suma_sofia, suma_mateo, movimientos, monedas_sofia, monedas_mateo = juego_monedas(monedas)

        print(nombre_archivo)
        print("; ".join(movimientos))
        print("Monedas de Sophia:", monedas_sofia)
        print("Monedas de Mateo:", monedas_mateo)
        print("Ganancia de Sophia:", suma_sofia)
        print("Ganancia de Mateo:", suma_mateo)
        print()