class Solution:
    def imageSmoother(self, M: List[List[int]]) -> List[List[int]]:
        result = []

        for i, line in enumerate(M):
            new_line = []

            for j, value in enumerate(line):
                grayscale = [value]

                if i > 0:
                    grayscale.append(M[i - 1][j])

                    if j + 1 < len(line):
                        grayscale.append(M[i - 1][j + 1])

                    if j > 0:
                        grayscale.append(M[i - 1][j - 1])

                if i + 1 < len(M):
                    grayscale.append(M[i + 1][j])

                    if j + 1 < len(line):
                        grayscale.append(M[i + 1][j + 1])

                    if j > 0:
                        grayscale.append(M[i + 1][j - 1])

                if j > 0:
                    grayscale.append(M[i][j - 1])

                if j + 1 < len(line):
                    grayscale.append(M[i][j + 1])

                new_line.append(sum(grayscale) // len(grayscale))

            result.append(new_line)

        return result
