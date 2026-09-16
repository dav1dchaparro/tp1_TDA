# Trabajo Practico 1: Los Algoritmos Greedy son juegos de niños

## Integrantes
* Nicolas Llosas - 105397 - [Email](mailto:nllosas@fi.uba.ar)
* Joaquín Acevedo - 89863 - [Email](mailto:racevedo@fi.uba.ar)
* Juan David Chaparro - 111481 - [Email](mailto:jchaparro@fi.uba.ar)

---

## De que se trata

El TP es un juego entre Sophia y su hermano Mateo. Hay una fila de monedas con distintos valores. En cada turno un jugador saca una moneda, pero solo puede sacar la primera o la ultima de la fila. Empieza Sophia, despues Mateo, y asi se van turnando hasta que no quedan monedas. Gana el que junta mas valor. Sophia juega por los dos, o sea que tambien decide que moneda le toca a Mateo, y tiene que asegurarse de ganar.

La regla greedy que usamos es simple:

* En el turno de Sophia, se queda con la punta mas grande.
* En el turno de Mateo, le da la punta mas chica.

Con esta regla Sophia nunca pierde. Si ademas los valores son todos distintos, como dice el enunciado, gana siempre. Si hay valores repetidos y la cantidad de monedas es par puede haber empate. Por ejemplo, si la cantidad de monedas es par y todas valen lo mismo, siempre empatan, sin importar como se juegue, y por eso el enunciado descarta ese caso.

Ganar no es lo mismo que sacar lo maximo posible. El algoritmo asegura ganar, pero no siempre le da a Sophia la mayor ganancia que podria sacar. Por ejemplo, con las monedas `10;2;5;20;50` Sophia saca 75 y Mateo 12, pero jugando distinto Sophia podria llegar a 80. En el informe se explica esto con mas detalle.

---

## Archivos del repositorio

* `tp1.py`: el algoritmo y la lectura del archivo de entrada.
* `tp1`: ejecutable que llama a `tp1.py`, para poder correr `./tp1 entrada.txt`.
* `pruebas.py`: pruebas con monedas al azar y casos borde.
* `verificar.py`: corre los casos de la catedra y compara con los resultados esperados.
* `prueba_exhaustiva.py`: prueba todas las permutaciones de `1, ..., n` con `n` entre 2 y 8.
* `mediciones.py`: mide tiempos, ajusta por cuadrados minimos y genera los graficos.
* `variabilidad.py`: mide como cambia el margen de Sophia segun la variabilidad de los valores.
* `TP1___Teoria_de_algoritmos_2c_2026.pdf`: el informe del TP.
* `casos_catedra/`: los casos de prueba que dio la catedra.
* `Resultados Esperados.txt`: los resultados de la catedra para esos casos.

---

## Como ejecutar

Todo esta hecho en Python 3. Para correr `tp1.py`, `pruebas.py`, `verificar.py` y `prueba_exhaustiva.py` no hace falta instalar nada. Para `mediciones.py` y `variabilidad.py` hacen falta `numpy` y `matplotlib`.

### Preparar el entorno (solo para `mediciones.py` y `variabilidad.py`)

Desde la carpeta del repositorio:

```bash
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install matplotlib numpy
```

Al terminar, se sale del entorno con `deactivate`.

### Correr el algoritmo

```bash
python3 tp1.py ruta/a/entrada.txt
```

O con el ejecutable, que hace lo mismo:

```bash
./tp1 ruta/a/entrada.txt
```

Se pueden pasar varios archivos a la vez:

```bash
python3 tp1.py entrada1.txt entrada2.txt
```

### Correr las pruebas

```bash
python3 pruebas.py
```

### Verificar los casos de la catedra

Hay que correrlo desde la carpeta del repositorio. Recibe la carpeta con los archivos `20.txt`, `25.txt`, `50.txt`, `100.txt`, `1000.txt`, `10000.txt` y `20000.txt`. Lee `Resultados Esperados.txt` y compara la ganancia de Sophia y los movimientos, uno por uno, con los de la catedra. Si se quiere usar otro archivo de resultados se pasa como segundo argumento.

