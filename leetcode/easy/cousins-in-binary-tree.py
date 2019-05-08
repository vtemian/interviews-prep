# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        parents = {}

        def dfs(node, depth=0, parent=None):
            if not node:
                return

            if node.val == x:
                parents[x] = [depth, parent]

            if node.val == y:
                parents[y] = [depth, parent]

            dfs(node.left, depth + 1, node)
            dfs(node.right, depth + 1, node)

        dfs(root)

        if x not in parents and y not in parents:
            return False

        if x not in parents or y not in parents:
            return False

        return parents[x][0] == parents[y][0] and parents[x][1] != parents[y][1]
