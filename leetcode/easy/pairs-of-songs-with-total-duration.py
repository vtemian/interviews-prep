class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        res = [0] * 60

        for t in time:
            res[t % 60] += 1

        result = 0

        for idx in range(31):
            time = res[idx]

            if idx == 0 or idx == 30:
                result += (time * (time - 1) // 2)
            else:
                result += res[idx] * res[60 - idx]

        return result
