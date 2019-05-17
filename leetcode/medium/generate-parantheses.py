class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def generate(answer, open=0, close=0):
            nonlocal result

            if len(answer) == n * 2:
                result.append(answer)
                return

            if open < n:
                generate(answer + "(", open + 1, close)

            if close < open and close < n:
                generate(answer + ")", open, close + 1)

        generate("")

        return result
