class Solution:
    def rotatedDigits(self, N: 'int') -> 'int':
        result = 0

        for nr in range(1, N + 1):
            ok = False

            for digit in str(nr):
                if digit in '347':
                    break

                if digit in '6952':
                    ok = True
            else:
                result += int(ok)

        return result
