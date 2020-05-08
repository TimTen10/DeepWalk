def _get_alpha(graph_dict, current_node, last_node, node, p, q):
    if last_node == node:
        alpha = 1/p
    elif node in graph_dict[last_node]:
        alpha = 1
    else:
        alpha = 1/q
    return alpha


def transition_probabilities(graph_dict, current_node, last_node, p, q):
    if not last_node:
        alphas = [1 for neighbor in graph_dict[current_node]]
    else:
        # distances berechnen und abhängig davon alphas
        alphas = [_get_alpha(graph_dict, current_node, last_node, node, p, q) for node in graph_dict[current_node]]
    return alphas
