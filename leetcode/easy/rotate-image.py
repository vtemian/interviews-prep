class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        q = 0
        m = len(matrix) - 1
        while q < len(matrix) // 2:
            c = 0
            while c < len(matrix) - 1 - q * 2:
                n = matrix[q][q + c]
                n, matrix[q + c][m - q] = matrix[q + c][m - q], n
                n, matrix[m - q][m - q - c] = matrix[m - q][m - q - c], n
                n, matrix[m - q - c][q] = matrix[m - q - c][q], n
                n, matrix[q][q + c] = matrix[q][q + c], n
                c += 1
            q += 1
