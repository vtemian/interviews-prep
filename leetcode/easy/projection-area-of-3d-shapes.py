"""
On a N * N grid, we place some 1 * 1 * 1 cubes that are axis-aligned with the x, y, and z axes.

Each value v = grid[i][j] represents a tower of v cubes placed on top of grid cell (i, j).

Now we view the projection of these cubes onto the xy, yz, and zx planes.

A projection is like a shadow, that maps our 3 dimensional figure to a 2 dimensional plane.

Here, we are viewing the "shadow" when looking at the cubes from the top, the front, and the side.

Return the total area of all three projections.

"""


class Solution:
    def projectionArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        n = 0
        x = 0
        y = []

        for i, line in enumerate(grid):
            x += max(line)

            for j, value in enumerate(line):
                if j < len(y):
                    if value > y[j]:
                        y[j] = value
                else:
                    y.append(value)

                if value:
                    n += 1

        return n + x + sum(y)


result = Solution().projectionArea([[1,0],[0,2]])
print(result)
