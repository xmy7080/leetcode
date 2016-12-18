# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        intervals = sorted(intervals,key=lambda x:x.start)
        heap = []
        for i in intervals:
            if heap and i.start >= heap[0]:#new meeing can fit in the earliest free room
                heapq.heapreplace(heap,i.end)
            else:#cannot fit in, we allocate a new room
                heapq.heappush(heap,i.end)
        return len(heap)
                
        