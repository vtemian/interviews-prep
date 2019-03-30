from typing import List


class LinkedNode:
    def __init__(self, val: int, next: 'LinkedNode' = None):
        self.val = val
        self.next = next

    @staticmethod
    def build(nodes: List) -> 'LinkedNode':
        if not nodes:
            return None

        head = current_node = LinkedNode(nodes[0])

        for node in nodes[1:]:
            current_node.next = LinkedNode(node)
            current_node = current_node.next

        return head

    def __repr__(self) -> str:
        """ 1->2->3 ... """

        store = {}
        result = str(self.val)

        head = self.next

        while head and id(head) not in store:
            result += '->{}'.format(head.val)

            store[id(head)] = head

            head = head.next

        return result


class TreeNode:
    def __init__(self, val: int, left: 'TreeNode' = None, right: 'TreeNode' = None):
        self.val = val

        self.left = left
        self.right = right

    def __str__(self):
        return str(self.val)

    @staticmethod
    def build(nodes: List):
        """
            (1,
                [(2,
                    [3, 4]
                 ),
                 (10,
                    [11, 12]
                 )]
            )
        """

        if nodes is None:
            return None

        if isinstance(nodes, int):
            return TreeNode(nodes)

        root, kids = nodes
        if len(kids) > 1:
            return TreeNode(root, TreeNode.build(kids[0]),
                            TreeNode.build(kids[1]))

        return TreeNode(root, TreeNode.build(kids[0]))


def build_linked_list(node: TreeNode):
    result = []
    current_layer = LinkedNode(node)

    while current_layer:
        result.append(current_layer)

        head = current_layer
        new_layer = []

        while head:
            if head.val.left:
                new_layer.append(head.val.left)

            if head.val.right:
                new_layer.append(head.val.right)

            head = head.next

        current_layer = LinkedNode.build(new_layer)

    return result


tree = TreeNode.build(
    (
        1,
        [
            (2, [3, 4]),
            (10, [11, 12])
        ]
    )
)
assert str(build_linked_list(tree)) == "[1, 2->10, 3->4->11->12]"
