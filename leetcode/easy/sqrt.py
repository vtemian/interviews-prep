class Solution:
    def mySqrt(self, x: int) -> int:
        if not x:
            return 0

        start = 1
        end = x

        while start <= end:
            avg = (start + end) // 2
            root = avg ** 2

            if (avg + 1) ** 2 > x and root <= x:
                return avg

            if root > x:
                end = avg - 1
            else:
                start = avg + 1

        return start
