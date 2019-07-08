class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        first = 0
        second = 0

        while first <len(nums) and second < len(nums):
            while first < len(nums) and nums[first] != 0:
                first += 1

            second = first
            while second < len(nums) and nums[second] == 0:
                second += 1

            if first < len(nums) and second < len(nums):
                nums[first] = nums[second]
                nums[second] = 0
