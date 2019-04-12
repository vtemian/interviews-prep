# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def is_mirrored(node1, node2):
            if node1 is None and node2 is None:
                return True
            if node1 is None or node2 is None:
                return False

            return node1.val == node2.val and is_mirrored(node1.left, node2.right) and is_mirrored(node2.left, node1.right)

        #return is_mirrored(root, root)

        queue = [root, root]
        while queue:
            node1 = queue.pop(0)
            node2 = queue.pop(0)

            if node1 is None and node2 is None:
                continue

            if node1 is None or node2 is None:
                return False

            if node1.val != node2.val:
                return False

            queue.append(node1.left)
            queue.append(node2.right)

            queue.append(node1.right)
            queue.append(node2.left)

        return True
