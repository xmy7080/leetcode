#  jiuzhang lesson 7, before optimized way
class Solution:
    """
    @param k1: The coefficient of A
    @param k2: The  coefficient of B
    @param c: The volume of backpack
    @param n: The amount of A
    @param m: The amount of B
    @param a: The volume of A
    @param b: The volume of B
    @return: Return the max value you can get
    """
    def getMaxValue(self, k1, k2, c, n, m, a, b):
        if not c: return 0
        #dp[0 - n][0 - m]
        dp = [[0] * (m+1) for _ in xrange(n+1)]
        a.sort()
        b.sort()
        suma = [0] * (n+1)
        sumb = [0] * (m+1)
        #suma, sumb[k] means total sum from 0 to k th item
        
        for i in xrange(1, n+1):
            suma[i] = suma[i-1] + a[i-1]
        for j in xrange(1, m+1):
            sumb[j] = sumb[j-1] + b[j-1]
        
        for i in xrange(n+1):
            for j in xrange(m+1):
                if i == 0 and j == 0:
                    continue
                if i == 0 and c - sumb[j] > 0:
                    dp[i][j] = dp[i][j-1] + k2* (c - sumb[j])
                elif j == 0 and c - suma[i] > 0:
                    dp[i][j] = dp[i-1][j] + k1* (c - suma[i])
                elif c - suma[i] - sumb[j] >= 0:
                    dp[i][j] = max(dp[i-1][j] + k1*(c - suma[i] - sumb[j]), dp[i][j-1] + k2*(c - suma[i] - sumb[j]) )
        return max(x for row in dp for x in row)
