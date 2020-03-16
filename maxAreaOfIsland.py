class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # seen = set()
        def area(i, j):
            #pay attention this check actually is a not (condition not over the bound and unvisited):
            if not (0 <= i < len(grid) and 0 <= j < len(grid[0]) 
                and grid[i][j] == 1 ):
                return 0
            grid[i][j] = 2
            # seen.add((i,j) )
            return 1 + area(i -1,j) + area(i +1,j) + area(i,j -1) + area(i,j+1)
        
        return max(area(i, j) 
                   for i, row in enumerate(grid)
                   for j in xrange(len(row))
                  )
