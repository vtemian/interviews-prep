"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]], start_l: int = 0, start_c: int = 0, end_l: int = -1, end_c: int = -1) -> 'Node':
        if not grid:
            return None

        if end_l == -1:
            end_l = len(grid)

        if end_c == -1:
            end_c = len(grid[0])

        def is_complete(grid, start_l, start_c, end_l, end_c):
            be_same = grid[start_l][start_c]

            for line in grid[start_l: end_l]:
                for value in line[start_c: end_c]:
                    if value != be_same:
                        return False
            return True

        n = len(grid)
        m = len(grid[0])

        if not is_complete(grid, start_l, start_c, end_l, end_c):
            delta = (end_c - start_c) // 2

            top_left = self.construct(grid, start_l, start_c, start_l + delta, start_c + delta)

            top_right = self.construct(grid, start_l, start_c + delta, start_l + delta, end_c)

            bottom_left = self.construct(grid, start_l + delta, start_c, end_l, start_c + delta)

            bottom_right = self.construct(grid, start_l + delta, start_c + delta, end_l, end_c)

            return Node(top_left.val or top_right.val or bottom_left.val or bottom_right.val, False, 
                        top_left, top_right, bottom_left, bottom_right)

        return Node(bool(grid[start_l][start_c]), True, None, None, None, None)
