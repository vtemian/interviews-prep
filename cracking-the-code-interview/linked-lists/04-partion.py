"""
3 -> 5 -> 8 -> 5 -> 10 -> 2 -> 1 [partion=5]
3 -> 1 -> 2 -> 10 -> 5 -> 5 -> 8
"""

from node import Node


def solve(head: Node, partion: int) -> Node:
    if not head:
        return

    before = Node(None)
    after = Node(None)
    start_before = before
    start_after = after

    while head:
        if head.val < partion:
            # put it in before
            if before.val is None:
                before.val = head.val
            else:
                before.next = Node(head.val)
                before = before.next
        else:
            # put it in after
            if after.val is None:
                after.val = head.val
            else:
                after.next = Node(head.val)
                after = after.next

        head = head.next

    before.next = start_after

    return start_before


for use_case, expected_result in [
        (([3, 5, 8, 5, 10, 2, 1], 5), [3, 2, 1, 5, 8, 5, 10]),
]:

    nodes, partion = use_case
    result = solve(Node.build(nodes), partion)
    expected_result = Node.build(expected_result)

    assert result == expected_result, \
           "{} != {}".format(result, expected_result)
