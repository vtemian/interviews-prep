from copy import deepcopy


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board:
            return False

        if not word:
            return False

        zero_visited = []
        n = len(board[0])
        for _ in board:
            zero_visited.append([0] * n)

        visited = zero_visited

        def dfs(l_idx, c_idx, depth):
            nonlocal visited

            if (l_idx >= 0 and c_idx >= 0 and l_idx < len(board) and c_idx < len(board[0])
                 and word[depth] == board[l_idx][c_idx] and not visited[l_idx][c_idx]):

                visited[l_idx][c_idx] = 1
                if depth + 1 == len(word):
                    return True

                if dfs(l_idx - 1, c_idx, depth + 1):
                    return True

                if dfs(l_idx + 1, c_idx, depth + 1):
                    return True

                if dfs(l_idx, c_idx - 1, depth + 1):
                    return True

                if dfs(l_idx, c_idx + 1, depth + 1):
                    return True

                visited[l_idx][c_idx] = 0

            return False

        for l_idx, line in enumerate(board):
            for c_idx, value in enumerate(line):
                if value == word[0]:
                    if dfs(l_idx, c_idx, 0):
                        return True

        return False
