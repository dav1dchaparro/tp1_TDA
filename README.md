# Trabajo Práctico 1: Los Algoritmos Greedy son juegos de niños

## Integrantes
* Nicolas Llosas - 105397 - [Email](mailto:nllosas@fi.uba.ar)
* Joaquín Acevedo - 89863 - [Email](mailto:racevedo@fi.uba.ar)
* Juan David Chaparro - 111481 - [Email](mailto:jchaparro@fi.uba.ar)


---

## Descripcion del proyecto
Este proyecto contiene la resolución del Trabajo Práctico 1 de la materia. El objetivo es analizar, demostrar e implementar un algoritmo Greedy óptimo para resolver el problema de la fila de monedas entre Sophia y Mateo.

Dado que Sophia controla tanto sus decisiones como las de su hermano Mateo, el algoritmo implementado utiliza la siguiente regla Greedy: en su propio turno Sophia elige el mayor de los dos extremos disponibles y, en el turno de Mateo, le asigna el menor de los dos extremos disponibles. Bajo la hipótesis del problema de que los valores de las monedas son distintos, esta estrategia garantiza que Sophia gane.

Conviene aclarar qué quiere decir óptimo acá, porque se presta a confusión. Óptimo quiere decir que asegura la victoria, que es lo que pide el enunciado. No quiere decir que maximice la ganancia de Sophia: con la entrada `3;1;2;4;5` el algoritmo le saca 11 sobre un total de 15, y el máximo alcanzable era 12.

El teorema completo es: con valores positivos, y además n impar o los n valores todos distintos, se garantiza que Sophia saque estrictamente más que Mateo. Sin ninguna hipótesis extra se garantiza que saque al menos lo mismo, o sea que Sophia nunca pierde.

Con n par y valores repetidos puede haber empate. Algunos empates son inevitables para cualquier estrategia: la familia `x; y; ...; y; x` con n par y x <= y, que incluye el caso de monedas todas iguales que el enunciado permite descartar. Otros sí serían evitables, por ejemplo `1;2;3;3;2;1`, donde el algoritmo termina 6 a 6 y existe un reparto 7 a 5.

La estructura del repositorio incluye:
* `tp1.py`: implementación principal del algoritmo Greedy y lectura de los archivos de entrada.
* `tp1`: ejecutable que llama a `tp1.py`, para poder correr `./tp1 entrada.txt`.
* `pruebas.py`: conjunto de pruebas funcionales, aleatorias y casos borde para validar la implementación.
* `verificar.py`: verificación del algoritmo contra los casos y resultados esperados provistos por la cátedra.
* `mediciones.py`: mediciones de tiempos para distintos tamaños de entrada, ajuste por cuadrados mínimos y generación de gráficos.
* `prueba_exhaustiva.py`: prueba exhaustiva de todas las permutaciones de los valores `1, ..., n` para `2 <= n <= 8`.
* `variabilidad.py`: experimento de cómo afecta la variabilidad de los valores al margen con el que gana Sophia.
* `casos_catedra/`: Carpeta con sets de datos de prueba provistos por la cátedra.

---

## Instrucciones de ejecucion

El programa está desarrollado en Python 3. La ejecución principal de `tp1.py`, `pruebas.py`, `verificar.py` y `prueba_exhaustiva.py` no requiere dependencias externas. Para `mediciones.py` y `variabilidad.py` se utilizan las librerías `numpy` y `matplotlib`.

### Opción rápida: copiar y ejecutar todo junto

Se pueden ejecutar estos comandos directamente:

python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install matplotlib numpy

o bien, por separado, según:

### Crear y activar el entorno virtual

Desde la raíz del repositorio, crear el entorno virtual con:

```bash
python3 -m venv .venv
```

Activarlo con:

```bash
source .venv/bin/activate
```

Con el entorno virtual activado, instalar las dependencias necesarias para las mediciones y los gráficos:

```bash
python3 -m pip install matplotlib numpy
```

`matplotlib` se utiliza para generar los gráficos de las mediciones de tiempo, mientras que `numpy` se utiliza para los cálculos numéricos y los ajustes por cuadrados mínimos.

Cuando se termine de trabajar en el proyecto, el entorno virtual puede desactivarse con:

```bash
deactivate
```


### Ejecutar el algoritmo principal

Para ejecutar el algoritmo utilizando uno o más archivos de entrada con el set de monedas, correr el siguiente comando desde la raíz del repositorio:

