import os
import sys

from tp1 import juego_monedas, leer_monedas

casos = ["20.txt", "25.txt", "50.txt", "100.txt", "1000.txt", "10000.txt", "20000.txt"]

if len(sys.argv) < 2:
    print("Uso: python3 verificar.py carpeta_con_los_casos [archivo_de_resultados_esperados]")
    sys.exit(1)

carpeta = sys.argv[1]
if len(sys.argv) > 2:
    archivo_esperados = sys.argv[2]
else:
    archivo_esperados = "Resultados Esperados.txt"

if not os.path.exists(archivo_esperados):
    print("No encuentro el archivo", archivo_esperados)
    sys.exit(1)


# El archivo de la catedra tiene, para cada caso, tres lineas seguidas: el
# nombre (a veces con un comentario despues), los movimientos separados por ";"
# y la ganancia de Sophia. Me quedo con eso y el resto lo salteo.
def leer_esperados(nombre_archivo):
    esperados = {}
    with open(nombre_archivo, encoding="utf-8") as archivo:
        lineas = archivo.read().split("\n")
    for j in range(len(lineas)):
        nombre = lineas[j].split(" ")[0]
        if nombre in casos:
            movimientos = []
            for parte in lineas[j + 1].split(";"):
                if parte.strip() != "":
                    movimientos.append(parte.strip())
            ganancia = int(lineas[j + 2].split(":")[1])
            esperados[nombre] = (movimientos, ganancia)
    return esperados


# Con n impar queda una sola moneda al final y la catedra aclara que da lo mismo
# decir "Primera" o "Ultima", asi que ese ultimo movimiento lo comparo aparte.
def mismos_movimientos(mov, mov_esperados):
    if len(mov) != len(mov_esperados):
        return False
    hasta = len(mov)
    if len(mov) % 2 == 1:
        hasta -= 1
        if not mov[-1].endswith("para Sophia") or not mov_esperados[-1].endswith("para Sophia"):
            return False
    return mov[:hasta] == mov_esperados[:hasta]


esperados = leer_esperados(archivo_esperados)
fallas = 0
coinciden = 0

print("%10s %8s %11s %11s %7s %10s %13s" % (
    "caso", "n", "Sophia", "Mateo", "gana", "ganancia", "movimientos"))

for caso in casos:
    monedas = leer_monedas(carpeta + "/" + caso)
    suma_sophia, suma_mateo, mov, m_sophia, m_mateo = juego_monedas(monedas)
    mov_esperados, ganancia_esperada = esperados[caso]

    if suma_sophia > suma_mateo:
        gana = "si"
    else:
        gana = "NO"
        fallas += 1

    if suma_sophia == ganancia_esperada:
        comparacion = "igual"
    else:
        comparacion = str(suma_sophia - ganancia_esperada)

    if mismos_movimientos(mov, mov_esperados):
        movimientos = "iguales"
        coinciden += 1
    else:
        movimientos = "DISTINTOS"

    print("%10s %8d %11d %11d %7s %10s %13s" % (
        caso, len(monedas), suma_sophia, suma_mateo, gana, comparacion, movimientos))

print()
if fallas == 0:
    print("Sophia gana en los 7 casos de la catedra.")
else:
    print("Sophia no gana en", fallas, "casos.")
print("Los movimientos coinciden con los de la catedra en", coinciden, "de 7 casos.")
