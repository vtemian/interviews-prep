from heapq import heappush, heappop
from typing import List


class Point:
    def __init__(self, x: int, y: int, z: int):
        self.x = x
        self.y = y
        self.z = z

    @property
    def distance(self) -> int:
        return -(self.x ** 2 + self.y ** 2 + self.z ** 2)

    def __eq__(self, friend: 'Point'):
        return self.distance == friend.distance

    def __lt__(self, friend: 'Point'):
        return self.distance < friend.distance

    def __gt__(self, friend: 'Point'):
        return self.distance > friend.distance

    def __repr__(self) -> str:
        return f"{{{self.x} {self.y}, {self.z}}}"


def k_closest(k: int, points: List[Point]) -> List[Point]:
    heap = []

    for point in points:
        heappush(heap, point)

        if k <= 0:
            heappop(heap)
            continue

        k -= 1

    return heap


points = [
    Point(*xyz)
    for xyz in [(0, 0, 0), (1, 2, 3), (10, 10, 1), (2, 2, 2), (5, 5, 5)]
]
result = k_closest(2, points)
assert result == [Point(2, 2, 2), Point(0, 0, 0)], result
