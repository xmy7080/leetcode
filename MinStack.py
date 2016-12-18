import sys
class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stk = []
        

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        if not self.stk:
            self.stk.append([x,x])
            return
        [top,min] = self.stk[-1]
        if min>x:
            min = x
        self.stk.append([x,min])
        

    def pop(self):
        """
        :rtype: void
        """
        [res,min] = self.stk.pop()
        return res
        

    def top(self):
        """
        :rtype: int
        """
        [res,min] = self.stk[-1]
        return res
        
        

    def getMin(self):
        """
        :rtype: int
        """
        [res,min] = self.stk[-1]
        return min
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()