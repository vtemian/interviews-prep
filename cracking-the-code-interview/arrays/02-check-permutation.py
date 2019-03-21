"""Give two strings, write a method to decide if one is a permutation of the other"""


def check_permutation(initial_string: str, maybe_permutation: str) -> bool :
    if len(initial_string) != len(maybe_permutation):
        return False

    initial_letters = {}

    for letter in initial_string:
        if letter not in initial_letters:
            initial_letters[letter] = 0

        initial_letters[letter] += 1

    for letter in maybe_permutation:
        if not initial_letters.get(letter):
            return False

        initial_letters[letter] -= 1

    return sum(initial_letters.values()) == 0


for test_case, expected_result in [
    (('asd', 'dsa'), True),
    (('asda', 'dsa'), False),
    (('', ''), True),
]:
    assert check_permutation(*test_case) == expected_result
