from collections import Counter


class Solution:
    def rotateString(self, A: str, B: str) -> bool:
        # aalleall
        # eallaall

        if not A and not B:
            return True

        if not A or not B:
            return False

        if len(A) != len(B):
            return False

        if Counter(A) != Counter(B):
            return False

        occurrences = [len(B) - index for index, letter in enumerate(B)
                       if letter == A[0]]

        for delta in occurrences:
            for idx, letter in enumerate(A):
                if letter != B[idx - delta]:
                    break
            else:
                return True

        return False