```bash
python3 tp1.py ruta/a/entrada.txt
```

También puede usarse el ejecutable, que hace lo mismo:

```bash
./tp1 ruta/a/entrada.txt
```

También pueden indicarse varios archivos:

```bash
python3 tp1.py entrada1.txt entrada2.txt entrada3.txt
```

### Ejecutar las pruebas funcionales

```bash
python3 pruebas.py
```

### Verificar los casos provistos por la cátedra

El script recibe como argumento la carpeta que contiene los archivos `20.txt`, `25.txt`, `50.txt`, `100.txt`, `1000.txt`, `10000.txt` y `20000.txt`:

```bash
python3 verificar.py casos_catedra
```

### Ejecutar la prueba exhaustiva

La prueba exhaustiva genera todas las permutaciones posibles de los valores `1, ..., n` para `n` entre 2 y 8 y verifica que Sophia gane en cada caso:

```bash
python3 prueba_exhaustiva.py
```

### Ejecutar las mediciones

Para realizar las mediciones de tiempos, los ajustes por cuadrados mínimos y generar los gráficos:

```bash
python3 mediciones.py
```

El script genera los archivos:

* `grafico_a_tiempo_vs_n.png`: tiempo de ejecución según la cantidad de monedas.
* `grafico_b_tiempo_vs_varianza.png`: tiempo según la variabilidad de los valores, manteniendo `n` fijo.
* `grafico_c_tiempo_vs_magnitud.png`: tiempo según la magnitud de los valores, manteniendo `n` fijo.

### Ejecutar el experimento de variabilidad contra optimalidad

El enunciado pide analizar si la variabilidad de los valores afecta la optimalidad del algoritmo. Como óptimo acá quiere decir asegurar la victoria, lo que se mide es el margen: qué fracción del total se lleva Sophia. Se fija `n = 200`, se generan monedas al azar alrededor de 1000 con dispersión creciente, y se promedian 100 instancias por punto:

```bash
python3 variabilidad.py
```

Genera `grafico_d_margen_vs_varianza.png`: margen de Sophia según el desvío estándar de los valores.

Lo que sale: con dispersión 0 (todas las monedas iguales) el margen es exactamente 0.5, o sea empate, que es el caso que el enunciado permite descartar. Con dispersión 1 ya no hubo ningún empate en las 100 instancias. De ahí en adelante el margen crece casi linealmente con el desvío, hasta 0.707 con valores entre 1 y 1999. La variabilidad no cambia si Sophia gana, que está garantizado, sino cuánto gana. Probamos también con `n = 1000` y la curva es la misma.

### Formato de los archivos

#### Archivo de Entrada (`entrada.txt`)
El archivo de entrada debe contener los valores de las monedas separados por punto y coma (`;`). También pueden incluirse líneas de comentario que comiencen con `#`.

```text
10;25;5;1;8;20
```

#### Formato de la Salida por Consola
El programa imprimirá de forma cronológica cada una de las decisiones tomadas por Sophia (tanto para ella como para Mateo), junto con las monedas y ganancias finales de ambos jugadores:

```text
entrada.txt
Última moneda para Sophia; Última moneda para Mateo; Primera moneda para Sophia; Última moneda para Mateo; Primera moneda para Sophia; Última moneda para Mateo
Monedas de Sophia: [20, 10, 25]
Monedas de Mateo: [8, 1, 5]
Ganancia de Sophia: 55
Ganancia de Mateo: 14
```

---

## Resumen tecnico

La decisión Greedy es local: en cada turno de Sophia se compara el valor de los dos extremos y se elige el mayor, y en el turno de Mateo se compara de nuevo y se le asigna el menor.

La complejidad temporal es O(n), y más precisamente Theta(n), donde n es la cantidad total de monedas. El algoritmo procesa exactamente una moneda por iteración y cada decisión son unas pocas comparaciones, que cuestan O(1).

La complejidad espacial es O(n) si se cuentan las listas de movimientos y de monedas de cada jugador. La memoria auxiliar que hace falta solo para decidir, que son los dos índices, es O(1).

---

## Reproducir experimentos

Para reproducir los experimentos, mediciones de tiempos o gráficos por cuadrados mínimos detallados en el informe, se requiere crear y activar el entorno virtual e instalar `numpy` y `matplotlib` como se indicó anteriormente:

```bash
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install matplotlib numpy
```

Luego, ejecutar:

```bash
python3 mediciones.py
python3 variabilidad.py
```
