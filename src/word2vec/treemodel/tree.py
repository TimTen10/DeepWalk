from anytree import Node, RenderTree, ContStyle, walker


def create_tree(leaves):
    counter = 0
    tree = [Node('0')]
    length = len(leaves)
    for i in range(1, length + length - 1):
        if i >= length - 1:
            tree.append(Node(leaves[i - length + 1], tree[counter]))
        else:
            tree.append(Node(f'{i}', tree[counter]))
        if not i % 2:
            counter += 1
    return tree


def get_path(node):
    return [s for s in str(node).split("'")[1].split('/')[1:]]


def main():
    counter = 0
    tree = [Node("0")]
    for i in range(1, 127 + 128):
        if i < 90:
            tree.append(Node(f"{i}", tree[counter]))
        else:
            tree.append(Node(f"{i}", tree[counter]))
        if not i % 2:
            counter += 1

    w = walker.Walker()
    node = str(w.walk(tree[0], tree[127])[-1][-1])
    for s in node.split("'")[1].split('/')[1:]:
        print(s)
    print(tree[127].is_leaf)


if __name__ == '__main__':
    main()