from typing import List


def search(nums: List[int], needle: int) -> int:
    if not nums:
        return -1

    result = -1
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == needle:
            result = mid

            right = mid - 1
        elif nums[mid] < needle:
            left = mid + 1
        else:
            right = mid - 1

    return result


result = search([1, 2, 3, 4, 5, 6, 6, 6, 6, 6, 7, 8, 9, 10], 6)
assert result == 5, result
