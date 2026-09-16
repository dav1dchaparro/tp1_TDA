import sys


def juego_monedas(monedas):
    primera = 0
    ultima = len(monedas) - 1

    ganancia_sophia = 0
    ganancia_mateo = 0
    movimientos = []
    monedas_sophia = []
    monedas_mateo = []

    turno_sophia = True

    while primera <= ultima:
        if turno_sophia:
            if monedas[primera] > monedas[ultima]:
                ganancia_sophia += monedas[primera]
                monedas_sophia.append(monedas[primera])
                movimientos.append("Primera moneda para Sophia")
                primera += 1
            else:
                ganancia_sophia += monedas[ultima]
                monedas_sophia.append(monedas[ultima])
                movimientos.append("Última moneda para Sophia")
                ultima -= 1
        else:
            if monedas[primera] < monedas[ultima]:
                ganancia_mateo += monedas[primera]
                monedas_mateo.append(monedas[primera])
                movimientos.append("Primera moneda para Mateo")
                primera += 1
            else:
                ganancia_mateo += monedas[ultima]
                monedas_mateo.append(monedas[ultima])
                movimientos.append("Última moneda para Mateo")
                ultima -= 1

        turno_sophia = not turno_sophia

    return ganancia_sophia, ganancia_mateo, movimientos, monedas_sophia, monedas_mateo


def leer_monedas(nombre_archivo):
    monedas = []
    with open(nombre_archivo, encoding="utf-8") as archivo:
        for linea in archivo:
            if linea.startswith("#"):
                continue
            for valor in linea.split(";"):
                if valor.strip() != "":
                    monedas.append(int(valor))
    return monedas


def main():
    for nombre_archivo in sys.argv[1:]:
        monedas = leer_monedas(nombre_archivo)
        ganancia_sophia, ganancia_mateo, movimientos, monedas_sophia, monedas_mateo = juego_monedas(monedas)

        print(nombre_archivo)
        print("; ".join(movimientos))
        print("Monedas de Sophia:", monedas_sophia)
        print("Monedas de Mateo:", monedas_mateo)
        print("Ganancia de Sophia:", ganancia_sophia)
        print("Ganancia de Mateo:", ganancia_mateo)
        print()


if __name__ == "__main__":
    main()
