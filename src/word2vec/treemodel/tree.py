import numpy as np


class Tree:

    def __init__(self, dimensionality, nodes, walks):
        self.dimensionality = dimensionality
        self.leaves = nodes
        self.walks = walks
        self.frequencies = self._generate_frequencies(walks)
        self.node_vectors = np.random.uniform(size=(dimensionality, len(nodes) - 1))
        # self.codes = self._generate_code(self.frequencies)

    def _generate_frequencies(self, walks):
        normalization = sum(len(walk) for walk in walks)
        frequencies = {leave: (sum(walk.count(leave) for walk in walks)/normalization) for leave in self.leaves}
        sorted_frequencies = {k: v for k, v in sorted(frequencies.items(), key=lambda item: item[1])}
        return sorted_frequencies
