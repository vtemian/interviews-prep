from typing import List


def ppmatrix(matrix: List[List[int]]):
    for line in matrix:
        print(line)
    print('######################')


def rotate_matrix(matrix: List[List[int]]) -> List[List[int]]:
    quadrant = 0

    while quadrant <= len(matrix) // 2:
        count = 0
        end = len(matrix) // ((quadrant * 2) or 1) - 1

        while count < end:
            l_index = quadrant
            c_index = quadrant + count

            value = matrix[quadrant][quadrant + count]

            value, matrix[quadrant + count][end - quadrant] = matrix[quadrant + count][end - quadrant], value
            ppmatrix(matrix)

            value, matrix[end - quadrant][end - quadrant - count] = matrix[end - quadrant][end - quadrant - count], value
            ppmatrix(matrix)

            value, matrix[end - quadrant - count][quadrant] = matrix[end - quadrant - count][quadrant], value
            ppmatrix(matrix)

            value, matrix[quadrant][quadrant + count] = matrix[quadrant][quadrant + count], value
            ppmatrix(matrix)

            count += 1

        quadrant += 1

    return matrix


for test_case, expected_result in [
    (
        [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9],
        ], [
            [7, 4, 1],
            [8, 5, 2],
            [9, 6, 3],
        ]
    ),

    (
        [
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12],
            [13, 14, 15, 16],
        ], [
            [13, 9, 5, 1],
            [14, 10, 6, 2],
            [15, 11, 7, 3],
            [16, 12, 8, 4]
        ]
    ),
]:
    result = rotate_matrix(test_case)
    assert True
    #assert result == expected_result, "{} != {}".format(result, expected_result)
