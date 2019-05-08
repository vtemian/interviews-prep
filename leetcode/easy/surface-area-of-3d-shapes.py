class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        result = 0

        for line_idx, line in enumerate(grid):
            for col_idx, value in enumerate(line):
                if not value:
                    continue

                if line_idx == 0:
                    result += value
                else:
                    if value > grid[line_idx - 1][col_idx]:
                        result += value - grid[line_idx - 1][col_idx]

                if line_idx == len(grid) - 1:
                    result += value
                else:
                    if value > grid[line_idx + 1][col_idx]:
                        result += value - grid[line_idx + 1][col_idx]

                if col_idx == 0:
                    result += value
                else:
                    if value > grid[line_idx][col_idx - 1]:
                        result += value - grid[line_idx][col_idx - 1]

                if col_idx == len(line) - 1:
                    result += value
                else:
                    if value > grid[line_idx][col_idx + 1]:
                        result += value - grid[line_idx][col_idx + 1]

                result += 2

        return result
