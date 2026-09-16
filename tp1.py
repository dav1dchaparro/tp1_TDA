import sys


def juego_monedas(monedas):
    i = 0
    k = len(monedas) - 1
    suma_sophia = 0
    suma_mateo = 0
    movimientos = []
    monedas_sophia = []
    monedas_mateo = []
    contador = 0
    while i <= k:
        if contador % 2 == 0:  # Turno de Sophia
            if monedas[i] > monedas[k]:
                suma_sophia += monedas[i]
                monedas_sophia.append(monedas[i])
                movimientos.append("Primera moneda para Sophia")
                i += 1
            else:
                suma_sophia += monedas[k]
                monedas_sophia.append(monedas[k])
                movimientos.append("Última moneda para Sophia")
                k -= 1
        else:                  # Turno de Mateo (Sophia elige la más chica)
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
        contador += 1
    return suma_sophia, suma_mateo, movimientos, monedas_sophia, monedas_mateo


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


def main():
    for nombre_archivo in sys.argv[1:]:
        monedas = leer_monedas(nombre_archivo)
        suma_sophia, suma_mateo, movimientos, monedas_sophia, monedas_mateo = juego_monedas(monedas)

        print(nombre_archivo)
        print("; ".join(movimientos))
        print("Monedas de Sophia:", monedas_sophia)
        print("Monedas de Mateo:", monedas_mateo)
        print("Ganancia de Sophia:", suma_sophia)
        print("Ganancia de Mateo:", suma_mateo)
        print()


if __name__ == "__main__":
    main()
