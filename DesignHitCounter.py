class HitCounter(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.arr = [(0,0)]*300#first ele is the stamp, second is the number of hit
        

    def hit(self, timestamp):
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: void
        """
        moded = timestamp%300
        if timestamp == self.arr[moded][0]:
            self.arr[moded] = (timestamp, self.arr[moded][1]+1)
        else:
            self.arr[moded] = (timestamp,1)
        

    def getHits(self, timestamp):
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: int
        """
        sum = 0
        for tple in self.arr:
            if tple[0]<=timestamp-300:
                continue
            else:
                sum += tple[1]
        return sum


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)