class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) < 1:
            return ''

        start = end = 0

        def expand(start, end):
            while start >= 0 and end < len(s) and s[start] == s[end]:
                start -= 1
                end += 1

            return end - start - 1

        for idx, char in enumerate(s):
            length_odd = expand(idx, idx)
            length_even = expand(idx, idx + 1)

            length = max(length_odd, length_even)
            if length > end - start:
                start = idx - (length - 1) // 2
                end = idx + length // 2

        return s[start:end + 1]
