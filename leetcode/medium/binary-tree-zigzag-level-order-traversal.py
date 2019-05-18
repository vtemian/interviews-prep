# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        result = []
        queue = [root]
        l = True


        while queue:
            new_queue = []
            lvl = []

            while queue:
                node = queue.pop()

                lvl.append(node.val)

                left, right = node.left, node.right
                if not l:
                    left, right = right, left

                if left:
                    new_queue.append(left)

                if right:
                    new_queue.append(right)

            l ^= True

            queue = new_queue
            result.append(lvl)
        return result
