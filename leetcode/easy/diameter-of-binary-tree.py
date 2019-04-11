# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root) -> int:
        max_diameter = 0

        def dfs(node):
            nonlocal max_diameter
            if not node:
                return 0

            if not node.left and not node.right:
                return 1

            left = dfs(node.left)
            right = dfs(node.right)

            max_diameter = max(max_diameter, left + right)

            return max(left, right) + 1

        dfs(root)

        return max_diameter
