# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """

        if not p and not q:
            return True

        if not p:
            return False

        if not q:
            return False

        if not q.val == p.val:
            return False

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
