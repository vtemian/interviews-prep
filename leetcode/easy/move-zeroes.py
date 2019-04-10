class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        count = 0

        for n in nums:
            if n == 0:
                count += 1

        start = end = 0

        while end < len(nums):
            while start < len(nums) and nums[start] != 0:
                start += 1
                end += 1

            while end < len(nums) and nums[end] == 0:
                end += 1

            if end < len(nums) and start < len(nums):
                nums[start] = nums[end]
                nums[end] = 0

                end += 1
                start += 1

        while start < len(nums):
            nums[start] = 0
            start += 1

        return nums


result = Solution().moveZeroes([1, 0, 2, 0, 3, 4, 0])
print(result)
