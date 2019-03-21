"""
Write a class RecentCounter to count recent requests.

It has only one method: ping(int t), where t represents some time in milliseconds.

Return the number of pings that have been made from 3000 milliseconds ago until now.

Any ping with time in [t - 3000, t] will count, including the current ping.

It is guaranteed that every call to ping uses a strictly larger value of t than before.



Example 1:

Input: inputs = ["RecentCounter","ping","ping","ping","ping"], inputs = [[],[1],[100],[3001],[3002]]
Output: [null,1,2,3,3]


Note:

Each test case will have at most 10000 calls to ping.
Each test case will call ping with strictly increasing values of t.
Each call to ping will have 1 <= t <= 10^9.
"""


class RecentCounter:

    def __init__(self):
        self.store = []
        self.current_position = 0

    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """

        self.store.append(t)
        while t - self.store[self.current_position] > 3000:
            self.current_position += 1

        return len(self.store) - self.current_position


# Your RecentCounter object will be instantiated and called as such:
obj = RecentCounter()
for t in [1, 100, 3001, 3002, 90000, 90011, 93011]:
    print(obj.ping(t))
