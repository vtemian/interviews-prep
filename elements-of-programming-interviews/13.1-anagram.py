from collections import defaultdict
from typing import List


def anagram(words: str) -> List[List[str]]:
    words = words.split()

    grouped = defaultdict(list)

    for word in words:
        grouped[''.join(sorted(word))].append(word)

    return sorted(grouped.values())


result = anagram("123 321 456 564")
assert result == [["123", "321"], ["456", "564"]], result
