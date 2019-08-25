from heapq import heappush, heappop
from typing import List


def merge(*lists: List[List[int]]) -> List[int]:
    heap = []

    for sorted_list in lists:
        heappush(heap, (sorted_list[0], sorted_list[1:]))

    output = []
    while heap:
        item, sorted_list = heappop(heap)
        output.append(item)

        if sorted_list:
            heappush(heap, (sorted_list[0], sorted_list[1:]))

    return output


result = merge([1, 3, 5], [2, 4, 6])
assert result == [1, 2, 3, 4, 5, 6], result
