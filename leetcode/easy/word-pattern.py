class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        if not pattern:
            return False

        str = str.split()
        if len(str) != len(pattern):
            return False

        mapping = {}
        rev_mapping = {}

        for idx, letter in enumerate(pattern):
            if letter not in mapping:
                if str[idx] in rev_mapping:
                    return False
                mapping[letter] = str[idx]
                rev_mapping[str[idx]] = letter
            elif mapping[letter] != str[idx]:
                return False

        return True
