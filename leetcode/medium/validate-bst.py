# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def valid(node, lower=float('-inf'), upper=float('inf')):
            if not node:
                return True

            if node.val >= upper or node.val <= lower:
                return False

            if not valid(node.left, lower, node.val):
                return False

            if not valid(node.right, node.val, upper):
                return False

            return True

        return valid(root)
