#====jiuzhang interval dp solution, the fifith lesson homework=====
#https://leetcode.com/articles/burst-balloons/
class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        lth = len(nums)
        dp = [[0] * lth for _ in xrange(lth)]
        for s in xrange(1, lth+1):
            for i in xrange(0, lth -s + 1):
                j = i + s -1
                for w in xrange(i, j+1):
                    #dp[i][w-1] and dp[w+1][j], they could be either [3][2] which makes no sense
                    # or out of bound, in both case, we treat it as 0
                    lproduct = dp[i][w-1] if w >0 else 0
                    rproduct = dp[w+1][j] if w+1< lth else 0
                    #left and right most balloon which are not bursted, it could hit the 
                    #boundary hence it's 1
                    lmost = nums[i-1] if i>0 else 1
                    rmost = nums[j+1] if j+1 < lth else 1
                    dp[i][j] = max(dp[i][j], lmost * nums[w] * rmost + lproduct + rproduct)
        return dp[0][lth-1]
