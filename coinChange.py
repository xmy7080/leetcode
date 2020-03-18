#==========first solution by a dictionary, when there are no way, dict will give -1===
class Solution(object):
    d = {}
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        self.d = {0: 0}
        def helper(amount):
            if amount < 0:
                return -1
            if amount in self.d:
                return self.d[amount]
            count = []
            for c in coins:
                tmpCount = helper(amount - c) + 1
                if tmpCount > 0:
                    count.append(tmpCount)
            minCount = min(count) if count else -1
            self.d[amount] = minCount
            return minCount
        return helper(amount)
        
#=============second solution for count from 0 to amount, use array of int, -1 stands for no way====
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp = [0] + [-1] * amount #[0, -1, -1, -1, -1 ..., -1]
        for n in xrange(1, amount+1):
            count = sys.maxint
            for c in coins:
                if n >= c and dp[n-c] + 1 >0:
                    count = min(count, dp[n-c] + 1)
            if count != sys.maxint:
                dp[n] = count
        return dp[amount]
