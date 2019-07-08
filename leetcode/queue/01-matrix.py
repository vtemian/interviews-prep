class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:

        def get_next(l_idx, c_idx):
            for transform in [
                (1, 0),
                (-1, 0),
                (0, 1),
                (0, -1)
            ]:
                l, c = l_idx + transform[0], c_idx + transform[1]

                if l < len(matrix) and l >= 0 and c < len(matrix[0]) and c >= 0:
                    yield l, c

        queue = [
            ((l_idx, c_idx), 0)
            for c_idx in range(len(matrix[0]))
            for l_idx in range(len(matrix))
            if matrix[l_idx][c_idx] == 0
        ]
        visited = set([
            point
            for point, _ in queue
        ])
        result = [[0] * len(matrix[0]) for _ in matrix]

        while queue:
            (l, c), depth = queue.pop(0)
            result[l][c] = depth

            for n in get_next(l, c):
                if n not in visited:
                    visited.add(n)
                    queue.append((n, depth + 1))

        return result
