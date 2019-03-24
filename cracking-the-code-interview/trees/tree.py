from typing import List


class Node:
    def __init__(self, val: str, nodes: List['Node'] = []):
        self.val = val
        self.nodes = nodes

    def __str__(self) -> str:
        nodes = '\n\t'.join([str(node) for node in self.nodes])
        return "{}\n\t{}".format(self.val, nodes)

    def __eq__(self, other: 'Node') -> bool:
        return self.val == other.val

    def __lt__(self, other: 'Node') -> bool:
        return self.val < other.val

    def __gt__(self, other: 'Node') -> bool:
        return self.val > other.val


class Tree:
    def __init__(self, root: Node):
        self.root = root

    @property
    def is_binary_tree(self) -> bool:
        def check(node: Node) -> bool:
            if not node or not node.nodes:
                return True

            if len(node.nodes) > 2:
                return False

            result = True
            for kid in node.nodes:
                result &= check(kid)

            return result

        return check(self.root)

    @staticmethod
    def build(nodes: List):
        """
            (1,
                [(2,
                    [3, 4, 5]
                 ),
                 (10,
                    [11, 12, 13]
                )]
            )
        """

        if nodes is None:
            return None

        if isinstance(nodes, int):
            return Node(nodes)

        root, kids = nodes
        kids = [
            Tree.build(kid)
            for kid in kids
        ]
        return Node(root, kids)

    def __str__(self) -> str:
        return str(self.root)


class BinarySearchTree(Tree):
    @property
    def is_binary_search_tree(self) -> bool:
        def check(node: Node) -> bool:
            if node is None:
                return True

            if not node.nodes:
                return True

            left, right = node.nodes
            if left is None:
                return not node > right and check(right)

            if right is None:
                return not node < left and check(left)

            if not left < node < right:
                return False

            return check(left) and check(right)

        return self.is_binary_tree and check(self.root)


# check for binary tree
for use_case, *expected_result in [
        (
            (8,
             [(4,
               [2, 6]),
              (10,
               [None, 20])]),
            True, True
        ),
        (
            (1,
             [(2,
               [3, 4, 5, 6]),
              (10,
               [11])]),
            False, False
        ),
]:
    tree = BinarySearchTree(BinarySearchTree.build(use_case))

    is_binary_tree, is_binary_search_tree = expected_result

    assert tree.is_binary_tree == is_binary_tree, \
           "{} != {}".format(tree.is_binary_tree, is_binary_tree)

    assert tree.is_binary_search_tree == is_binary_search_tree, \
           "{} != {}".format(tree, is_binary_search_tree)
