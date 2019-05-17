class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        for l_i, line in enumerate(board):
            for c_i, value in enumerate(line):
                alive = []
                deads = []

                if c_i > 0:
                    if board[l_i][c_i - 1] == 0 or board[l_i][c_i - 1] == 2:
                        deads.append(board[l_i][c_i - 1])
                    else:
                        alive.append(board[l_i][c_i - 1])

                if c_i + 1 < len(line):
                    if board[l_i][c_i + 1] == 0 or board[l_i][c_i + 1] == 2:
                        deads.append(board[l_i][c_i + 1])
                    else:
                        alive.append(board[l_i][c_i + 1])

                if l_i > 0:

                    if board[l_i - 1][c_i] == 0 or board[l_i - 1][c_i] == 2:
                        deads.append(board[l_i - 1][c_i])
                    else:
                        alive.append(board[l_i - 1][c_i])

                    if c_i > 0:
                        if board[l_i - 1][c_i - 1] == 0 or board[l_i - 1][c_i - 1] == 2:
                            deads.append(board[l_i - 1][c_i - 1])
                        else:
                            alive.append(board[l_i - 1][c_i - 1])

                    if c_i + 1 < len(line):
                        if board[l_i - 1][c_i + 1] == 0 or board[l_i - 1][c_i + 1] == 2:
                            deads.append(board[l_i - 1][c_i + 1])
                        else:
                            alive.append(board[l_i - 1][c_i + 1])

                if l_i + 1 < len(board):
                    if board[l_i + 1][c_i] == 0 or board[l_i + 1][c_i] == 2:
                        deads.append(board[l_i + 1][c_i])
                    else:
                        alive.append(board[l_i + 1][c_i])

                    if c_i > 0:
                        if board[l_i + 1][c_i - 1] == 0 or board[l_i + 1][c_i - 1] == 2:
                            deads.append(board[l_i + 1][c_i - 1])
                        else:
                            alive.append(board[l_i + 1][c_i - 1])

                    if c_i + 1 < len(line):
                        if board[l_i + 1][c_i + 1] == 0 or board[l_i + 1][c_i + 1] == 2:
                            deads.append(board[l_i + 1][c_i + 1])
                        else:
                            alive.append(board[l_i + 1][c_i + 1])

                if value == 1 and (len(alive) < 2 or len(alive) > 3):
                    board[l_i][c_i] = -1

                if value == 0 and len(alive) == 3:
                    board[l_i][c_i] = 2

        for l_i, line in enumerate(board):
            for c_i, value in enumerate(line):
                if value == 2:
                     board[l_i][c_i] = 1
                elif value == -1:
                     board[l_i][c_i] = 0
