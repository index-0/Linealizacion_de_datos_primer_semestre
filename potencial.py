#!/usr/bin/env python

from main import *
from funciones import draw_graph, csv_file, row_maker, sup
import math
import numpy as np
from colors import *

def potencial(d):

    # Obtiene el logaritmo natural de las 2 listas
    ln_x = [math.log(i) for i in d['x']]
    ln_y = [math.log(i) for i in d['y']]

    # Imprime los datos obtenidos sobre los logaritmos
    print('\tLos logaritmos naturales de los datos obtenidos son los siguientes:')

    print('Los logaritmos naturales de "' + d['v_x'] + '" son;')
    print(CGREEN + str(ln_x) + CEND)

    print('Los logaritmos naturales de "' + d['v_y'] + '" son;')
    print(CGREEN + str(ln_y) + CEND)

    # ln(x) * ln(y)
    ln_xy = [a*b for a, b in zip(ln_x, ln_y)]

    print('\tEl logaritmo natural de "' + d['v_x'] + '" por el logaritmo natural de "' + d['v_y'] + '" es igual a:')
    print(CGREEN + str(ln_xy) + CEND)

    # La suma de cada una de las listas
    # Suma ln(x)
    suma_ln_x = sum(ln_x)
    print('La suma de los logaritmos naturales de "' + d['v_x'] + '" es:')
    print(CGREEN + str(suma_ln_x) + CEND)

    # Suma ln(y)
    suma_ln_y = sum(ln_y)
    print('La suma de los logaritmos naturales de "' + d['v_y'] + '" es:')
    print(CGREEN + str(suma_ln_y) + CEND)

    # Suma ln(x) * ln(y)
    suma_ln_xy = sum(ln_xy)
    print('La suma de la multiplicacion de los logaritmos naturales de "' + d['v_x'] + '" por los logaritmos naturales de "' + d['v_y'] + '" es:')
    print(CGREEN + str(suma_ln_xy) + CEND)

    x_o_y = input(CCYAN + "Para obtener la funcion " + d['v_y'] + "(" + d['v_x'] + ") inserte '1' " +
                          "y para obtener la funcion " + d['v_x'] + "(" + d['v_y'] + ") inserte '2': " + CEND)


    if x_o_y == '1':
        v = d['v_x']
        ln_x_cuadrado = ln_v_cuadrado = [d['n'] ** 2 for d['n'] in ln_x]
        print('El cuadrado de los logaritmos naturales de "' + d['v_x'] + '" es:')
        print(CGREEN + str(ln_x_cuadrado) + CEND)

        # Es la suma de los logaritmos naturales de "x" al cuadrado

        suma_ln_x_cuadrado = suma_ln_v_cuadrado = sum(ln_x_cuadrado)
        print('La suma de los logaritmos naturales de "' + d['v_x'] + '" al cuadrado es:')
        print(CGREEN + str(suma_ln_x_cuadrado) + CEND)

        csv_file(row_maker(v, d['x'], d['y'], ln_x, ln_y, ln_xy, ln_v_cuadrado, d['v_x'], d['v_y']))
        # Pendiente
        m = (d['n'] * suma_ln_xy - suma_ln_x * suma_ln_y) / (
             d['n'] * suma_ln_x_cuadrado - suma_ln_x ** 2)
        print('La pendiente es igual a:')
        print('m = ' + CGREEN + str(m) + CEND)

        # Bisectriz
        b = (suma_ln_x_cuadrado * suma_ln_y - suma_ln_x * suma_ln_xy) / (
            d['n'] * suma_ln_x_cuadrado - suma_ln_x ** 2)
        print('La bisectriz es:')
        print('b = ' + CGREEN + str(b) + CEND)

        a = math.exp(b)
        print('El exponente (n) es: ' + CGREEN + str(m) + CEND)
        print('La constante (a) es: ' + CGREEN + str(a) + CEND)

        eq = "$\ " + d['v_y'] + " = " + str(a) + d['v_x'] + " ^"+ sup(str(m))
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
                val_y = a * i ** m
                y.append(val_y)
            draw_graph(x, y, 0, eq, d['v_x'], d['v_y'], d['u_x'], d['u_y'])

        while True:
            x = eval(input(CCYAN + '\nInserte algun valor de "' + d['v_x'] + '": ' + CEND))
            y = a * x ** m
            print(d['v_y'] + " = " + str(a) + "*(" + str(x) + d['u_x'] + ")**" + str(m))
            print(d['v_y'] + " = " + str(y) + d['u_y'])

    elif x_o_y == '2':
        v = d['v_y']
        ln_y_cuadrado = ln_v_cuadrado = [d['n'] ** 2 for d['n'] in ln_y]
        print('El cuadrado de los logaritmos de "' + d['v_y'] + '" es:')
        print(CGREEN + str(ln_y_cuadrado) + CEND)

        # Es la suma de los logaritmos de "y" al cuadrado

        suma_ln_y_cuadrado = suma_ln_v_cuadrado = sum(ln_y_cuadrado)
        print('La suma de los logaritmos de "' + d['v_y'] + '" al cuadrado es:')
        print(CGREEN + str(suma_ln_y_cuadrado) + CEND)

        csv_file(row_maker(v, d['x'], d['y'], ln_x, ln_y, ln_xy, ln_v_cuadrado, d['v_x'], d['v_y']))
        # Pendiente
        m = (d['n'] * suma_ln_xy - suma_ln_y * suma_ln_x) / (
             d['n'] * suma_ln_y_cuadrado - suma_ln_y ** 2)
        print('La pendiente es igual a:')
        print('m = ' + CGREEN + str(m) + CEND)

        # Interseccion con eje y
        b = (suma_ln_y_cuadrado * suma_ln_x - suma_ln_y * suma_ln_xy) / (
            d['n'] * suma_ln_y_cuadrado - suma_ln_y ** 2)
        print('La bisectriz es:')
        print('b = ' + CGREEN + str(b) + CEND)

        a = math.exp(b)
        print('El exponente (n) es: ' + CGREEN + str(m) + CEND)
        print('La constante (a) es: ' + CGREEN + str(a) + CEND)

        eq = "$\ " + d['v_x'] + " = " + str(a) + d['v_y'] + " ^"+ sup(str(m))
        grafica = input(CCYAN + 'Quiere graficar la ecuacion obtenida? (y/n) ' + CEND)
        if grafica == 'y':
            val_p = input(CCYAN + 'Desea insertar valores personalizados?(y/n) ' + CEND)
            if val_p == 'y':
                rango_yi = eval(input(CCYAN + 'Inserte el valor inicial de "' + d['v_y'] + '": ' + CEND))
                rango_yf = eval(input(CCYAN + 'Inserte el valor final de "' + d['v_y'] + '": ' + CEND))
                delta_y = eval(input(CCYAN + 'Inserte la diferencia de distancia para "' + d['v_y'] + '": ' + CEND))
                y = np.arange(rango_yi, rango_yf, delta_y)
                x = []
            else:
                y = np.arange(0, d['max_y'], 0.001)
                x = []
            for i in y:
                val_x = a * i ** m
                x.append(val_x)
            draw_graph(x, y, 0, eq, d['v_x'], d['v_y'], d['u_x'], d['u_y'])

        while True:
            y = eval(input(CCYAN + '\nInserte algun valor de "' + d['v_y'] + '": ' + CEND))
            x = a * y ** m
            print(d['v_x'] + " = " + str(a) + "*(" + str(y) + d['u_y'] + ")**" + str(m))
            print(d['v_x'] + " = " + str(x) + d['u_x'])

    else:
        quit(CERROR + 'Intente de nuevo e inserte un valor valido que sea "1" o "2" sin comillas.' + CEND)

