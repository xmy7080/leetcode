#lt solution using two heap, difference between two version is, latest one actually pushed in a tuple in lo heap
#cause in python we need reverse all number in min heap to form a max heap
from heapq import heapify,heappush,heappop
class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.lo = [] #max heap
        self.hi = [] #min heap
        heapify(self.lo)
        heapify(self.hi)
        

    def addNum(self, num: int) -> None:
        heappush(self.lo, (-num, num))
        heappush(self.hi, heappop(self.lo)[1])
        
        while len(self.lo) < len(self.hi):
            minInHi = heappop(self.hi)
            heappush(self.lo, (-minInHi, minInHi))

    def findMedian(self) -> float:
        if len(self.lo) > len(self.hi): 
            return self.lo[0][1] 
        else:
            return (self.lo[0][1] + self.hi[0]) * 0.5
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
#============
#old version
class MedianFinder(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.minh, self.maxh, self.total = [], [], 0
        heapq.heapify(self.minh)
        heapq.heapify(self.maxh)

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        # self.total += 1
        heapq.heappush(self.maxh, num)
        heapq.heappush(self.minh, - heapq.heappop(self.maxh))
        if len(self.minh) > len(self.maxh):
            heapq.heappush(self.maxh, - heapq.heappop(self.minh))

    def findMedian(self):
        """
        :rtype: float
        """
        if len(self.maxh) > len(self.minh):
            return self.maxh[0]
        else:
            return (self.maxh[0] - self.minh[0])/2.0
        
