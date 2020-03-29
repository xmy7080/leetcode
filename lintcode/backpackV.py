class Solution:
    """
    @param nums: an integer array and all positive numbers
    @param target: An integer
    @return: An integer
    """
    def backPackV(self, A, m):
        # write your code here
        if not A or not m: return 0
        dp = [0] * (m+1)
        dp[0] = 1
        # dp[new][0] = True
        for i in xrange(len(A)):
            #no need to update dp[0-A[i]], cause the furthest w can go is from m+1 to A[i]
            for w in xrange(m, A[i]-1, -1):
                #ultimate rolling array, only 1 dimension and update from right to left
                #since the new status only rely on old up and old up left
                dp[w] += dp[w - A[i]]
        
        return dp[m]
