# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        result = 0

        def dfs(node, is_left=False):
            if not node:
                return

            if not node.left and not node.right and is_left:
                nonlocal result
                result += node.val
                return
            else:
                dfs(node.left, True)
                dfs(node.right)

        dfs(root)

        return result
