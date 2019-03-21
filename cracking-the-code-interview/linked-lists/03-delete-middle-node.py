"""
Implement an algorigthm to delete a node in the middle of singly linked list,
given only access to that node.
"""

from node import Node


def delete_middle_node(middle: Node):
    if not middle or not middle.next:
        return

    middle.val = middle.next.val
    middle.next = middle.next.next


head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)

expected = Node(1)
expected.next = Node(3)
expected.next.next = Node(4)

delete_middle_node(head.next)

assert head == expected, \
       "{} != {}".format(head, expected)
