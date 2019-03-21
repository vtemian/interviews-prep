def is_palindrom(permutation: str) -> bool:
    if not permutation:
        return False

    permutation = permutation.replace(' ', '').lower()

    store = {}
    odd = 0
    for letter in permutation:
        if letter not in store:
            store[letter] = 0

        store[letter] += 1
        if store[letter] % 2 == 0:
            odd -= 1
        else:
            odd += 1

    return odd <= 1


for test_case, expected_result in [
    ('asd', False),
    ('', False),
    ('  1 ', True),
    ('asa', True)
]:
    assert is_palindrom(test_case) == expected_result
