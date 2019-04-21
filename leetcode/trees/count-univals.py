# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def countUnivalSubtrees(self, root: TreeNode) -> int:
        if not root:
            return 0

        result = 0

        def unival(node, equals=None):
            nonlocal result

            if not equals:
                equals = node.val

            if not node.left and not node.right:
                result += 1
                return node.val == equals

            left = unival(node.left, node.val) if node.left else True
            right = unival(node.right, node.val) if node.right else True
            current = left and right

            if node.left:
                current = current and node.left.val == node.val

            if node.right:
                current = current and node.right.val == node.val

            result += int(current)

            return current

        unival(root)

        return result

