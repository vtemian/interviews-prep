class Solution:
    def minCostClimbingStairs(self, costs: List[int]) -> int:
        current = prev = 0

        for cost in costs:
            current, prev = cost + min(current, prev), current

        return min(current, prev)
