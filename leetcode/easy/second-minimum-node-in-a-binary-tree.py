# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        answer = 999999999999999999
        min = root.val

        def dfs(node):
            nonlocal min, answer
            if not node:
                return

            if min < node.val < answer:
                answer = node.val
            elif node.val <= min:
                min = node.val

                dfs(node.left)
                dfs(node.right)
        dfs(root)
        return answer if answer < 999999999999999999 else -1
