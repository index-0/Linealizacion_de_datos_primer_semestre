#!/usr/bin/env python

__author__ = "Alfredo Perez"
__copyright__ = "Copyright 2017, Alfredo Perez"
__license__ = "GNU General Public License version 3"
__email__ = "alfredoperez1998@protonmail.com"

def data(reg_type, n = 0, x = [], y = [], input_f = True):

    print(CRED + 'Para finalizar el proceso presione Ctrl+Z en cualquier momento.' + CEND)

    v_x = input("Inserte la primera variable a usar: ")
    v_y = input("Inserte la segunda variable a usar: ")

    if input_f == False:
        array_x = {}
        array_y = {}
        x = []
        y = []
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
    min_x = min(y)
    max_y = max(y)
    min_y = min(y)

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

    if reg_type == '1' or '2':
        return {'x': x, 'y': y, 'n': n, 'v_x': v_x, 'v_y': v_y, 'u_x': u_x,
                'u_y': u_y, 'max_x': max_x, 'min_x': min_x, 'max_y': max_y, 'min_y': min_y}
    else:
        quit()

if __name__ == '__main__':
    import sys
    from funciones import draw_graph
    from colors import *

    print('Tipos de regresion disponibles: ')
    print("Regresion potencial =  1")
    print("Regresion lineal    =  2")
    reg_type = input('Inserte el modelo de regresion a usar: ')

    try:
        input_file = sys.argv[1]
        with open(input_file, 'r', newline='') as filereader:
            x_header = filereader.readline()
            x_header = x_header.strip()
            x_header = x_header.split(',')

            y_header = filereader.readline()
            y_header = y_header.strip()
            y_header = y_header.split(',')

            x = []
            y = []
            for i in x_header:
                x.append(float(i))
            for i in y_header:
                y.append(float(i))

            n = len(x)

            if reg_type == '1':
                from potencial import potencial
                potencial(data(reg_type, n, x, y, input_f = True))

            elif reg_type == '2':
                from lineal import lineal
                lineal(data(reg_type, n, x, y, input_f = True))

    except IndexError:
        if reg_type == '1':
            from potencial import potencial
            potencial(data(reg_type, input_f = False))

        elif reg_type == '2':
            from lineal import lineal
            lineal(data(reg_type, input_f = False))


