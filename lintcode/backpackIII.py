#=====O(nm) time for optimization on dp[i-1][w- k*A[i-1]] to dp[i][w - A[i-1]], used to be O(n*m*m) time
class Solution:
    """
    @param A: an integer array
    @param V: an integer array
    @param m: An integer
    @return: an array
    """
    def backPackIII(self, A, V, m):
        if not A or not V: return 0
        n = len(A)
        dp = [[-1] * (m+1) for i in xrange(n+1)]
        dp[0][0] = 0
        
        for i in xrange(1, n+1):
            for w in xrange(0, m+1):
                dp[i][w] = dp[i-1][w]
                if w >= A[i-1] and dp[i][w - A[i-1]] != -1:
                    dp[i][w] = max(dp[i][w], dp[i][w - A[i-1]] + V[i-1])
        
        
        ans = -1
        while m >= 0:
            if dp[n][m] != -1:
                ans = max(ans, dp[n][m])
            m -= 1
        return ans


#=====single row array optimization, from left to right===
class Solution:
    """
    @param A: an integer array
    @param V: an integer array
    @param m: An integer
    @return: an array
    """
    def backPackIII(self, A, V, m):
        if not A or not V: return 0
        n = len(A)
        dp = [-1] * (m+1)
        dp[0] = 0
        
        for i in xrange(1, n+1):
            for w in xrange(A[i-1], m+1):
                #up old: dp[w]
                #left new: dp[w - A[i-1]]
                if dp[w - A[i-1]] != -1:
                    dp[w] = max(dp[w], dp[w - A[i-1]] + V[i-1])
        
        
        ans = -1
        while m >= 0:
            if dp[m] != -1:
                ans = max(ans, dp[m])
            m -= 1
        return ans
