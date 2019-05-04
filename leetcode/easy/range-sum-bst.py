# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        result = 0

        def dfs(node):
            nonlocal L, R, result

            if not node:
                return False

            if L <= node.val <= R:
                result += node.val

            if L < node.val:
                dfs(node.left)

            if node.val < R:
                dfs(node.right)

        dfs(root)

        return result
