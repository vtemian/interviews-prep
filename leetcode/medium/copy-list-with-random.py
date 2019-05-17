"""
# Definition for a Node.
class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None

        nodes = {}

        current_old = head
        new_head = current_new = Node(head.val, None, None)
        if head.random == head:
            new_head.random = head

        nodes[id(current_old)] = current_new
        current_old = head.next

        while current_old:
            node = Node(current_old.val, None, None)
            if current_old.random == current_old:
                node.random = node

            current_new.next = node
            current_new = node

            nodes[id(current_old)] = current_new
            current_old = current_old.next

        current_old = head
        current_new = new_head

        while current_old:
            current_new.random = nodes[id(current_old.random)] if current_old.random else None

            current_new = current_new.next
            current_old = current_old.next

        return new_head
