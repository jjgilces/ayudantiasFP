# Fundamentos de Programación
## Examen Segunda Evaluación 

#### Sobre el examen
Esta actividad está diseñada para evaluarlo en todos los conceptos revisados hasta el momento en la clase, incluyendo colecciones de datos, arreglos de Numpy y archivos.

### TEMA 1 (100 PUNTOS)
Asuma que tiene un archivo **"vacunacion.txt"** con los datos de vacunación desde el 01 de enero de 2021 al 31 de agosto de 2021 para varias ciudades del mundo. El archivo tendrá la estructura como en el siguiente ejemplo:

```
Etiquetas de filas y columnas
=============================
Vacunas:Pfizer,Sinovac,Astrazeneca,...,Cansino...
Ciudades:Bogota,Lima,Quito,La Paz,Santiago,Manizales,Dallas,New York City,...

Poblacion
=========
Bogota:11000000,Lima:10882000,Quito:1900500,La Paz:1880000,Santiago:23434000,...

Vacunacion
==========
Bogota;28-03-2021;Pfizer,157|Sinovac,103|Astrazeneca,109|Cansino,222
. . .
Bogota;29-05-2021;Pfizer,100|Sinovac,100|Astrazeneca,200|Cansino,180
. . .
```

Implemente las siguientes funciones:

1. `[30 puntos]` **cargarDatos(nomArchivo, mes)** que recibe el nombre del archivo con datos de vacunación y un número de mes. La función retorna una tupla con los siguientes datos:

 `a.` Vector con los nombres de todas las vacunas administradas (etiquetas de las filas)

 `b.` Vector con los nombres de todas las ciudades (etiquetas de las columnas)

 `c.` Vector con la población para cada una de las ciudades

 `d.` Matriz donde las filas representan las ciudades por región, las columnas representan las vacunas y las celdas representan el total de vacunas aplicadas en cada ciudad **solo para el mes** especificado en el parámetro. Ejemplo de la matriz:

```
                      +------+-------+-----------+-----+-------+-----+
                      |Pfizer|Sinovac|Astrazeneca|. . .|Cansino|. . .|
+------------+---------+------+-------+-----------+-----+-------+-----+
|            |Bogotá   | 257  |  203  |    109    |. . .|  222  |. . .|
|            +---------+------+-------+-----------+-----+-------+-----+
|            |Lima     | 122  |  154  |    208    |. . .|  279  |. . .|
|            +---------+------+-------+-----------+-----+-------+-----+
|            |Quito    | 176  |  228  |    157    |. . .|  166  |. . .|
|LatinAmerica+---------+------+-------+-----------+-----+-------+-----+
|            |  . . .  |. . . | . . . |   . . .   |. . .| . . . |. . .|
|            +---------+------+-------+-----------+-----+-------+-----+
|            |Santiago | 232  |  186  |    278    |. . .|   86  |. . .|
|            +---------+------+-------+-----------+-----+-------+-----+
|            |Manizales|  90  |  264  |    110    |. . .|  153  |. . .|
+------------+---------+------+-------+-----------+-----+-------+-----+
|            |Dallas   | 150  |  110  |    214    |. . .|  107  |. . .|
+NorteAmerica    +---------+------+-------+-----------+-----+-------+-----+
|            |New York | 157  |  144  |    116    |. . .|   82  |. . .|
+------------+---------+------+-------+-----------+-----+-------+-----+
|. . .       |  . . .  |. . . | . . . |   . . .   |. . .| . . . |. . .|
+------------+---------+------+-------+-----------+-----+-------+-----+
```

**Note que las líneas 3 y 4 del archivo contienen las etiquetas de las filas y columnas ya agrupadas y en el orden correcto.**

2. `[5 puntos]` **totalVacunados(nomArchivo, mesInicio, mesFin)** que recibe el nombre del archivo con datos de vacunación, un número de mes de inicio y un número de mes de fin. La función retorna una matriz con el total de vacunados entre los meses de inicio y fin. **Nota: la matriz resultante tiene la misma estructura que la matriz del tema 1.**

**Ayuda: recuerde usar la función del tema 1 en lugar de reescribir todo (y perder puntos así).**

3. `[10 puntos]` **masVacunados(nomArchivo, mes, N)** que recibe el nombre del archivo con datos de vacunación, un número de mes y un número entero. La función retorna una tupla con un elemento para cada vacuna. Cada elemento será un vector con los nombres de las **N** ciudades que más dosis de esa vacuna han recibido en el mes. **Los nombres de las ciudades deben estar ordenados descendentemente por cantidad de dosis.**

Ejemplo de retorno asumiendo un N=3 y 4 tipos de vacunas:
```
(array(["Guayaquil", "Manizales", "Bogotá"]), array(["Buenos Aires", "New York", "Cali"]), array(["Cali", "Miami", "Roma"]), array(["Paris", "Lima", "Montevideo"]))
```



Finalmente, en el programa principal:

5. `[2 puntos]` Usando alguna de las funciones anteriores, calcule la matriz de total de vacunados entre los meses de enero y agosto.
6. `[9 puntos]` Muestre por pantalla las ciudades en las que el total de vacunados entre los meses de enero y agosto, representa el 25% o más de la población (`porcentaje = total_vacunados/población`).
7. `[9 puntos]` De las ciudades del numeral anterior, muestre por pantalla la diferencia en el número de vacunados por ciudad entre el mes de **abril** y **junio**.
