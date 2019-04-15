"""
2, 3, 1, 4, 5, 6, 7
"""

from typing import List
from tree import Node, BinarySearchTree


# 1. get all tree's nodes
# 2. weave list


def _generate_weaved_nodes(root: Node) -> List[Node]:
    if not root:
        return []

    if not root.nodes:
        return [root.val]

    left = _generate_weaved_nodes(root.nodes[0])
    right = _generate_weaved_nodes(root.nodes[1])

    return [
        [root.val] + left + right,
        [root.val] + right + left,
    ]


def unfold(nodes):
    for node in nodes:
        if isinstance(node, list):
            break
    else:
        return nodes

    result = []

    for p in nodes[1:]:
        flat = unfold(p)
        if not isinstance(flat[0], list):
            flat = [flat]
        for n in flat:
            result.append([nodes[0]] + n)

    return result



for count, (tree, expected_result) in enumerate([
    [
        [2, [1, 3]],
        [
            [2, 1, 3],
            [2, 3, 1]
        ]
    ],

    [
        [2, [(1, [(0, [5, 6]), (3, [-1, -2])]), (6, [(5, [10, 11]), (7, [13, 14]) ]) ]],
        [

          [
              [2, 1, 0, 5, 6],
              [2, 1, 0, 6, 5],
              [2, 1, 3, -1, -2],
              [2, 1, 3, -2, -1],
              [2, 1, 3, -1, -2],
              [2, 1, 3, -2, -1],
              [2, 1, 0, 5, 6],
              [2, 1, 0, 6, 5],
              [2, 6, 5, 10, 11],
              [2, 6, 5, 11, 10],
              [2, 6, 7, 13, 14],
              [2, 6, 7, 14, 13],
              [2, 6, 7, 13, 14],
              [2, 6, 7, 14, 13],
              [2, 6, 5, 10, 11],
              [2, 6, 5, 11, 10]
          ],
          [
              [2, 6, 5, 10, 11],
              [2, 6, 5, 11, 10],
              [2, 6, 7, 13, 14],
              [2, 6, 7, 14, 13],
              [2, 6, 7, 13, 14],
              [2, 6, 7, 14, 13],
              [2, 6, 5, 10, 11],
              [2, 6, 5, 11, 10],
              [2, 1, 0, 5, 6],
              [2, 1, 0, 6, 5],
              [2, 1, 3, -1, -2],
              [2, 1, 3, -2, -1],
              [2, 1, 3, -1, -2],
              [2, 1, 3, -2, -1],
              [2, 1, 0, 5, 6],
              [2, 1, 0, 6, 5]
           ]
        ]
    ],
]):
    bst = BinarySearchTree(BinarySearchTree.build(tree))

    result = []
    folded = _generate_weaved_nodes(bst.root)
    for fold in folded:
        r = unfold(fold)
        result.append(unfold(fold))

    assert result == expected_result, "{} != {}".format(result, expected_result)
