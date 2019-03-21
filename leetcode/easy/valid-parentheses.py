class Solution:
    def isValid(self, s: 'str') -> 'bool':
        stack = []
        pairs = {
            ']': '[',
            ')': '(',
            '}': '{'
        }

        for letter in s:
            if letter in "([{":
                stack.append(letter)
            else:
                if not stack or pairs[letter] != stack[-1]:
                    return False

                stack.pop()

        return len(stack) == 0
