
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        lowest = prices[0]
        lastDayPrice = prices[0]
        MaxProfit = 0
        for dayPrice in prices:
            if dayPrice > lastDayPrice and (dayPrice - lowest) > MaxProfit:
                MaxProfit = dayPrice - lowest
            else:
                if lowest>dayPrice:
                    lowest = dayPrice
            lastDayPrice = dayPrice
        return MaxProfit