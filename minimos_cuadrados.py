#!/usr/bin/env python

import math
import matplotlib.pyplot as plt
import numpy as np

__author__ = "Alfredo Perez"
__copyright__ = "Copyright 2017, Alfredo Perez"
__license__ = "GNU General Public License version 3"
__version__ = "0.01"
__maintainer__ = "Alfredo Perez"
__email__ = "alfredoperez1998@gmail.com"
__status__ = "Production"


print("Para finalizar el codigo inserte 'q' en cualquier dato de entrada.")

array_x = {}
array_y = {}
x = []
y = []

n = int(input("Cual es el numero de datos que quiere linealizar?"))

for i in range(1, n + 1):
    dict_print = "Inserte x" + str(format(i)) + ': '
    array_x['x{0}'.format(i)] = eval(input(dict_print))

print(array_x)

for i in range(1, n + 1):
    dict_print = "Inserte y" + str(format(i)) + ': '
    array_y['y{0}'.format(i)] = eval(input(dict_print))

print(array_y)

for i in array_x.values():
    x.append(i)

for i in array_y.values():
    y.append(i)

# Imprime los datos insertados
print('\tLos datos insertados fueron los siguientes:')
print("Numeros de datos = " + str(n))
print('Las "x" insertadas;')
print(x)
print('Las "y" insertadas;')
print(y)

w_x = input("Que es x?")
u_x = input("Cual es su unidad?")
w_y = input("Que es y?")
u_y = input("Cual es su unidad?")

# Grafica
grafica = input('Quiere visualizar la grafica de los datos insertados?(y/n)')
if grafica == 'y':
    plt.plot(x, y)
    plt.xlabel(w_x.title() + "(" + u_x + ")")
    plt.ylabel(w_y.title() + "(" + u_y + ")")
    plt.plot(x, y, 'co')
    plt.title('Grafica')
    plt.show()
elif grafica == 'q':
    quit('Programa finalizado')

# Obtiene el logaritmo natural de las 2 listas
ln_x = [math.log(i) for i in x]
ln_y = [math.log(i) for i in y]

# Imprime los datos obtenidos sobre los logaritmos
print('\tLos logaritmos naturales de los datos obtenidos son los siguientes:')

print('Los logaritmos naturales de "x" son;')
print(ln_x)

print('Los logaritmos naturales de "y" son;')
print(ln_y)

# ln(x) * ln(y)
ln_xy = [a*b for a, b in zip(ln_x, ln_y)]

print('\tEl logaritmo natural de "x" por el logaritmo natural de "y" es igual a:')
print(ln_xy)

# La suma de cada una de las listas
# Suma ln(x)
suma_ln_x = sum(ln_x)
print('La suma de los logaritmos naturales de "x" es:')
print(suma_ln_x)

# Suma ln(y)
suma_ln_y = sum(ln_y)
print('La suma de los logaritmos naturales de "y" es:')
print(suma_ln_y)

# Suma ln(x) * ln(y)
suma_ln_xy = sum(ln_xy)
print('La suma de la multiplicacion de los logaritmos naturales de "x" por los logaritmos naturales de "y":')
print(suma_ln_xy)

x_o_y = input("\tQuiere usar x(inserte 'x' sin comillas) o y(inserte 'y' sin comillas)"
              "; si inserta x en la ecuacion linealizada obtendra 'y' y viceversa.")


def draw_l_graph(x, y):
    plt.plot(x, y)
    plt.xlabel(w_x.title() + "(" + u_x + ")")
    plt.ylabel(w_y.title() + "(" + u_y + ")")
    plt.title('Grafica')
    plt.show()

