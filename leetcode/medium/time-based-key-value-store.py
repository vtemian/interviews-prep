from collections import defaultdict


class TimeMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """

        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ''

        start = 0
        end = len(self.store[key]) - 1

        while start <= end:
            mid = (start + end) // 2
            if self.store[key][mid][0] <= timestamp:
                if self.store[key][mid][0] == timestamp:
                    return self.store[key][mid][1]

                if mid + 1 >= len(self.store[key]):
                    return self.store[key][mid][1]

                if self.store[key][mid + 1][0] > timestamp:
                    return self.store[key][mid][1]

                start = mid + 1
            else:
                end = mid - 1

        return ""


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
