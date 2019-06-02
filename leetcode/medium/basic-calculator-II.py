class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """

        operands = []
        numbers = []

        idx = 0

        operations = {
            "+": lambda x, y: x + y,
            "-": lambda x, y: x - y,
            "*": lambda x, y: x * y,
            "/": lambda x, y: x / y
        }

        def number(start):
            nr = []

            while start < len(s) and not s[start].isdigit():
                start += 1

            while start < len(s) and s[start].isdigit():
                nr.append(s[start])
                start += 1

            start -= 1

            return start, int("".join(nr))

        while idx < len(s):
            if s[idx].isdigit():
                idx, nr = number(idx)
                numbers.append(nr)

            if s[idx] in "+-":
                operands.append(s[idx])

            if s[idx] in "/*":
                op = s[idx]

                first = numbers.pop()
                idx, second = number(idx + 1)

                numbers.append(operations[op](first, second))

            idx += 1

        numbers = numbers[::-1]
        operands = operands[::-1]

        while operands:
            first, second = numbers.pop(), numbers.pop()
            numbers.append(operations[operands.pop()](first, second))

        return numbers[0]
