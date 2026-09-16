import random

from tp1 import juego_monedas

fallas = 0


def chequear(descripcion, condicion):
    global fallas
    if condicion:
        print("ok    ", descripcion)
    else:
        fallas += 1
        print("FALLA ", descripcion)


# Sophia nunca pierde, con cualquier cantidad de monedas y cualquier valor.
azar = random.Random(1)
nunca_pierde = True
for prueba in range(5000):
    monedas = []
    for j in range(azar.randint(1, 40)):
        monedas.append(azar.randint(1, 50))
    suma_sophia, suma_mateo, mov, m_sophia, m_mateo = juego_monedas(monedas)
    if suma_sophia < suma_mateo:
        nunca_pierde = False
        print("       contraejemplo:", monedas)
chequear("Sophia nunca pierde (5000 instancias al azar)", nunca_pierde)


# Si los valores son todos distintos, gana estricto: no empata.
azar = random.Random(2)
gana_estricto = True
for prueba in range(5000):
    monedas = azar.sample(range(1, 10000), azar.randint(1, 40))
    suma_sophia, suma_mateo, mov, m_sophia, m_mateo = juego_monedas(monedas)
    if suma_sophia <= suma_mateo:
        gana_estricto = False
        print("       contraejemplo:", monedas)
chequear("con valores distintos gana estricto (5000 instancias)", gana_estricto)


# Se reparten todas las monedas y las sumas cierran con el total.
azar = random.Random(3)
cierran = True
for prueba in range(1000):
    monedas = []
    for j in range(azar.randint(1, 50)):
        monedas.append(azar.randint(1, 100))
    suma_sophia, suma_mateo, mov, m_sophia, m_mateo = juego_monedas(monedas)
    if len(mov) != len(monedas):
        cierran = False
    if suma_sophia + suma_mateo != sum(monedas):
        cierran = False
chequear("se reparten todas las monedas y las sumas cierran", cierran)


# El ejemplo que usa el informe para mostrar que ganar no es maximizar.
suma_sophia, suma_mateo, mov, m_sophia, m_mateo = juego_monedas([10, 2, 5, 20, 50])
chequear("[10,2,5,20,50] da 75 a 12 con monedas [50,20,5]",
         suma_sophia == 75 and suma_mateo == 12 and m_sophia == [50, 20, 5])


# Casos borde.
suma_sophia, suma_mateo, mov, m_sophia, m_mateo = juego_monedas([42])
chequear("una sola moneda: se la lleva Sophia",
         suma_sophia == 42 and suma_mateo == 0)

suma_sophia, suma_mateo, mov, m_sophia, m_mateo = juego_monedas([3, 8])
chequear("dos monedas: Sophia se queda la mayor",
         suma_sophia == 8 and suma_mateo == 3)

suma_sophia, suma_mateo, mov, m_sophia, m_mateo = juego_monedas([7, 7, 7, 7])
chequear("todas iguales y n par: empata", suma_sophia == suma_mateo)

suma_sophia, suma_mateo, mov, m_sophia, m_mateo = juego_monedas([7, 7, 7])
chequear("todas iguales y n impar: gana Sophia", suma_sophia > suma_mateo)


print()
if fallas == 0:
    print("Pasaron todas las pruebas.")
else:
    print(fallas, "pruebas fallaron.")