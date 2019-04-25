class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        op = {
            '+': lambda a, b: a + b,
            '-': lambda a, b: a - b,
            '*': lambda a, b: a * b,
            '/': lambda a, b: abs(a) // abs(b) * (1 if ((a > 0 and b > 0) or (a < 0 and b < 0)) else -1)
        }

        for token in tokens:
            if token in "+-*/":
                a, b = stack.pop(), stack.pop()
                stack.append(op[token](b, a))
            else:
                stack.append(int(token))

        if stack:
            return stack[0]
        else:
            return 0
