class Solution:
    def findNthDigit(self, n: int) -> int:
        n -= 1

        for digit in range(1, 11):
            first = 10 ** (digit - 1)

            if n < 9 * first * digit:
                return int(str(first + n / digit)[n % digit])

            n -= 9 * first * digit
