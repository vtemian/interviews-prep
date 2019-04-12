class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0

        if len(needle) > len(haystack):
            return -1

        kmp = [0] * len(needle)

        i = 0
        j = 1
        while j < len(needle):
            k = kmp[j - 1]

            while k > 0 and needle[k] != needle[j]:
                k = kmp[k - 1]

            kmp[j] = k + 1 if needle[k] == needle[j] else k

            j += 1

        kmp_idx = idx = 0

        while idx < len(haystack):
            if needle[kmp_idx] == haystack[idx]:
                kmp_idx += 1
                idx += 1

            if len(needle) == kmp_idx:
                return idx - len(needle)

            if idx < len(haystack) and needle[kmp_idx] != haystack[idx]:
                if kmp_idx != 0:
                    kmp_idx = kmp[kmp_idx - 1]
                else:
                    idx += 1

        return -1
