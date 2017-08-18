#!/usr/bin/env python

import math
import matplotlib.pyplot as plt
import numpy as np

__author__ = "Alfredo Perez"
__copyright__ = "Copyright 2017, Alfredo Perez"
__license__ = "GNU General Public License version 3"
__version__ = "0.04"
__email__ = "alfredoperez1998@protonmail.com"
__status__ = "Production"

# Variables de los colores
CGREEN = "\x1b[6;30;42m"
CRED = "\x1b[0;31;40m"
CCYAN = "\x1b[0;36;40m"
CERROR = "\x1b[1;30;41m"
CEND = "\x1b[0m"

print('Para finalizar el proceso presione Ctrl+Z en cualquier momento.')

array_x = {}
array_y = {}
x = []
y = []

n = int(input(CCYAN + "Inserte el numero de datos: " + CEND))

print(CRED + "Inserte 'r' para reingresar un valor." + CEND)

i = 0

while i <= (n - 1):
    dict_print = "Inserte x" + str(format(i + 1)) + ': '
    xinput = input(CCYAN + dict_print + CEND)
    if xinput == 'r':
        i = i - 1
    else:
        array_x['x{0}'.format(i + 1)] = eval(xinput)
        i = i + 1

print("")
i = 0

while i <= (n - 1):
    dict_print = "Inserte y" + str(format(i + 1)) + ': '
    yinput = input(CCYAN + dict_print + CEND)
    if yinput == 'r':
        i = i - 1
    else:
        array_y['y{0}'.format(i + 1)] = eval(yinput)
        i = i + 1

for i in array_x.values():
    x.append(i)

for i in array_y.values():
    y.append(i)

# Imprime los datos insertados
print('\tLos datos insertados fueron los siguientes:')
print("Numeros de datos = " + CGREEN + str(n) + CEND)
print('Las "x" insertadas;')
print(CGREEN + str(x) + CEND)
print('Las "y" insertadas;')
print(CGREEN + str(y) + CEND)

w_x = input(CCYAN + "Que clase de medida es x? " + CEND)
u_x = input(CCYAN + "Cual es su unidad? " + CEND)
w_y = input(CCYAN + "Que clase de medida es y? " + CEND)
u_y = input(CCYAN + "Cual es su unidad? " + CEND)

# Grafica
grafica = input(CCYAN + 'Quiere visualizar la grafica de los datos insertados?(y/n) ' + CEND)
if grafica == 'y':
    plt.plot(x, y)
    plt.xlabel(w_x.title() + "(" + u_x + ")")
    plt.ylabel(w_y.title() + "(" + u_y + ")")
    plt.plot(x, y, 'co')
    plt.title('Grafica')
    plt.show()

# Obtiene el logaritmo natural de las 2 listas
ln_x = [math.log(i) for i in x]
ln_y = [math.log(i) for i in y]

# Imprime los datos obtenidos sobre los logaritmos
print('\tLos logaritmos naturales de los datos obtenidos son los siguientes:')

print('Los logaritmos naturales de "x" son;')
print(CGREEN + str(ln_x) + CEND)

print('Los logaritmos naturales de "y" son;')
print(CGREEN + str(ln_y) + CEND)

# ln(x) * ln(y)
ln_xy = [a*b for a, b in zip(ln_x, ln_y)]

print('\tEl logaritmo natural de "x" por el logaritmo natural de "y" es igual a:')
print(CGREEN + str(ln_xy) + CEND)

# La suma de cada una de las listas
# Suma ln(x)
suma_ln_x = sum(ln_x)
print('La suma de los logaritmos naturales de "x" es:')
print(CGREEN + str(suma_ln_x) + CEND)

# Suma ln(y)
suma_ln_y = sum(ln_y)
print('La suma de los logaritmos naturales de "y" es:')
print(CGREEN + str(suma_ln_y) + CEND)

# Suma ln(x) * ln(y)
suma_ln_xy = sum(ln_xy)
print('La suma de la multiplicacion de los logaritmos naturales de "x" por los logaritmos naturales de "y" es:')
print(CGREEN + str(suma_ln_xy) + CEND)

x_o_y = input(CCYAN + "Para obtener la funcion x(y) inserte '1' " +
			  "y para obtener la funcion y(x) inserte '2'." + CEND)


def draw_l_graph(x, y):
    plt.plot(x, y)
    plt.xlabel(w_x.title() + "(" + u_x + ")")
    plt.ylabel(w_y.title() + "(" + u_y + ")")
    plt.title('Grafica')
    plt.show()

