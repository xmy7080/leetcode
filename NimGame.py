#====jiuzhang dp game solution which will timeout===
class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if not n: return False
        elif n in [1,2,3]: return True
        elif n > 10000: return n & 0b11 != 0
        dp = [False] * (n+1)
        dp[1:4] = [True, True, True]
        for i in xrange(4, n +1):
            dp[i] = not dp[i-1] or not dp[i-2] or not dp[i-3]
        return dp[n]
    #======rolling array solution
        if not n: return False
        elif n in [1,2,3]: return True
        elif n > 10000: return n & 0b11 != 0
        dp = [False] * 3
        dp = [True, True, True]
        for i in xrange(4, n +1):
            canWinNextNumber = not dp[0] or not dp[1] or not dp[2]
            dp = dp[1:] + [canWinNextNumber]
        return dp[2]
#====math solution with tricks===
class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n%4 != 0
