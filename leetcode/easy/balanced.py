# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def balanced(node):
            if not node:
                return True, 0

            left = balanced(node.left)
            right = balanced(node.right)

            return left[0] and right[0] and abs(left[1] - right[1]) < 2, max(left[1], right[1]) + 1

        return balanced(root)[0]
