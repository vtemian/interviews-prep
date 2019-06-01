import random
import bisect


class Solution:

    def __init__(self, w: List[int]):
        self.field = []
        self.partial_range = 0

        for nr in w:
            self.partial_range += nr
            self.field.append(self.partial_range)

    def pickIndex(self) -> int:
        crop = random.randint(0, self.partial_range - 1)

        return bisect.bisect_right(self.field, crop)


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
