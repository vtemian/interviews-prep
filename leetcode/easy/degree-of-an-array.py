class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        left, right, store = {}, {}, {}

        for idx, num in enumerate(nums):
            if num not in left:
                left[num] = idx

            right[num] = idx

            if num not in store:
                store[num] = 0

            store[num] += 1

        result = len(nums)
        max_occ = max(store.values())
        for num, occ in store.items():
            if occ != max_occ:
                continue

            result = min(result, right[num] - left[num] + 1)

        return result
