#!/usr/bin/env python

__author__ = "Alfredo Perez"
__copyright__ = "Copyright 2017, Alfredo Perez"
__license__ = "GNU General Public License version 3"
__email__ = "alfredoperez1998@protonmail.com"

def data(reg_type):

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
        draw_graph(x, y, 1, '', v_x, v_y, u_x, u_y)

    if reg_type == '1':
        return {'x': x, 'y': y, 'n': n, 'v_x': v_x, 'v_y': v_y, 'u_x': u_x,
                'u_y': u_y, 'max_x': max_x, 'max_y': max_y}
    else:
        quit()

if __name__ == '__main__':
    from funciones import draw_graph
    from colors import *

    reg_type = input('Inserte el modelo de regresion a usar')
    if reg_type == '1':
        from potencial import potencial
        potencial(data(reg_type))

    elif reg_type == '2':
        from lineal import lineal
        lineal(data(reg_type))
