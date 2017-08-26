# Requerimientos
Para usar el siguiente script es necesario:
##### Version
- Python 3.6 (debido a que los diccionarios se ordenan por defecto)
##### Modulos
- Matplotlib
- Numpy
- Math

##### Opcional
Para la renderizacion de texto con latex es necesario instalar lo que se menciona en el siguiente articulo:

http://matplotlib.org/users/usetex.html

# Guia de uso
* Esta guia usa datos obtenidos experimentalmente *

1.- Ejecutar el script

`python minimos_cuadrados.py`

2.- Insertar las variables a usar y el numero de datos

![ScreenShot](https://raw.github.com/index-0/Regresion/master/Images/1.png)

3.- Ingresar los datos y la unidad correspondiente a las variables

| Distancia             | Tiempo                     |
|-----------------------|----------------------------|
| x<sub>1</sub> = 0.1 m | t<sub>1</sub> = 0.7805 s   |
| x<sub>2</sub> = 0.2 m | t<sub>2</sub> = 1.099 s    |
| x<sub>3</sub> = 0.3 m | t<sub>3</sub> = 1.3265 s   |
| x<sub>4</sub> = 0.4 m | t<sub>4</sub> = 1.51775 s  |
| x<sub>5</sub> = 0.5 m | t<sub>5</sub> = 1.7185 s   |
| x<sub>6</sub> = 0.6 m | t<sub>6</sub> = 1.8835 s   |
| x<sub>7</sub> = 0.7 m | t<sub>7</sub> = 2.048 s    |
| x<sub>8</sub> = 0.8 m | t<sub>8</sub> = 2.18775 s  |
| x<sub>9</sub> = 0.9 m | t<sub>9</sub> = 2.32175 s  |
| x<sub>10</sub> = 1 m  | t<sub>10</sub> = 2.44975 s |

![ScreenShot](https://raw.github.com/index-0/Regresion/master/Images/2.png)

4.- Visualizar la grafica de los datos (Opcional)

![ScreenShot](https://raw.github.com/index-0/Regresion/master/Images/figure_1.png)

5.- Decidir la ecuacion que desee

![ScreenShot](https://raw.github.com/index-0/Regresion/master/Images/3.png)

6.- Visualizar la grafica de la ecuacion obtenida (Opcional)

![ScreenShot](https://raw.github.com/index-0/Regresion/master/Images/figure_2.png)

7.- Se guardara un archivo .csv el cual contiene la hoja de calculos

![ScreenShot](https://raw.github.com/index-0/Regresion/master/Images/4.png)

# Acerca De La Practica

La practica constaba en un riel inclinado con una longuitud de 1.5 m, con uno de los extremos a una altura de 14.8 cm y el otro extremo a una altura de 19.4 cm.

h<sub>1</sub> = 14.8 cm

h<sub>2</sub> = 19.4 cm

Δh = h<sub>2</sub> - h<sub>1</sub> = 0.046 m

R = 1.5 m

Tomando los datos como un triangulo rectangulo donde R es la hipotenusa y la diferencia de altura es el cateto opuesto podemos usar la funcion seno para obtener el angulo de inclinacion.

θ = arcsin(Δh/R) = arcsin(0.046m/1.5m) = 1.757346093º

Como la ecuacion obtenida es:

x = at<sup>n</sup>

Se puede deducir que la ecuacion:

x(t) = 0.16726733794128215t<sup>2.0085135783055086</sup> ≈ 0.5gsen(θ)t<sup>2</sup>
