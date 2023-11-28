import math

from utils import plot_points, show_plot, get_equidistant_points


def find_ordinary_path(upper_bound: tuple, lower_bound: tuple, num_points_each_obstacle=10, _plot=False):
    middle_points = [(min(up[0], down[0]), (down[1] + up[1]) / 2)
                     for up, down in zip(upper_bound, lower_bound)]
    path = []
    for i in range(1, len(middle_points)):
        path += get_equidistant_points(middle_points[i - 1], middle_points[i], num_points_each_obstacle)

    if _plot:
        plot_points(middle_points, color='red')
        plot_points(path, color='black', marker='->')
        plot_points(upper_bound, color='orange')
        plot_points(lower_bound, color='blue')
        show_plot()

    return path


class Dijkstra:
    def __init__(self, obstacles):
        # x, y, cost
        # NOTE: don't let robot go in minus x-axis (only forward movement)
        self.movements = [
            [1, 0, 1],
            [0, 1, 1],
            [0, -1, 1],
            [1, -1, math.sqrt(2)],
            [1, 1, math.sqrt(2)]
        ]
        self.back_movements = [
            [-1, 0],
            [0, 1],
            [0, -1],
            [-1, -1],
            [-1, 1]
        ]
        self.obstacles = {self.hash_position(obs[0], obs[1]) for obs in obstacles}

    def hash_position(self, x, y):
        return f'{x}_{y}'

    def get_x_from_hash(self, string):
        return int(string.split('_')[0])

    def get_y_from_hash(self, string):
        return int(string.split('_')[1])

    def is_valid(self, node):
        return node not in self.obstacles

    def backtrack(self, initial, goal, costs):
        # idea start at the last node then choose the least number of steps to go back
        # last node
        path = [goal]

        while True:
            # check up down left right - choose the direction that has the least distance
            potential_distances = []
            potential_nodes = []

            for move_x, move_y in self.back_movements:
                node = self.hash_position(self.get_x_from_hash(path[-1]) + move_x,
                                          self.get_y_from_hash(path[-1]) + move_y)
                if self.is_valid(node) and node in costs:
                    potential_nodes.append(node)
                    potential_distances.append(costs[node])

            least_distance_index = min(range(len(potential_distances)), key=lambda i: potential_distances[i])
            path.append(potential_nodes[least_distance_index])

            if path[-1] == initial:
                break

        return list(reversed(path))

    def find_minimal_path(self, initial, goal, _plot=False):
        start_node = self.hash_position(initial[0], initial[1])
        goal_node = self.hash_position(goal[0], goal[1])

        open_set, closed_set = dict(), dict()
        open_set[start_node] = 0  # node: cost

        while True:
            current = min(open_set, key=lambda n: open_set[n])
            cost = open_set[current]

            if current == goal_node:
                break

            # Remove the item from the open set
            del open_set[current]

            # Add it to the closed set
            closed_set[current] = cost

            # expand search grid based on motion model
            for move_x, move_y, move_cost in self.movements:
                node = self.hash_position(self.get_x_from_hash(current) + move_x,
                                          self.get_y_from_hash(current) + move_y)
                node_cost = closed_set[current] + move_cost

                if node in closed_set:
                    continue

                if not self.is_valid(node):
                    continue

                if node not in open_set:
                    open_set[node] = node_cost  # Discover a new node
                else:
                    if open_set[node] >= node_cost:
                        # This path is the best until now. record it!
                        open_set[node] = node_cost

        path = self.backtrack(start_node, goal_node, closed_set)
        path = [(self.get_x_from_hash(p), self.get_y_from_hash(p)) for p in path]
        if _plot:
            plot_points([initial], color='red', marker='c')
            plot_points([goal], color='green', marker='c')
            plot_points([(self.get_x_from_hash(obs), self.get_y_from_hash(obs)) for obs in self.obstacles], marker='o', color='orange')
            plot_points(path, marker='o:r')
            show_plot()

        return path
