import numpy as np

from closest_point import find_closest_point
from path_planning import find_ordinary_path, Dijkstra
from tsp import find_shortest_path


def main():
    # CLOSEST POINT PROBLEM
    initial_point = (0, 0)
    waypoints = np.random.uniform(-20, 20, size=(10, 2))
    print(f"Closest point: {find_closest_point(initial_point, waypoints, _plot=True)}")

    # SHORTEST PATH TO COVER ALL POINTS
    find_shortest_path(initial_point, tuple(tuple(point) for point in waypoints) + (initial_point,), _plot=True)

    # PATH PLANNING PROBLEM
    initial_point = (0, 2)
    upper_bound = (
        (0, 3),
        (1, 4),
        (2, 5),
        (3, 5),
        (4, 6),
        (5, 7),
        (6, 8),
        (7, 9),
        (8, 9),
        (9, 9),
        (10, 9),
        (11, 9),
        (12, 9),
        (13, 9),
    )
    lower_bound = (
        (0, 0),
        (1, 1),
        (2, 2),
        (3, 2),
        (4, 2),
        (5, 3),
        (6, 4),
        (7, 5),
        (8, 6),
        (9, 6),
        (10, 6),
        (11, 6),
        (12, 6),
        (12, 6),
        (13, 6),
    )
    path = find_ordinary_path(upper_bound, lower_bound, _plot=True, num_points_each_obstacle=3)

    # OPTIMAL PATH PLANNING
    goal_point = [13, 8]
    obstacles = np.array(list(upper_bound) + list(lower_bound))
    dijkstra = Dijkstra(obstacles)
    path = dijkstra.find_minimal_path(initial_point, goal_point, _plot=True)


if __name__ == '__main__':
    main()
