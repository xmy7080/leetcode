#======sort the intervals, then compare adjacent pairs, cause if A[0] not overlap with A[1], it cannot overlap with A[2]..3 4 5
class Solution(object):
    def canAttendMeetings(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: bool
        """
        def isOverlap(a, b):
            return not (a[0] >= b[1] or a[1] <= b[0])
        intervals.sort(key = lambda x: x[0])
        for i in xrange(len(intervals)-1):
            if isOverlap(intervals[i], intervals[i+1]):
                return False
        return True
#=========
# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

#====another approach, two pointers====
class Solution(object):
    def canAttendMeetings(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: bool
        """
        if len(intervals) == 0:
            return True
        transp = map(list, zip(*intervals))
        starts, ends = sorted(transp[0]), sorted(transp[1])
        s, e = 0, 0
        overlap = 0
        while s < len(intervals) and e < len(intervals):
            if starts[s] < ends[e]:
                overlap += 1
                s += 1
            else:
                overlap -= 1
                e += 1
            if overlap >1:
                return False
        return True
        
        
        #=====N^2 approach, too slow===
        
class Solution(object):
    def canAttendMeetings(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: bool
        """
        #input check
        if not intervals: return True
        #sort by starting point
        intervals = sorted(intervals, cmp = lambda x,y:x.start-y.start)
        #loop for 1 and 2, 2 and 3, etc..
        #anything overlapped, return False
        start, end = intervals[0].start, intervals[0].end
        for i in xrange(1,len(intervals)):#intervals[1] to ... intervals[length-1]
            itv = intervals[i]
            if itv.start < end:
                return False
            else:
                start, end  = itv.start, itv.end
        return True
        
#divide and conqur(not the ideal solution)
# # Definition for an interval.
# # class Interval(object):
# #     def __init__(self, s=0, e=0):
# #         self.start = s
# #         self.end = e

# class Solution(object):
#     def canAttendMeetings(self, intervals):
#         """
#         :type intervals: List[Interval]
#         :rtype: bool
#         """
        
#         #sort part
#         intervals = sorted(intervals,cmp = lambda x,y: x[0] - y[0])
#         #divide and conqur
#         return self.dAndc(intervals)
    
#     def dAndc(self,intervals):
#         #size check: 0 or 1 list or 2 lists, or more
#         #0
#         #1
#         #2
#         #over 2
#         mid = len(intervals)/2
#         pivot = intervals[mid]
#         #divide
#         i = 0
#         while i < len(intervals):
#             if i == mid: continue
#             #comparing
#             meeting = intervals[i]
#             if self.isOverlap(pivot, meeting):
#                 return False
#             i+= 1
#         return self.dAndc(intervals[:mid]) and self.dAndc(intervals[mid+1:])
        
#     def isOverlap(self,m1,m2)
    
