class Solution:
    """
    @param m: An integer m denotes the size of a backpack
    @param A: Given n items with size A[i]
    @param V: Given n items with value V[i]
    @return: The maximum value
    """
    def backPackII(self, m, A, V):
        if not A or not V: return 0
        n = len(A)
        dp = [[-1] * (m+1) for i in xrange(n+1)]
        dp[0][0] = 0
        
        for i in xrange(1, n+1):
            for w in xrange(0, m+1):
                dp[i][w] = dp[i-1][w]
                if w >= A[i-1] and dp[i-1][w - A[i-1]] != -1:
                    dp[i][w] = max(dp[i][w], dp[i-1][w - A[i-1]] + V[i-1])
        
        
        ans = -1
        while m >= 0:
            ans = max(ans, dp[n][m])
            m -= 1
        return ans
