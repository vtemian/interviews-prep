# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0

        result = float('inf')

        def dfs(node, depth):
            nonlocal result

            if not node.left and not node.right:
                result = min(result, depth)
                return

            if depth > result:
                return

            if node.left:
                dfs(node.left, depth + 1)

            if node.right:
                dfs(node.right, depth + 1)

        dfs(root, 1)

        return result

