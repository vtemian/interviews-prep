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


def has_cycle(head: Node) -> bool:
    slow = head
    fast = head

    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next

        if slow != fast:
            continue

        cycle = 1
        fast = fast.next

        while slow != fast:
            fast = fast.next
            cycle += 1

        to_cycle = head

        while cycle:
            cycle -= 1
            to_cycle = to_cycle.next

        start = head

        while start != to_cycle:
            to_cycle = to_cycle.next
            start = start.next

        return start
    return None


n3 = Node(3)
n3.next = Node(5, n3)
example = Node(1, Node(2, n3))

print(has_cycle(example).val)
