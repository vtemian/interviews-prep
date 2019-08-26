from collections import Counter


def is_constructible(letter: str, magazine: str) -> bool:
    letter_index = Counter(letter.split())
    magazine_index = Counter(magazine.split())

    return letter_index == magazine_index


result = is_constructible("ana are mere", "mere are ana")
assert result, result
