#!/usr/bin/env python

from matplotlib import rc, rcParams
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import csv
from numpy import arange
from pickle import load
from configuration import *

def draw_graph(x, y, graph, eq, v_x, v_y, u_x, u_y):
    if latex == True:
        try:
            rc('text', usetex = True)
            rc('font',**{'family':font_family, font_family:[font], 'size':font_size})
            rcParams['text.latex.preamble'] = [r"\usepackage{amsmath}"]
            rcParams['axes.labelsize'] = label_font_size
        except IndexError:
            print("Make sure that latex is installed in your machine including the amsmath package or disable latex in the configuration.py file.")

    if graph == 1:
        plt.plot(x, y,
                 ls = data_graph_line_type, color = data_graph_line_color, lw = data_graph_line_width,
                 marker = data_graph_marker_type, mec = data_graph_marker_color, mew = data_graph_marker_edge_width, mfc = data_graph_marker_edge_color, ms = data_graph_marker_size,
                 alpha = data_graph_transparency, aa = antialiased)
        plt.xlabel('$' + v_x + "(" + u_x + ")" + '$')
        plt.ylabel('$' + v_y + "(" + u_y + ")" + '$')
        plt.savefig('data.' + save_format, dpi = save_dpi, format = save_format, transparent = save_transparent, bbox_inches = save_bbox_inches, orientation = save_orientation)
    else:
        plt.plot(x, y,
                 ls = equation_graph_line_type, color = equation_graph_line_color, lw = equation_graph_line_width,
                 alpha = equation_graph_transparency, aa = antialiased)
        plt.title(eq)
        plt.xlabel('$' + v_x + "(" + u_x + ")" + '$')
        plt.ylabel('$' + v_y + "(" + u_y + ")" + '$')
        plt.savefig('equation.' + save_format, dpi = save_dpi, format = save_format, transparent = save_transparent, bbox_inches = save_bbox_inches, orientation = save_orientation)
    plt.show()

    if graph != 1:
        comp = input(C3 + 'Do you want to compare the equation with the entered data? (y/n) ' + CE)
        if comp == 'y':
            plt.plot(x, y,
                     ls = comparison_graph_equation_line_type, color = comparison_graph_equation_line_color, lw = comparison_graph_equation_line_width,
                     alpha = comparison_graph_equation_transparency, aa = antialiased)
            plt.plot(load(open('x.dump', 'rb')), load(open('y.dump', 'rb')),
                     ls = comparison_graph_data_line_type, color = comparison_graph_data_line_color, lw = comparison_graph_data_lide_width,
                     marker = comparison_graph_data_marker_type, mec = comparison_graph_data_marker_color, mew = comparison_graph_data_marker_edge_width, mfc = comparison_graph_data_marker_edge_color, ms = comparison_graph_data_marker_size,
                     alpha = comparison_graph_data_transparency, aa = antialiased)


            if latex == True:
                patch_1 = mpatches.Patch(color = comparison_graph_data_line_color, label = r'\textrm{\textnormal{' + data_graph_title + '}}')
                patch_2 = mpatches.Patch(color = comparison_graph_equation_line_color, label = eq)
            else:
                patch_1 = mpatches.Patch(color = comparison_graph_data_line_color, label = data_graph_title)
                patch_2 = mpatches.Patch(color = comparison_graph_equation_line_color, label = eq)


            plt.legend(handles=[patch_1, patch_2])

            plt.xlabel('$' + v_x + "(" + u_x + ")" + '$')
            plt.ylabel('$' + v_y + "(" + u_y + ")" + '$')

            plt.savefig('comparison.' + save_format, dpi = save_dpi, format = save_format, transparent = save_transparent, bbox_inches = save_bbox_inches, orientation = save_orientation)
            plt.show()

def D(max_v, min_v):
    v = []
    AB = max_v - min_v
    if AB < 1:
        v = arange(min_v, max_v, 0.0001)
    elif AB < 10:
        v = arange(min_v, max_v, 0.001)
    elif AB < 100:
        v = arange(min_v, max_v, 0.01)
    elif AB < 1000:
        v = arange(min_v, max_v, 0.1)
    elif AB < 10000:
        v = arange(min_v, max_v, 1)
    elif AB < 100000:
        v = arange(min_v, max_v, 10)
    elif AB < 1000000:
        v = arange(min_v, max_v, 100)
    elif AB < 10000000:
        v = arange(min_v, max_v, 1000)
    else:
        v = arange(min_v, max_v, 10000)
    return v


def csv_file(rows):
    with open('data.csv', 'w', encoding = 'utf8') as csvfile:
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

