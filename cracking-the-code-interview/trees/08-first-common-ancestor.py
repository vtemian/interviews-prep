from copy import deepcopy

from tree import Tree, Node


def _get_first_leaf(node: Node = None) -> Node:
    if node is None:
        return None

    if not node.nodes:
        return node

    for kid in node.nodes:
        result = _get_first_leaf(kid)
        if result:
            return result

    return None


def find_first_common_ancestor(first: Tree, second: Tree) -> Node:
    first = first.root
    second = second.root

    if len(first.nodes) != len(second.nodes) or second != first:
        return None

    queue = []
    count = 0
    while count < len(first.nodes):
        queue.append(
            (first.nodes[count], second.nodes[count], first),
        )
        count += 1

    while queue:
        first, second, _from = queue.pop(0)

        if first != second:
            return _from

        if not first.nodes or not second.nodes:
            continue

        count = 0
        while count < len(first.nodes):
            queue.append(
                (first.nodes[count], second.nodes[count], first),
            )
            count += 1
    return None


for common, first_nodes, second_nodes in [
        (
            (1,
             [(2,
               [3, 4, 5, 6]),
              (10,
               [11])]),
            (90, [1, 2]),
            (91, [5, 6]),
        )
]:
    first = Tree(Tree.build(common))
    second = deepcopy(first)

    last_first = _get_first_leaf(first.root)
    last_first.nodes = [Tree.build(first_nodes)]

    last_second = _get_first_leaf(second.root)
    last_second.nodes = [Tree.build(second_nodes)]

    result = find_first_common_ancestor(first, second)
    assert result == last_first, "{} != {}".format(result, last_first)
