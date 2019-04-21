# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False

        def has_path(node, sum):
            if not node.left and not node.right:
                return node.val == sum

            left = right = None

            if node.left:
                left = has_path(node.left, sum - node.val)
                if left:
                    return left

            if node.right:
                right = has_path(node.right, sum - node.val)
                if right:
                    return right

            return False

        return has_path(root, sum)
