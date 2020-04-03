#jiuzhang example solution, 2 d backpack problem
class Solution(object):
    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """
        ns= len(strs)
        #dp[i][j][k] is for the i front strs, how many possible str can j 0s and k 1s form
        dp = [[[0] * (n+1) for _ in xrange(m+1)] for _ in xrange(ns+1)]
        for i in xrange(1, ns+1):
            zeros, ones = strs[i-1].count('0'), strs[i-1].count('1')
            for j in xrange(m+1):
                for k in xrange(n +1):
                    #if strs[i-1] not be in our backpack
                    dp[i][j][k] = dp[i-1][j][k]
                    
                    if j >= zeros and k >= ones:
                        dp[i][j][k] = max(dp[i][j][k], dp[i-1][j-zeros][k-ones] + 1)
        
        return max(x for row in dp[ns] for x in row)
