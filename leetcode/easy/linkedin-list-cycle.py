# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        if head is None:
            return False

        slow = fast = head

        while fast.next:
            if fast == slow:
                return True

            fast = fast.next
            if not fast.next:
                return False

            fast = fast.next
            slow = slow.next

        return False
