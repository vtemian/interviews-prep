import heapq


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.store = nums
        self.k = k

        heapq.heapify(self.store)

        while len(self.store) > self.k:
            heapq.heappop(self.store)

    def add(self, val: int) -> int:
        if len(self.store) < self.k:
            heapq.heappush(self.store, val)
        elif val > self.store[0]:
            heapq.heapreplace(self.store, val)

        return self.store[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
