from collections import Counter


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s = Counter(s)
        t = Counter(t)

        for letter in t:
            if letter not in s:
                return letter

            if s[letter] < t[letter]:
                return letter

        return ''
