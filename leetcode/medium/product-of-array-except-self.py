class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #  1   2   6   24
        # 24  24  12    4

        result = [0] * len(nums)
        result[0] = 1

        idx = 1
        while idx < len(nums):
            result[idx] = result[idx - 1] * nums[idx - 1]
            idx += 1

        idx = len(nums) - 1
        R = 1
        while idx >= 0:
            result[idx] *= R
            R *= nums[idx]
            idx -= 1

        return result
