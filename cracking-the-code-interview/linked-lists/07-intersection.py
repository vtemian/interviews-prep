"""
     1 -> \
           2 -> 3 -> 4
9 -> 8 -> /

return node 2
"""

from node import Node


def get_intersection(first: Node, second: Node) -> Node:
    store = {}  # Map[int, Node]

    while first:
        store[id(first)] = first
        first = first.next

    while second:
        if id(second) in store:
            return second

        store[id(second)] = second
        second = second.next

    return None


for use_case in [
        ([2, 3, 4], [1], [9, 8]),
        ([], [1, 2, 3], [1, 2, 3]),
]:

    common, first, second = use_case

    common = Node.build(common)

    first = Node.build(first)
    first.next = common

    second = Node.build(second)
    second.next = common

    result = get_intersection(first, second)

    assert result == common, \
           "{} != {}".format(result, common)
