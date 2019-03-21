from math import log2


class Solution:
    def binaryGap(self, N):
        pre_pos_1 = None
        max_dist = 0

        while N:
            mask = N ^ (N - 1)

            pos_1 = int(log2(mask + 1))

            if pre_pos_1:
                max_dist = max(max_dist, pos_1 - pre_pos_1)

            pre_pos_1 = pos_1

            N = N & (N - 1)

        return max_dist


for test in [22, 5, 6, 8]:
    result = Solution().binaryGap(test)
    print(result)
