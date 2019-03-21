"""
Given a string S and a character C, return an array of integers representing the shortest distance from the
character C in the string.

Example 1:

Input: S = "loveleetcode", C = 'e'
Output: [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]


Note:

S string length is in [1, 10000].
C is a single character, and guaranteed to be in string S.
All letters in S and C are lowercase.
"""


class Solution:
    def shortestToChar(self, S, C):
        base = None
        store = []
        result = [len(S)] * len(S)

        for letter_idx, letter in enumerate(S):
            if letter == C:
                base = letter_idx
                result[letter_idx] = 0

                while store:
                    idx = store.pop(0)
                    result[idx] = min(result[idx], abs(base - idx))
            else:
                store.append(letter_idx)
                if base is not None:
                    result[letter_idx] = min(result[letter_idx], abs(letter_idx - base))

        while store:
            idx = store.pop(0)
            result[idx] = min(result[idx], abs(base - idx))

        return result


result = Solution().shortestToChar('baaab', 'b')
print(result)
