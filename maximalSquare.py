#jiuzhang dp lesson 7, dp[i][j] stores the max square size when its right bottom ends on [i][j]
class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        # write your code here
        if not matrix: return 0
        m, n = len(matrix), len(matrix[0])
        dp = [map(int, row[:]) for row in matrix]
        for i in xrange(1, m):
            for j in xrange(1, n):
                if dp[i][j]:
                    dp[i][j] = min(dp[i-1][j], dp[i-1][j-1], dp[i][j-1]) + 1
                    # dp[i][j] = min(dp[i-1][j], dp[i-1][j-1], dp[i][j-1]) + 1
        return max(x for row in dp for x in row) ** 2
        
