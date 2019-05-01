from collections import Counter


class Solution(object):
    def commonChars(self, A):
        """
        :type A: List[str]
        :rtype: List[str]
        """

        if not A:
            return []

        common = Counter(A[0])

        for word in A[1:]:
            index = Counter(word)

            for letter in common:
                if letter not in index:
                    del common[letter]
                common[letter] = min(common[letter], index[letter])

        results = []
        for letter, value in common.items():
            if not letter:
                continue
            results.extend([letter] * value)

        return results
