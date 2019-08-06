def _to_digit(letter: str) -> int:
    if 'A' <= letter <= 'Z':
        return 10 + ord(letter) - ord('A')

    return ord(letter) - ord('0')


def _to_letter(digit: int) -> str:
    if digit >= 10:
        return chr(ord('A') + digit - 10)

    return str(digit)


def solve(number: str, initial_base: int, second_base: int) -> str:
    dec = 0
    result = []

    for letter in number:
        dec = dec * initial_base + _to_digit(letter)

    while dec:
        result.append(_to_letter(dec % second_base))
        dec //= second_base

    return "".join(result[::-1])


for use_case, expected_result in [
        (("1234", 10, 16), "4D2"),
        (("1234", 10, 2), "10011010010"),
        (("615", 7, 13), "1A7"),
]:
    result = solve(*use_case)
    assert result == expected_result, f"{result} != {expected_result}"
