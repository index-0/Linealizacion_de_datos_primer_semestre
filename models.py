#!/usr/bin/env python

from functions import draw_graph, csv_file, row_maker, D
from math import log, exp
from numpy import arange
from colors import *


def power(d):
    # Power Regression
    ln_x = [log(i) for i in d['x']]
    ln_y = [log(i) for i in d['y']]

    print('\tThe natural logarithms of the data are:')

    print('The natural logarithms of "' + d['v_x'] + '" are;')
    print(C1 + str(ln_x) + CE)

    print('The natural logarithms of "' + d['v_y'] + '" are;')
    print(C1 + str(ln_y) + CE)

    ln_xy = [a*b for a, b in zip(ln_x, ln_y)]

    print('\tThe natural logarithms of "' + d['v_x'] + '" times the natural logarithms of "' + d['v_y'] + '" are:')
    print(C1 + str(ln_xy) + CE)

    sum_ln_x = sum(ln_x)
    print('The sum of the natural logarithms of "' + d['v_x'] + '" is:')
    print(C1 + str(sum_ln_x) + CE)

    sum_ln_y = sum(ln_y)
    print('The sum of the natural logarithms of "' + d['v_y'] + '" is:')
    print(C1 + str(sum_ln_y) + CE)

    sum_ln_xy = sum(ln_xy)
    print('The sum of the natural logarithms of "' + d['v_x'] + '" times the natural logarithms of "' + d['v_y'] + '" is:')
    print(C1 + str(sum_ln_xy) + CE)

    x_o_y = input(C3 + "To compute the function " + d['v_y'] + "(" + d['v_x'] + ") input '1' " + "or input '2' to compute the function " + d['v_x'] + "(" + d['v_y'] + "): " + CE)

    if x_o_y == '1':
        v = d['v_x']
        ln_x_squared = ln_v_squared = [i ** 2 for i in ln_x]
        print('The natural logarithms squared of "' + d['v_x'] + '" are:')
        print(C1 + str(ln_x_squared) + CE)

        sum_ln_x_squared = sum_ln_v_squared = sum(ln_x_squared)
        print('The sum of the natural logarithms squared of "' + d['v_x'] + '" is:')
        print(C1 + str(sum_ln_x_squared) + CE)

        csv_file(row_maker(v, d['x'], d['y'], ln_x, ln_y, ln_xy, ln_v_squared, d['v_x'], d['v_y']))
        m = (d['n'] * sum_ln_xy - sum_ln_x * sum_ln_y) / (
             d['n'] * sum_ln_x_squared - sum_ln_x ** 2)
        print('The slope is:')
        print('m = ' + C1 + str(m) + CE)

        b = (sum_ln_x_squared * sum_ln_y - sum_ln_x * sum_ln_xy) / (
            d['n'] * sum_ln_x_squared - sum_ln_x ** 2)
        print('The vertical intercept is:')
        print('b = ' + C1 + str(b) + CE)

        a = exp(b)
        print('The exponent (n) is: ' + C1 + str(m) + CE)
        print('The constant (a) is: ' + C1 + str(a) + CE)

        eq = "$\ " + d['v_y'] + " = " + str(a) + d['v_x'] + "^{"+ str(m) + '}$'
        grafica = input(C3 + 'Do you want to graph the equation? (y/n) ' + CE)
        if grafica == 'y':
            val_p = input(C3 + 'Do you want to input custom values? (y/n) ' + CE)
            if val_p == 'y':
                xi = eval(input(C3 + 'Input the initial value of "' + d['v_x'] + '": ' + CE))
                xf = eval(input(C3 + 'Input the final value of "' + d['v_x'] + '": ' + CE))
                delta_x = eval(input(C3 + 'Input the difference of "' + d['v_x'] + '": '+ CE))
                x = arange(xi, xf, delta_x)
                y = []
            else:
                x = arange(d['min_x'], d['max_x'], 0.001)
                y = []
            for i in x:
                val_y = a * i ** m
                y.append(val_y)
            draw_graph(x, y, 0, eq, d['v_x'], d['v_y'], d['u_x'], d['u_y'])

        while True:
            x = eval(input(C3 + '\nInput some value of "' + d['v_x'] + '": ' + CE))
            y = a * x ** m
            print(d['v_y'] + " = " + str(a) + "*(" + str(x) + d['u_x'] + ")**" + str(m))
            print(d['v_y'] + " = " + str(y) + d['u_y'])

    elif x_o_y == '2':
        v = d['v_y']
        ln_y_squared = ln_v_squared = [i ** 2 for i in ln_y]
        print('The natural logarithms squared of "' + d['v_y'] + '" are:')
        print(C1 + str(ln_y_squared) + CE)

        sum_ln_y_squared = sum_ln_v_squared = sum(ln_y_squared)
        print('The sum of the natural logarithms squared of "' + d['v_y'] + '" is:')
        print(C1 + str(sum_ln_y_squared) + CE)

        csv_file(row_maker(v, d['x'], d['y'], ln_x, ln_y, ln_xy, ln_v_squared, d['v_x'], d['v_y']))

        m = (d['n'] * sum_ln_xy - sum_ln_y * sum_ln_x) / (
             d['n'] * sum_ln_y_squared - sum_ln_y ** 2)
        print('The slope is:')
        print('m = ' + C1 + str(m) + CE)

        b = (sum_ln_y_squared * sum_ln_x - sum_ln_y * sum_ln_xy) / (
            d['n'] * sum_ln_y_squared - sum_ln_y ** 2)
        print('The vertical intercept is:')
        print('b = ' + C1 + str(b) + CE)

        a = exp(b)
        print('The exponent (n) is: ' + C1 + str(m) + CE)
        print('The constant (a) is: ' + C1 + str(a) + CE)

        eq = "$\ " + d['v_x'] + " = " + str(a) + d['v_y'] + " ^{"+ str(m) + '}$'
        grafica = input(C3 + 'Do you want to graph the equation? (y/n) ' + CE)
        if grafica == 'y':
            val_p = input(C3 + 'Do you want to input custom values? (y/n) ' + CE)
            if val_p == 'y':
                yi = eval(input(C3 + 'Input the initial value of "' + d['v_y'] + '": ' + CE))
                yf = eval(input(C3 + 'Input the final value of "' + d['v_y'] + '": ' + CE))
                delta_y = eval(input(C3 + 'Input the difference of "' + d['v_y'] + '": ' + CE))
                y = arange(yi, yf, delta_y)
                x = []
            else:
                y = arange(d['min_y'], d['max_y'], 0.001)
                x = []
            for i in y:
                val_x = a * i ** m
                x.append(val_x)
            draw_graph(x, y, 0, eq, d['v_x'], d['v_y'], d['u_x'], d['u_y'])

        while True:
            y = eval(input(C3 + '\nInput some value of "' + d['v_y'] + '": ' + CE))
            x = a * y ** m
            print(d['v_x'] + " = " + str(a) + "*(" + str(y) + d['u_y'] + ")**" + str(m))
            print(d['v_x'] + " = " + str(x) + d['u_x'])

    else:
        quit(C2 + 'Try again and input a valid value.' + CE)


