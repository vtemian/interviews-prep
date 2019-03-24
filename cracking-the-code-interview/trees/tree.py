from typing import List


class Node:
    def __init__(self, name: str, nodes: List['Node'] = []):
        self.name = name
        self.nodes = nodes

    def __str__(self) -> str:
        nodes = '\n\t'.join([str(node) for node in self.nodes])
        return "{}\n\t{}".format(self.name, nodes)


class Tree:
    def __init__(self, root: Node):
        self.root = root

    @property
    def is_binary_tree(self) -> bool:
        def check(node: Node) -> bool:
            if not node.nodes:
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


# check for binary tree
for use_case, expected_result in [
        (
            (1,
             [(2,
               [3, 4]),
              (10,
               [11, 12])]),
            True
        ),
        (
            (1,
             [(2,
               [3, 4, 5, 6]),
              (10,
               [11])]),
            False
        ),
]:
    tree = Tree(Tree.build(use_case))
    result = tree.is_binary_tree
    assert result == expected_result, "{} != {}".format(result, expected_result)
