#!/usr/bin/env python

__author__ = "Alfredo Pérez"
__copyright__ = "Copyright 2017, Alfredo Pérez"
__license__ = "GNU General Public License version 3"
__email__ = "alfredoperez1998@protonmail.com"

def data(reg_type, n = 0, x = [], y = [], input_f = True):

    v_x = input("Input the first variable to use: ")
    v_y = input("Input the second variable to use: ")

    if input_f == False:
        array_x = {}
        array_y = {}
        x = []
        y = []
        n = int(input(C3 + "Input the data number: " + CE))

        print(C2 + "Input 'r' to re-enter a value." + CE)

        i = 0

        while i <= (n - 1):
            dict_print = "Input " + v_x +  str(format(i + 1)) + ': '
            xinput = input(C3 + dict_print + CE)
            if xinput == 'r':
                i = i - 1
            else:
                array_x[v_x + '{0}'.format(i + 1)] = eval(xinput)
                i = i + 1

        print("")
        i = 0

        while i <= (n - 1):
            dict_print = "Input " + v_y + str(format(i + 1)) + ': '
            yinput = input(C3 + dict_print + CE)
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

    print('\tThe entered data were the following:')
    print("Number of data = " + C1 + str(n) + CE)
    print('The entered "' + v_x + '" are;')
    print(C1 + str(x) + CE)
    print('The entered "' + v_y + '" are;')
    print(C1 + str(y) + CE)

    u_x = input(C3 + "Input the unit type of " + v_x + ": " + CE)
    u_y = input(C3 + "Input the unit type of " + v_y + ": " + CE)

    # Graph
    graph = input(C3 + 'Do you want to visualize the graph of the entered data? (y/n) ' + CE)
    if graph == 'y':
        draw_graph(x, y, 1, '', v_x, v_y, u_x, u_y)

    if reg_type == '1' or '2':
        return {'x': x, 'y': y, 'n': n, 'v_x': v_x, 'v_y': v_y, 'u_x': u_x,
                'u_y': u_y, 'max_x': max_x, 'min_x': min_x, 'max_y': max_y, 'min_y': min_y}
    else:
        quit()

if __name__ == '__main__':
    import sys
    from functions import draw_graph
    from colors import *

    print('Regression Models: ')
    print("\tPower regression  =  1")
    print("\tLinear regression =  2")
    reg_type = input('Input the regression model to use: ')

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
                from models import power
                power(data(reg_type, n, x, y, input_f = True))

            elif reg_type == '2':
                from models import linear
                linear(data(reg_type, n, x, y, input_f = True))

    except IndexError:
        if reg_type == '1':
            from models import power
            power(data(reg_type, input_f = False))

        elif reg_type == '2':
            from models import linear
            linear(data(reg_type, input_f = False))


