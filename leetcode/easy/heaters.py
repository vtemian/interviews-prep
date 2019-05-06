class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        heaters.sort()
        houses.sort()

        result = 0

        """288ms

        def bs(house):
            nonlocal heaters

            start = 0
            end = len(heaters) - 1

            while start <= end:
                mid = (start + end) // 2

                if heaters[mid] == house:
                    return mid

                if heaters[mid] > house:
                    end = mid - 1
                else:
                    start = mid + 1

            if end < 0:
                return 0

            if start > len(heaters) - 1:
                return len(heaters) - 1

            if abs(heaters[start] - house) < abs(heaters[end] - house):
                return start
            return end

        for house in houses:
            idx = bs(house)
            result = max(result, abs(heaters[idx] - house))
        """

        idx = 0
        heaters = [float('-inf')] + heaters + [float('inf')]

        for house in houses:
            while house > heaters[idx]:
                idx += 1

            distance = min(house - heaters[idx - 1], heaters[idx] - house)
            if distance > result:
                result = distance

        return result
