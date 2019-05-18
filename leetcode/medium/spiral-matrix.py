class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []

        quadrant = 0
        nums = []
        i = j = 0

        while len(nums) < len(matrix) * len(matrix[0]):
            i = j = quadrant

            while len(nums) < len(matrix) * len(matrix[0]) and j < len(matrix[0]) - quadrant:
                nums.append(matrix[i][j])
                j += 1

            j -= 1
            i += 1

            while len(nums) < len(matrix) * len(matrix[0]) and i < len(matrix) - quadrant:
                nums.append(matrix[i][j])
                i += 1

            i -= 1
            j -= 1

            while len(nums) < len(matrix) * len(matrix[0]) and j >= quadrant:
                nums.append(matrix[i][j])
                j -= 1

            j += 1
            i -= 1

            while len(nums) < len(matrix) * len(matrix[0]) and i > quadrant:
                nums.append(matrix[i][j])
                i -= 1

            quadrant += 1

        return nums
