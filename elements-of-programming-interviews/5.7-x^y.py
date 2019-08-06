def solve(x: int, y: int) -> int:
    result = 1.0
    if y < 0:
        x = 1.0 / x
        y *= -1

    while y:
        if y & 1:
            result *= x

        x *= x
        y >>= 1

    return result


for (x, y), expected_result in [
        ((5, 2), 25),
        ((5, 3), 125),
        ((5, -3), 0.008000000000000002),
        ((5, -1), 0.2),
        ((5, 1), 5.0),
        ((5, 0), 1.0),
]:
    result = solve(x, y)
    assert result == expected_result, f"{x} ^ {y} [{result}] != {expected_result}"
