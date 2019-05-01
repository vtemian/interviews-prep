class NumArray:

    def __init__(self, nums: List[int]):
        self.sums = [nums[0]] if nums else []

        idx = 1
        while idx < len(nums):
            self.sums.append(self.sums[idx - 1] + nums[idx])
            idx += 1

    def sumRange(self, i: int, j: int) -> int:
        if i == 0:
            return self.sums[j]
        return self.sums[j] - self.sums[i - 1]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
