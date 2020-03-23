# simple DP solution ===O(1) space and O(n) time ====
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        low = prices[0]
        ans = 0
        for p in prices:
            if p < low:
                low = p
                continue
            ans = max(ans, p - low)
        return ans

#======old solution with same time space complexity
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
