class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        peri = 0
        for i in xrange(len(grid)):
            for j in xrange(len(grid[0])):
                if grid[i][j] == 1:
                    peri += self.getOneCellPeri(i, j, grid)
        return peri
    
    def getOneCellPeri(self, i, j, grid):
        m, n = len(grid), len(grid[0])
        di= [1, -1, 0, 0]
        dj= [0, 0, 1, -1]
        zeroToFour = 0
        for k in range(4):
            newi, newj = i + di[k], j + dj[k]
            if 0 <= newi < m and 0 <= newj < n and grid[newi][newj] == 0:
                #adjacent cell is water
                zeroToFour += 1
            elif newi in [-1, m]:
                #left or right adjacent cell is non-exist, mark as 1 perimeter
                zeroToFour += 1
            elif newj in [-1, n]:
                #up or down adjacent cell is non-exist, mark 1 peri
                zeroToFour += 1
        return zeroToFour
    
    #===========another quicker solution======
    class Solution(object):
    def islandPerimeter(self, grid):
        grid_ext = ['0' + ''.join(str(x) for x in row) + '0' for row in grid]
        grid_trans = list(map(list, zip(*grid)))
        grid_ext += [ '0' + ''.join(str(x) for x in row) + '0' for row in grid_trans ]                
        return sum(row.count('01') + row.count('10') for row in grid_ext)
