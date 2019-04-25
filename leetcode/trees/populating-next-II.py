"""
# Definition for a Node.
class Node:
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution:
    def connect(self, root: 'Node') -> 'Node':

        def dfs(node, next):
            if not node:
                return

            node.next = next

            while next:
                if next.left or next.right:
                    break

                next = next.next

            next_next = None
            if next:
                if next.left:
                    next_next = next.left
                else:
                    next_next = next.right

            if node.right:
                dfs(node.right, next_next)
                dfs(node.left, node.right)
            else:
                dfs(node.left, next_next)

        dfs(root, None)
        return root
