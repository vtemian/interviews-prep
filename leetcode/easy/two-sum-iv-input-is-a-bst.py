# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        def dfs(node, nodes):
            if not node:
                return False

            c = k - node.val
            if c in nodes:
                return True

            nodes.add(node.val)

            return dfs(node.left, nodes) or dfs(node.right, nodes)

        if not root:
            return False

        return dfs(root, set())
