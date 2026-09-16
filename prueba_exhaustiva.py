from itertools import permutations
from tp1 import juego_monedas

def prueba_exhaustiva(n_min=2, n_max=8):
    total_general = 0
    victorias_general = 0
    empates_general = 0
    derrotas_general = 0

    print("Prueba exhaustiva de todas las permutaciones de 1..n")
    print()

    for n in range(n_min, n_max + 1):
        valores = list(range(1, n + 1))

        total = 0
        victorias = 0
        empates = 0
        derrotas = 0

        primer_empate = None
        primera_derrota = None

        # Genera TODAS las permutaciones posibles de [1, 2, ..., n]
        for permutacion in permutations(valores):
            suma_sophia, suma_mateo, _, _, _ = juego_monedas(list(permutacion))

            total += 1

            if suma_sophia > suma_mateo:
                victorias += 1
            elif suma_sophia == suma_mateo:
                empates += 1
                if primer_empate is None:
                    primer_empate = (permutacion, suma_sophia, suma_mateo)
            else:
                derrotas += 1
                if primera_derrota is None:
                    primera_derrota = (permutacion, suma_sophia, suma_mateo)

        total_general += total
        victorias_general += victorias
        empates_general += empates
        derrotas_general += derrotas

        print("n = %d: %d casos, %d victorias, %d empates, %d derrotas" % (
            n, total, victorias, empates, derrotas))

        # Si apareciera un contraejemplo, lo mostramos.
        if primer_empate is not None:
            p, s, m = primer_empate
            print("    Primer empate encontrado:", p, "Sophia =", s, "Mateo =", m)

        if primera_derrota is not None:
            p, s, m = primera_derrota
            print("    Primera derrota encontrada:", p, "Sophia =", s, "Mateo =", m)

    print()
    print("Total de configuraciones probadas: %d" % total_general)
    print("Victorias de Sophia: %d" % victorias_general)
    print("Empates: %d" % empates_general)
    print("Derrotas de Sophia: %d" % derrotas_general)
    print()

    if empates_general == 0 and derrotas_general == 0:
        print("Sophia gano en todos los casos probados.")
    else:
        print("Se encontraron casos en los que Sophia no gano.")


if __name__ == "__main__":
    prueba_exhaustiva(2, 8)
