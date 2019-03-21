class Solution:
    def openLock(self, deadends: 'List[str]', target: 'str') -> 'int':
        queue = [("0000", 0)]
        deadends = set(deadends)
        visited = {}

        while queue:
            solution, level = queue.pop()

            if solution in deadends or solution in visited:
                continue

            if solution == target:
                return level




