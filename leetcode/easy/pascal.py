class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if not numRows:
            return []

        result = [[1]]

        if numRows == 1:
            return result

        result = [[1], [1, 1]]
        if numRows == 2:
            return result

        numRows -= 2
        start = 2
        while numRows:
            prev = result[start - 1]

            idx = 1
            line = [1]

            while idx < len(prev):
                line.append(prev[idx] + prev[idx - 1])
                idx += 1

            line.append(1)
            result.append(line)

            start += 1
            numRows -= 1

        return result
