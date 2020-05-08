import random

from src.util.bias import transition_probabilities


class Graph:

    def __init__(self, graph_dict):
        self.graph_dict = graph_dict
        self.nodes = graph_dict.keys()

    def random_walk(self, node, length, p=1, q=1):
        """
        Currently only working for unweighted graphs!

        :param node: starting node of the walk
        :param length: length of the walk
        :param p: backtrack parameter (high: new nodes, low: already sampled)
        :param q: In-Out parameter (visit closer or further away nodes)
        :return: sequence of randomly chosen, connected nodes
        """
        walk = [node]
        current_node = node
        while len(walk) < length:
            last_node = None if len(walk) == 1 else walk[-2]
            walk += random.choices(
                # self.graph_dict[node] returns a list of all neighboring nodes
                population=self.graph_dict[current_node],
                weights=transition_probabilities(self.graph_dict, current_node, last_node, p, q)
            )
            current_node = walk[-1]
        return walk


def main():
    g_d = {
        't': ['x1', 'v'],
        'v': ['t', 'x1', 'x2', 'x3'],
        'x1': ['t', 'v'],
        'x2': ['v'],
        'x3': ['v']
    }
    graph = Graph(g_d)
    print(graph.random_walk('t', 17))


if __name__ == '__main__':
    main()
