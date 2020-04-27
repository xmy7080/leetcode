#https://leetcode.com/articles/logger-rate-limiter/
#this is the implementation of queue and set, also we should using hashtable to do it in O(1) time
class Logger(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.msgs = set()
        self.que = collections.deque()
        

    def shouldPrintMessage(self, timestamp, message):
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        :type timestamp: int
        :type message: str
        :rtype: bool
        """
        while self.que:
            msg, ts = self.que[0]
            if timestamp - ts >= 10:
                self.que.popleft()
                self.msgs.remove(msg)
            else:
                break
        if message not in self.msgs:
            self.que.append((message, timestamp) )
            self.msgs.add(message)
            return True
        else:
            return False
        


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)
