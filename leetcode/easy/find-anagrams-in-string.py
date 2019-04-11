from collections import Counter


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if not p:
            return -1

        idx = 0

        initial = Counter(p)
        moving = Counter(s[:len(p) - 1])
        result = []

        while idx + len(p) - 1 < len(s):
            if s[idx + len(p) - 1] not in moving:
                moving[s[idx + len(p) - 1]] = 1
            else:
                moving[s[idx + len(p) - 1]] += 1

            if moving == initial:
                result.append(idx)

            moving[s[idx]] -= 1
            if moving[s[idx]] == 0:
                del moving[s[idx]]

            idx += 1

        return result
