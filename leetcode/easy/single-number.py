class Solution:
    def singleNumber(self, nums: 'List[int]') -> 'int':
        if not nums:
            return 0

        store = nums[0]
        for number in nums[1:]:
            store ^= number

        return store
