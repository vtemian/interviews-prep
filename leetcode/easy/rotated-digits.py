class Solution:
    def rotatedDigits(self, N: 'int') -> 'int':
        def is_rotated(N):
            rotated_digits = {
                2: 5,
                5: 2,
                6: 9,
                9: 6
            }

            old_number = N
            new_number = 0

            while N:
                new_number = new_number * 10 + rotated_digits.get(N % 10, N % 10)
                N //= 10

            rotated_number = 0
            while new_number:
                rotated_number = rotated_number * 10 + new_number % 10
                new_number //= 10

            return rotated_number != old_number

        result = [
            n for n in range(N + 1)
            if is_rotated(n)
        ]
        print(result)
        return len(result)


result = Solution().rotatedDigits(10)
print(result)
