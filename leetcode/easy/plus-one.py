class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        result = []

        for digit in digits[::-1]:
            digit += carry

            result.append(digit % 10)
            carry = digit // 10

        if carry:
            result.append(carry)

        return result[::-1]
