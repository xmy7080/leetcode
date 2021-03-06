#======boxed the isOverlap and merge function together, to make reasoning easier=====
class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        def isOverlap(A, B):
            return not (A[0] > B[1] or A[1] < B[0])
        def merge(A, B):
            return [min(A[0], B[0]), max(A[1], B[1])]
        
        if not intervals:
            return []
        intervals.sort(key = lambda x: (x[0]))
        ans = []
        l = len(intervals)
        i = 0
        while i < l:
            j = i+1
            tmp = intervals[i]
            while j < l and isOverlap(tmp, intervals[j]):
                tmp = merge(tmp, intervals[j])
                j += 1
            ans.append(tmp)
            i = j
        return ans
#================
# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if not intervals:
            return []
        intervals = sorted(intervals, key = lambda x:x.start)
        news, newe = intervals[0].start, intervals[0].end
        res = []
        for (i, itv) in enumerate(intervals,1):
            if itv.start <= newe:
                newe = newe if newe > itv.end else itv.end
            else:
                res.append([news,newe])
                news, newe = itv.start, itv.end
        res.append([news,newe])
        return res
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # #check input
        # l = len(intervals)
        # if l <= 1: return intervals
        # #sort
        # intervals = sorted(intervals, cmp=lambda x,y: x.start - y.start)
        # #set base interval
        # start, end = intervals[0].start, intervals[0].end
        # #start loop
        # res = []
        # for i in xrange(1,l):
        #     #if it has overlap, update the end
        #     if end >= intervals[i].start:
        #         end = intervals[i].end if intervals[i].end > end else end
        #     else:#if doesn't overlap, save curr intv to res, update start and end
        #         res.append(Interval(start,end))
        #         start, end  = intervals[i].start, intervals[i].end
        # res.append(Interval(start,end))
        # return res
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # res = []
        # if not intervals: return []
        # intervals = sorted(intervals,cmp = lambda a,b: a.start - b.start)
        # start, end = intervals[0].start,intervals[0].end
        # for itv in intervals:
        #     s, e = itv.start, itv.end
        #     if s <= end:
        #         end = e if e>end else end
        #     else:
        #         res.append([start,end])
        #         start, end = s, e
        # res.append([start,end])
        # return res
