# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        result = []

        def paths(node, path=None):
            if not node:
                return

            if not path:
                path = str(node.val)
            else:
                path = '{}->{}'.format(path, str(node.val))

            if not node.left and not node.right:
                result.append(path)
            else:
                paths(node.left, path)
                paths(node.right, path)

        paths(root)

        return result
