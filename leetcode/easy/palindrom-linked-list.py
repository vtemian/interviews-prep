# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head:
            return True

        start = head

        def deep(node):
            nonlocal start

            if not node:
                return None

            if deep(node.next) is False:
                return False

            if node.val != start.val:
                return False

            start = start.next
            return True

        return deep(head)
