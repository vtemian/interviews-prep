class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        cost = [0] * 3

        for house in costs:
            cost = [house[i] + min(cost[:i] + cost[i + 1:]) for i in range(3)]

        return min(cost)
