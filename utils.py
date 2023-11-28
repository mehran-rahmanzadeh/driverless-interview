from math import sqrt
import matplotlib.pyplot as plt
import numpy as np


def __tuple_points_to_x_y(points):
    x = [point[0] for point in points]
    y = [point[1] for point in points]
    return x, y


def get_distance(point_x: tuple, point_y: tuple):
    """
    :param point_x: (x, y)
    :param point_y: (x, y)
    :return: float
    """
    return sqrt((point_x[0] - point_y[0]) ** 2 + (point_x[1] - point_y[1]) ** 2)


def get_equidistant_points(point_x, point_y, num):
    return zip(np.linspace(point_x[0], point_y[0], num + 1),
               np.linspace(point_x[1], point_y[1], num + 1))


def plot_points(points, color='red', marker='o'):
    x, y = __tuple_points_to_x_y(points)
    plt.plot(x, y, marker, color=color)


def show_plot():
    plt.grid()
    plt.show()


class Node:
    def __init__(self, x, y, cost):
        self.x = x
        self.y = y
        self.cost = cost
