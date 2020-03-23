#======dp solution from jiuzhang, set 5 states (before 1st buy, during 1st holding, after 1 st holding but before 2nd buy, during and after 2nd holding
#, and maintain a [n][5] array keep those state==
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices: return 0
        dp = [[0] * 6 for i in xrange(len(prices)+1)]
        
        for i in xrange(1, len(prices)+1):
            #phase 1,3,5, 
            for j in [1,3,5]:
                dp[i][j] = dp[i-1][j] #case keep prev day state
                if i >1 and j > 1:
                    #case start new state, need add prev day gain. also prices[i-1] is the price on day i, cause i started at 1
                    dp[i][j] = max(dp[i][j], dp[i-1][j-1] + prices[i-1] - prices[i-2])
            
            #phase 2,4
            for j in [2,4]:
                dp[i][j] = dp[i-1][j-1] #case just start new state, no gain yet
                if i >1:
                    #case keep prev state, accumualating gain every day
                    dp[i][j] = max(dp[i][j], dp[i-1][j] + prices[i-1] - prices[i-2]) 
        return max(dp[len(prices)][3], dp[len(prices)][5])
#======
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        lowest = prices[0]
        lastday = prices[0]
        mostprofitTrendFromBegin = [0] * len(prices)
        mostprofit = 0
        for i in range(len(prices)):
            today = prices[i]
            if today > lastday and (today - lowest)>mostprofit:
                mostprofit = today - lowest
            if today < lastday and lowest>today:
                lowest = today
            mostprofitTrendFromBegin[i] = mostprofit
            lastday = today
        
        highest = prices[-1]
        tomorrow = prices[-1]
        mostlossTrendFromEnd = [0] * len(prices)
        mostloss = 0
        for i in range(len(prices)-1,-1,-1):
            today = prices[i]
            if today<tomorrow and (highest - today)>mostloss:
                mostloss = highest -today
            if today > tomorrow and highest < today:
                highest = today
            mostlossTrendFromEnd[i] = mostloss
            tomorrow = today
        
        res = 0
        for i in range(len(prices)):
            if res < mostprofitTrendFromBegin[i] + mostlossTrendFromEnd[i]:
                res = mostprofitTrendFromBegin[i] + mostlossTrendFromEnd[i]
        return res
