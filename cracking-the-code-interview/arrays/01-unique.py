"""
Implement an alghorithm to determine if a sting has all unique characters.
What if you can't use additional data structures?
"""

def is_unique_n_2(string: str) -> bool:
    """
        We take the first character and check for all letters if we found a copy of it.
        This is going to take O(n ^ 2) time and O(1) space.
    """

    for idx, letter in enumerate(string):
        for next_letter in string[idx + 1:]:
            if letter == next_letter:
                return False
    return True


def is_unique_n_lg(string: str) -> bool:
    """
        We sort the string and take each neighbour. If they are equal, return False.
    """

    start = 0
    sorted_string = sorted(string)

    while start + 1 < len(sorted_string):
        if string[start] == string[start + 1]:
            return False

        start += 1

    return True


def is_unique_n_dict(string: str) -> bool:
    """
        Let's use a dict to store all occurences for every char.
    """

    store = {}

    for letter in string:
        if letter in store:
            return False
        store[letter] = 1

    return True


def is_unique_n_set(string: str) -> bool:
    """
        Transform the string in a set and check it's length.
        If it's different from the lenght of the string, return False
    """

    return len(set(string)) == len(string)


def is_unique_n_bit_vector(string: str) -> bool:
    """
        Similiar to the dict solution, it just uses a bit vector instead of a dict or array.
    """

    vector = 0
    for letter in string:
        if vector & 1 << ord(letter):
            return False
        vector |= 1 << ord(letter)

    return True


for test_case, expected_result in [
    ('asdzxc', True),
    ('111a', False),
    (' ', True),
    ('', True),
    ('😁😁', False),
    ('😁🏘' ,True),
]:
    assert is_unique_n_2(test_case) == expected_result
    assert is_unique_n_lg(test_case) == expected_result
    assert is_unique_n_dict(test_case) == expected_result
    assert is_unique_n_set(test_case) == expected_result
    assert is_unique_n_bit_vector(test_case) == expected_result
