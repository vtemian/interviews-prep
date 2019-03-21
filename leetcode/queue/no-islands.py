class Solution:
    def numIslands(self, grid: 'List[List[str]]') -> 'int':
        if not grid:
            return 0

        no_lines = len(grid)
        no_cols = len(grid[0])

        def solve(line_idx, col_idx):
            grid[line_idx][col_idx] = '-1'
            queue = [(line_idx, col_idx)]
            idx = 0

            while idx < len(queue):
                land_x, land_y = queue[idx]
                idx += 1

                if land_x + 1 < no_lines and grid[land_x + 1][land_y] == '1':
                    grid[land_x + 1][land_y] = '-1'
                    queue.append((land_x + 1, land_y))

                if land_x - 1 >= 0 and grid[land_x - 1][land_y] == '1':
                    grid[land_x - 1][land_y] = '-1'
                    queue.append((land_x - 1, land_y))

                if land_y + 1 < no_cols and grid[land_x][land_y + 1] == '1':
                    grid[land_x][land_y + 1] = '-1'
                    queue.append((land_x, land_y + 1))

                if land_y - 1 >= 0 and grid[land_x][land_y - 1] == '1':
                    grid[land_x][land_y - 1] = '-1'
                    queue.append((land_x, land_y - 1))

        count = 0

        for line_idx, line in enumerate(grid):
            for col_idx, value in enumerate(line):
                if grid[line_idx][col_idx] != '1':
                    continue
                count += 1
                solve(line_idx, col_idx)

        return count
