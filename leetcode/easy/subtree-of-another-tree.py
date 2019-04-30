# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def is_equal(self, first_tree, second_tree):
        if first_tree is None and second_tree is None:
            return True

        if first_tree is None:
            return False

        if second_tree is None:
            return False

        if first_tree.val != second_tree.val:
            return False

        return self.is_equal(first_tree.left, second_tree.left) and self.is_equal(first_tree.right, second_tree.right)

    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if s is None and t is None:
            return True

        if s is None:
            return False

        if s.val == t.val:
            result = self.is_equal(t, s)
            if result:
                return result

        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)
