from copy import deepcopy


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        def backtrack(solution, target):
            nonlocal result

            if target < 0:
                return

            if target == 0:
                solution.sort()
                if solution not in result:
                    result.append(solution)

            for candidate in candidates:
                if target - candidate < 0:
                    continue

                s = deepcopy(solution)
                s.append(candidate)
                backtrack(s, target - candidate)

        backtrack([], target)

        return result
