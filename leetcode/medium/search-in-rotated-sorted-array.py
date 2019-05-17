class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return -1

        if len(nums) == 1:
            return 0 if nums[0] == target else -1

        def find_rotated_index():
            if nums[0] < nums[-1]:
                return 0

            start = 0
            end = len(nums) - 1

            while start <= end:
                mid = (start + end) // 2

                if nums[mid] > nums[mid + 1]:
                    return mid + 1

                if nums[mid] < nums[start]:
                    end = mid - 1
                else:
                    start = mid + 1

        def find_target(start, end):

            while start <= end:
                mid = (start + end) // 2

                if nums[mid] == target:
                    return mid

                if nums[mid] > target:
                    end = mid - 1
                else:
                    start = mid + 1

            return -1

        rotated = find_rotated_index()

        if nums[rotated] == target:
            return rotated

        if rotated == 0:
            return find_target(0, len(nums) - 1)

        if target < nums[0]:
            return find_target(rotated, len(nums) - 1)

        return find_target(0, rotated)
