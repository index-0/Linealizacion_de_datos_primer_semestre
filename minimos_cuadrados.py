#!/usr/bin/env python

import sys
import csv
import math
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import rc, rcParams

__author__ = "Alfredo Perez"
__copyright__ = "Copyright 2017, Alfredo Perez"
__license__ = "GNU General Public License version 3"
__email__ = "alfredoperez1998@protonmail.com"

# Funciones


def draw_graph(x, y, graph, eq):
    latex = input("Desea usar LaTeX para renderizar el texto? (y/n) ")
    if latex == 'y':
        rc('text', usetex=True)
        rcParams['text.latex.preamble']=[r"\usepackage{amsmath}"]
        rcParams['axes.labelsize'] = 15
        if graph == 1:
            plt.plot(x, y, 'co')
            plt.title('Datos Obtenidos')
        else:
            plt.plot(x, y)
            plt.title(eq)
        plt.xlabel('$' + v_x + "(" + u_x + ")" + '$')
        plt.ylabel('$' + v_y + "(" + u_y + ")" + '$')
    else:
        if graph == 1:
            plt.plot(x, y, 'co')
            plt.title('Datos Obtenidos')
        else:
            plt.plot(x, y)
            plt.title(eq)
        plt.xlabel(v_x + "(" + u_x + ")")
        plt.ylabel(v_y + "(" + u_y + ")")
    plt.show()


def csv_file(rows):
    with open('practica.csv', 'w', encoding='utf8') as csvfile:
        writer = csv.writer(csvfile)
        for row in rows:
            writer.writerow(row)


def row_maker(v, x, y, ln_x, ln_y, ln_xy, ln_v_cuadrado):
    x.insert(0, v_x)
    y.insert(0, v_y)
    ln_x.insert(0, 'ln(' + v_x + ')')
    ln_y.insert(0, 'ln(' + v_y + ')')
    ln_xy.insert(0, 'ln(' + v_x + ')' + ' * ln(' + v_y + ')')
    ln_v_cuadrado.insert(0, 'ln(' + v + ')²')
    rows = zip(x, y, ln_x, ln_y, ln_xy, ln_v_cuadrado)
    return rows

# Variables de los colores
CGREEN = "\x1b[6;30;42m"
CRED = "\x1b[0;31;40m"
CCYAN = "\x1b[0;36;40m"
CERROR = "\x1b[1;30;41m"
CEND = "\x1b[0m"

print(CRED + 'Para finalizar el proceso presione Ctrl+Z en cualquier momento.' + CEND)

array_x = {}
array_y = {}
x = []
y = []

v_x = input("Inserte la primera variable a usar: ")
v_y = input("Inserte la segunda variable a usar: ")

n = int(input(CCYAN + "Inserte el numero de datos: " + CEND))

print(CRED + "Inserte 'r' para reingresar un valor." + CEND)

i = 0

while i <= (n - 1):
    dict_print = "Inserte " + v_x +  str(format(i + 1)) + ': '
    xinput = input(CCYAN + dict_print + CEND)
    if xinput == 'r':
        i = i - 1
    else:
        array_x[v_x + '{0}'.format(i + 1)] = eval(xinput)
        i = i + 1

print("")
i = 0

while i <= (n - 1):
    dict_print = "Inserte " + v_y + str(format(i + 1)) + ': '
    yinput = input(CCYAN + dict_print + CEND)
    if yinput == 'r':
        i = i - 1
    else:
        array_y[v_y + '{0}'.format(i + 1)] = eval(yinput)
        i = i + 1

for i in array_x.values():
    x.append(i)

for i in array_y.values():
    y.append(i)

max_x = max(x)
max_y = max(y)

# Imprime los datos insertados
print('\tLos datos insertados fueron los siguientes:')
print("Numeros de datos = " + CGREEN + str(n) + CEND)
print('Las "' + v_x +'" insertadas;')
print(CGREEN + str(x) + CEND)
print('Las "' + v_y + '" insertadas;')
print(CGREEN + str(y) + CEND)

u_x = input(CCYAN + "Inserte el tipo de unidad de " + v_x + ": " + CEND)
u_y = input(CCYAN + "Inserte el tipo de unidad de " + v_y + ": " + CEND)

# Grafica
grafica = input(CCYAN + 'Quiere visualizar la grafica de los datos insertados?(y/n) ' + CEND)
if grafica == 'y':
    draw_graph(x, y, 1, '')

# Obtiene el logaritmo natural de las 2 listas
ln_x = [math.log(i) for i in x]
ln_y = [math.log(i) for i in y]

# Imprime los datos obtenidos sobre los logaritmos
print('\tLos logaritmos naturales de los datos obtenidos son los siguientes:')

print('Los logaritmos naturales de "' + v_x + '" son;')
print(CGREEN + str(ln_x) + CEND)

print('Los logaritmos naturales de "' + v_y + '" son;')
print(CGREEN + str(ln_y) + CEND)

# ln(x) * ln(y)
ln_xy = [a*b for a, b in zip(ln_x, ln_y)]

print('\tEl logaritmo natural de "' + v_x + '" por el logaritmo natural de "' + v_y + '" es igual a:')
print(CGREEN + str(ln_xy) + CEND)

# La suma de cada una de las listas
# Suma ln(x)
suma_ln_x = sum(ln_x)
print('La suma de los logaritmos naturales de "' + v_x + '" es:')
print(CGREEN + str(suma_ln_x) + CEND)

# Suma ln(y)
suma_ln_y = sum(ln_y)
print('La suma de los logaritmos naturales de "' + v_y + '" es:')
print(CGREEN + str(suma_ln_y) + CEND)

