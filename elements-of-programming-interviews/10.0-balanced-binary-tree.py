from typing import List, Tuple, Optional


class Node:
    def __init__(self, val: int, left: 'Node' = None, right: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right


def is_balanced(tree: Node) -> bool:
    def balanced(node: Optional[Node], current_depth: int = 0) -> Tuple[int, bool]:
        if not node:
            return current_depth, True

        left, is_balanced = balanced(node.left, current_depth + 1)
        if not is_balanced:
            return left + current_depth, False

        right, is_balanced = balanced(node.right, current_depth + 1)
        if not is_balanced:
            return right + current_depth, False

        return max(left, right) + 1, abs(left - right) < 2

    return balanced(tree)[1]

tree = Node(
    1,
    Node(
        2,
        Node(3),
        Node(4)
    ),
    Node(
        5,
        Node(6),
        Node(7)
    )
)

result = is_balanced(tree)
assert result, result


tree = Node(
    1,
    Node(
        2,
        Node(3),
        Node(4,
             Node(9),
             Node(8,
                  Node(10),
                  Node(11)))
        ),
    Node(
        5,
        Node(6),
        Node(7))
    )

result = is_balanced(tree)
assert not result, result
