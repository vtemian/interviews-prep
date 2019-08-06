from typing import List


def solve(numbers: List[int], pivot: int) -> List[int]:
    start = 0

    for index, number in enumerate(numbers):
        if number < pivot:
            numbers[index], numbers[start] = numbers[start], numbers[index]
            start += 1

    end = index = len(numbers) - 1

    while index:
        number = numbers[index]
        if number > pivot:
            numbers[index], numbers[end] = numbers[end], numbers[index]
            end -= 1
        index -= 1

    return numbers


result = solve([5, 2, -1, 6, 3, -1, 7, -1, 3], 3)
assert result == [2, -1, -1, -1, 3, 3, 5, 7, 6], result
