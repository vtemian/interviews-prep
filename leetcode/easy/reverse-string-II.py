class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        if not s or not k or k < 0:
            return ""

        s = list(s)
        for i in range(0, len(s), 2 * k):
            s[i: i+k] = reversed(s[i:i+k])

        return ''.join(s)
