def generate_walks(graph, length, quantity):
    """
    This methods generates and returns quantity * |V| many random walks (|V| = number of nodes in graph)

    :param graph: graph to do random walks on
    :param length: length of the random walks
    :param quantity: number of walks per node
    :return: random walks
    """
    # These two lines changes the order of walks: 1. one walk each node and repeat 2. all works of one node then next
    # return [graph.random_walk(node, length) for _ in range(quantity) for node in graph.nodes]
    return [graph.random_walk(node, length) for node in graph.nodes for _ in range(quantity)]


# TODO: Input pairs have to be 1-hot vectors or get "translated" on the fly
def generate_pairs(walks, window):
    """
    This method takes in a number of random walks and returns input pairs for a word2vec model
    :param walks: random walks to generate input pairs from
    :param window: window size
    :return: input pairs
    """
    pairs = []
    for walk in walks:
        m = len(walk)
        for node in walk:
            i = walk.index(node)
            # both variants work! Understand why part behind + works as it does!
            # slice = walk[max(0, i-window):min(m, i+window+1)]
            neighbors = walk[max(0, i-window):i] + walk[i+1:min(m, i+window+1)]
            # TODO: Pairs have to stay grouped in regard to walk / window and node they originate from!
            pairs.extend((node, i) for i in neighbors)
    return pairs


def generate_one_hot(nodes, pair):
    """
    Generates an one-hot encoded vector for both values in the pair

    :param nodes: a list of nodes in the graph
    :param pair: training pair to generate one-hot encoding for
    :return: one-hot encoding for input value pair[0] and output value pair[1]
    """
    return [0 if n != pair[0] else 1 for n in nodes], [0 if n != pair[1] else 1 for n in nodes]
