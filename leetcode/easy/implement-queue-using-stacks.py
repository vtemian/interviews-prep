class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.first = []
        self.second = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """

        self.first.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """

        if not self.second:
            while self.first:
                self.second.append(self.first.pop())

        if self.second:
            return self.second.pop()

        return None

    def peek(self) -> int:
        """
        Get the front element.
        """

        if not self.second:
            while self.first:
                self.second.append(self.first.pop())

        if self.second:
            return self.second[-1]

        return None

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """

        return len(self.first) == len(self.second) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
