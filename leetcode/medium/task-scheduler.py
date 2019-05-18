from collections import Counter


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if not tasks:
            return 0

        tasks = list(Counter(tasks).values())
        tasks.sort(reverse=True)
        result = 0

        while tasks[0] > 0:
            current = 0

            while current <= n:
                if tasks[0] == 0:
                    break

                if current< len(tasks):
                    tasks[current] -= 1

                result += 1
                current += 1

            tasks.sort(reverse=True)

        return result
