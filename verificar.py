import sys

from monedas import juego_monedas, leer_monedas

# Las ganancias que trae el archivo "Resultados Esperados.txt" de la catedra.
esperadas = {
    "20.txt": 7165,
    "25.txt": 9635,
    "50.txt": 17750,
    "100.txt": 35009,
    "1000.txt": 357814,
    "10000.txt": 3550307,
    "20000.txt": 7139357,
}

if len(sys.argv) < 2:
    print("Uso: python3 verificar.py carpeta_con_los_casos")
    sys.exit(1)

carpeta = sys.argv[1]
fallas = 0

print("      caso        n      Sophia       Mateo    gana   referencia")

for caso in ["20.txt", "25.txt", "50.txt", "100.txt",
             "1000.txt", "10000.txt", "20000.txt"]:
    monedas = leer_monedas(carpeta + "/" + caso)
    suma_sophia, suma_mateo, mov, m_sophia, m_mateo = juego_monedas(monedas)

    if suma_sophia > suma_mateo:
        gana = "si"
    else:
        gana = "NO"
        fallas += 1

    if suma_sophia == esperadas[caso]:
        comparacion = "igual"
    else:
        comparacion = str(suma_sophia - esperadas[caso])

    print("%10s %8d %11d %11d %7s %12s" % (
        caso, len(monedas), suma_sophia, suma_mateo, gana, comparacion))

print()
if fallas == 0:
    print("Sophia gana en los 7 casos de la catedra.")
else:
    print("Sophia no gana en", fallas, "casos.")