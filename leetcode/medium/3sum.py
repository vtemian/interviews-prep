class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        result = set()

        def find_values(value, idx):
            nonlocal result

            start = idx + 1
            end = len(nums) - 1

            while start < end:
                rest = value + nums[start] + nums[end]

                if rest == 0:
                    result.add((value, nums[start], nums[end]))
                    start += 1
                    end -= 1
                elif rest > 0:
                    end -= 1
                else:
                    start += 1

        for idx, value in enumerate(nums):
            find_values(value, idx)

        return list(result)
