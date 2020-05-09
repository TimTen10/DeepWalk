import src.network.graph as g
from src.word2vec.util import preprocess as pp
import json


def main():
    # generate a graph with a graph dict file
    with open(f"./../examplegraphs/pokegraph.json", 'r') as pokefile:
        graph_data = json.load(pokefile)
    graph = g.Graph(graph_data)

    # generate walks
    walks = pp.generate_walks(graph, 5, 1)

    # it keeps the order! Very important
    for w, n in zip(walks, graph.nodes):
        print(n, w)

    # generate input pairs
    pairs = pp.generate_pairs(walks, 2)
    print(pairs)


if __name__ == '__main__':
    main()