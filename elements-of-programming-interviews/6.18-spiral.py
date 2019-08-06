from typing import List


def solve(matrix: List[List[int]]) -> List[int]:
    result = []
    quadrant = 0

    while len(result) < len(matrix) * len(matrix):
        l_idx = quadrant
        c_idx = quadrant

        while c_idx < len(matrix) - quadrant:
            result.append(matrix[l_idx][c_idx])
            c_idx += 1

        l_idx += 1
        c_idx -= 1

        while l_idx < len(matrix) - quadrant:
            result.append(matrix[l_idx][c_idx])
            l_idx += 1

        l_idx -= 1
        c_idx -= 1

        while c_idx >= quadrant:
            result.append(matrix[l_idx][c_idx])
            c_idx -= 1

        c_idx += 1
        l_idx -= 1

        while l_idx > quadrant:
            result.append(matrix[l_idx][c_idx])
            l_idx -= 1

        quadrant += 1

    return result


print(solve([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(solve([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]))
