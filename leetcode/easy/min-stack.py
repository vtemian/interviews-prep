class MinStack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """

        if not self.stack:
            self.stack.append((x, x))
        else:
            self.stack.append((x, min(x, self.getMin())))

    def pop(self):
        """
        :rtype: None
        """

        if not self.stack:
            return None
        return self.stack.pop()[0]

    def top(self):
        """
        :rtype: int
        """

        if not self.stack:
            return None

        return self.stack[-1][0]

    def getMin(self):
        """
        :rtype: int
        """

        if not self.stack:
            return None

        return self.stack[-1][1]
