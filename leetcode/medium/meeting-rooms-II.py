class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:

        start_time = sorted(intervals, key=lambda interval: interval[0])
        end_time = sorted(intervals, key=lambda interval: interval[1])

        start = end = 0
        rooms = 0

        while start < len(intervals) and end < len(intervals):
            if start_time[start][0] >= end_time[end][1]:
                rooms -= 1
                end += 1

            start += 1
            rooms += 1

        return rooms
