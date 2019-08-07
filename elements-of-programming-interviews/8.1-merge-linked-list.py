class Node:
    def __init__(self, val: int, next: 'Node' = None):
        self.val = val
        self.next = next

    def __str__(self):
        result = str(self.val)

        if self.next:
            return result + '->' + str(self.next)

        return result

    def __repr__(self):
        return str(self)


def merge(first_list: Node, second_list: Node) -> Node:
    if not first_list or not second_list:
        return first_list or second_list

    # TODO: treat for special case
    head = current = Node(-1)

    while first_list and second_list:
        if first_list.val > second_list.val:
            current.next = second_list
            second_list = second_list.next
        else:
            current.next = first_list
            first_list = first_list.next

        current = current.next

    while first_list:
        current.next = first_list
        first_list = first_list.next
        current = current.next

    while second_list:
        current.next = second_list
        second_list = second_list.next
        current = current.next

    return head.next


first = Node(1, Node(3, (Node(5))))
second = Node(2, Node(4, Node(6)))

print(first)
print(second)
print(merge(first, second))
