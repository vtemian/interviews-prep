class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        if not num1:
            return num2

        if not num2:
            return num1

        if len(num1) < len(num2):
            num1, num2 = num2, num1

        num1 = num1[::-1]
        num2 = num2[::-1]

        result = []
        count = 0
        reminder = 0

        while count < len(num2):
            digit = int(num1[count]) + int(num2[count]) + reminder

            result.append(str(digit % 10))
            reminder = digit // 10

            count += 1

        while count < len(num1):
            digit = int(num1[count]) + reminder

            result.append(str(digit % 10))
            reminder = digit // 10

            count += 1

        if reminder:
            result.append(str(reminder))

        return ''.join(result[::-1])
