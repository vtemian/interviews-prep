from typing import List


# describe a simple tree
RAW_NODES = (
    8,
    [(4,
      [2, 6]),
     (10,
      [None, 20])]
)


class Node:
    def __init__(self, val: str, nodes: List['Node'] = None):
        self.val = val
        self.nodes = nodes or []

    def __str__(self) -> str:
        return str(self.val)

    def __eq__(self, other: 'Node') -> bool:
        return self.val == other.val

    def __lt__(self, other: 'Node') -> bool:
        return self.val < other.val

    def __gt__(self, other: 'Node') -> bool:
        return self.val > other.val


class Tree:
    def __init__(self, root: Node):
        self.root = root

    def find(self, val: int) -> bool:
        def _find(node: Node):
            if node is None:
                return False

            if node.val == val:
                return True

            result = False
            for kid in node.nodes:
                result |= _find(kid)

            return result

        return _find(self.root)

    @staticmethod
    def build(nodes: List):
        """
            (1,
                [(2,
                    [3, 4, 5]
                 ),
                 (10,
                    [11, 12, 13]
                 ),
                 (8, )]
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

    def insert(self, val: int) -> bool:
        self.root.nodes.append(Node(val))
        return True

    def __str__(self) -> str:
        def _repr(node: Node, depth: int = 0) -> str:
            if not node:
                return ''

            output = '\n' + '|  ' * depth
            if depth == 0:
                output += '-- ' + str(node)
            else:
                output += '|-- ' + str(node)

            for kid in node.nodes:
                output += _repr(kid, depth + 1)

            return output

        return _repr(self.root)


class BinaryTree(Tree):
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

    def insert(self, val: int) -> bool:
        if self.find(val):
            return False

        def _insert(node: Node):
            if node is None:
                return False

            if len(node.nodes) < 2:
                node.nodes.append(Node(val))
                return True

            for kid in node.nodes:
                if _insert(kid):
                    return True

            return False

        return _insert(self.root)


class BinarySearchTree(BinaryTree):
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

    def insert(self, val: int) -> bool:
        if self.find(val):
            return False

        def _insert(node: Node):
            if node is None:
                return False

            # [None, None]
            if not node.nodes:
                left, right = None, None

                if val > node.val:
                    right = Node(val)
                else:
                    left = Node(val)

                node.nodes = [left, right]
                return True

            # [None, 2]
            # [1, None]
            left, right = node.nodes
            if left is None or right is None:
                if left is None and val < node.val:
                    node.nodes[0] = Node(val)
                    return True
                if right is None and val > node.val:
                    node.nodes[1] = Node(val)
                    return True

            if val > node.val:
                return _insert(right)

            return _insert(left)


        return _insert(self.root)


# test basic structures
for use_case, *expected_result in [
        (
            RAW_NODES,
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


# test find method
bst = BinarySearchTree(BinarySearchTree.build(RAW_NODES))
for use_case, expected_result in [
        (8, True),
        (20, True),
        (-1, False),
]:
    result = bst.find(use_case)
    assert result == expected_result, "{} != {}".format(result, expected_result)


# test insert method
bt = BinaryTree(BinaryTree.build(RAW_NODES))
for use_case, *expected_result in [
        (1, True, True, """
-- 8
|  |-- 4
|  |  |-- 2
|  |  |  |-- 1
|  |  |-- 6
|  |-- 10
|  |  |-- 20"""),

        (0, True, True, """
-- 8
|  |-- 4
|  |  |-- 2
|  |  |  |-- 1
|  |  |  |-- 0
|  |  |-- 6
|  |-- 10
|  |  |-- 20"""),

        (3, True, True, """
-- 8
|  |-- 4
|  |  |-- 2
|  |  |  |-- 1
|  |  |  |  |-- 3
|  |  |  |-- 0
|  |  |-- 6
|  |-- 10
|  |  |-- 20"""),
        (8, False, True, """
-- 8
|  |-- 4
|  |  |-- 2
|  |  |  |-- 1
|  |  |  |  |-- 3
|  |  |  |-- 0
|  |  |-- 6
|  |-- 10
|  |  |-- 20"""),
]:
    insert_result, find_result, tree_repr = expected_result

    result = bt.insert(use_case)
    assert result == insert_result, "{} != {}".format(result, insert_result)

    result = bt.find(use_case)
    assert result == find_result, "{} != {}".format(result, find_result)

    assert str(bt) == tree_repr, "{} != {}".format(str(bt), tree_repr)


# test insert method
bst = BinarySearchTree(BinarySearchTree.build(RAW_NODES))
for use_case, *expected_result in [
        (1, True, """
-- 8
|  |-- 4
|  |  |-- 2
|  |  |  |-- 1
|  |  |-- 6
|  |-- 10
|  |  |-- 20"""),
        (15, True, """
-- 8
|  |-- 4
|  |  |-- 2
|  |  |  |-- 1
|  |  |-- 6
|  |-- 10
|  |  |-- 20
|  |  |  |-- 15"""),
        (15, False, """
-- 8
|  |-- 4
|  |  |-- 2
|  |  |  |-- 1
|  |  |-- 6
|  |-- 10
|  |  |-- 20
|  |  |  |-- 15"""),
]:
    insert_result, tree_repr = expected_result

    result = bst.insert(use_case)

    assert result == insert_result, "{} != {}".format(result, insert_result)
    assert str(bst) == tree_repr, "{} != {}".format(str(bst), tree_repr)
