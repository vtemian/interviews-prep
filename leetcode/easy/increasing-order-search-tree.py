"""
Given a tree, rearrange the tree in in-order so that the leftmost node in the tree is now the root of the tree,
and every node has no left child and only 1 right child.

Example 1:
Input: [5,3,6,2,4,null,8,1,null,null,null,7,9]

       5
      / \
    3    6
   / \    \
  2   4    8
 /        / \
1        7   9

Output: [1,null,2,null,3,null,4,null,5,null,6,null,7,null,8,null,9]

 1
  \
   2
    \
     3
      \
       4
        \
         5
          \
           6
            \
             7
              \
               8
                \
                 9
 """


# Definition for a binary tree node.
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None


class Solution:
    def increasingBST(self, root):
        prev = None

        def play(root):
            if not root:
                return root

            play(root.right)

            root.right = prev
            prev = root

            play(root.left)

            root.left = None

        play(root)

        return prev



raw_tree = iter([5, 3, 6, 2, 4, None, 8, 1, None, None, None, 7, 9])


def construct():
    try:
        val = next(raw_tree)
    except Exception as e:
        return

    if not val:
        return None

    root = TreeNode(val)

    root.left = construct()
    root.right = construct()

    return root


tree = construct()


def depth(root):
    if not root:
        print('None')
        return

    print(root.val)

    depth(root.left)
    depth(root.right)


result = Solution().increasingBST(tree)
depth(result)
