"""

1 -> 2 -> 3 -> 4 -> 5 -> 6
          |              |
          + ------------ +

return node 3

"""

from node import Node


def detect_loop(head: Node) -> Node:
    slow = fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if id(slow) == id(fast):
            break

    if fast is None or fast.next is None:
        return None

    slow = head
    while id(slow) != id(fast):
        slow = slow.next
        fast = fast.next

    return fast


for use_case in [
        ([1, 2, 3, 4, 5, 6], 2),
        ([1, 2, 3, 4, 5, 6], None)
]:

    nodes, loop_index = use_case
    loopy_list = Node.build(nodes)

    expected_result = None

    if loop_index is not None:
        count = 0
        head = loopy_list
        last = loopy_list

        while count < loop_index:
            count += 1
            head = head.next
            last = last.next

        while last.next:
            last = last.next

        last.next = head
        expected_result = head

    result = detect_loop(loopy_list)

    assert id(result) == id(expected_result), \
           "{} != {}".format(id(result), id(expected_result))
