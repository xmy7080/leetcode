#=======a gotcha point is, when initialize the two demensional array in python, it's n in side and m out side
#instead of [[1] * m] * n, should be [[1] * n] * m
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m == 0 or n == 0:
            return 0
        grid = [[1] * n] * m
        for i in xrange(1, m):
            for j in xrange(1, n):
                grid[i][j] = grid[i-1][j] + grid[i][j-1]
        return grid[m-1][n-1]
                    
