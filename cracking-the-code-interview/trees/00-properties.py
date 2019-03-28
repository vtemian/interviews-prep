from fixtures import (SIMPLE_TREE,
                      COMPLETE_TREES, INCOMPLETE_TREES,
                      FULL_TREES, NOT_FULL_TREES,
                      PERFECT_TREES, IMPERFECT_TREES)
from tree import Node, Tree, BinaryTree, BinarySearchTree

# test basic structures
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


# test find method
bst = BinarySearchTree(BinarySearchTree.build(SIMPLE_TREE))
for use_case, expected_result in [
        (8, True),
        (20, True),
        (-1, False),
]:
    result = bst.find(use_case)
    assert result == expected_result, "{} != {}".format(result, expected_result)


# test insert method
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


# test insert method
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


# test that a tree is completed
for raw_nodes in COMPLETE_TREES:
    bt = BinaryTree(BinaryTree.build(raw_nodes))
    assert bt.is_complete, "Tree {} is not complete".format(bt)

# test that a tree is incompleted
for raw_nodes in INCOMPLETE_TREES:
    bt = BinaryTree(BinaryTree.build(raw_nodes))
    assert not bt.is_complete, "Tree {} is complete".format(bt)

# test that a tree is full
for raw_nodes in FULL_TREES:
    bt = BinaryTree(BinaryTree.build(raw_nodes))
    assert bt.is_full, "Tree {} is not full".format(bt)

# test that a tree is not full
for raw_nodes in NOT_FULL_TREES:
    bt = BinaryTree(BinaryTree.build(raw_nodes))
    assert not bt.is_full, "Tree {} is full".format(bt)

# test that a tree is perfect
for raw_nodes in PERFECT_TREES:
    bt = BinaryTree(BinaryTree.build(raw_nodes))
    assert bt.is_perfect, "Tree {} is not perfect".format(bt)

# test that a tree is not perfect
for raw_nodes in IMPERFECT_TREES:
    bt = BinaryTree(BinaryTree.build(raw_nodes))
    assert not bt.is_perfect, "Tree {} is perfect".format(bt)

# test in order traversal
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

# test pre order traversal
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
