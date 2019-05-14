class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2:
            return len(s)

        store = set()
        result = 0
        i = j = 0

        while i < len(s) and j < len(s):
            if s[i] not in store:
                store.add(s[i])
                i += 1
                result = max(result, i - j)
            else:
                store.remove(s[j])
                j += 1

        return result
