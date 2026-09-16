# Trabajo Práctico 1: Los Algoritmos Greedy son juegos de niños

## Integrantes
* **Nicolas Llosas** - 105397 - [Email](mailto:nllosas@fi.uba.ar)
* **Joaquín Acevedo** - 89863 - [Email](mailto:racevedo@fi.uba.ar)
* **Juan David Chaparro** - Padron/Legajo - [Email](mailto:jchaparro@fi.uba.ar)


---

## 📌 Descripción del Proyecto
Este proyecto contiene la resolución del **Trabajo Práctico 1** de la materia. El objetivo es analizar, demostrar e implementar un **Algoritmo Greedy** óptimo para resolver el problema de la fila de monedas entre Sophia y Mateo. 

Dado que Sophia controla tanto sus decisiones como las de su hermano Mateo, el algoritmo implementado utiliza la siguiente regla Greedy: **en su propio turno Sophia elige el mayor de los dos extremos disponibles y, en el turno de Mateo, le asigna el menor de los dos extremos disponibles**. Bajo la hipótesis del problema de que los valores de las monedas son distintos, esta estrategia garantiza que Sophia gane.

La estructura del repositorio incluye:
* `tp1.py`: implementación principal del algoritmo Greedy y lectura de los archivos de entrada.
* `tp1`: ejecutable que llama a `tp1.py`, para poder correr `./tp1 entrada.txt`.
* `pruebas.py`: conjunto de pruebas funcionales, aleatorias y casos borde para validar la implementación.
* `verificar.py`: verificación del algoritmo contra los casos y resultados esperados provistos por la cátedra.
* `mediciones.py`: mediciones de tiempos para distintos tamaños de entrada, ajuste por cuadrados mínimos y generación de gráficos.
* `prueba_exhaustiva.py`: prueba exhaustiva de todas las permutaciones de los valores `1, ..., n` para `2 <= n <= 8`.
* `casos_catedra/`: Carpeta con sets de datos de prueba provistos por la cátedra.

---

## 🚀 Instrucciones de Ejecución

El programa está desarrollado en **Python 3**. La ejecución principal de `tp1.py`, `pruebas.py`, `verificar.py` y `prueba_exhaustiva.py` no requiere dependencias externas. Para `mediciones.py` se utilizan las librerías `numpy` y `matplotlib`.

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

### 📂 Formato de los Archivos

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

## 📊 Resumen Técnico

* **Decisión Greedy Local:** En cada turno de Sophia se compara el valor de los dos extremos y se elige el mayor. En el turno de Mateo, Sophia compara nuevamente los extremos disponibles y le asigna el menor.
* **Complejidad Temporal:** $\mathcal{O}(n)$ y, más precisamente, $\Theta(n)$, donde $n$ es la cantidad total de monedas. El algoritmo procesa exactamente una moneda por iteración y cada decisión requiere operaciones de costo constante $\mathcal{O}(1)$.
* **Complejidad Espacial:** $\mathcal{O}(n)$ si se consideran las listas utilizadas para guardar movimientos y monedas asignadas a cada jugador. La memoria auxiliar necesaria únicamente para tomar las decisiones mediante los índices es $\mathcal{O}(1)$.

---

## 🛠️ Reproducir experimentos

Para reproducir los experimentos, mediciones de tiempos o gráficos por cuadrados mínimos detallados en el informe, se requiere crear y activar el entorno virtual e instalar `numpy` y `matplotlib` como se indicó anteriormente:

```bash
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install matplotlib numpy
```

Luego, ejecutar:

```bash
python3 mediciones.py
```
