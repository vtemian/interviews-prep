from math import sqrt


class Solution:
    def numSquares(self, n: 'int') -> 'int':
        if not n:
            return 0

        perfect_squares = [nr ** 2 for nr in range(1, int(sqrt(n)) + 1)][::-1]
        queue = []
        min_squares = 2 ** 32
        for square in perfect_squares:
            queue.append((n // square, n % square))

        while queue:
            nr_squares, new_n = queue.pop(0)

            if not new_n:
                min_squares = min(min_squares, nr_squares)
                continue

            if nr_squares >= min_squares:
                continue

            n = new_n
            for square in perfect_squares:
                new_n = n
                if square > new_n:
                    continue

                no_squares, new_n = new_n // square, new_n % square
                if not new_n:
                    min_squares = min(min_squares, no_squares + nr_squares)
                    continue

                if no_squares + nr_squares >= min_squares:
                    continue

                queue.append((no_squares + nr_squares, new_n))

        return -1 if min_squares == 2 ** 32 else min_squares
