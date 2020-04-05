#jiuzhang lesson 7, similar to frog jump game
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
