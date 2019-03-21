class Solution:
    def islandPerimeter(self, grid):
        if not grid:
            return 0

        perimeter = 0
        no_lines = len(grid)
        no_columns = len(grid[0])

        for line_idx, line in enumerate(grid):
            for column_idx, land in enumerate(line):
                if not land:
                    continue

                if not (line_idx - 1 >= 0 and grid[line_idx - 1][column_idx] == 1):
                    perimeter += 1

                if not (column_idx - 1 >= 0 and grid[line_idx][column_idx - 1] == 1):
                    perimeter += 1

                if not (line_idx + 1 < no_lines and grid[line_idx + 1][column_idx] == 1):
                    perimeter += 1

                if not (column_idx + 1 < no_columns and grid[line_idx][column_idx + 1] == 1):
                    perimeter += 1

        return perimeter

island = [
    [0,1,0,0],
    [1,1,1,0],
    [0,1,0,0],
    [1,1,0,0]
]
result = Solution().islandPerimeter(island)
print(result)