def linear(d):
    # Linear Regression
    sum_x = sum(d['x'])
    print('The sum of "' + d['v_x'] + '" is:')
    print(C1 + str(sum_x) + CE)

    sum_y = sum(d['y'])
    print('The sum of "' + d['v_y'] + '" is:')
    print(C1 + str(sum_y) + CE)

    prom_x = sum_x / d['n']
    print('The average of "' + d['v_x'] + '" is:')
    print(C1 + str(prom_x) + CE)

    prom_y = sum_y / d['n']
    print('The average of "' + d['v_y'] + '" is:')
    print(C1 + str(prom_y) + CE)

    xy = [a*b for a, b in zip(d['x'], d['y'])]
    print(d['v_x'] + '*' + d['v_y'] + ' is:')
    print(C1 + str(xy) + CE)

    sum_xy = sum(xy)
    print('The sum of ' + d['v_x'] + '*' + d['v_y'] + ' is:')
    print(C1 + str(sum_xy) + CE)

    x_o_y = input(C3 + "To compute the function " + d['v_y'] + "(" + d['v_x'] + ") input '1' " + "or input '2' to compute the function " + d['v_x'] + "(" + d['v_y'] + "): " + CE)
    if x_o_y == '1':
        v = d['v_x']
        print('The squared "' + d['v_x'] + '" are:')
        x_squared = [i ** 2 for i in d['x']]
        print(C1 + str(x_squared) + CE)

        sum_x_squared = sum(x_squared)
        print('The sum of the squared "' + d['v_x'] + '" is:')
        print(C1 + str(sum_x_squared) + CE)

        a = (sum_xy - d['n'] * prom_x * prom_y) / (sum_x_squared - d['n'] * prom_x ** 2)
        b = prom_y - a * prom_x

        print('The constant (a) is:  ' + C1 + str(a) + CE)
        print('The bisection (b) is: ' + C1 + str(b) + CE)

        if b > 0:
            eq = "$\ " + d['v_y'] + " = " + str(a) + d['v_x'] + " + " + str(b) + "$"
        elif b < 0:
            eq = "$\ " + d['v_y'] + " = " + str(a) + d['v_x'] + " " + str(b) + "$"
        else:
            eq = "$\ " + d['v_y'] + " = " + str(a) + d['v_x'] + "$"

        grafica = input(C3 + 'Do you want to graph the equation? (y/n) ' + CE)
        if grafica == 'y':
            val_p = input(C3 + 'Do you want to input custom values?(y/n) ' + CE)
            if val_p == 'y':
                xi = eval(input(C3 + 'Input the initial value of "' + d['v_x'] + '": ' + CE))
                xf = eval(input(C3 + 'Input the final value of "' + d['v_x'] + '": ' + CE))
                delta_x = eval(input(C3 + 'Input the difference of "' + d['v_x'] + '": '+ CE))
                x = arange(xi, xf, delta_x)
                y = []
            else:
                x = D(d['max_x'], d['min_x'])
                print(x)
                y = []
            for i in x:
                val_y = a * i + b
                y.append(val_y)
            draw_graph(x, y, 0, eq, d['v_x'], d['v_y'], d['u_x'], d['u_y'])

        while True:
            x = eval(input(C3 + '\nInput some value of "' + d['v_x'] + '": ' + CE))
            y = a * x + b
            print(d['v_y'] + " = " + str(a) + "*(" + str(x) + d['u_x'] + ") + " + str(b))
            print(d['v_y'] + " = " + str(y) + d['u_y'])

    elif x_o_y == '2':
        v = d['v_y']
        print('The squared "' + d['v_y'] + '" are:')
        y_squared = [i ** 2 for i in d['y']]
        print(C1 + str(y_squared) + CE)

        sum_y_squared = sum(y_squared)
        print('The sum of the squared "' + d['v_y'] + '" is:')
        print(C1 + str(sum_y_squared) + CE)

        a = (sum_xy - d['n'] * prom_x * prom_y) / (sum_y_squared - d['n'] * prom_y ** 2)
        b = prom_x - a * prom_y

        print('The constant (a) es: ' + C1 + str(a) + CE)
        print('The bisection (b) es: ' + C1 + str(b) + CE)

        if b > 0:
            eq = "$\ " + d['v_x'] + " = " + str(a) + d['v_y'] + " + " + str(b) + "$"
        elif b < 0:
            eq = "$\ " + d['v_x'] + " = " + str(a) + d['v_y'] + " " + str(b) + "$"
        else:
            eq = "$\ " + d['v_x'] + " = " + str(a) + d['v_y'] + "$"

        grafica = input(C3 + 'Do you want to graph the equation? (y/n) ' + CE)
        if grafica == 'y':
            val_p = input(C3 + 'Do you want to input custom values? (y/n) ' + CE)
            if val_p == 'y':
                xi = eval(input(C3 + 'Input the initial value of "' + d['v_y'] + '": ' + CE))
                xf = eval(input(C3 + 'Input the final value of "' + d['v_y'] + '": ' + CE))
                delta_x = eval(input(C3 + 'Input the difference of  "' + d['v_y'] + '": '+ CE))
                y = arange(yi, yf, delta_y)
                x = []
            else:
                y = D(d['max_y'], d['min_y'])
                x = []
            for i in y:
                val_x = a * i + b
                x.append(val_x)
            draw_graph(x, y, 0, eq, d['v_x'], d['v_y'], d['u_x'], d['u_y'])

        while True:
            y = eval(input(C3 + '\nInput some value of "' + d['v_y'] + '": ' + CE))
            x = a * y + b
            print(d['v_x'] + " = " + str(a) + "(" + str(y) + d['u_y'] + ") + " + str(b))
            print(d['v_x'] + " = " + str(x) + d['u_x'])

