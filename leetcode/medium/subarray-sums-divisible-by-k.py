from collections import Counter


class Solution:
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        partials = [0]

        for nr in A:
            partials.append((partials[-1] + nr) % K)

        counter = Counter(partials)
        return sum(res * (res - 1) // 2 for res in counter.values())
