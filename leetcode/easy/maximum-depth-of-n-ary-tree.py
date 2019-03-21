"""
Given a n-ary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

For example, given a 3-ary tree:

We should return its max depth, which is 3.


Note:

The depth of the tree is at most 1000.
The total number of nodes is at most 5000.
"""


"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root, depth=0):
        """
        :type root: Node
        :rtype: int
        """

        if not root:
            return depth

        return max([
            self.maxDepth(kid, depth + 1)
            for kid in root.children
        ] + [depth + 1])
