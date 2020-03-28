#====pay attention to the rolling array detail, new always stays at the last updated row
class Solution:
    """
    @param m: An integer m denotes the size of a backpack
    @param A: Given n items with size A[i]
    @return: The maximum size
    """
    def backPack(self, m, A):
        # write your code here
        if not A or not m: return 0
        dp = [[False] * (m+1) for i in [0,1] ]
        old, new  = 0, 0
        dp[old][0] = True
        # dp[new][0] = True
        for i in xrange(len(A)):
        #gotcha point, new always stays at the last updated row
            old = new
            new = 1- new
            for w in xrange(0, m+1):
                #do not take i th item, weight inherit from old
                dp[new][w] = dp[old][w]
                if w >= A[i]:
                    #when targeting weight is bigger equals i th item, we can have the option take it
                    dp[new][w] = dp[new][w] or dp[old][w - A[i]]
        
        while m >=0:
            if dp[new][m]: return m
            else: m -= 1
        return 0
