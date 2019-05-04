class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if not nums:
            return 0

        current = eliminate = 0
        while current < len(nums) and nums[current] != val:
            current += 1

        eliminate = current + 1

        while eliminate < len(nums):
            while eliminate < len(nums) and nums[eliminate] == val:
                eliminate += 1

            if eliminate >= len(nums):
                return current

            nums[current], nums[eliminate] = nums[eliminate], nums[current]
            current += 1

            while current < len(nums) and nums[current] != val:
                current += 1

        return current
