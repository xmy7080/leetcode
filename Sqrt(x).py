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
                