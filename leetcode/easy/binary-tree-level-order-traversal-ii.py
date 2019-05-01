# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        levels = []
        queue = [root]

        while queue:
            next_queue = []
            level = []

            while queue:
                node = queue.pop(0)
                level.append(node.val)

                if node.left:
                    next_queue.append(node.left)
                if node.right:
                    next_queue.append(node.right)

            if level:
                levels.append(level)

            queue = next_queue

        return levels[::-1]
