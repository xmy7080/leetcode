#jiuzhang example problem, using two sequence dp approach, sixth lesson =====
class Solution(object):
    def longestCommonSubsequence(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        #solution printing out result subsequence
        
        #solution with rolling array
        if not A or not B: return 0
        m, n = len(A), len(B)
        dp = [[0] * (n+1) for _ in xrange(2)]
        old, new = 0, 0
        pi = [[0] * (n+1) for _ in xrange(m+1)]
        for i in xrange(1, m+1):
            old = new
            new = 1-new
            for j in xrange(1, n+1):
                dp[new][j] = max(dp[old][j], dp[new][j-1])
                if dp[new][j] == dp[old][j]:
                    pi[i][j] = 1
                else:
                    pi[i][j] = 2
                if A[i-1] == B[j-1]:
                    dp[new][j] = max(dp[new][j], dp[old][j-1] + 1)
                    if dp[new][j] == dp[old][j-1] + 1:
                        pi[i][j] = 3
        
        ans = [""] * dp[new][n]
        p = dp[new][n] -1
        i,j  = m, n
        while i and j:
            if pi[i][j] == 1:
                #not using A's tail
                i -= 1
            elif pi[i][j] == 2:
                #not using B's tail
                j -= 1
            elif pi[i][j] == 3:
                ans[p] = A[i-1]
                p -= 1
                i -= 1
                j -= 1
        print("\n common subsequence is: " + "".join(ans) )
        return dp[new][n]
        
        #solution with rolling array
        if not A or not B: return 0
        m, n = len(A), len(B)
        dp = [[0] * (n+1) for _ in xrange(2)]
        old, new = 0, 0
        for i in xrange(1, m+1):
            old = new
            new = 1-new
            for j in xrange(1, n+1):
                dp[new][j] = max(dp[old][j], dp[new][j-1])
                if A[i-1] == B[j-1]:
                    dp[new][j] = max(dp[new][j], dp[old][j-1] + 1)
        return dp[new][n]
    
        # solution with m * n matrix
        if not A or not B: return 0
        m, n = len(A), len(B)
        dp = [[0] * (n+1) for _ in xrange(m+1)]
        for i in xrange(1, m+1):
            for j in xrange(1, n+1):
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
                if A[i-1] == B[j-1]:
                    dp[i][j] = max(dp[i][j], dp[i-1][j-1] + 1)
        return dp[m][n]
