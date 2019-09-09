from typing import List


class Node:
    def __init__(self, val: int, left: 'Node' = None, right: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right


def largest(root: Node, k: int) -> List[int]:
    collector = []

    def helper(node):
        nonlocal collector

        if not node or len(collector) > k:
            return

        helper(node.right)
        if len(collector) < k:
            collector.append(node.val)
            helper(node.left)

    helper(root)

    return collector


root = Node(19,
    Node(7,
        Node(3,
            Node(2),
            Node(5),
        ),
        Node(11,
            None,
            Node(17,
                Node(13),
                None
            )
        )
    ),
    Node(43,
        Node(23,
            None,
            Node(37,
                Node(29,
                    None,
                    Node(31)
                ),
                Node(41)
            )
        ),
        Node(47,
            None,
            Node(53)
        )
    )
)

result = largest(root, 5)
assert result == [53, 47, 43, 41, 37], result
