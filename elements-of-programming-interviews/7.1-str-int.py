def to_int(number: str) -> int:
    result = 0
    order = 10 ** (len(number) - 1)

    is_negative = number[0] == '-'
    if is_negative:
        number = number[1:]
        order /= 10

    for letter in number:
        result += (ord(letter) - ord('0')) * order
        order //= 10

    return result if not is_negative else result * -1


def to_str(number: int) -> str:
    result = []

    is_negative = number < 0
    if is_negative:
        number *= -1

    while number:
        digit = number % 10
        number //= 10

        result.append(chr(digit + ord('0')))

    if is_negative:
        result.append('-')

    return "".join(result[::-1] if result else ["0"])


print('to_int')
for use_case, expected_result in [
        ("1234", 1234),
        ("1111", 1111),
        ("0", 0),
        ("-1", -1),
        ("-123", -123),
]:
    result = to_int(use_case)
    assert result == expected_result, f"{result} != {expected_result}"


print('to_str')
for use_case, expected_result in [
        (1234, "1234"), (0, "0"),
        (1, "1"),
        (-1, "-1"),
        (-1234, "-1234"),
]:
    result = to_str(use_case)
    assert result == expected_result, f"{result} != {expected_result}"
