import itertools


class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        result = 0

        for key, group in itertools.groupby(seats):
            if key:
                continue

            result = max((len(list(group)) + 1) // 2, result)

        return max(result, seats.index(1), seats[::-1].index(1))
