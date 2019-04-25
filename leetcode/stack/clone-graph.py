"""
# Definition for a Node.
class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors
"""
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        visited = {}
        def dfs(root):
            nonlocal visited

            if root.val in visited:
                return visited[root.val]

            if not root:
                return None

            node = Node(root.val, [])
            visited[node.val] = node

            for neighbor in root.neighbors:
                result = dfs(neighbor)
                if result:
                    node.neighbors.append(result)

            return node

        return dfs(node)
