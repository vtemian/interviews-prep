from tree import Node, BinaryTree


def find_right_left_most_node(node: Node):
    current = node.nodes[1]

    while current.nodes:
        if current.nodes[0] is None:
            return current

        current = current.nodes[0]

    return current


def find_successor(node: Node):
    if not node:
        return None

    if len(node.nodes) > 1 and node.nodes[1] is not None:
        return find_right_left_most_node(node)

    # we need to check the parent
    # we may be the left child, thus we need to return parent
    # we may be the right child, we need to go to grandpa

    while node.parent and node.parent.nodes[0] != node:
        node = node.parent

    return node.parent


bt = BinaryTree(BinaryTree.build(
    (
        8,
        [(4,
          [2, 6]),
         (10,
          [None, 20])]
    )
))

for use_case, expected_result in [
    (4, 6),
    (6, 8),
    (10, 20),
    (20, None),
]:
    node = bt.find_node(use_case)

    result = find_successor(node)
    if not expected_result:
        assert result is None, "{} is not None".format(result)
    else:
        if result is None:
            assert False, "None != {}".format(expected_result)
        else:
            assert result.val == expected_result, "{} != {}".format(result, expected_result)
