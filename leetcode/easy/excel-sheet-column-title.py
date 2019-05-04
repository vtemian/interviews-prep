import string


class Solution:
    def convertToTitle(self, n: int) -> str:
        store = {
            index + 1: letter
            for index, letter in enumerate(string.ascii_uppercase)
        }

        result = []

        while n > 26:
            to_append = n % 26
            result.append(store[n % 26] if n % 26 else store[26])
            n = n // 26
            if to_append == 0:
                n -= 1

        result.append(store[n % 26] if n % 26 else store[26])
        return ''.join(result[::-1])
