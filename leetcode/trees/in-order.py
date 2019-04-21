# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        stack = [root]
        result = []

        while stack:
            node = stack.pop()

            if not (node.left or node.right):
                result.append(node.val)
            else:
                if node.right:
                    stack.append(node.right)

                stack.append(node)

                if node.left:
                    stack.append(node.left)

                node.left = None
                node.right = None

        return result
