#https://leetcode.com/articles/longest-increasing-path-matrix/
# this is the second approach, dfs with memoisation
class Solution(object):
    m, n = 0, 0
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        if not matrix: return 0
        self.m, self.n = len(matrix), len(matrix[0])
        cache = [[0 for j in xrange(self.n)] for i in xrange(self.m)]
        ans = 0
        for i in xrange(self.m):
            for j in xrange(self.n):
                ans = max(ans, self.dfs(matrix, i, j, cache))
        return ans
    
    def dfs(self, matrix, i, j, cache):
        if cache[i][j] != 0: return cache[i][j]
        for delta in [[1,0], [-1,0], [0,1], [0,-1]]:
            a, b = i + delta[0], j + delta[1]
            if 0 <= a < self.m and 0 <= b < self.n and matrix[a][b] > matrix[i][j]:
                cache[i][j] = max(cache[i][j], self.dfs(matrix, a, b, cache))
        cache[i][j] += 1
        return cache[i][j]
