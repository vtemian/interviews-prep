class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        current = 0
        result = -1

        for num in nums:
            if num:
                current += 1
            else:
                result = max(result, current)
                current = 0

        return max(result, current)
