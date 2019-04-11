class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0

        if len(nums) < 3:
            return max(nums)

        best = [nums[0], max(nums[1], nums[0])]

        for idx, num in enumerate(nums[2:]):
            idx += 2
            best.append(max(num, best[idx - 1], best[idx - 2] + num))

        return best[-1]
