class Solution:
    def addDigits(self, n: int) -> int:
        if not n:
            return 0
        return n - 9 * ((n - 1) // 9)
