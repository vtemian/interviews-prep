from typing import List


def add_one(x: List[int]) -> List[int]:
    x = x[::-1]

    rest = 1
    idx = 0

    while idx < len(x):
        c = x[idx]

        c += rest

        x[idx] = c % 10
        rest = c // 10

        idx += 1

    if rest:
        x.append(rest)

    return x[::-1]


assert add_one([1, 2, 9]) == [1, 3, 0]
assert add_one([9, 9, 9]) == [1, 0, 0, 0]
