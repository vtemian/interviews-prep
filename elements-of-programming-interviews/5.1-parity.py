def no_ones(number: int) -> int:
    """
        nr: 101010
        nr - 1: 101001

        nr & (nr - 1) == 101000
    """

    ones = 0

    while number:
        ones += 1
        number = number & (number - 1)

    return ones


def solve_ok(number: int) -> int:
    """ O(k) complexity, where k == no ones """
    return no_ones(number) % 2


def solve_efficient(number: int) -> int:
    number ^= number >> 32
    number ^= number >> 16
    number ^= number >> 8
    number ^= number >> 4
    number ^= number >> 2
    number ^= number >> 1
    return number & 1


for solve in [solve_ok, solve_efficient]:
    print(f"Using {solve.__name__}")

    for (use_case, expected_result) in [
            (int('101010101', 2), 1),
            (int('101010100', 2), 0),
            (int('0', 2), 0),
            (int('1', 2), 1),
    ]:
        result = solve(use_case)
        assert result == expected_result, \
            f"Invalid parity {result} for {use_case}, expected {expected_result}"
