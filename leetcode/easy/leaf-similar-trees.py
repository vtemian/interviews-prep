"""
Consider all the leaves of a binary tree.
From left to right order, the values of those leaves form a leaf value sequence.


For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9, 8).

Two binary trees are considered leaf-similar if their leaf value sequence is the same.

Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def leafSimilar(self, root1, root2):
        leafs_1 = []
        leafs_2 = []

        def count_leafs(root, container):
            if root is None:
                return

            if root.left is None and root.right is None:
                container.append(root.val)
                return

            count_leafs(root.left, container)
            count_leafs(root.right, container)

        count_leafs(root1, leafs_1)
        count_leafs(root2, leafs_2)

        return leafs_1 == leafs_2
