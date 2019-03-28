import sys

from fixtures import (SIMPLE_TREE,
                      COMPLETE_TREES, INCOMPLETE_TREES,
                      FULL_TREES, NOT_FULL_TREES,
                      PERFECT_TREES, IMPERFECT_TREES)
from tree import Node, Tree, BinaryTree, BinarySearchTree


def test_basic_structures():
    for use_case, *expected_result in [
            (
                SIMPLE_TREE,
                True, True, 3
            ),
            (
                (1,
                 [(2,
                   [3, 4, 5, 6]),
                  (10,
                   [11])]),
                False, False, 3
            ),
    ]:
        tree = BinarySearchTree(BinarySearchTree.build(use_case))

        is_binary_tree, is_binary_search_tree, depth = expected_result

        assert tree.is_binary_tree == is_binary_tree, \
               "{} != {}".format(tree.is_binary_tree, is_binary_tree)

        assert tree.is_binary_search_tree == is_binary_search_tree, \
               "{} != {}".format(tree, is_binary_search_tree)

        assert tree.depth == depth, \
               "{} != {}".format(tree.depth, depth)


def test_find_method_in_BST():
    bst = BinarySearchTree(BinarySearchTree.build(SIMPLE_TREE))
    for use_case, expected_result in [
            (8, True),
            (20, True),
            (-1, False),
    ]:
        result = bst.find(use_case)
        assert result == expected_result, "{} != {}".format(result, expected_result)


def test_insert_method_for_BT():
    bt = BinaryTree(BinaryTree.build(SIMPLE_TREE))
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


def test_insert_method_for_BST():
    bst = BinarySearchTree(BinarySearchTree.build(SIMPLE_TREE))
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


def test_that_a_tree_is_completed():
    for raw_nodes in COMPLETE_TREES:
        bt = BinaryTree(BinaryTree.build(raw_nodes))
        assert bt.is_complete, "Tree {} is not complete".format(bt)

def test_that_a_tree_is_incompleted():
    for raw_nodes in INCOMPLETE_TREES:
        bt = BinaryTree(BinaryTree.build(raw_nodes))
        assert not bt.is_complete, "Tree {} is complete".format(bt)

def test_that_a_tree_is_full():
    for raw_nodes in FULL_TREES:
        bt = BinaryTree(BinaryTree.build(raw_nodes))
        assert bt.is_full, "Tree {} is not full".format(bt)

def test_that_a_tree_is_full():
    for raw_nodes in NOT_FULL_TREES:
        bt = BinaryTree(BinaryTree.build(raw_nodes))
        assert not bt.is_full, "Tree {} is full".format(bt)

def test_that_a_tree_is_perfect():
    for raw_nodes in PERFECT_TREES:
        bt = BinaryTree(BinaryTree.build(raw_nodes))
        assert bt.is_perfect, "Tree {} is not perfect".format(bt)

def test_that_a_tree_is_not_perfect():
    for raw_nodes in IMPERFECT_TREES:
        bt = BinaryTree(BinaryTree.build(raw_nodes))
        assert not bt.is_perfect, "Tree {} is perfect".format(bt)


def test_in_order_traversal():
    for nodes, expected_result in [
        (
            (
                8,
                [(4,
                  [2, 6]),
                 (10,
                  [None, 20])]
            ),
            "2->4->6->8->10->20"
        ),
        (
            (1, ), "1"
        ),

        (
            (1, [2]), "2->1"
        ),

        (
            (1, [None, 2]), "1->2"
        ),
    ]:
        result = []
        def visit(node: Node) -> None:
            result.append(node.val)

        bt = BinaryTree(BinaryTree.build(nodes))
        bt.in_order(visit)

        result = "->".join([str(val) for val in result])
        assert result == expected_result, "{} != {}".format(result, expected_result)


def test_pre_order_traversal():
    for nodes, expected_result in [
        (
            (
                8,
                [(4,
                  [2, 6]),
                 (10,
                  [None, 20])]
            ),
            "8->4->2->6->10->20"
        ),
        (
            (1, ), "1"
        ),

        (
            (1, [2]), "1->2"
        ),

        (
            (1, [None, 2]), "1->2"
        ),
    ]:
        result = []
        def visit(node: Node) -> None:
            result.append(node.val)

        bt = BinaryTree(BinaryTree.build(nodes))
        bt.pre_order(visit)

        result = "->".join([str(val) for val in result])
        assert result == expected_result, "{} != {}".format(result, expected_result)


def test_post_order_traversal():
    for nodes, expected_result in [
        (
            (
                8,
                [(4,
                  [2, 6]),
                 (10,
                  [None, 20])]
            ),
            "2->6->4->20->10->8"
        ),
        (
            (1, ), "1"
        ),

        (
            (1, [2]), "2->1"
        ),

        (
            (1, [None, 2]), "2->1"
        ),
    ]:
        result = []
        def visit(node: Node) -> None:
            result.append(node.val)

        bt = BinaryTree(BinaryTree.build(nodes))
        bt.post_order(visit)

        result = "->".join([str(val) for val in result])
        assert result == expected_result, "{} != {}".format(result, expected_result)


def run_test(local, test: str):
    try:
        local[test]()
        sys.stdout.write('.')
    except AssertionError as exc:
        print("{} failed with {}".format(test, exc))


if __name__ == '__main__':
    if len(sys.argv) > 1:
        run_test(locals(), sys.argv[1])
    else:
        tests = [
            fn
            for fn in locals()
            if fn.startswith('test_')
        ]
        local = locals()
        for fn in tests:
            run_test(local, fn)
