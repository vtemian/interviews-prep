def count_chars(string: str) -> dict:
    store = {}

    for letter in string:
        if letter not in store:
            store[letter] = 0
        store[letter] += 1

    return store


def one_way(initial: str, to_be: str) -> bool:
    if abs(len(initial) - len(to_be)) > 1:
        return False

    initial_store = count_chars(initial)
    to_be_store = count_chars(to_be)

    missing = 0
    for letter, count in initial_store.items():
        diff = abs(to_be_store.get(letter, 0) - count)
        if diff > 1:
            return False

        if letter in to_be_store:
            to_be_store[letter] = diff
        elif not missing:
            missing = diff
        else:
            return False

    return True


for test_case, expected_result in [
    (('pale', 'ple'), True),
    (('pales', 'pale'), True),
    (('pale', 'bale'), True),
    (('pale', 'bake'), False),
    (('aaaa', 'bbba'), False),
]:
    assert one_way(*test_case) == expected_result
