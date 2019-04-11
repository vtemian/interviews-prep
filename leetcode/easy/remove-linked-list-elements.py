# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if not head:
            return None

        while head.val == val:
            head = head.next
            if not head:
                return

        node = head

        while node.next:
            while node.next and node.next.val == val:
                node.next = node.next.next

            if node.next:
                node = node.next

        return head
