class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        stack = []
        result = [0] * len(T)

        for idx, t in enumerate(T):
            while stack and T[stack[-1]] < t:
                prev_idx = stack.pop()
                result[prev_idx] = idx - prev_idx

            stack.append(idx)

        return result
