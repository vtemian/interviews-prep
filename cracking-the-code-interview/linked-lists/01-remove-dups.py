"""
Write code to remove duplicates from a unsorted linked list.

FOLLOW UP
How you would you solve this problem if a temporary buffer is not allowed.
"""

from node import Node


def remove_dup_with_buffer(head: Node) -> Node:
    if not head:
        return None

    node_store = {
        head.val: True
    }

    current_node = head

    while current_node and current_node.next:
        if current_node.next.val in node_store:
            # delete the node
            current_node.next = current_node.next.next
        else:
            current_node = current_node.next

        if current_node:
            node_store[current_node.val] = True

    return head


def remove_dup_without_buffer(head: Node) -> Node:
    """
        1 2 3 1 1 2 2 1
        ^
          ^ ^ ^ ^ ^ ^ ^
          2 3     2 2
    """

    if not head:
        return None

    current_node = head

    while current_node and current_node.next:
        next_node = current_node

        while next_node and next_node.next:
            if next_node.next.val == current_node.val:
                next_node.next = next_node.next.next
            else:
                next_node = next_node.next

        current_node = current_node.next

    return head

for use_case, expected_result in [
        ([], []),
        ([1, 2], [1, 2]),
        ([1, 2, 2, 1, 2], [1, 2]),
        ([1, 1, 2, 2], [1, 2]),
        ([1, 1, 1, 1, 1, 2], [1, 2]),
        ([1, 2, 3, 3, 3, 1, 1], [1, 2, 3]),
]:

    use_case = Node.build(use_case)
    expected_result = Node.build(expected_result)

    #result = remove_dup_with_buffer(use_case)
    result = remove_dup_without_buffer(use_case)

    assert result == expected_result, \
           "{} != {}".format(result, expected_result)
