class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return len(nums)

        start = 0
        moving = 1

        while moving < len(nums):
            while moving < len(nums) and nums[start] == nums[moving]:
                moving += 1

            if moving == len(nums):
                break

            nums[start + 1] = nums[moving]
            start += 1
            moving += 1

        return start + 1