```bash
python3 verificar.py casos_catedra
```

Muestra una tabla con una fila por caso: cuantas monedas tiene, la ganancia de cada jugador, si Sophia gano, si su ganancia es igual a la de la catedra y si los movimientos son iguales. Al final dice si Sophia gano en los 7 casos y en cuantos coincidieron los movimientos.

### Correr la prueba exhaustiva

Genera todas las permutaciones de `1, ..., n` con `n` de 2 a 8 y se fija que Sophia gane en todas. Como son permutaciones, los valores son todos distintos.

```bash
python3 prueba_exhaustiva.py
```

### Correr las mediciones

```bash
python3 mediciones.py
```

Para las mediciones no hay archivos de casos: el mismo script arma las monedas al azar con una semilla fija, asi que siempre salen las mismas. Genera tres graficos:

* `grafico_a.png`: tiempo segun la cantidad de monedas.
* `grafico_b.png`: tiempo segun la varianza de los valores, con `n` fijo.
* `grafico_c.png`: tiempo segun que tan grandes son los valores, con `n` fijo.

Los graficos ya estan subidos al repo, asi que no hace falta correr el script para verlos.

### Correr el experimento de variabilidad

El enunciado pide ver si la variabilidad de los valores afecta al algoritmo. Como el algoritmo nunca pierde, lo que medimos es por cuanto gana: que parte del total se lleva Sophia. Se usan 200 monedas con valores al azar alrededor de 1000. Se prueba con una dispersion cada vez mas grande. Para cada dispersion se arman 100 filas de monedas al azar y se promedia el resultado.

```bash
python3 variabilidad.py
```

Genera `grafico_d.png`, que muestra el margen de Sophia segun el desvio estandar de los valores. Tambien esta subido al repo.

Lo que se ve: con dispersion 0 todas las monedas son iguales y el margen es 0.5, o sea empate. Con dispersion 1 ya no hubo ningun empate en las 100 filas. Despues el margen crece casi en linea recta con el desvio, hasta 0.707 con valores entre 1 y 1999. La variabilidad no cambia si Sophia gana, sino por cuanto gana. Si se cambia `n` a 1000 en el codigo, la curva sale igual.

---

## Formato de los archivos

### Entrada

Es un archivo de texto con los valores de las monedas separados por punto y coma. Las lineas que empiezan con `#` se ignoran, como las que traen los archivos de la catedra.

```text
10;25;5;1;8;20
```

### Salida

El programa imprime primero el nombre del archivo que se le paso. Despues imprime en orden cada decision de Sophia, para ella y para Mateo, y al final las monedas y la ganancia de cada uno. Si se pasan varios archivos, deja una linea en blanco entre uno y otro:

```text
entrada.txt
Última moneda para Sophia; Última moneda para Mateo; Primera moneda para Sophia; Última moneda para Mateo; Primera moneda para Sophia; Última moneda para Mateo
Monedas de Sophia: [20, 10, 25]
Monedas de Mateo: [8, 1, 5]
Ganancia de Sophia: 55
Ganancia de Mateo: 14
```

Cuando la salida dice primera o ultima moneda, se refiere a las puntas de la fila que va quedando, no a la posicion en la fila original. Si las dos puntas valen lo mismo se saca la ultima. Con este criterio la salida coincide con la de la catedra.

---

## Resumen

* En cada turno se comparan las dos puntas. Sophia se queda con la mayor, y a Mateo le da la menor.
* Tiempo: O(n), con n la cantidad de monedas. Se saca una moneda por vuelta y cada vuelta hace una comparacion y una suma.
* Memoria: O(n) por las listas de movimientos y de monedas de cada uno. Para decidir solo hacen falta los dos indices de las puntas.
* Variabilidad de los valores: no cambia el tiempo. El tiempo cambia cuando los valores son enormes, porque comparar y sumar numeros de muchos digitos tarda mas. Eso se ve en `grafico_c.png`.
