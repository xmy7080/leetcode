# O(n^ 3/2) time complexity, O(n) space, quite slow
#dp with partition type
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0] + [sys.maxint] * n
        for i in xrange(n+1):
            j = 1
            while j*j <= n:
                dp[i] = min(dp[i], dp[i- j*j] + 1)
                j += 1
        return dp[n]
