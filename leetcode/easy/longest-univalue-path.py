# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        result = 0

        def dfs(node):
            if not node:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)

            l_result = r_result = 0

            if node.left and node.left.val == node.val:
                l_result = left + 1

            if node.right and node.right.val == node.val:
                r_result = right + 1

            nonlocal result
            result = max(result, r_result + l_result)

            return max(r_result, l_result)

        dfs(root)

        return result
