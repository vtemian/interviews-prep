"""
Implement an algorithm to find the kth to last element of a singly linked list.
"""

from node import Node


def find_kth_to_last(head: Node, kth: int) -> int:
    if not head:
        return -1

    if kth == -1:
        return head.val

    needle = -1

    def find(head: Node) -> int:
        nonlocal needle

        if not head:
            return 1

        result = find(head.next)
        if result == kth:
            needle = head.val

        return result + 1

    find(head)

    return needle

for use_case, expected_result in [
        (([1, 2, 3, 4, 5, 6], 2), 5),
]:

    nodes, kth = use_case
    head = Node.build(nodes)

    result = find_kth_to_last(head, kth)

    assert result == expected_result, \
           "{} != {}".format(result, expected_result)
