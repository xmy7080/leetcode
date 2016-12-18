# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        if not intervals:return [newInterval]
        res = []
        start, end = newInterval.start, newInterval.end
        overlaping = False  #do overlaping happening?
        overlaped = False   #did overlap happened at all?
        for itv in intervals:
            s, e = itv.start, itv.end
            if not (end<s or start>e):
                overlaping = True
                overlaped = True
                #when new introduced(included emerged intervals) overlap with an exist one
                start = s if s<start else start #update emerged interval start
                end = e if e>end else end #update emerged interval end
                continue
            elif overlaping:
                #when overlap happened, store the first non-overlap interval, and set overlap is false
                res.append([start,end])
                overlaping = False
            if end < s and not overlaped:#if insert [2,3] into [4,6], no overlap will happen, 
                #insert new interval
                res.append([start,end])
                #and we are done with the overlaped bool, set it to true
                overlaped = True
            res.append([s,e])
        if overlaping:#overlaping still not end, say insert [3,7] into [1,4],
            res.append([start,end])
        if not overlaped:#if insert [9,10] into [2,3], new itv will be at the end, append it.
            res.append([start,end])
        return res