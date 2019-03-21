n = int(input())
matrix_size = n


MATRIX = []


while n:
    MATRIX.append(input())
    n -= 1


count = 0
for i, line in enumerate(MATRIX):
    for j, value in enumerate(line):
        if i - 1 >= 0 and i + 1 < matrix_size and j - 1 >= 0 and j + 1 < matrix_size:
            count += int(value == 'X' and MATRIX[i - 1][j - 1] == value and MATRIX[i - 1][j + 1] == value and
                         MATRIX[i + 1][j - 1] == value and MATRIX[i + 1][j + 1] == value)

print(count)
