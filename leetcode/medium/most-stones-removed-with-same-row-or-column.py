from collections import defaultdict


class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        graph = defaultdict(list)

        for idx, x in enumerate(stones):
            for j in range(idx):
                y = stones[j]

                if x[0] == y[0] or x[1] == y[1]:
                    graph[idx].append(j)
                    graph[j].append(idx)


        seen = [False] * len(stones)
        result = 0

        for stone in range(len(stones)):
            if seen[stone]:
                continue

            stack = [stone]
            seen[stone] = True

            while stack:
                node = stack.pop()
                result += 1

                for n in graph[node]:
                    if not seen[n]:
                        stack.append(n)
                        seen[n] = True
            result -= 1

        return result
