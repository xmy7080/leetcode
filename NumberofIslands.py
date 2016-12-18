class Solution(object):
    dx = [-1,1,0,0]
    dy = [0,0,1,-1]
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """

        islands = 0
        for i in xrange(len(grid)):
            for j in xrange(len(grid[0])):
                if grid[i][j] == '1':
                    self.explore(grid,i,j)
                    islands+=1
        return islands
        
    def explore(self, grid, x, y):
        grid[x][y] = 'X'
        for i in xrange(len(self.dx)):
            newx, newy = x+self.dx[i], y+self.dy[i]
            if 0 <= newx < len(grid) and 0<=newy < len(grid[0]) and grid[newx][newy] == '1':
                self.explore(grid, newx, newy)
        