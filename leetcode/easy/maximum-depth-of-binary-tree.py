class Solution:
    def maxDepth(self, root: 'TreeNode', current_level = 1) -> 'int':
        if root is None:
            return current_level - 1

        return max(current_level, self.maxDepth(root.left, current_level + 1),
                   self.maxDepth(root.right, current_level + 1))
