class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:  
        for num in nums:
            if nums[abs(num) - 1] < 0:
                continue

            nums[abs(num) - 1] *= -1

        return [
            idx + 1
            for idx in range(len(nums))
            if nums[idx] > 0
        ]
