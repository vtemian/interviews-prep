class Node:
    def __init__(self, val: str, key: str, left: 'Node' = None, right: 'Node' = None):
        self.val = val
        self.key = key
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        return self.val


class LRU:
    def __init__(self, size: int):
        self.store = {}

        self.current_size = 0
        self.max_size = size

        self.head = self.tail = None

    def add(self, key: str, val: str):
        if self.current_size == self.max_size:
            # we're full so we need to delete last node
            old_key = self.tail.key

            self.tail = self.tail.left
            self.tail.right = None

            del self.store[old_key]

            self.current_size -= 1

        # add it to the head
        node = Node(val, key)
        node.right = self.head

        if self.head:
            self.head.left = node

        self.head = node
        if not self.tail:
            self.tail = self.head

        self.store[key] = node
        self.current_size += 1

    def get(self, key: str) -> str:
        if key not in self.store:
            return ""

        node = self.store[key]
        if node == self.tail:
            self.tail = node.left

        if node.left:
            node.left.right = node.right

        if node.right:
            node.right.left = node.left

        node.right = self.head
        node.left = None
        self.head = node

        return node.val


lru = LRU(3)

lru.add("1", "1")
lru.add("2", "2")
lru.add("3", "3")
lru.add("4", "4")

assert lru.get("1") == "", lru.get("1")
assert lru.get("2") == "2"

lru.add("1", "1")

assert lru.get("1") == "1"
assert lru.get("3") == ""
