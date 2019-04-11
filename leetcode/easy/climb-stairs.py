class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0:
            return 0

        if n == 1:
            return 1

        if n == 2:
            return 2

        prev = 2
        current = 3

        idx = 3
        while idx < n:
            tmp = current
            current += prev
            prev = tmp
            idx += 1

        return current
