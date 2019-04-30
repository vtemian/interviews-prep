class Node:
    def __init__(self, val, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

    def __repr__(self):
        return str(self.val)


class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """

        self.store = []


    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """

        if len(self.store) <= abs(index):
            return -1

        return self.store[index].val


    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """

        node = Node(val)

        if not self.store:
            self.store.append(node)
        else:
            self.store[0].prev = node
            node.next = self.store[0]
            self.store.insert(0, node)

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """

        node = Node(val)

        if not self.store:
            self.store.append(node)
        else:
            self.store[-1].next = node
            node.prev = self.store[-1]
            self.store.append(node)


    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """

        if len(self.store) < abs(index) and not (len(self.store) == 0 and index == -1):
            return

        if len(self.store) == abs(index) or (len(self.store) == 0 and index == -1):
            return self.addAtTail(val)

        node = Node(val)
        start = index

        while start < len(self.store):
            self.store[start - 1].next = node
            node.prev = self.store[start - 1]
            node.next = self.store[start]

            node, self.store[start] = self.store[start], node
            start += 1

        self.store[-1].next = node
        node.prev = self.store[-1]
        self.store.append(node)

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """

        if abs(index) >= len(self.store):
            return

        if index == 0:
            if len(self.store) > 1:
                self.store[-1].prev = None
            self.store.pop(0)
        elif index + 1 == len(self.store):
            self.store[-2].next = None
            self.store.pop()
        else:
            self.store[index - 1].next = self.store[index + 1]
            self.store[index + 1].prev = self.store[index - 1]
            self.store.pop(index)

        print(self.store)


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
