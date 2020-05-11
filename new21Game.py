#solution from lee215, plain dp but dynamically add dp[i] when i< K and remove dp[i-W] when i-W == 0
#https://leetcode.com/problems/new-21-game/discuss/132334/One-Pass-DP-O(N)
class Solution:
    def new21Game(self, N: int, K: int, W: int) -> float:
        if not K or N - W >= K-1: return 1.0
        dp = [1.0] + [0.0] * N
        Wsum = 1.0
        for i in range(1, N+1):
            dp[i] = Wsum / W
            if i < K: Wsum += dp[i]
            if i - W >= 0: Wsum -= dp[i-W]
        # print(str(dp))
        return sum(dp[K:])
