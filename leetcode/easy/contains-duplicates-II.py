class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        store = {}

        for idx, num in enumerate(nums):
            if num not in store:
                store[num] = [idx]
            else:
                for i in store[num]:
                    if abs(idx - i) <= k:

                        return True
                store[num].append(idx)

        return False
