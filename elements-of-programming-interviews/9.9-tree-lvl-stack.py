from typing import List


class Node:
    def __init__(self, val: int, left: 'Node' = None, right: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right


def traverse(tree: Node) -> List[int]:
    stack = [tree]
    result = []

    while stack:
        current = stack

        line = []
        new_stack = []
        while current:
            node = current.pop()
            line.append(node.val)

            if node.left:
                new_stack.append(node.left)

            if node.right:
                new_stack.append(node.right)

        stack = new_stack

        if line:
            result.append(line)

    return result


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

result = traverse(tree)
assert result == [[1], [5, 2], [4, 3, 7, 6]]
