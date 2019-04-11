from collections import Counter


class Solution:
    def firstUniqChar(self, s: str) -> int:
        letters_index = Counter(s)

        for index, letter in enumerate(s):
            if letters_index[letter] == 1:
                return index

        return -1
