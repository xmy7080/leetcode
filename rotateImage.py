#first approach, transpose the matrix and reverse each row
#https://leetcode.com/articles/rotate-image/
class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in xrange(n):
            for j in xrange(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        for i in xrange(n):
            matrix[i].reverse()
        return
