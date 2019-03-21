"""
We are given two sentences A and B.
(A sentence is a string of space separated words.  Each word consists only of lowercase letters.)

A word is uncommon if it appears exactly once in one of the sentences, and does not appear in the other sentence.

Return a list of all uncommon words.

You may return the list in any order.



Example 1:

Input: A = "this apple is sweet", B = "this apple is sour"
Output: ["sweet","sour"]
Example 2:

Input: A = "apple apple", B = "banana"
Output: ["banana"]


Note:

0 <= A.length <= 200
0 <= B.length <= 200
A and B both contain only spaces and lowercase letters.
"""
from collections import Counter


class Solution:
    def uncommonFromSentences(self, A, B):
        A = Counter(A.split())
        B = Counter(B.split())

        result = []

        for word in A:
            if A[word] == 1 and word not in B:
                result.append(word)

        for word in B:
            if B[word] == 1 and word not in A:
                result.append(word)

        return result


result = Solution().uncommonFromSentences("apple apple", "banana")
print(result)
