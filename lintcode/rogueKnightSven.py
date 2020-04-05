#jiuzhang lesson 7, similar to frog jump game, time O(n^2 * m)
class Solution:
    """
    @param n: the max identifier of planet.
    @param m: gold coins that Sven has.
    @param limit: the max difference.
    @param cost: the number of gold coins that reaching the planet j through the portal costs.
    @return: return the number of ways he can reach the planet n through the portal.
    """
    def getNumberOfWays(self, n, m, limit, cost):
        dp = [[0] * (m+1) for _ in xrange(n+1)]
        #very beginning, on planet 0 and money is unused, 1 way
        dp[0][m] = 1
        
        for i in xrange(1, n+1):
            for j in xrange(m+1):
                for k in xrange(i-limit, i):
                    if k >= 0 and cost[i] + j <= m:
                        dp[i][j] += dp[k][cost[i] + j]
        #results are all cases that reached planet n with at least 0 coins, no negative
        return sum(dp[n])

#optimized way, using range sum to minimize the time to O(nm)
class Solution:
    """
    @param n: the max identifier of planet.
    @param m: gold coins that Sven has.
    @param limit: the max difference.
    @param cost: the number of gold coins that reaching the planet j through the portal costs.
    @return: return the number of ways he can reach the planet n through the portal.
    """
    def getNumberOfWays(self, n, m, limit, cost):
        dp = [[0] * (m+1) for _ in xrange(n+1)]
        sm = [[0] * (m+1) for _ in xrange(n+1)]
        #very beginning, on planet 0 and money is unused, 1 way
        dp[0][m] = 1
        sm[0][m] = 1
        
        for i in xrange(1, n+1):
            for j in xrange(m+1):
                sm[i][j] = sm[i-1][j]
                #also here we can pre-eliminate the cases when impossible to have over m coins
                if cost[i] + j > m:
                    continue
                dp[i][j] = sm[i-1][cost[i] + j]
                #check if the range sum( i-limit, i-1) hit sum(0, i-1)
                #if not, need remove the upfront sum(0, i -limit -1)
                if i - limit -1 >= 0:
                    dp[i][j] -= sm[i - limit - 1][cost[i] + j]
                sm[i][j] += dp[i][j]
        
        return sum(dp[n])
