#!/usr/bin/env python

from matplotlib import rc, rcParams
import matplotlib.pyplot as plt
import csv

def draw_graph(x, y, graph, eq, v_x, v_y, u_x, u_y):
    # Crea las graficas
    latex = input("Desea usar LaTeX para renderizar el texto? (y/n) ")
    if latex == 'y':
        rc('text', usetex=True)
        rcParams['text.latex.preamble']=[r"\usepackage{amsmath}"]
        rcParams['axes.labelsize'] = 15
        if graph == 1:
            plt.plot(x, y, 'co-')
            plt.title('Datos Obtenidos')
        else:
            plt.plot(x, y)
            plt.title(eq)
        plt.xlabel('$' + v_x + "(" + u_x + ")" + '$')
        plt.ylabel('$' + v_y + "(" + u_y + ")" + '$')
    else:
        if graph == 1:
            plt.plot(x, y, 'co-')
            plt.title('Datos Obtenidos')
        else:
            plt.plot(x, y)
            plt.title(eq)
        plt.xlabel(v_x + "(" + u_x + ")")
        plt.ylabel(v_y + "(" + u_y + ")")
    plt.show()


def csv_file(rows):
    # Crea la hoja de calculo
    with open('practica.csv', 'w', encoding='utf8') as csvfile:
        writer = csv.writer(csvfile)
        for row in rows:
            writer.writerow(row)


def row_maker(v, x, y, ln_x, ln_y, ln_xy, ln_v_cuadrado, v_x, v_y):
    # Hace las filas para las hoja de calculo
    x.insert(0, v_x)
    y.insert(0, v_y)
    ln_x.insert(0, 'ln(' + v_x + ')')
    ln_y.insert(0, 'ln(' + v_y + ')')
    ln_xy.insert(0, 'ln(' + v_x + ')' + ' * ln(' + v_y + ')')
    ln_v_cuadrado.insert(0, 'ln(' + v + ')²')
    rows = zip(x, y, ln_x, ln_y, ln_xy, ln_v_cuadrado)
    return rows

def sup(m):
    # Convierte los numeros de la ecuacion en superindices
    m_sup = '^'.join(m[i:i+1] for i in range(0, len(m), 1))
    return m_sup


