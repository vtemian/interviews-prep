class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        if not S:
            return S

        start = 0
        end = len(S) - 1
        S = list(S)

        def is_letter(ch):
            return 'a' <= ch <= 'z' or 'A' <= ch <= 'Z'

        while start < end:
            while start < end and not is_letter(S[start]):
                start += 1
                print(start, end)

            while start < end and not is_letter(S[end]):
                end -= 1

            if start < end:
                S[start], S[end] = S[end], S[start]

            start += 1
            end -= 1

        return ''.join(S)
