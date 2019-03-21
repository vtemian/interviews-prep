"""
Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window.

Example:

MovingAverage m = new MovingAverage(3);
m.next(1) = 1
m.next(10) = (1 + 10) / 2
m.next(3) = (1 + 10 + 3) / 3
m.next(5) = (10 + 3 + 5) / 3
"""


class MovingAverage:

    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """

        self.queue = []
        self.max_size = size

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """

        if len(self.queue) >= self.max_size:
            self.queue.pop(0)

        self.queue.append(val)
        return sum(self.queue) / float(len(self.queue))



# Your MovingAverage object will be instantiated and called as such:
obj = MovingAverage(3)
for val in [1, 10, 3, 5]:
    print(obj.next(val))
