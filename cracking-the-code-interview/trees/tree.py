from typing import List, Callable, Union, Tuple


class Node:
    def __init__(self, val: Union[str, int], nodes: List['Node'] = None):
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

    @staticmethod
    def node_depth(node: Node) -> int:
        if node is None:
            return 0

        max_depth = 1
        for kid in node.nodes:
            kid_depth = 1 + Tree.node_depth(kid)
            max_depth = max(max_depth, kid_depth)

        return max_depth

    @property
    def depth(self) -> int:
        return Tree.node_depth(self.root)

    @property
    def last_layer(self) -> List[Node]:
        depth = self.depth - 1

        def _get_last_layer(node: Node, current_layer: int = 0) -> List[Node]:
            if node is None or current_layer == depth:
                return [node]

            kids = []
            for kid in node.nodes:
                kids += _get_last_layer(kid, current_layer + 1)

            return kids

        return _get_last_layer(self.root)

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

        if len(nodes) < 2:
            return Node(nodes[0])

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
    def in_order(self, visit: Callable) -> None:
        def _in_order(node: Node) -> None:
            nonlocal visit

            if node is None:
                return

            if len(node.nodes) > 0:
                _in_order(node.nodes[0])

            visit(node)

            if len(node.nodes) > 1:
                _in_order(node.nodes[1])

        return _in_order(self.root)

    def pre_order(self, visit: Callable) -> None:
        def _pre_order(node: Node) -> None:
            nonlocal visit

            if node is None:
                return

            visit(node)

            if len(node.nodes) > 0:
                _pre_order(node.nodes[0])

            if len(node.nodes) > 1:
                _pre_order(node.nodes[1])

        return _pre_order(self.root)

    def post_order(self, visit: Callable) -> None:
        def _post_order(node: Node) -> None:
            nonlocal visit

            if node is None:
                return

            if len(node.nodes) > 0:
                _post_order(node.nodes[0])

            if len(node.nodes) > 1:
                _post_order(node.nodes[1])

            visit(node)

        return _post_order(self.root)

    @property
    def is_balanced(self) -> bool:
        """ Each subtrees have a difference of maxmimum one in height. """

        def _is_balanced(node: Node) -> bool:
            if not node:
                return False

            if not node.nodes:
                return True

            if len(node.nodes) < 2:
                return Tree.node_depth(node.nodes[0]) == 1

            depth = abs(Tree.node_depth(node.nodes[0]) -
                        Tree.node_depth(node.nodes[1]))
            if depth > 1:
                return False

            return _is_balanced(node.nodes[0]) and _is_balanced(node.nodes[1])

        return _is_balanced(self.root)

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

    @property
    def is_complete(self) -> bool:
        """
        All levels are filled, except maybe the last level.
        Check last level if it's filled from left to right.

                  10
               /      \
              5       20
             / \        \
            3   7       30
                 False


                  10
               /      \
              5       20
             / \      /
            3   7    15

                 True


                  10
               /      \
              5       20
             /
            3
                 True
        """

        last_layer = self.last_layer

        idx = 1
        while idx < len(last_layer):
            prev, current = last_layer[idx - 1], last_layer[idx]

            if prev is None and current is not None:
                return False

            idx += 1

        return True

    @property
    def is_full(self) -> bool:
        """
        All nodes need to have two or zero children.
        """

        def _is_full(node: Node) -> bool:
            if node is None:
                return False

            if len(node.nodes) == 1:
                return False

            for kid in node.nodes:
                if not _is_full(kid):
                    return False

            return True

        return _is_full(self.root)

    @property
    def is_perfect(self) -> bool:
        last_layer = self.last_layer
        return (len(last_layer) == 2 ** (self.depth - 1)
                and all([node is not None for node in last_layer]))


class BinarySearchTree(BinaryTree):
    @property
    def is_binary_search_tree(self) -> bool:
        def check(node: Node) -> bool:
            if node is None:
                return True

            if not node.nodes:
                return True

            if len(node.nodes) < 2:
                return False

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


class Trie(Tree):
    def __init__(self):
        self.root = Node('*')

    def _find_start(self, node: Node, ch: str) -> Tuple[Union[None, Node], str]:
        if not ch:
            return None, ch

        if node.val != ch[0]:
            return None, ch

        for kid in node.nodes:
            result, rest = self._find_start(kid, ch[1:])
            if result:
                return result, rest

        return node, ch[1:]

    def index(self, string: str):
        rest = string
        start = self.root

        for node in self.root.nodes:
            result = self._find_start(node, string)
            if result[0]:
                start, rest = result
                break

        for ch in rest:
            start.nodes.append(Node(ch))
            start = start.nodes[-1]

    def has_prefix(self, string: str) -> bool:
        def _has_prefix(node: Node, rest: str) -> bool:
            if not rest:
                return True

            if not node:
                return None

            if node.val != rest[0]:
                return False

            for kid in node.nodes:
                if _has_prefix(kid, rest[1:]):
                    return True

            return len(rest) == 1

        for kid in self.root.nodes:
            if _has_prefix(kid, string):
                return True

        return False
