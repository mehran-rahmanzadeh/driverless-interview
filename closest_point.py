import numpy as np

from utils import get_distance, plot_points, show_plot


def find_closest_point(initial_point, waypoints, _plot=False):
    """
    find the closest point to initial point

    :param _plot:
    :param initial_point: (x, y)
    :param waypoints: ((x1, y1), (x2, y2), ...)
    :return: (xf, yf)
    """
    nodes = np.asarray(waypoints)
    dist = np.sum((nodes - initial_point) ** 2, axis=1)
    idx = np.argmin(dist)
    waypoint = waypoints[idx]

    if _plot:
        plot_points([initial_point], marker='o', color='green')
        plot_points(waypoints, marker='.', color='blue')
        plot_points([waypoint], marker='*', color='red')
        show_plot()

    return waypoint
