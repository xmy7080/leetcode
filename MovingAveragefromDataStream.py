class MovingAverage(object):

    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.size = size
        self.deque = collections.deque()
        self.total = 0
        

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        out = 0
        if len(self.deque) == self.size:
            out = self.deque.popleft()
        self.total += val - out
        self.deque.append(val)
        return self.total*1.0/len(self.deque)
            


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)