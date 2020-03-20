class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if len(grid) == 0: return 0
        m, n = len(grid), len(grid[0])
        for i in xrange(m):
            for j in xrange(n):
                if i == 0 and j==0 :
                    continue
                upcell   = grid[i-1][j] if i-1>=0 else sys.maxint
                leftcell = grid[i][j-1] if j-1>=0 else sys.maxint
                grid[i][j] += min(upcell, leftcell)
        return grid[m-1][n-1]
