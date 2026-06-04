"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals: return 0
        intervals.sort(key=lambda x: x.start)
        rooms = [intervals[0].end]
        n = 1
        for i in range(1, len(intervals)):
            if intervals[i].start < rooms[0]:
                heapq.heappush(rooms, intervals[i].end)
                n += 1
            else:
                heapq.heapreplace(rooms, intervals[i].end)
        return n
