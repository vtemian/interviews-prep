import string


class Solution:
    def titleToNumber(self, s: str) -> int:
        store = {
            letter: index + 1
            for index, letter in enumerate(string.ascii_uppercase)
        }

        s = s[::-1]
        result = 0

        for index, letter in enumerate(s):
            power = 26 ** index if index else 1
            result += store[letter] * power

        return result
