class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 31]

        for prime in primes:
            if (1 << (prime - 1)) * ((1 << prime) - 1) == num:
                return True

        return False
