import sys


class Node:
    def __init__(self, val: int, left: 'Node' = None, right: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right


def is_bst(root: Node, min_interval: int = -sys.maxsize - 1, max_interval = sys.maxsize) -> bool:
    if root.val >= max_interval or root.val <= min_interval:
        return False

    left = True
    if root.left:
        left = is_bst(root.left, min_interval, root.val)

    right = True
    if root.right:
        right = is_bst(root.right, root.val, max_interval)

    return left and right


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

assert is_bst(root)

root = Node(19,
    Node(7,
        Node(3,
            Node(2),
            Node(8),
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

assert not is_bst(root)
