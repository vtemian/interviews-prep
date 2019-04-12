class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0

        idx = 0

        while idx < len(prices):
            while idx + 1 < len(prices) and prices[idx] > prices[idx + 1]:
                idx += 1

            valley = prices[idx]

            while idx + 1 < len(prices) and prices[idx] < prices[idx + 1]:
                idx += 1

            peak = prices[idx]

            result += peak - valley
            idx += 1

        return result
