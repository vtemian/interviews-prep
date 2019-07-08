class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        columns = [
            set() for _ in range(9)
        ]
        grid = []
        for l in range(3):
            g = []
            for x in range(3):
                g.append(set())
            grid.append(g)

        lines = [
            set() for _ in range(9)
        ]

        for l_idx, line in enumerate(board):
            for c_idx, value in enumerate(line):
                if value == '.':
                    continue

                if value in columns[c_idx]:
                    return False
                columns[c_idx].add(value)

                if value in lines[l_idx]:
                    return False
                lines[l_idx].add(value)

                if value in grid[l_idx // 3][c_idx // 3]:
                    return False
                grid[l_idx // 3][c_idx // 3].add(value)

        return True
