class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        if not nums:
            return 0
        length = len(nums)
        result = [0]

        def dfs(nums, current, idx, sign, res, length):

            if sign == '+':
                current += nums[idx]
            elif sign == '-':
                current -= nums[idx]

            if idx == length - 1:
                if current == S:
                    res[0] += 1
            else:
                dfs(nums, current, idx + 1, '-', res, length)
                dfs(nums, current, idx + 1, '+', res, length)

        dfs(nums, 0, 0, '-', result, length)
        dfs(nums, 0, 0, '+', result, length)

        return result[0]
