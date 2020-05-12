import src.network.graph as g
from src.word2vec.util import preprocess as pp
from src.word2vec.treemodel import tree
from anytree import RenderTree, ContStyle
import json


def main():
    # generate a graph with a graph dict file
    with open(f"./../examplegraphs/pokegraph.json", 'r') as pokefile:
        graph_data = json.load(pokefile)
    graph = g.Graph(graph_data)

    # generate walks
    walks = pp.generate_walks(graph, 5, 1)
    print(graph.nodes)
    # it keeps the order, very important! But why again?
    # Only order of graph.nodes plays a role (later on in generate_one_hot)
    for w, n in zip(walks, graph.nodes):
        print(n, w)

    # generate input pairs
    pairs = pp.generate_pairs(walks, 2)
    # print(pairs)

    print("Tree Test")
    baum = tree.create_tree(list(graph.nodes))
    """
    print(RenderTree(baum[0], style=ContStyle))
    for knoten in baum:
        if knoten.is_leaf:
            print(knoten)
    """
    print(tree.get_path(baum[92].children[0]))


if __name__ == '__main__':
    main()
