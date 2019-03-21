"""
Check if a linked list is a palindrom
1 -> 2 -> 3 -> 3 -> 2 -> 1 == True
"""

from node import Node


def is_palindrom(head: Node) -> Node:
    first = head
    result = False

    def find(node: Node):
        nonlocal first
        nonlocal result

        if not node.next:
            return node

        last = find(node.next)
        if not last:
            return None

        if (first.next == last and first.val == last.val) or first == last:
            result = True
            return None

        result = last.val == first.val
        first = first.next

        if not result:
            result = result
            return None

        return node

    find(head)

    return result


for use_case, expected_result in [
        ([1, 2, 3, 3, 2, 1], True),
        ([1, 2, 3, 2, 1], True),
        ([1, 2, 3, 4, 2, 1], False),
]:

    result = is_palindrom(Node.build(use_case))

    assert result == expected_result, \
           "{} != {}".format(result, expected_result)
