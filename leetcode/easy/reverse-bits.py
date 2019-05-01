class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        result = 0
        bit = 0

        while bit < 32:
            result |= (n & 1)
            n = n >> 1
            if bit < 31:
                result <<= 1
            bit += 1

        return result
