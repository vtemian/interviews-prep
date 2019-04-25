from collections import deque


class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """

        self.queue_a = deque()
        self.queue_b = deque()

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """

        self.queue_b.append(x)

        while self.queue_a:
            self.queue_b.append(self.queue_a.popleft())

        self.queue_a, self.queue_b = self.queue_b, self.queue_a

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """

        if not self.queue_a:
            return None

        return self.queue_a.popleft()

    def top(self) -> int:
        """
        Get the top element.
        """

        if not self.queue_a:
            return None

        return self.queue_a[0]

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """

        return len(self.queue_a) == 0

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
