# Trabajo Práctico 1: Los Algoritmos Greedy son juegos de niños

## Integrantes
* **Nicolas Llosas** - 105397 - [Email](mailto:nllosas@fi.uba.ar)
* **Joaquín Acevedo** - Padron/Legajo - [Email](mailto:racevedo@fi.uba.ar)
* **Juan David Chaparro** - Padron/Legajo - [Email](mailto:jchaparro@fi.uba.ar)


---

## 📌 Descripción del Proyecto
Este proyecto contiene la resolución del **Trabajo Práctico 1** de la materia. El objetivo es analizar, demostrar e implementar un **Algoritmo Greedy** óptimo para resolver el problema de la fila de monedas entre Sophia y Mateo. 

Dado que Sophia controla tanto sus decisiones como las de su hermano Mateo, el algoritmo utiliza un enfoque basado en el análisis de **paridades e índices estratégicos** para garantizar de forma matemática que Sophia **gane o empate siempre**, independientemente de si la cantidad de monedas (\(n\)) es par o impar.

La estructura del repositorio incluye:
* `tp1.py`: Código fuente principal con la lógica del algoritmo greedy optimizado.
* `informe.pdf`: Informe académico autocontenido detallando el análisis, la demostración de optimalidad y los análisis de complejidad temporal/espacial.
* `tests/`: Carpeta con sets de datos de prueba provistos y propios.

---

## 🚀 Instrucciones de Ejecución

El programa está desarrollado en **Python 3** y no requiere la instalación de dependencias externas para su ejecución principal.

Para ejecutar el algoritmo utilizando un archivo de entrada con el set de monedas, corra el siguiente comando desde la raíz del repositorio:

```bash
python3 tp1.py ruta/a/entrada.txt
```

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
