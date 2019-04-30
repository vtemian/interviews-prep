class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        result = None
        idx = 0

        while idx < len(nums) - 1:
            if nums[idx] > nums[idx + 1]:
                if result is not None:
                    return False

                result = idx
            idx += 1

        return result is None or result == 0 or result == len(nums) - 2 or nums[result] <= nums[result + 2] or nums[result - 1] <= nums[result + 1]
