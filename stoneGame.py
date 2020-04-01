#===jiuzhang interval dp solution O(n^2) time and O(n^2) space
class Solution(object):
    def stoneGame(self, piles):
        """
        :type piles: List[int]
        :rtype: bool
        """
        if not piles: return False
        lth = len(piles)
        dp = [[0] * lth for _ in xrange(lth)]
        for i in xrange(lth):
            dp[i][i] = True
        
        for s in xrange(2, lth+1):
            for i in xrange(0, lth-s+1):
                j = i + s -1
                dp[i][j] = max(piles[i] - dp[i+1][j], piles[j] - dp[i][j-1] ) 
        return dp[0][lth-1] > 0
        
