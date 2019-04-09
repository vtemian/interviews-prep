def get_bit(n: int, position: int) -> int:
    return n & (1 << (position - 1)) != 0


def set_bit(n: int, position: int, bit: int) -> int:
    if bit == 0:
        mask = n >> position
        mask = mask << position
        mask += (1 << (position - 1)) - 1
        return mask & n

    return n | 1 << (position - 1)


def toggle_bit(n: int, position: int) -> int:
    return n ^ 1 << (position - 1)


assert get_bit(int('101011', 2), 4) == 1

assert set_bit(int('101011', 2), 4, 0) == int('100011', 2)
assert set_bit(int('101011', 2), 3, 1) == int('101111', 2)

assert toggle_bit(int('101011', 2), 3) == int('101111', 2)
assert toggle_bit(int('101011', 2), 4) == int('100011', 2)
