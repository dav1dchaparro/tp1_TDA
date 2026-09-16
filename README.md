# Trabajo Práctico 1: Los Algoritmos Greedy son juegos de niños

## Integrantes
* **Nicolas Llosas** - 105397 - [Email](mailto:nllosas@fi.uba.ar)
* **Joaquín Acevedo** - Padron/Legajo - [Email](mailto:racevedo@fi.uba.ar)
* **Juan David Chaparro** - Padron/Legajo - [Email](mailto:jchaparro@fi.uba.ar)


---

## 📌 Descripción del Proyecto
Este proyecto contiene la resolución del **Trabajo Práctico 1** de la materia. El objetivo es analizar, demostrar e implementar un **Algoritmo Greedy** óptimo para resolver el problema de la fila de monedas entre Sophia y Mateo. 

Dado que Sophia controla tanto sus decisiones como las de su hermano Mateo, el algoritmo implementado utiliza la siguiente regla Greedy: **en su propio turno Sophia elige el mayor de los dos extremos disponibles y, en el turno de Mateo, le asigna el menor de los dos extremos disponibles**. Bajo la hipótesis del problema de que los valores de las monedas son distintos, esta estrategia garantiza que Sophia gane.

La estructura del repositorio incluye:
* `monedas.py`: implementación principal del algoritmo Greedy y lectura de los archivos de entrada.
* `pruebas.py`: conjunto de pruebas funcionales, aleatorias y casos borde para validar la implementación.
* `verificar.py`: verificación del algoritmo contra los casos y resultados esperados provistos por la cátedra.
* `mediciones.py`: mediciones de tiempos para distintos tamaños de entrada, ajuste por cuadrados mínimos y generación de gráficos.
* `informe.pdf`: Informe académico autocontenido detallando el análisis, la demostración de optimalidad y los análisis de complejidad temporal/espacial.
* `casos_catedra/`: Carpeta con sets de datos de prueba provistos por la cátedra.

---

## 🚀 Instrucciones de Ejecución

El programa está desarrollado en **Python 3**. La ejecución principal de `monedas.py`, `pruebas.py` y `verificar.py` no requiere dependencias externas. Para `mediciones.py` se utilizan las librerías `numpy` y `matplotlib`.

### Opción rápida: copiar y ejecutar todo junto

Se pueden ejecutar estos comandos directamente:

python3 -m venv .venv
source .venv/bin/activate
python -m pip install matplotlib numpy

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
python -m pip install matplotlib numpy
```

`matplotlib` se utiliza para generar los gráficos de las mediciones de tiempo, mientras que `numpy` se utiliza para los cálculos numéricos y los ajustes por cuadrados mínimos.

Cuando se termine de trabajar en el proyecto, el entorno virtual puede desactivarse con:

```bash
deactivate
```


### Ejecutar el algoritmo principal

Para ejecutar el algoritmo utilizando uno o más archivos de entrada con el set de monedas, correr el siguiente comando desde la raíz del repositorio:

```bash
python monedas.py ruta/a/entrada.txt
```

También pueden indicarse varios archivos:

```bash
python monedas.py entrada1.txt entrada2.txt entrada3.txt
```

### Ejecutar las pruebas funcionales

```bash
python pruebas.py
```

### Verificar los casos provistos por la cátedra

El script recibe como argumento la carpeta que contiene los archivos `20.txt`, `25.txt`, `50.txt`, `100.txt`, `1000.txt`, `10000.txt` y `20000.txt`:

```bash
python verificar.py casos_catedra
```

### Ejecutar las mediciones

Para realizar las mediciones de tiempos, los ajustes por cuadrados mínimos y generar los gráficos:

```bash
python mediciones.py
```

El script genera los archivos:

* `grafico_a.png`: tiempo de ejecución según la cantidad de monedas.
* `grafico_b.png`: tiempo según la variabilidad de los valores, manteniendo `n` fijo.
* `grafico_c.png`: tiempo según la magnitud de los valores, manteniendo `n` fijo.

### 📂 Formato de los Archivos

#### Archivo de Entrada (`entrada.txt`)
El archivo de entrada debe contener los valores de las monedas separados por comas o por espacios en una única línea:
```text
10, 25, 5, 1, 8, 20
```

#### Formato de la Salida por Consola
El programa imprimirá de forma cronológica cada una de las decisiones tomadas por Sophia (tanto para ella como para Mateo), finalizando con el recuento total de los puntajes:
```text
Sophia elige extremo izquierdo (Paridad): 10
Sophia obliga a Mateo a elegir extremo derecho: 20
Sophia elige extremo izquierdo (Paridad): 25
Sophia obliga a Mateo a elegir extremo izquierdo: 5
Sophia elige extremo derecho (Paridad): 8
Sophia obliga a Mateo a elegir extremo izquierdo: 1

--- Resultado Final ---
Resultado Sophia: 43
Resultado Mateo: 26
Ganadora: Sophia
```

---

## 📊 Resumen Técnico

* **Decisión Greedy Local:** En cada turno, el algoritmo evalúa la posición de los punteros actuales respecto a la paridad o índice objetivo calculado en la fase de inicialización global, reduciendo el tamaño del problema de manera lineal.
* **Complejidad Temporal:** $\mathcal{O}(n)$, donde $n$ es la cantidad total de monedas. El algoritmo realiza una única pasada inicial de pre-cálculo y luego un ciclo de remoción con punteros que toma exactamente $n$ pasos elementales de tiempo constante $\mathcal{O}(1)$.
* **Complejidad Espacial:** $\mathcal{O}(n)$ para almacenar el historial de pasos impreso al finalizar la ejecución ($\mathcal{O}(1)$ en memoria auxiliar de cómputo).

---

## 🛠️ Requisitos de Desarrollo (Opcional)
Si desea reproducir los experimentos, mediciones de tiempos o gráficos por cuadrados mínimos detallados en el informe, se requiere contar con las siguientes librerías de análisis de datos:

```bash
pip install numpy matplotlib
```
Para ejecutar el script de benchmarking (si aplica):
```bash
python3 benchmark.py
```
