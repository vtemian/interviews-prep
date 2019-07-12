class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        return n > 0 and 3 ** 20 % n == 0
