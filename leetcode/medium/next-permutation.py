class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # 1, 3, 2 => 3 1 2

        idx = len(nums) - 2
        while idx >= 0 and nums[idx] >= nums[idx + 1]:
            idx -= 1

        def reverse(start):
            end = len(nums) - 1

            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1

        found = idx

        if idx >= 0:
            idx = len(nums) - 1
            while idx >= 0 and nums[idx] <= nums[found]:
                idx -= 1

            nums[idx], nums[found] = nums[found], nums[idx]

        reverse(found + 1)
