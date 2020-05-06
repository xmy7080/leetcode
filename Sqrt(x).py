#implementation that can return float, percision to 0.01
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: float
        :rtype: float
        """
        if x in (0,1): return x
        e = 0.01
        l, r = float(1), float(x)
        if x <1:
            tmp = r
            r = l
            l = tmp
        while l < r:
            mid = l + (r-l)/2
            if mid < (x - e)/ mid:
                l = mid
            elif mid > (x + e)/ mid:
                r = mid
            else:
                return mid
#leetcode original question, only return integer
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x in (0,1): return x
        l = 1
        h = x
        while True:
            mid = l + (h-l)/2
            if mid > x/mid:
                h = mid -1
            else:
                if mid+1 > x/(mid+1):
                    return mid
                l = mid + 1
                
