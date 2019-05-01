class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        idx = 0

        while idx < len(bits) - 1:
            idx += bits[idx] + 1

        return idx == len(bits) - 1
