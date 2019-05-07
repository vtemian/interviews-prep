class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        stack = []
        l = len(nums)
        r = 0

        for idx, num in enumerate(nums):
            while stack and nums[stack[-1]] > num:
                l = min(l, stack.pop())
            stack.append(idx)

        stack = []

        for idx, num in enumerate(nums[::-1]):
            while stack and nums[stack[-1]] < num:
                r = max(r, stack.pop())

            stack.append(len(nums) - 1 - idx)

        return r - l + 1 if r - l > 0 else 0
