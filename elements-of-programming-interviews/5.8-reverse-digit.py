def reverse(x: int) -> int:
    neg = x < 0
    if neg:
        x *= -1

    result = 0
    while x:
        result = result * 10 + x % 10
        x //= 10

    return result if not neg else -1 * result


assert reverse(123) == 321
assert reverse(-123) == -321
