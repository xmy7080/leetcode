class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n<0:
            x = 1/x
            n = -n
            
        res = 1
        while n:
            if n & 1:
                res *= x
                n -= 1
            else:
                x *= x
                n >>= 1
        return res
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # if n <0:
        #     n = -n
        #     x = 1/x
        # pow = 1
        # while n:
        #     if n & 1:
        #         pow *= x
        #     x *= x
        #     n >>= 1
        # return pow