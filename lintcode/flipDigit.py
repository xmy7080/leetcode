#==gotcha is, 1 if nums[i-1] != 0 else 0 will pulling anything ahead of it, in this case, we need () around them
#== (1 if nums[i-1] != 0 else 0)
class Solution:
    """
    @param nums: the array
    @return: the minimum times to flip digit
    """
    def flipDigit(self, nums):
        # Write your code here
        dp = [[0, 0]] * (len(nums) + 1)
        for i in xrange(1, len(nums) + 1):
            dp[i][0] = min(dp[i-1][0] + (1 if nums[i-1] != 0 else 0), dp[i-1][1] + (1 if nums[i-1] != 0 else 0) )
            dp[i][1] = dp[i-1][1] + (1 if nums[i-1] != 1 else 0)
        return min(dp[len(nums)])
