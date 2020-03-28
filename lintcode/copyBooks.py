#===python dp partitioning solution, same idea with jiuzhang java solution, but always time exceed===
import sys
class Solution:
    """
    @param pages: an array of integers
    @param k: An integer
    @return: an integer
    """
    def copyBooks(self, A, K):
        if not A: return 0
        lth = len(A)
        
        if K > lth: K = lth
        #dp = new int()[0-K][0-lth]
        dp = [[0] * (lth+1) for i in range(K+1)]
        dp[0] = [0] + [sys.maxint] * lth
        
        # dp[0] = [0] * (lth+1)
        # print("\n dp is look like" + str(dp))
        
        for k in range(1, K+1):
            dp[k][0] = 0
            for i in range(1, lth+1):
                dp[k][i] = sys.maxint
                s = 0
                for j in range(i, -1, -1):
                    if dp[k-1][j] != sys.maxint:
                        # print("\n in "+ str() +"dp[k-1][j] and s is like: "+ str(dp[-1][j]) + " " + str(s))
                        dp[k][i] = min(dp[k][i], max(dp[k-1][j], s))
                    if j > 0:
                        s += A[j-1]
        
        return dp[K][lth]
