import random


class Solution:

    def __init__(self, nums: List[int]):
        self.orig = nums
        self.current = [nr for nr in self.orig]

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        self.current = [nr for nr in self.orig]
        return self.current

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        initial = self.current
        for idx in range(len(self.current) - 1, 0, -1):
            new_idx = random.randint(0, idx)
            initial[idx], initial[new_idx] = initial[new_idx], initial[idx]

        self.current = initial
        return self.current


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
