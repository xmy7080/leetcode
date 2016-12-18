
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        lastDay = prices[0]
        profit = 0
        for today in prices:
            if today > lastDay:
                profit += today - lastDay
            lastDay = today
        return profit