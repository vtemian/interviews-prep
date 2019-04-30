class Solution:
    def minMoves(self, nums: List[int]) -> int:
        if not nums:
            return 0

        return sum(nums) - min(nums) * len(nums)
