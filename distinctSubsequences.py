#jiuzhang dp two sequence solution, homework for lesson 6
class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        #rolling array
        m, n = len(s), len(t)
        dp = [[0] * (n+1) for _ in xrange(2)]
        dp[0][0] = 1
        old, new = 0, 0
        for i in xrange(1, m+1):
            old = new
            new = 1 - new
            for j in xrange(n+1):
                #i th char not used for j th char
                dp[new][j] = dp[old][j]
                #need check j >0 because in python d[-1] will return the last char instead of throw out of bound
                if j > 0 and s[i-1] == t[j-1]:
                    dp[new][j] += dp[old][j-1]
        return dp[new][n]
    
        # m, n = len(s), len(t)
        # dp = [[0] * (n+1) for _ in xrange(m+1)]
        # dp[0][0] = 1
        # for i in xrange(1, m+1):
        #     for j in xrange(n+1):
        #         #i th char not used for j th char
        #         dp[i][j] = dp[i-1][j]
        #         #need check j >0 because in python d[-1] will return the last char instead of throw out of bound
        #         if j > 0 and s[i-1] == t[j-1]:
        #             dp[i][j] += dp[i-1][j-1]
        # return dp[m][n]
