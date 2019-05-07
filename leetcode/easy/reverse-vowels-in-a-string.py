class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)

        start = 0
        end = len(s) - 1

        while start < end:
            while start < len(s) and s[start] not in 'aeiouAEIOU':
                start += 1

            while end >= 0 and s[end] not in 'aeiouAEIOU':
                end -= 1

            if start < end:
                s[start], s[end] = s[end], s[start]

                start += 1
                end -= 1

        return ''.join(st
