"""
Given two strings A and B, find the minimum number of times A
has to be repeated such that B is a substring of it.
If no such solution, return -1.

For example, with A = "abcd" and B = "cdabcdab".

Return 3, because by repeating A three times ("abcdabcdabcd"),
B is a substring of it; and B is not a substring of A repeated two times ("abcdabcd").

Note:
The length of A and B will be between 1 and 10000.
"""


class Solution:
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """

        if not B:
            return 0 if not A else -1

        count = 1
        original_A = A

        while count < 3 or len(A) <= len(B) * 3:
            if B in A:
                return count

            A += original_A
            count += 1

        print(A, B)

        return -1


solution = Solution()
print(solution.repeatedStringMatch('abcbc', 'cabcbca'))
