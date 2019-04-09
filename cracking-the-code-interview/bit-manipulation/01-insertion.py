def insert(n: int, m: int, i: int, j: int) -> int:
    mask = ((n >> j) << j) + (1 << j) + ((1 << i) - 1)
    n = n & mask
    return n | (m << i)


assert insert(int('10000000000', 2), int('10011', 2), 2, 6) == int('10001001100', 2)
assert insert(int('11100000001', 2), int('10011', 2), 2, 6) == int('11101001101', 2)
