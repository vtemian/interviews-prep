# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return

        node = head

        while node.next:
            current_val = node.val

            while node.next and node.next.val == current_val:
                node.next = node.next.next

            node = node.next
            if not node:
                break

        return head
