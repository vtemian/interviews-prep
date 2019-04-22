class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        if k < 0:
            return 0

        store = {}

        for index, num in enumerate(nums):
            if num in store:
                store[num].append(index)
            else:
                store[num] = [index]

        result = {}

        for index, num in enumerate(nums):
            needle = k + num

            if needle not in store:
                continue

            for maybe in store[needle]:
                if index == maybe or (num, nums[maybe]) in result or (nums[maybe], num) in result:
                    continue

                result[(num, nums[maybe])] = 1

        return len(result.keys())
