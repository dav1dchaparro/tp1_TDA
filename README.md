# Trabajo Práctico 1: Los Algoritmos Greedy son juegos de niños

## Integrantes
* **Nicolas Llosas** - 105397 - [Email](mailto:nllosas@fi.uba.ar)
* **Joaquín Acevedo** - 89863 - [Email](mailto:racevedo@fi.uba.ar)
* **Juan David Chaparro** - Padron/Legajo - [Email](mailto:jchaparro@fi.uba.ar)

---

## 📌 Descripción del Proyecto

Este proyecto contiene la resolución del **Trabajo Práctico 1** de la materia. El objetivo es analizar, demostrar e implementar un **Algoritmo Greedy** óptimo para resolver el problema de la fila de monedas entre Sophia y Mateo.

Dado que Sophia controla tanto sus decisiones como las de su hermano Mateo, el algoritmo implementado utiliza la siguiente regla Greedy: **en su propio turno Sophia elige el mayor de los dos extremos disponibles y, en el turno de Mateo, le asigna el menor de los dos extremos disponibles**.

Esta estrategia garantiza que Sophia **nunca pierda**, sin necesidad de ninguna hipótesis sobre los valores de las monedas. Si además los valores son distintos entre sí, como plantea el enunciado, la victoria es **estricta**. La distinción es relevante en la práctica: los casos de prueba más grandes provistos por la cátedra tienen muchos valores repetidos (`20000.txt` contiene 20.000 monedas que toman solamente 991 valores distintos), de modo que allí aplica el resultado general y no el estricto. Sophia gana igual en los siete casos.

Es importante señalar que *ganar* y *obtener el máximo posible* son objetivos distintos, y el algoritmo cumple el primero. Por ejemplo, con la instancia `[10, 2, 5, 20, 50]` la regla le asigna a Sophia un total de 75 contra 12 de Mateo, cuando el máximo alcanzable para ella sería 80. El informe desarrolla este punto.

La estructura del repositorio incluye:

* `monedas.py`: implementación principal del algoritmo Greedy y lectura de los archivos de entrada.
* `pruebas.py`: pruebas de las propiedades demostradas en el informe, sobre instancias aleatorias, más casos borde y los contraejemplos que el informe cita.
* `verificar.py`: verificación del algoritmo contra los casos y resultados esperados provistos por la cátedra.
* `prueba_exhaustiva.py`: prueba exhaustiva de todas las permutaciones de los valores `1, ..., n` para `2 <= n <= 8`.
* `mediciones.py`: mediciones de tiempos, ajuste por cuadrados mínimos y generación de gráficos.
* `informe.pdf`: informe académico autocontenido con el análisis, la demostración de optimalidad y los análisis de complejidad temporal y espacial.
* `casos_catedra/`: sets de datos de prueba provistos por la cátedra.

---

## 🚀 Instrucciones de Ejecución

El programa está desarrollado en **Python 3**. La ejecución de `monedas.py`, `pruebas.py`, `verificar.py` y `prueba_exhaustiva.py` **no requiere dependencias externas**. Únicamente `mediciones.py` necesita `numpy` y `matplotlib`.

### Preparar el entorno (solo necesario para las mediciones)

Desde la raíz del repositorio:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install matplotlib numpy
```

`matplotlib` se utiliza para generar los gráficos y `numpy` para los cálculos numéricos y los ajustes por cuadrados mínimos. Al terminar, el entorno virtual puede desactivarse con `deactivate`.

### Ejecutar el algoritmo principal

Para ejecutar el algoritmo con uno o más archivos de entrada:

```bash
python monedas.py ruta/a/entrada.txt
```

También pueden indicarse varios archivos:

```bash
python monedas.py entrada1.txt entrada2.txt entrada3.txt
```

### Ejecutar las pruebas

```bash
python pruebas.py
```

### Verificar los casos provistos por la cátedra

El script recibe como argumento la carpeta que contiene los archivos `20.txt`, `25.txt`, `50.txt`, `100.txt`, `1000.txt`, `10000.txt` y `20000.txt`:

```bash
python verificar.py casos_catedra
```

Imprime una tabla con la ganancia de cada jugador en cada caso y comprueba que Sophia gane en todos.

### Ejecutar la prueba exhaustiva

Genera todas las permutaciones de los valores `1, ..., n` para `n` entre 2 y 8 y verifica que Sophia gane en cada una. Al ser permutaciones los valores son distintos, de modo que corresponde el caso estricto del teorema:

```bash
python prueba_exhaustiva.py
```

### Ejecutar las mediciones

```bash
python mediciones.py
```

El script genera los archivos:

* `grafico_a.png`: tiempo de ejecución según la cantidad de monedas.
* `grafico_b.png`: tiempo según la varianza de los valores dentro de una instancia, con `n` fijo.
* `grafico_c.png`: tiempo según la magnitud de los valores entre instancias, con `n` fijo.

---

## 📂 Formato de los Archivos

### Archivo de Entrada

El archivo de entrada debe contener los valores de las monedas separados por punto y coma (`;`). Pueden incluirse líneas de comentario que comiencen con `#`, como las que traen los archivos de la cátedra.

```text
10;25;5;1;8;20
```

### Formato de la Salida por Consola

El programa imprime cronológicamente cada una de las decisiones tomadas por Sophia, tanto para ella como para Mateo, junto con las monedas y ganancias finales de ambos jugadores:

```text
entrada.txt
Última moneda para Sophia; Última moneda para Mateo; Primera moneda para Sophia; Última moneda para Mateo; Primera moneda para Sophia; Última moneda para Mateo
Monedas de Sophia: [20, 10, 25]
Monedas de Mateo: [8, 1, 5]
Ganancia de Sophia: 55
Ganancia de Mateo: 14
```

Las etiquetas `Primera` y `Última` indican de qué extremo de la fila **vigente** se retira cada moneda, no la posición en el arreglo original. Cuando los dos extremos tienen el mismo valor se toma el último; la elección es indistinta para el resultado, pero se fija un criterio para que el algoritmo sea determinista, y éste es el que reproduce exactamente las salidas de referencia de la cátedra.

---

## 📊 Resumen Técnico

* **Decisión Greedy local:** en cada turno de Sophia se comparan los dos extremos y se elige el mayor. En el turno de Mateo se comparan nuevamente los extremos disponibles y se le asigna el menor.
* **Por qué es Greedy:** el óptimo local es la diferencia que cada ronda aporta al marcador, y la métrica global se descompone aditivamente en esas diferencias. Garantizar el signo de cada aporte local alcanza para garantizar el resultado global.
* **Complejidad temporal:** $\mathcal{O}(n)$ y, más precisamente, $\Theta(n)$, donde $n$ es la cantidad de monedas. El algoritmo procesa exactamente una moneda por iteración y cada decisión requiere operaciones de costo constante.
* **Complejidad espacial:** $\mathcal{O}(n)$ considerando las listas de movimientos y de monedas asignadas a cada jugador. La memoria auxiliar necesaria únicamente para tomar las decisiones, mediante los dos índices, es $\mathcal{O}(1)$.
* **Variabilidad de los valores:** no afecta el tiempo en el modelo de costo uniforme. Con enteros de precisión arbitraria, en cambio, comparar y sumar cuestan proporcional a la cantidad de dígitos, y el tiempo total pasa a ser $\Theta(n \log v)$ con $v$ el mayor valor. El experimento C lo comprueba empíricamente.