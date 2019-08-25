from random import randint
from typing import List


def rearange(nums: List[int], left: int, right: int, pivot: int):
    value = nums[pivot]
    new_pivot = left
    nums[right], nums[pivot] = nums[pivot], nums[right]

    idx = left
    while idx < right:
        if nums[idx] > value:
            nums[idx], nums[new_pivot] = nums[new_pivot], nums[idx]
            new_pivot += 1
        idx += 1

    nums[right], nums[new_pivot] = nums[new_pivot], nums[right]

    return nums, new_pivot


def largest(nums: List[int], k: int) -> int:
    start = 0
    end = len(nums) - 1

    while start <= end:
        pivot = randint(start, end)

        nums, new_pivot = rearange(nums, start, end, pivot)
        if new_pivot == k - 1:
            return nums[new_pivot]
        elif new_pivot > k - 1:
            end = new_pivot - 1
        else:
            start = new_pivot + 1


result = largest([1,2,3,4,5,6,7], 2)
assert result == 6, result
