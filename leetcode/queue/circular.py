class MyCircularQueue:

    def __init__(self, k: 'int'):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        """

        self.queue = []
        self.max_size = k
        self.start = 0
        self.end = -1

    def enQueue(self, value: 'int') -> 'bool':
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        """

        next_position = (self.end + 1) % self.max_size
        if len(self.queue) > next_position and self.queue[next_position] is not None:
            return False

        if len(self.queue) < self.max_size:
            self.queue.append(value)
        elif self.queue[next_position] == None:
            self.queue[next_position] = value
        else:
            return False

        self.end = (self.end + 1) % self.max_size
        return True

    def deQueue(self) -> 'bool':
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        """

        if not self.queue:
            return False

        self.queue[self.start] = None
        self.start = (self.start + 1) % self.max_size

        return True

    def Front(self) -> 'int':
        """
        Get the front item from the queue.
        """
        if not self.queue:
            return -1
        return self.queue[self.start]

    def Rear(self) -> 'int':
        """
        Get the last item from the queue.
        """
        if not self.queue:
            return -1
        return self.queue[self.end]

    def isEmpty(self) -> 'bool':
        """
        Checks whether the circular queue is empty or not.
        """
        return self.queue == []

    def isFull(self) -> 'bool':
        """
        Checks whether the circular queue is full or not.
        """
        return len(self.queue) == self.max_size


# Your MyCircularQueue object will be instantiated and called as such:
queue = MyCircularQueue(3)
print(queue.enQueue(1))
print(queue.enQueue(2))
print(queue.enQueue(3))
print(queue.enQueue(4))

print(queue.Rear())
print(queue.isFull())

print(queue.deQueue())
print(queue.enQueue(4))

print(queue.Rear())