# Suma ln(x) * ln(y)
suma_ln_xy = sum(ln_xy)
print('La suma de la multiplicacion de los logaritmos naturales de "' + v_x + '" por los logaritmos naturales de "' + v_y + '" es:')
print(CGREEN + str(suma_ln_xy) + CEND)

x_o_y = input(CCYAN + "Para obtener la funcion " + v_y + "(" + v_x + ") inserte '1' " +
                      "y para obtener la funcion " + v_x + "(" + v_y + ") inserte '2': " + CEND)


if x_o_y == '1':
    v = v_x
    ln_x_cuadrado = ln_v_cuadrado = [n ** 2 for n in ln_x]
    print('El cuadrado de los logaritmos naturales de "' + v_x + '" es:')
    print(CGREEN + str(ln_x_cuadrado) + CEND)

    # Es la suma de los logaritmos naturales de "x" al cuadrado

    suma_ln_x_cuadrado = suma_ln_v_cuadrado = sum(ln_x_cuadrado)
    print('La suma de los logaritmos naturales de "' + v_x + '" al cuadrado es:')
    print(CGREEN + str(suma_ln_x_cuadrado) + CEND)

    csv_file(row_maker(v, x, y, ln_x, ln_y, ln_xy, ln_v_cuadrado))
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

    eq = "$\ " + v_y + " = " + str(a) + v_x + " ^"+ str(m)
    grafica = input(CCYAN + 'Quiere graficar la ecuacion obtenida? (y/n) ' + CEND)
    if grafica == 'y':
        val_p = input(CCYAN + 'Desea insertar valores personalizados?(y/n) ' + CEND)
        if val_p == 'y':
            rango_xi = eval(input(CCYAN + 'Inserte el valor inicial de "' + v_x + '": ' + CEND))
            rango_xf = eval(input(CCYAN + 'Inserte el valor final de "' + v_x + '": ' + CEND))
            delta_x = eval(input(CCYAN + 'Inserte la diferencia de distancia para "' + v_x + '": '+ CEND))
            x = np.arange(rango_xi, rango_xf, delta_x)
            y = []
        else:
            x = np.arange(0, max_x, 0.001)
            y = []
        for i in x:
            val_y = a * i ** m
            y.append(val_y)
        draw_graph(x, y, 0, eq)

    while True:
        x = eval(input(CCYAN + '\nInserte algun valor de "' + v_x + '": ' + CEND))
        y = a * x ** m
        print(v_y + " = " + str(a) + "*(" + str(x) + u_x + ")**" + str(m))
        print(v_y + " = " + str(y) + u_y)

elif x_o_y == '2':
    v = v_y
    ln_y_cuadrado = ln_v_cuadrado = [n ** 2 for n in ln_y]
    print('El cuadrado de los logaritmos de "' + v_y + '" es:')
    print(CGREEN + str(ln_y_cuadrado) + CEND)

    # Es la suma de los logaritmos de "y" al cuadrado

    suma_ln_y_cuadrado = suma_ln_v_cuadrado = sum(ln_y_cuadrado)
    print('La suma de los logaritmos de "' + v_y + '" al cuadrado es:')
    print(CGREEN + str(suma_ln_y_cuadrado) + CEND)

    csv_file(row_maker(v, x, y, ln_x, ln_y, ln_xy, ln_v_cuadrado))
    # Pendiente
    m = (n * suma_ln_xy - suma_ln_y * suma_ln_x) / (
         n * suma_ln_y_cuadrado - suma_ln_y ** 2)
    print('La pendiente es igual a:')
    print('m = ' + CGREEN + str(m) + CEND)

    # Interseccion con eje y
    b = (suma_ln_y_cuadrado * suma_ln_x - suma_ln_y * suma_ln_xy) / (
         n * suma_ln_y_cuadrado - suma_ln_y ** 2)
    print('La bisectriz es:')
    print('b = ' + CGREEN + str(b) + CEND)

    a = math.exp(b)
    print('El exponente (n) es: ' + CGREEN + str(m) + CEND)
    print('La constante (a) es: ' + CGREEN + str(a) + CEND)

    eq = "$\ " + v_x + " = " + str(a) + v_y + " ^"+ str(m)
    grafica = input(CCYAN + 'Quiere graficar la ecuacion obtenida? (y/n) ' + CEND)
    if grafica == 'y':
        val_p = input(CCYAN + 'Desea insertar valores personalizados?(y/n) ' + CEND)
        if val_p == 'y':
            rango_yi = eval(input(CCYAN + 'Inserte el valor inicial de "' + v_y + '": ' + CEND))
            rango_yf = eval(input(CCYAN + 'Inserte el valor final de "' + v_y + '": ' + CEND))
            delta_y = eval(input(CCYAN + 'Inserte la diferencia de distancia para "' + v_y + '": ' + CEND))
            y = np.arange(rango_yi, rango_yf, delta_y)
            x = []
        else:
            y = np.arange(0, max_y, 0.001)
            x = []
        for i in y:
            val_x = a * i ** m
            x.append(val_x)
        draw_graph(x, y, 0, eq)

    while True:
        y = eval(input(CCYAN + '\nInserte algun valor de "' + v_y + '": ' + CEND))
        x = a * y ** m
        print(v_x + " = " + str(a) + "*(" + str(y) + u_y + ")**" + str(m))
        print(v_x + " = " + str(x) + u_x)

else:
    quit(CERROR + 'Intente de nuevo e inserte un valor valido que sea "1" o "2" sin comillas.' + CEND)

