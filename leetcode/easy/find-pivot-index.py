class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left = sum(nums)
        right = 0

        idx = 0

        while idx < len(nums):
            if right == left - right - nums[idx]:
                return idx

            right += nums[idx]
            idx += 1

        return -1
