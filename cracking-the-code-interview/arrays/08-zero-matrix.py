from typing import List


def ppmatrix(matrix: List[List[int]]):
    for line in matrix:
        print(line)
    print('######################')


def zero_matrix(matrix: List[List[int]]) -> List[List[int]]:
    zero_positions = []

    for l_index, line in enumerate(matrix):
        for c_index, value in enumerate(line):
            if value == 0:
                zero_positions.append((l_index, c_index))

    for l_index, c_index in zero_positions:
        start = 0
        end = len(matrix[l_index])

        while start < end:
            matrix[l_index][start] = 0
            start += 1

        start = 0
        end = len(matrix)

        while start < end:
            matrix[start][c_index] = 0
            start += 1

    return matrix


for test_case, expected_result in [
    (
        [
            [1, 2, 3],
            [4, 0, 6],
            [7, 8, 9],
        ], [
            [1, 0, 3],
            [0, 0, 0],
            [7, 0, 9],
        ]
    ),

    (
        [
            [0, 0, 0, 0],
            [5, 6, 7, 8],
            [9, 10, 11, 12],
            [13, 14, 15, 16],
        ], [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ]
    ),
]:
    result = zero_matrix(test_case)
    assert result == expected_result, "{} != {}".format(result, expected_result)
