class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        if not matrix: return None
        m, n = len(matrix), len(matrix[0])
        self.accuSum = [[0] * n for _ in xrange(m)]
        for i in xrange(m):
            for j in xrange(n):
                self.accuSum[i][j] = matrix[i][j]
                if j > 0:
                    self.accuSum[i][j] += self.accuSum[i][j-1]
        

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        ans = 0
        for i in xrange(row1, row2 + 1):
            ans += self.accuSum[i][col2]
            if col1 > 0:
                ans -= self.accuSum[i][col1-1]
        return ans
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
