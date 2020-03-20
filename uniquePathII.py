class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        grid = obstacleGrid
        m, n = len(grid), len(grid[0])
        #===standard way to initial 2 dimenstional array in python
        dp = [[0 for j in xrange(n)] for i in xrange(m)]
        if grid[0][0] == 1 or grid[m-1][n-1] == 1:
            return 0
        for i in xrange(m):
            for j in xrange(n):
                if i == 0 and j == 0:
                    dp[i][j] = 1
                    continue
                if grid[i][j] == 1:
                    dp[i][j] = 0
                    continue
                upcell   = dp[i-1][j] if 0<=i<m else 0
                leftcell = dp[i][j-1] if 0<=j<n else 0
                dp[i][j] = upcell + leftcell
        return dp[m-1][n-1]
