from typing import List


class Node:
    def __init__(self, val: int, next: 'Node' = None):
        self.val = val
        self.next = next

    @staticmethod
    def build(vals: List[int]) -> 'Node':
        if not vals:
            return None

        head = current_node = Node(vals[0])

        for val in vals[1:]:
            current_node.next = Node(val)
            current_node = current_node.next

        return head

    def __repr__(self) -> str:
        """ 1->2->3 ... """

        store = {}
        result = str(self.val)

        head = self.next

        while head and id(head) not in store:
            result += '->{}'.format(head.val)

            store[id(head)] = head

            head = head.next

        return result

    def __eq__(self, other: 'Node') -> bool:
        current = self

        while current and other:
            if current.val != other.val:
                return False

            current = current.next
            other = other.next

        if current or other:
            return False

        return True
