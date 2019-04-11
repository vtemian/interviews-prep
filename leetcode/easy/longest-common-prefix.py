class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        if len(strs) == 1:
            return strs[0]

        def _find_common_prefix(current_prefix, string):
            start = 0

            while start < len(current_prefix) and start < len(string):
                if string[start] != current_prefix[start]:
                    break

                start += 1

            return string[:start]

        longest_prefix = strs[0]

        for string in strs[1:]:
            longest_prefix = _find_common_prefix(longest_prefix, string)
            if not longest_prefix:
                return ""

        return longest_prefix
