from typing import List


def intersection(x: List[int], y: List[int]) -> List[int]:
    result = []
    idx_x = idx_y = 0

    while idx_x < len(x) and idx_y < len(y):
        if x[idx_x] == y[idx_y] and (not result or result[-1] != x[idx_x]):
            result.append(x[idx_x])
            idx_x += 1
            idx_y += 1
        elif x[idx_x] > y[idx_y]:
            idx_y += 1
        else:
            idx_x += 1

    return result


result = intersection([1, 2, 2, 3, 3, 4], [2, 3, 3])
assert result == [2, 3]

result = intersection([1, 2, 2, 3, 3, 4], [4])
assert result == [4]

result = intersection([1, 2, 2, 3, 3, 4], [5])
assert result == []
