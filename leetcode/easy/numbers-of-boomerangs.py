class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        result = 0
        idx = 0

        def distance(x, y):
            return (x[0] - y[0]) ** 2 + (x[1] - y[1]) ** 2

        for idx, point in enumerate(points):
            distances = {}

            for j, second in enumerate(points):
                if idx == j:
                    continue

                d = distance(point, second)
                if d not in distances:
                    distances[d] = 0
                distances[d] += 1

            for d in distances.values():
                result += d * (d - 1)

        return result
