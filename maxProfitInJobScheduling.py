#leetcode solution
#https://leetcode.com/problems/maximum-profit-in-job-scheduling/discuss/409009/JavaC%2B%2BPython-DP-Solution
#also be aware of the bisect.bisect func, explain of it is here:
#https://www.geeksforgeeks.org/bisect-algorithm-functions-in-python/
class Solution(object):
    def jobScheduling(self, startTime, endTime, profit):
        """
        :type startTime: List[int]
        :type endTime: List[int]
        :type profit: List[int]
        :rtype: int
        """
        jobs = sorted(zip(startTime, endTime, profit), key = lambda x:x[1] )
        dp = [[0,0]]
        for s, e, p in jobs:
            i = bisect.bisect(dp, [s, sys.maxint]) - 1
            #for [[0, 0], [3, 50], [5, 90], [6, 120]], find where [3, xprofit] located
            if dp[i][1] + p > dp[-1][1]: #if take curr job will bigger than highest profit so far
                dp.append([e, dp[i][1] + p] )
        return dp[-1][1]
                
                
