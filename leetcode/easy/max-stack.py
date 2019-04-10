class MaxStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """

        self.stack = []
        self.max_stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """

        self.stack.append(x)

        peek_max = self.peekMax()

        self.max_stack.append(max(peek_max, x)
                              if peek_max is not None else x)

    def pop(self):
        """
        :rtype: int
        """

        if not self.stack:
            return None

        self.max_stack.pop()
        return self.stack.pop()

    def top(self):
        """
        :rtype: int
        """

        if not self.stack:
            return None

        return self.stack[-1]

    def peekMax(self):
        """
        :rtype: int
        """

        if not self.max_stack:
            return None

        return self.max_stack[-1]

    def popMax(self):
        """
        :rtype: int
        """

        current_max = self.peekMax()
        if current_max is None:
            return None

        buff = []

        while current_max != self.top():
            buff.append(self.pop())

        self.pop()

        while buff:
            self.push(buff.pop())

        return current_max

# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()
