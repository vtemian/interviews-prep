from typing import List


def merge(big: List[int], small: List[int]) -> List[int]:
    start = len(big) - 1

    s_idx = len(small) - 1

    b_idx = len(big) - 1
    while big[b_idx] is None and b_idx > 0:
        b_idx -= 1

    while s_idx >= 0 and b_idx >= 0:
        if small[s_idx] > big[b_idx]:
            big[start] = small[s_idx]
            s_idx -= 1
        else:
            big[start] = big[b_idx]
            b_idx -= 1

        start -= 1

    while s_idx >= 0:
        big[start] = small[s_idx]
        s_idx -= 1
        start -= 1

    return big


result = merge([1, None, None, None, None], [5, 6, 7, 8])
assert result == [1, 5, 6, 7, 8], result

result = merge([1, None], [2])
assert result == [1, 2], result

result = merge([1, 2, 3, 4, 5, None], [0])
assert result == [0, 1, 2, 3, 4, 5], result
