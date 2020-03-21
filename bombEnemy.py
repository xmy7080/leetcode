#====gotcha is, xrange(n-1, 0, -1) in python can only iterate n-1 ~ 1, for n-1 ~ 0, need xrange(n-1, -1, -1)
class Solution(object):
    def maxKilledEnemies(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if len(grid) == 0: return 0
        m, n = len(grid), len(grid[0])
        up   = [[0 for j in xrange(n)] for i in xrange(m)]
        down = [[0 for j in xrange(n)] for i in xrange(m)]
        right= [[0 for j in xrange(n)] for i in xrange(m)]
        left = [[0 for j in xrange(n)] for i in xrange(m)]
        #up cases
        for i in xrange(m):
            for j in xrange(n):
                up[i][j] = 0
                if grid[i][j] != 'W': #if == 'w', default to 0
                    if grid[i][j] == 'E':
                        up[i][j] += 1
                    if i-1 >= 0:
                        up[i][j] += up[i-1][j]
        #down cases
        for i in xrange(m-1, -1, -1):
            for j in xrange(n):
                down[i][j] = 0
                if grid[i][j] != 'W': #if == 'w', default to 0
                    if grid[i][j] == 'E':
                        down[i][j] += 1
                    if i+1 < m:
                        down[i][j] += down[i+1][j]
        #right cases
        for i in xrange(m):
            for j in xrange(n-1, -1, -1):
                right[i][j] = 0
                if grid[i][j] != 'W': #if == 'w', default to 0
                    if grid[i][j] == 'E':
                        right[i][j] += 1
                    if j+1 < n:
                        right[i][j] += right[i][j+1]
                        
        #left cases
        for i in xrange(m):
            for j in xrange(n):
                left[i][j] = 0
                if grid[i][j] != 'W': #if == 'w', default to 0
                    if grid[i][j] == 'E':
                        left[i][j] += 1
                    if j-1 >=0:
                        left[i][j] += left[i][j-1]
        
        #get which one has largest 4 ways number
        ans = 0
        for i in xrange(m):
            for j in xrange(n):
                if grid[i][j] == '0': #enemy slot can't place bomb, so count all empty space
                    ans = max(ans, up[i][j]+ down[i][j] + left[i][j] + right[i][j])
        return ans
        
