class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return intervals

        intervals.sort(key=lambda interval: interval[0])

        result = []
        current = []

        for interval in intervals:
            if not current:
                current = interval
                continue

            if interval[0] <= current[1]:
                current[1] = max(interval[1], current[1])
            else:
                result.append(current)
                current = interval

        if current:
            result.append(current)

        return result
