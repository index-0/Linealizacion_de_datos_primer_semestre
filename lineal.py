#!/usr/bin/env python

from funciones import draw_graph, csv_file, row_maker
import math
import numpy as np
from colors import *

def lineal(d):

    suma_x = sum(d['x'])
    print('La sumatoria de "' + d['v_x'] + '" es:')
    print(CGREEN + str(suma_x) + CEND)

    suma_y = sum(d['y'])
    print('La sumatoria de "' + d['v_y'] + '" es:')
    print(CGREEN + str(suma_y) + CEND)

    prom_x = suma_x / d['n']
    print('El promedio de "' + d['v_x'] + '" es:')
    print(CGREEN + str(prom_x) + CEND)

    prom_y = suma_y / d['n']
    print('El promedio de "' + d['v_y'] + '" es:')
    print(CGREEN + str(prom_y) + CEND)

    xy = [a*b for a, b in zip(d['x'], d['y'])]
    print(d['v_x'] + '*' + d['v_y'] + ' es:')
    print(CGREEN + str(xy) + CEND)

    suma_xy = sum(xy)
    print('La suma de ' + d['v_x'] + '*' + d['v_y'] + ' es:')
    print(CGREEN + str(suma_xy) + CEND)

    x_o_y = input(CCYAN + "Para obtener la funcion " + d['v_y'] + "(" + d['v_x'] + ") inserte '1' " + "y para obtener la funcion " + d['v_x'] + "(" + d['v_y'] + ") inserte '2': " + CEND)
    if x_o_y == '1':
        v = d['v_x']
        print('Las "' + d['v_x'] + '" al cuadrado son:')
        x_cuadrado = [i ** 2 for i in d['x']]
        print(CGREEN + str(x_cuadrado) + CEND)

        suma_x_cuadrado = sum(x_cuadrado)
        print('La suma de las "' + d['v_x'] + '" al cuadrado es:')
        print(CGREEN + str(suma_x_cuadrado) + CEND)

        a = (suma_xy - d['n'] * prom_x * prom_y) / (suma_x_cuadrado - d['n'] * prom_x ** 2)
        b = prom_y - a * prom_x

        print('La constante (a) es: ' + CGREEN + str(a) + CEND)
        print('La bicectriz (b) es: ' + CGREEN + str(b) + CEND)

        eq = "$\ " + d['v_y'] + " = " + str(a) + d['v_x'] + " + " + str(b)

        grafica = input(CCYAN + 'Quiere graficar la ecuacion obtenida? (y/n) ' + CEND)
        if grafica == 'y':
            val_p = input(CCYAN + 'Desea insertar valores personalizados?(y/n) ' + CEND)
            if val_p == 'y':
                rango_xi = eval(input(CCYAN + 'Inserte el valor inicial de "' + d['v_x'] + '": ' + CEND))
                rango_xf = eval(input(CCYAN + 'Inserte el valor final de "' + d['v_x'] + '": ' + CEND))
                delta_x = eval(input(CCYAN + 'Inserte la diferencia de distancia para "' + d['v_x'] + '": '+ CEND))
                x = np.arange(rango_xi, rango_xf, delta_x)
                y = []
            else:
                x = np.arange(0, d['max_x'], 0.001)
                y = []
            for i in x:
                val_y = a * i + b
                y.append(val_y)
            draw_graph(x, y, 0, eq, d['v_x'], d['v_y'], d['u_x'], d['u_y'])

        while True:
            x = eval(input(CCYAN + '\nInserte algun valor de "' + d['v_x'] + '": ' + CEND))
            y = a * x + b
            print(d['v_y'] + " = " + str(a) + "*(" + str(x) + d['u_x'] + " + " + str(b))
            print(d['v_y'] + " = " + str(y) + d['u_y'])

        elif x_o_y == '2':
        v = d['v_y']
        print('Las "' + d['v_y'] + '" al cuadrado son:')
        y_cuadrado = [i ** 2 for i in d['y']]
        print(CGREEN + str(y_cuadrado) + CEND)

        suma_y_cuadrado = sum(y_cuadrado)
        print('La suma de las "' + d['v_y'] + '" al cuadrado es:')
        print(CGREEN + str(suma_y_cuadrado) + CEND)

        a = (suma_xy - d['n'] * prom_x * prom_y) / (suma_y_cuadrado - d['n'] * prom_y ** 2)
        b = prom_y - a * prom_x

        print('La constante (a) es: ' + CGREEN + str(a) + CEND)
        print('La bicectriz (b) es: ' + CGREEN + str(b) + CEND)

        eq = "$\ " + d['v_x'] + " = " + str(a) + d['v_y'] + " + " + str(b)

        grafica = input(CCYAN + 'Quiere graficar la ecuacion obtenida? (y/n) ' + CEND)
        if grafica == 'y':
            val_p = input(CCYAN + 'Desea insertar valores personalizados?(y/n) ' + CEND)
            if val_p == 'y':
                rango_xi = eval(input(CCYAN + 'Inserte el valor inicial de "' + d['v_y'] + '": ' + CEND))
                rango_xf = eval(input(CCYAN + 'Inserte el valor final de "' + d['v_y'] + '": ' + CEND))
                delta_x = eval(input(CCYAN + 'Inserte la diferencia de distancia para "' + d['v_y'] + '": '+ CEND))
                y = np.arange(rango_yi, rango_yf, delta_y)
                x = []
            else:
                y = np.arange(0, d['max_y'], 0.001)
                x = []
            for i in y:
                val_x = a * i + b
                x.append(val_x)
            draw_graph(x, y, 0, eq, d['v_x'], d['v_y'], d['u_x'], d['u_y'])

        while True:
            y = eval(input(CCYAN + '\nInserte algun valor de "' + d['v_y'] + '": ' + CEND))
            x = a * y + b
            print(d['v_x'] + " = " + str(a) + "(" + str(y) + d['u_y'] + ") + " + str(b))
            print(d['v_x'] + " = " + str(x) + d['u_x'])

