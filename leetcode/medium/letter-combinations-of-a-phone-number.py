class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        letters = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        result = []

        def backtrack(index, answer):
            nonlocal result

            if index >= len(digits):
                result.append(answer)
                return

            for letter in letters[digits[index]]:
                backtrack(index + 1, answer + letter)

        backtrack(0, "")

        return result
