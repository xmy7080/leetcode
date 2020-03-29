#===jiuzhang dp solution, same problem is backpackVI===
class Solution(object):
    def combinationSum4(self, A, t):
        # write your code here
        if not A: return 0
        # lth = len(A)
        dp = [0] * (t + 1)
        dp[0] = 1
        for i in xrange(1, t+1):
            for c in A:
                if i>=c:
                    dp[i] += dp[i-c]
        return dp[t]
