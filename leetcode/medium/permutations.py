class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        def back(index):
            nonlocal result
            if index == len(nums):
                result.append(nums[:])
                return

            for i in range(index, len(nums)):
                nums[index], nums[i] = nums[i], nums[index]

                back(index + 1)

                nums[index], nums[i] = nums[i], nums[index]

        back(0)

        return result
