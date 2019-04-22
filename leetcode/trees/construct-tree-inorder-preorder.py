# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder or not inorder:
            return

        root = TreeNode(preorder[0])
        in_order_idx = inorder.index(root.val)

        in_order_left = inorder[:in_order_idx]
        in_order_right = inorder[in_order_idx + 1:]

        pre_order_left = preorder[1:1 + len(in_order_left)]
        pre_order_right = preorder[1 + len(in_order_left):]

        root.left = self.buildTree(pre_order_left, in_order_left)
        root.right = self.buildTree(pre_order_right, in_order_right)

        return root
