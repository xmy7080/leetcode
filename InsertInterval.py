#way easier solution to reason about and implement
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]
        insS, insE = newInterval[0], newInterval[1]
        ends, starts = [itv[1] for itv in intervals], [itv[0] for itv in intervals]
        #for example like [[1,2],[3,5],[6,7],[8,10],[12,16]] and [4,8]
        #idea is to find [3,5] and [8, 10] as first end larger than 4, and last start that smaller than 8, then remove all intervals in between, form a new merged interval
        
        #find [3,5]
        l = bisect.bisect_left(ends, insS)
        
        #find [8,10], for -1 explain, see https://www.geeksforgeeks.org/bisect-algorithm-functions-in-python/
        r = bisect.bisect(starts, insE) -1
        
        #check if l, r is inbound
        newS = min(intervals[l][0], insS) if l < len(intervals) else insS
        newE = max(intervals[r][1], insE) if r >= 0 else insE
        return intervals[:l] + [[newS, newE]] + intervals[r+1:]

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
