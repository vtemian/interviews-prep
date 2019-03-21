"""
We are given an array A of N lowercase letter strings, all of the same length.

Now, we may choose any set of deletion indices, and for each string, we delete all the characters in those indices.

For example, if we have an array A = ["abcdef","uvwxyz"] and deletion indices {0, 2, 3},
then the final array after deletions is ["bef", "vyz"], and the remaining columns of A are
["b","v"], ["e","y"], and ["f","z"].  (Formally, the c-th column is [A[0][c], A[1][c], ..., A[A.length-1][c]].)

Suppose we chose a set of deletion indices D such that after deletions,
each remaining column in A is in non-decreasing sorted order.

Return the minimum possible value of D.length.


Example 1:

Input: ["cba","daf","ghi"]
Output: 1
Explanation:
After choosing D = {1}, each column ["c","d","g"] and ["a","f","i"] are in non-decreasing sorted order.
If we chose D = {}, then a column ["b","a","h"] would not be in non-decreasing sorted order.
Example 2:

Input: ["a","b"]
Output: 0
Explanation: D = {}
Example 3:

Input: ["zyx","wvu","tsr"]
Output: 3
Explanation: D = {0, 1, 2}


Note:

1 <= A.length <= 100
1 <= A[i].length <= 1000
"""


class Solution:
    def minDeletionSize(self, A):
        """
        :type A: List[str]
        :rtype: int
        """

        if not A or not A[0]:
            return 0

        unsorted_cols = 0

        col_idx = 0

        no_col = len(A[0])
        no_lines = len(A)

        while col_idx < no_col:
            line_idx = 0

            while line_idx + 1 < no_lines:
                if A[line_idx][col_idx] > A[line_idx + 1][col_idx]:
                    unsorted_cols += 1
                    break
                line_idx += 1

            col_idx += 1

        return unsorted_cols


result = Solution().minDeletionSize(["zyx","wvu","tsr"])
print(result)
