# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if not inorder or not postorder:
            return None

        root = TreeNode(postorder.pop())
        in_ord_idx = inorder.index(root.val)

        root.right = self.buildTree(inorder[in_ord_idx + 1:], postorder)
        root.left = self.buildTree(inorder[:in_ord_idx], postorder)

        return root
