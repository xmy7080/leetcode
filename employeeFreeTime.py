"""
# Definition for an Interval.
class Interval(object):
    def __init__(self, start=None, end=None):
        self.start = start
        self.end = end
"""

class Solution(object):
    def employeeFreeTime(self, schedule):
        """
        :type schedule: [[Interval]]
        :rtype: [Interval]
        """
        events = []
        for emp in schedule:
            for itv in emp:#nuance here is we need open marked as 0 while close marked as 1
                #hence if two timestamp came in, (5, start) will always be ahead of (5,end)
                #in this way, the (5, 5) interval can be eliminated.
                events.append((itv.start, 0))
                events.append((itv.end, 1))
        
        events.sort()
        ans = []
        prev = None
        count = 0
        for t, mark in events:
            if not count and prev is not None and prev != t:
                ans.append(Interval(prev, t))
            count += 1 if not mark else -1
            prev = t
        return ans
        
