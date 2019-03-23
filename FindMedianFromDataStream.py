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
        
