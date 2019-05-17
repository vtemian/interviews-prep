class Solution:
    def maxArea(self, height: List[int]) -> int:
        if not height:
            return 0

        start = 0
        end = len(height) - 1
        best = 0

        while start < end:
            best = max(best, min(height[start], height[end]) * (end - start))

            if height[start] < height[end]:
                start += 1
            else:
                end -= 1

        return best
