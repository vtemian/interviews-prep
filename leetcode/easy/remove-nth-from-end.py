# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if n == 0:
            return head

        fast = slow = head

        to_go = 0

        while to_go < n:
            fast = fast.next
            to_go += 1

        if not fast:
            return slow.next

        while fast.next:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next

        return head
