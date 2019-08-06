from typing import List
from random import randint


def solve(numbers: List[int], size: int) -> List[int]:
    index = 0

    while index < size:
        new_index = randint(0, len(numbers) - 1)

        numbers[index], numbers[new_index] = numbers[new_index], numbers[index]

        index += 1

    return numbers[:size]


print(solve([1, 2, 3, 4, 5], 3))
