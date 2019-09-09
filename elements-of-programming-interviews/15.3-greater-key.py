class Node:
    def __init__(self, val: int, left: 'Node' = None, right: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right


def greater(root: Node, val: int) -> bool:
    ok = None

    while root:
        if root.val > val:
            ok = root.val
            root = root.left
        else:
            root = root.right
    return ok


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

assert greater(root, 23) == 29
