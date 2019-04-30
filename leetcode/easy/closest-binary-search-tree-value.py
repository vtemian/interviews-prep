# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        if root.left and target < root.val:
            result = self.closestValue(root.left, target)

            if abs(result - target) < abs(root.val - target):
                return result
            return root.val

        if root.right and target > root.val:
            result = self.closestValue(root.right, target)

            if abs(result - target) < abs(root.val - target):
                return result
            return root.val

        return root.val
