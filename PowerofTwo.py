class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        ones = 0
        while n >0:
            ones += n &1
            n = n >>1
        return ones == 1