#=====O(n^2) time, lintcode will time out but leetcode won't=====
#solution explain https://leetcode.com/articles/russian-doll-envelopes/
class Solution(object):
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        e = envelopes
        if not e: return 0
        e.sort(key=lambda x: (x[0], -x[1]))
        dp = [0] * len(e)
        for i in xrange(len(e)):
            dp[i] = 1
            for j in xrange(i):
                if e[i][1] > e[j][1]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)
