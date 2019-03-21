"""
7 -> 1 -> 6 == 617
5 -> 9 -> 2 == 295
------------------
2 -> 1 -> 9 == 912
"""

from node import Node


def compute_sum(first: Node, second: Node) -> Node:
    carry = 0
    head = current = first

    while first and second:
        result = first.val + second.val + carry

        first.val = result % 10
        carry = result // 10

        current = first
        first = first.next
        second = second.next

    while first:
        result = first.val + carry

        first.val = result % 10
        carry = result // 10

        current = first
        first = first.next

    while second:
        result = second.val + carry

        second.val = result % 10
        carry = result // 10

        current.next = second
        current = current.next

        second = second.next

    if carry:
        current.next = Node(carry)

    return head


for use_case, expected_result in [
        (([7, 1, 6], [5, 9, 2]), [2, 1, 9]),
        (([7, 1], [5, 9, 2]), [2, 1, 3]),
        (([9, 9, 9], [1]), [0, 0, 0, 1]),
        (([9], [1]), [0, 1])
]:

    first, second = use_case
    result = compute_sum(Node.build(first), Node.build(second))

    expected_result = Node.build(expected_result)

    assert result == expected_result, \
           "{} != {}".format(result, expected_result)
