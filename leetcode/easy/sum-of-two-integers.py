class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        MAX = 0x7fffffffffffffffffffffffffffffff # 128-bit
        mask = 0xffffffffffffffffffffffffffffffff

        result = 0

        while b:
            a, b = (a ^ b) & mask, ((a & b) << 1) & mask

        return a if a <= MAX else ~(a ^ mask)
