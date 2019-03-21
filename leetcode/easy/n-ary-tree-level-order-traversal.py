"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    def levelOrder(self, root: 'Node') -> 'List[List[int]]':
        levels = []

        def dfs(root, level):
            if not root:
                return

            if len(levels) <= level:
                levels.append([])

            levels[level].append(root.val)
            for kid in root.children:
                dfs(kid, level + 1)

        dfs(root, 0)
        return levels
