from itertools import permutations
from monedas import juego_monedas

def prueba_exhaustiva(n_min=2, n_max=8):
    total_general = 0
    victorias_general = 0
    empates_general = 0
    derrotas_general = 0

    print("Verificación exhaustiva del algoritmo Greedy")
    print("=" * 72)
    print(f"{'n':>3} | {'Casos':>10} | {'Victorias':>10} | {'Empates':>8} | {'Derrotas':>9}")
    print("-" * 72)

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
            suma_sofia, suma_mateo, _, _, _ = juego_monedas(list(permutacion))

            total += 1

            if suma_sofia > suma_mateo:
                victorias += 1
            elif suma_sofia == suma_mateo:
                empates += 1
                if primer_empate is None:
                    primer_empate = (permutacion, suma_sofia, suma_mateo)
            else:
                derrotas += 1
                if primera_derrota is None:
                    primera_derrota = (permutacion, suma_sofia, suma_mateo)

        total_general += total
        victorias_general += victorias
        empates_general += empates
        derrotas_general += derrotas

        print(
            f"{n:>3} | {total:>10} | {victorias:>10} | "
            f"{empates:>8} | {derrotas:>9}"
        )

        # Si apareciera un contraejemplo, lo mostramos.
        if primer_empate is not None:
            p, s, m = primer_empate
            print(f"    Primer empate encontrado: {p} -> Sophia={s}, Mateo={m}")

        if primera_derrota is not None:
            p, s, m = primera_derrota
            print(f"    Primera derrota encontrada: {p} -> Sophia={s}, Mateo={m}")

    print("-" * 72)
    print(f"Total de configuraciones probadas: {total_general}")
    print(f"Victorias de Sophia:             {victorias_general}")
    print(f"Empates:                         {empates_general}")
    print(f"Derrotas de Sophia:              {derrotas_general}")

    if empates_general == 0 and derrotas_general == 0:
        print("\nRESULTADO: Sophia ganó en todos los casos probados.")
    else:
        print("\nRESULTADO: Se encontraron casos en los que Sophia no ganó.")


if __name__ == "__main__":
    prueba_exhaustiva(2, 8)
