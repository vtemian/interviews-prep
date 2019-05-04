class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        if not s:
            return False

        idx = 1

        while idx <= len(s) // 2:
            if s[:idx] * (len(s) // idx) == s:
                return True

            idx += 1
        return False
