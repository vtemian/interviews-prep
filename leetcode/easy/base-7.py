class Solution:
    def convertToBase7(self, num: int) -> str:
        if not num:
            return '0'

        reverse = False
        if num < 0:
            reverse = True
            num *= -1

        result = []

        while num:
            result.append(str(num % 7))
            num //= 7

        if reverse:
            result.append('-')

        return ''.join(result[::-1])
