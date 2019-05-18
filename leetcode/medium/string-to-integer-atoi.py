class Solution:
    def myAtoi(self, str: str) -> int:
        if not str:
            return 0

        isPos = isNeg = has_value = False
        ignore_all = False
        value = 0

        for char in str:
            if ignore_all:
                continue

            if char == ' ':
                if has_value:
                    ignore_all = True

                if not isPos and not isNeg and value == 0:
                    continue
                break

            if char == '-':
                if has_value or isNeg:
                    break

                isNeg = True
                continue

            if char == '+':
                if has_value or isPos:
                    break

                isPos = True
                continue

            try:
                next_digit = int(char)
                value = value * 10 + next_digit
                has_value = True
            except:
                break

        if isPos and isNeg:
            return 0

        if isNeg:
            if value > 2147483647:
                return -2147483648
            return -value
        else:
            if value > 2147483647:
                return 2147483647
            return value
