from math import sqrt


class Solution:
    def countPrimes(self, n: int) -> int:
        primes = [
            True
            for _ in range(n)
        ]

        for idx, is_prime in enumerate(primes):
            if not is_prime or idx < 2:
                continue

            maybe_prime = idx + idx
            while maybe_prime < n:
                primes[maybe_prime] = False
                maybe_prime += idx

        total = 0
        start = 2
        while start < n:
            total += primes[start]
            start += 1

        return total
