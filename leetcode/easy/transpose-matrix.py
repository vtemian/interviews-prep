"""
Given a matrix A, return the transpose of A.

The transpose of a matrix is the matrix flipped over it's main diagonal,
switching the row and column indices of the matrix.


Example 1:

Input: [[1,2,3],[4,5,6],[7,8,9]]
Output: [[1,4,7],[2,5,8],[3,6,9]]
Example 2:

Input: [[1,2,3],[4,5,6]]
Output: [[1,4],[2,5],[3,6]]


Note:

1 <= A.length <= 1000
1 <= A[0].length <= 1000
"""

class Solution:
    def transpose(self, A):
        transposed_A = []

        for line_idx, line in enumerate(A):
            for col_idx, val in enumerate(line):
                if col_idx >= len(transposed_A):
                    transposed_A.append([])

                transposed_A[col_idx].append(val)

        return transposed_A


result = Solution().transpose([[1,2,3],[4,5,6]])
print(result)
