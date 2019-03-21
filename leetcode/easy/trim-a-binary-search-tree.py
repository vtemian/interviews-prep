class Solution:
    def trimBST(self, root: 'TreeNode', L: 'int', R: 'int') -> 'TreeNode':
        if not root:
            return root

        left = self.trimBST(root.left, L, R)
        right = self.trimBST(root.right, L, R)

        if root.val < L or root.val > R:
            if left:
                return left

            return right

        root.left = left
        root.right = right

        return root
