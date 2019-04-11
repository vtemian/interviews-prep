class Solution:
    def isHappy(self, n: 'int') -> 'bool':
        happies = set()

        def powers(n):
            result = 0

            while n:
                result += (n % 10) ** 2
                n //= 10

            return result

        power = n
        while True:
            power = powers(power)

            if power // 10 == 0 and power % 10 == 1:
                return True

            if power in happies:
                return False

            happies.add(power)
