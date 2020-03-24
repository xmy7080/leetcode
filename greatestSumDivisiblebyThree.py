#1 dimensional DP with dp = [0,0,0] stands for biggest sum mode 3 = i
#gotcha is, when interate the dp list, we need to do "for j in dp[:]: " instead of "for j in dp:" cause dp is a list that could got changed
# hence we need a deep copy of dp, ie. dp[:]
class Solution(object):
    def maxSumDivThree(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [0] * 3
        
        for n in nums:
            for j in dp[:]:
                dp[(j + n) % 3] = max(dp[(j + n) % 3], j + n)
        return dp[0]
