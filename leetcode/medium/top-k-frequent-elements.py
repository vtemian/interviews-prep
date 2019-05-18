import heapq
from collections import Counter


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums = Counter(nums)
        return [
            x[0]
            for x in heapq.nlargest(k, [(nr, value) for nr, value in nums.items()], key=lambda nr: nr[1])
        ]
