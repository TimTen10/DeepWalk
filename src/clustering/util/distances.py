# might sometimes also be called metrics


def lp_metric(vec1, vec2, p=2):
    """
    :param vec1: first vector
    :param vec2: second vector
    :param p: p for Lp metric
    :return: distance between vec1 and vec2 calculated by the given Lp metric

    # TODO: missing the maximum metric!
    """
    return sum(abs(v1 - v2)**p for v1, v2 in zip(vec1, vec2))**(1/p)


def hamming_distance(vec1, vec2):
    """
    :param vec1: first vector
    :param vec2: second vector
    :return: hamming distance for vec1 and vec2
    """
    return sum(v1 != v2 for v1, v2 in zip(vec1, vec2))


def jaccard_metric(vec1, vec2):
    # TODO: Jaccard metric
    pass
