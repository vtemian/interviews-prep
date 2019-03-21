class Solution:
    def wallsAndGates(self, rooms: 'List[List[int]]') -> 'None':
        """
        Do not return anything, modify rooms in-place instead.
        """

        if not rooms:
            return

        no_lines = len(rooms)
        no_cols = len(rooms[0])

        queue = []

        for line_idx, line in enumerate(rooms):
            for col_idx, value in enumerate(line):
                if value == 0:
                    queue.append((line_idx, col_idx, 0))

        while queue:
            line_idx, col_idx, value = queue.pop(0)

            if rooms[line_idx][col_idx] < value:
                continue

            rooms[line_idx][col_idx] = value

            if line_idx + 1 < no_lines and rooms[line_idx + 1][col_idx] != -1:
                queue.append((line_idx + 1, col_idx, value + 1))

            if line_idx - 1 > -1 and rooms[line_idx -1][col_idx] != -1:
                queue.append((line_idx - 1, col_idx, value + 1))

            if col_idx - 1 > -1 and rooms[line_idx][col_idx - 1] != -1:
                queue.append((line_idx, col_idx - 1, value + 1))

            if col_idx + 1 < no_cols and rooms[line_idx][col_idx + 1] != -1:
                queue.append((line_idx, col_idx + 1, value + 1))
