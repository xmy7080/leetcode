#===same approach as stock iii, which was when k == 2===
#pay attention to do 2*k instead of 2k
#also, when 2*k > lenth, it's equivalent to stock ii, you can make as many as transactions you want
class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        if not prices: return 0
        if 2*k > len(prices):
            ans = 0
            for i in xrange(1, len(prices)):
                if prices[i] > prices[i-1]:
                    ans += prices[i] - prices[i-1]
            return ans
        
        dp = [[0] * (2*k+2) for i in xrange(len(prices)+1)]
        
        for i in xrange(1, len(prices)+1):
            #phase 1,3,5...2k+1
            for j in xrange(1, 2*k+2, 2):
                dp[i][j] = dp[i-1][j] #case keep prev day state
                if i >1 and j > 1:
                    #case start new state, need add prev day gain. also prices[i-1] is the price on day i, cause i started at 1
                    dp[i][j] = max(dp[i][j], dp[i-1][j-1] + prices[i-1] - prices[i-2])
            
            #phase 2,4,...2k
            for j in xrange(2, 2*k+1, 2):
                dp[i][j] = dp[i-1][j-1] #case just start new state, no gain yet
                if i >1:
                    #case keep prev state, accumualating gain every day
                    dp[i][j] = max(dp[i][j], dp[i-1][j] + prices[i-1] - prices[i-2]) 
        ans = 0
        for i in xrange(3, 2*k+2, 2):
            ans = max(ans, dp[len(prices)][i])
        return ans
