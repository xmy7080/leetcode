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