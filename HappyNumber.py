class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        s = set()
        t = n
        while t not in s:
            s.add(t)
            t = self.happy(t)
        return t==1
        
    def happy(self,n):
        sum = 0
        while n >0:
            digit = n % 10
            sum += digit * digit
            n = n / 10
        return sum