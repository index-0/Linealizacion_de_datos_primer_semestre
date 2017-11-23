#!/usr/bin/env python

from matplotlib import rc, rcParams
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import csv
import pickle

def draw_graph(x, y, graph, eq, v_x, v_y, u_x, u_y):
    latex = input("Do you want to use LaTeX for text rendering? (y/n) ")
    if latex == 'y':
        rc('text', usetex=True)
        rcParams['text.latex.preamble']=[r"\usepackage{amsmath}"]
        rcParams['axes.labelsize'] = 15
        if graph == 1:
            plt.plot(x, y, color = '#361156', ls = '-', marker = '.')
            plt.xlabel('$' + v_x + "(" + u_x + ")" + '$')
            plt.ylabel('$' + v_y + "(" + u_y + ")" + '$')
            plt.savefig('data.png', dpi = 250, format = 'png', transparent = True, bbox_inches = 'tight')
        else:
            plt.plot(x, y, color = '#287086', ls = '-')
            plt.title(eq)
            plt.xlabel('$' + v_x + "(" + u_x + ")" + '$')
            plt.ylabel('$' + v_y + "(" + u_y + ")" + '$')
            plt.savefig('equation.png', dpi = 250, format = 'png', transparent = True, bbox_inches = 'tight')
    else:
        if graph == 1:
            plt.plot(x, y, color = '#361156', ls = '-', marker = '.')
            plt.xlabel('$' + v_x + "(" + u_x + ")" + '$')
            plt.ylabel('$' + v_y + "(" + u_y + ")" + '$')
            plt.savefig('data.png', dpi = 250, format = 'png', transparent = True, bbox_inches = 'tight')
        else:
            plt.plot(x, y, color = '#287086', ls = '-')
            plt.title(eq)
            plt.xlabel('$' + v_x + "(" + u_x + ")" + '$')
            plt.ylabel('$' + v_y + "(" + u_y + ")" + '$')
            plt.savefig('equation.png', dpi = 250, format = 'png', transparent = True, bbox_inches = 'tight')
    plt.show()

    if  graph == 1:
        pickle.dump(x, open('d_x.dump', 'wb'))
        pickle.dump(y, open('d_y.dump', 'wb'))

    elif graph != 1:
        comp = input('Do you want to compare the equation with the entered data? (y/n)')
        if comp == 'y':
            plt.plot(x, y, color = '#287086', ls = '-')
            plt.plot(pickle.load(open('d_x.dump', 'rb')), pickle.load(open('d_y.dump', 'rb')), color = '#361156', ls='None', marker = '.')

            patch_1 = mpatches.Patch(color='#361156', label= r'\textrm{\textnormal{Data}}')
            patch_2 = mpatches.Patch(color='#287086', label= eq)

            plt.legend(handles=[patch_1, patch_2])

            plt.xlabel('$' + v_x + "(" + u_x + ")" + '$')
            plt.ylabel('$' + v_y + "(" + u_y + ")" + '$')

            plt.savefig('comparison.png', dpi = 250, format = 'png', transparent = True, bbox_inches = 'tight')
            plt.show()


def csv_file(rows):
    with open('data.csv', 'w', encoding='utf8') as csvfile:
        writer = csv.writer(csvfile)
        for row in rows:
            writer.writerow(row)


def row_maker(v, x, y, ln_x, ln_y, ln_xy, ln_v_squared, v_x, v_y):
    x.insert(0, v_x)
    y.insert(0, v_y)
    ln_x.insert(0, 'ln(' + v_x + ')')
    ln_y.insert(0, 'ln(' + v_y + ')')
    ln_xy.insert(0, 'ln(' + v_x + ')' + ' * ln(' + v_y + ')')
    ln_v_squared.insert(0, 'ln(' + v + ')²')
    rows = zip(x, y, ln_x, ln_y, ln_xy, ln_v_squared)
    return rows