if x_o_y == "x":
    ln_x_cuadrado = [n ** 2 for n in ln_x]
    print("El cuadrado de los logaritmos naturales de 'x' es:")
    print(ln_x_cuadrado)

    # Es la suma de los logaritmos naturales de "x" al cuadrado

    suma_ln_x_cuadrado = sum(ln_x_cuadrado)
    print('La suma de los logaritmos naturales de "x" al cuadrado es:')
    print(suma_ln_x_cuadrado)

    # Pendiente
    m = (n * suma_ln_xy - suma_ln_x * suma_ln_y) / (
         n * suma_ln_x_cuadrado - suma_ln_x ** 2)
    print('La pendiente es igual a:')
    print('m = ' + str(m))

    # Bisectriz
    b = (suma_ln_x_cuadrado * suma_ln_y - suma_ln_x * suma_ln_xy) / (
         n * suma_ln_x_cuadrado - suma_ln_x ** 2)
    print('La bisectriz es:')
    print('b = ' + str(b))

    a = math.exp(b)
    print('El exponente (n) es: ' + str(m))
    print('La constante (a) es: ' + str(a))

    grafica = input('Quiere graficar la ecuacion obtenida? (y/n)')
    if grafica == 'y':
        val_p = input('Desea insertar valores personalizados?(y/n)')
        if val_p == 'y':
            rango_xi = eval(input('Inserte el valor inicial de "x"'))
            rango_xf = eval(input('Inserte el valor final de "x"'))
            delta_x = eval(input('Inserte la diferencia de distancia para "x"'))
            x = np.arange(rango_xi, rango_xf, delta_x)
            y = []
        elif grafica == 'q':
            quit('Programa finalizado')
        else:
            x = np.arange(0, max(x), 0.001)
            y = []
        for i in x:
            val_y = a * i ** m
            y.append(val_y)
        draw_l_graph(x, y)
    elif grafica == 'q':
            quit('Programa finalizado')

    while True:
        x = eval(input('\nInserte algun valor de "x".'))
        y = a * x ** m
        print("\n" + str(a) + "*(" + str(x) + u_x + ")**" + str(m))
        print(w_y.title() + " = " + str(y))

elif x_o_y == "y":
    ln_y_cuadrado = [n ** 2 for n in ln_y]
    print("El cuadrado de los logaritmos de 'y' es:")
    print(ln_y_cuadrado)

    # Es la suma de los logaritmos de "y" al cuadrado

    suma_ln_y_cuadrado = sum(ln_y_cuadrado)
    print('La suma de los logaritmos de "y" al cuadrado es:')
    print(suma_ln_y_cuadrado)

    # Pendiente
    m = (n * suma_ln_xy - suma_ln_y * suma_ln_x) / (
         n * suma_ln_y_cuadrado - suma_ln_y ** 2)
    print('La pendiente es igual a:')
    print('m = ' + str(m))

    # Interseccion con eje y
    b = (suma_ln_y_cuadrado * suma_ln_x - suma_ln_y * suma_ln_xy) / (
         n * suma_ln_y_cuadrado - suma_ln_y ** 2)
    print('La interseccion con el eje y es:')
    print('b = ' + str(b))

    a = math.exp(b)
    print('El exponente de la ecuacion es (n): ' + str(m))
    print('a = ' + str(a))

    grafica = input('Quiere graficar la ecuacion obtenida? (y/n)')
    if grafica == 'y':
        val_p = input('Desea insertar valores personalizados?(y/n)')
        if val_p == 'y':
            rango_yi = eval(input('Inserte el valor inicial de "y"'))
            rango_yf = eval(input('Inserte el valor final de "y"'))
            delta_y = eval(input('Inserte la diferencia de distancia entre puntos para el eje "y"'))
            y = np.arange(rango_yi, rango_yf, delta_y)
            x = []
        elif val_p == 'q':
            quit('Programa finalizado')
        else:
            y = np.arange(0, max(y), 0.001)
            x = []
        for i in y:
            val_x = a * i ** m
            x.append(val_x)
        draw_l_graph(x, y)
    elif grafica == 'q':
        quit('Programa finalizado')

    while True:
        y = eval(input('\nInserte algun valor de "y".'))
        x = a * y ** m
        print(str(a) + "*(" + str(y) + u_y + ")**" + str(m))
        print(w_x.title() + " = " + str(x) + u_x)

elif x_o_y == 'q':
    quit('Programa finalizado')

else:
    quit('Intente de nuevo e inserte un valor valido que sea "x" o "y".')
