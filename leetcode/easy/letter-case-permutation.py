class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        result = []
        n = len(S)

        def backtrack(current):
            nonlocal result
            m = len(current)

            if m == n:
                result.append(current)
                return

            l = S[m]
            backtrack(current + S[m])

            if not l.isupper():
                backtrack(current + l.upper())
            else:
                backtrack(current + l.lower())

        backtrack('')

        return list(set(result))
