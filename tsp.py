from utils import get_distance, plot_points, show_plot

routes = []


def build_weighted_graph(points):
    graph = {}
    for start in points:
        graph[start] = {}
        for point in points:
            if point == start:
                continue
            graph[start][point] = get_distance(start, point)

    return graph


def brute_force(node, points, path, distance):
    # Add way point
    path.append(node)

    # Calculate path length from current to last node
    if len(path) > 1:
        distance += points[path[-2]][node]

    # If path contains all cities and is not a dead end,
    # add path from last to first city and return.
    if (len(points) == len(path)) and (path[0] in points[path[-1]]):
        path.append(path[0])
        distance += points[path[-2]][path[0]]
        routes.append([distance, path])
        return

    # Fork paths for all possible cities not yet used
    for point in points:
        if (point not in path) and (node in points[point]):
            brute_force(point, dict(points), list(path), distance)


def find_shortest_path(start, points, _plot=False):
    graph = build_weighted_graph(points)
    brute_force(start, graph, [], 0)
    routes.sort()
    shortest = routes[0]

    if _plot:
        plot_points(shortest[1], marker='o:b')
        plot_points([start], marker='*', color='black')
        show_plot()
