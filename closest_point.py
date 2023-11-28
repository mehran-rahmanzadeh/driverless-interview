from utils import get_distance, plot_points, show_plot


def find_closest_point(initial_point, waypoints, _plot=False):
    """
    find the closest point to initial point with complexity O(n)

    :param _plot:
    :param initial_point: (x, y)
    :param waypoints: ((x1, y1), (x2, y2), ...)
    :return: (xf, yf)
    """
    min_distance = float('+inf')
    waypoint = None
    for point in waypoints:
        distance = get_distance(initial_point, point)
        if distance < min_distance:
            min_distance = distance
            waypoint = point

    if _plot:
        plot_points([initial_point], marker='o', color='green')
        plot_points(waypoints, marker='.', color='blue')
        plot_points([waypoint], marker='*', color='red')
        show_plot()

    return waypoint
