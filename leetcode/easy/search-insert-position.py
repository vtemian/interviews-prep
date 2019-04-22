class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if not nums:
            return 0

        start = 0
        end = len(nums) - 1

        while start <= end:
            avg = (start + end) // 2

            if nums[avg] == target:
                return avg

            if nums[avg] > target:
                end = avg - 1
            else:
                start = avg + 1

        return start
