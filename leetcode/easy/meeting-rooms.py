class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals = sorted(intervals)

        start = 0
        while start < len(intervals) - 1:
            if intervals[start][1] > intervals[start + 1][0]:
                return False

            start += 1

        return True