if x_o_y == '1':
    ln_x_cuadrado = [n ** 2 for n in ln_x]
    print("El cuadrado de los logaritmos naturales de 'x' es:")
    print(CGREEN + str(ln_x_cuadrado) + CEND)

    # Es la suma de los logaritmos naturales de "x" al cuadrado

    suma_ln_x_cuadrado = sum(ln_x_cuadrado)
    print('La suma de los logaritmos naturales de "x" al cuadrado es:')
    print(CGREEN + str(suma_ln_x_cuadrado) + CEND)

    # Pendiente
    m = (n * suma_ln_xy - suma_ln_x * suma_ln_y) / (
         n * suma_ln_x_cuadrado - suma_ln_x ** 2)
    print('La pendiente es igual a:')
    print('m = ' + CGREEN + str(m) + CEND)

    # Bisectriz
    b = (suma_ln_x_cuadrado * suma_ln_y - suma_ln_x * suma_ln_xy) / (
         n * suma_ln_x_cuadrado - suma_ln_x ** 2)
    print('La bisectriz es:')
    print('b = ' + CGREEN + str(b) + CEND)

    a = math.exp(b)
    print('El exponente (n) es: ' + CGREEN + str(m) + CEND)
    print('La constante (a) es: ' + CGREEN + str(a) + CEND)

    grafica = input(CCYAN + 'Quiere graficar la ecuacion obtenida? (y/n) ' + CEND)
    if grafica == 'y':
        val_p = input(CCYAN + 'Desea insertar valores personalizados?(y/n) ' + CEND)
        if val_p == 'y':
            rango_xi = eval(input(CCYAN + 'Inserte el valor inicial de "x" ' + CEND))
            rango_xf = eval(input(CCYAN + 'Inserte el valor final de "x" ' + CEND))
            delta_x = eval(input(CCYAN + 'Inserte la diferencia de distancia para "x" '+ CEND))
            x = np.arange(rango_xi, rango_xf, delta_x)
            y = []
        else:
            x = np.arange(0, max(x), 0.001)
            y = []
        for i in x:
            val_y = a * i ** m
            y.append(val_y)
        draw_l_graph(x, y)

    while True:
        x = eval(input(CCYAN + '\nInserte algun valor de "x": ' + CEND))
        y = a * x ** m
        print("\n" + str(a) + "*(" + str(x) + u_x + ")**" + str(m))
        print(w_y.title() + " = " + str(y) + u_y)

elif x_o_y == '2':
    ln_y_cuadrado = [n ** 2 for n in ln_y]
    print("El cuadrado de los logaritmos de 'y' es:")
    print(CGREEN + str(ln_y_cuadrado) + CEND)

    # Es la suma de los logaritmos de "y" al cuadrado

    suma_ln_y_cuadrado = sum(ln_y_cuadrado)
    print('La suma de los logaritmos de "y" al cuadrado es:')
    print(CGREEN + str(suma_ln_y_cuadrado) + CEND)

    # Pendiente
    m = (n * suma_ln_xy - suma_ln_y * suma_ln_x) / (
         n * suma_ln_y_cuadrado - suma_ln_y ** 2)
    print('La pendiente es igual a:')
    print('m = ' + CGREEN + str(m) + CEND)

    # Interseccion con eje y
    b = (suma_ln_y_cuadrado * suma_ln_x - suma_ln_y * suma_ln_xy) / (
         n * suma_ln_y_cuadrado - suma_ln_y ** 2)
    print('La interseccion con el eje y es:')
    print('b = ' + CGREEN + str(b) + CEND)

    a = math.exp(b)
    print('El exponente (n) es: ' + CGREEN + str(m) + CEND)
    print('La constante (a) es: ' + CGREEN + str(a) + CEND)

    grafica = input(CCYAN + 'Quiere graficar la ecuacion obtenida? (y/n) ' + CEND)
    if grafica == 'y':
        val_p = input(CCYAN + 'Desea insertar valores personalizados?(y/n) ' + CEND)
        if val_p == 'y':
            rango_yi = eval(input(CCYAN + 'Inserte el valor inicial de "y" ' + CEND))
            rango_yf = eval(input(CCYAN + 'Inserte el valor final de "y" ' + CEND))
            delta_y = eval(input(CCYAN + 'Inserte la diferencia de distancia entre puntos para el eje "y" ' + CEND))
            y = np.arange(rango_yi, rango_yf, delta_y)
            x = []
        else:
            y = np.arange(0, max(y), 0.001)
            x = []
        for i in y:
            val_x = a * i ** m
            x.append(val_x)
        draw_l_graph(x, y)

    while True:
        y = eval(input(CCYAN + '\nInserte algun valor de "y": ' + CEND))
        x = a * y ** m
        print(str(a) + "*(" + str(y) + u_y + ")**" + str(m))
        print(w_x.title() + " = " + str(x) + u_x)

else:
    quit(CERROR + 'Intente de nuevo e inserte un valor valido que sea "1" o "2" sin comillas.' + CEND)

