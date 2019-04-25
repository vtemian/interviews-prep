# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """

        result = ''

        def dfs(node):
            nonlocal result

            if not node:
                result += '|' + ';'
                return

            result += str(node.val) + ';'

            dfs(node.left)
            dfs(node.right)

        dfs(root)

        return result

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """

        nodes = data.split(';')[:-1]

        def build(idx):
            if idx >= len(nodes):
                return (None, idx)

            if nodes[idx] == '|':
                return (None, idx)

            root = TreeNode(nodes[idx])
            root.left, idx = build(idx + 1)
            root.right, idx = build(idx + 1)

            return root, idx

        return build(0)[0]



# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
