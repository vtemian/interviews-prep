class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return bool(n and n & (n - 1) == 0)
