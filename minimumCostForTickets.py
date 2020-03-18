#================dp solution similar to coin change
#For each day, if you don't have to travel today, then it's strictly better to wait to buy a pass. 
#If you have to travel today, you have up to 3 choices: you must buy either a 1-day, 7-day, or 30-day pass.

# We can express those choices as a recursion and use dynamic programming.
#Let's say dp(i) is the cost to fulfill your travel plan from day i to the end of the plan. 
#Then, if you have to travel today, your cost is:

# dp(i)=min(dp(i+1)+costs[0],dp(i+7)+costs[1],dp(i+30)+costs[2])
class Solution(object):
    d = set()
    money = []
    costs = []
    def mincostTickets(self, days, costs):
        """
        :type days: List[int]
        :type costs: List[int]
        :rtype: int
        """
        self.d = set(days)
        self.money = [None] * 366
        self.costs = costs
        
        return self.dp(1)
    
    def dp(self, day):
        if day > 365:
            return 0
        if self.money[day] != None:
            return self.money[day]
        
        if day in self.d:
            ans = min(self.dp(day + 1) + self.costs[0],
                     self.dp(day + 7) + self.costs[1])
            ans = min(ans, self.dp(day + 30) + self.costs[2])
        else:
            ans = self.dp(day +1)
        self.money[day] = ans
        return ans
        
