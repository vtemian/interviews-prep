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


def reverse(head: Node) -> Node:
    current = head
    initial = None

    while current:
        next = current.next
        current.next = initial
        initial = current
        current = next

    return initial or head


example = Node(1, Node(3, (Node(5))))
print(reverse(example))
