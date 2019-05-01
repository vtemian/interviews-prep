from collections import Counter


class Solution:
    def longestPalindrome(self, s: str) -> int:
        s = Counter(s)

        result = 0

        for count in s.values():
            result += count // 2 * 2

            if result % 2 == 0 and count % 2 == 1:
                result += 1

        return result
