class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)

        if n < 2:
            return n

        idx = 1
        result = 1
        current = 1

        while idx < n:
            if nums[idx] > nums[idx - 1]:
                current += 1
            else:
                result = max(current, result)
                current = 1

            idx += 1

        return max(current, result)
