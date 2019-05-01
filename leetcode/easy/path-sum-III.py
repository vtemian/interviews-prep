# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        if not root:
            return 0

        result = 0
        stack = [(root, [0])]

        while stack:
            node, totals = stack.pop()

            new_totals = []
            for total in totals:
                if total + node.val == sum:
                    result += 1
                new_totals.append(total + node.val)

            new_totals.append(0)

            if node.left:
                stack.append((node.left, new_totals))
            if node.right:
                stack.append((node.right, new_totals))

        return result
