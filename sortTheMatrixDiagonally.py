#robinhood oa
class Solution(object):
    def diagonalSort(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """
        if not mat: return mat
        m, n = len(mat), len(mat[0])
        def singleDiagnal(a, b):
            tmp = []
            while a < m and b < n:
                tmp.append(mat[a][b])
                a += 1
                b += 1
            tmp.sort()
            a -= 1
            b -= 1
            for i in xrange(len(tmp)-1, -1, -1):
                mat[a][b] = tmp[i]
                a -= 1
                b -= 1
        for j in xrange(n): #starting point on first row
            singleDiagnal(0, j)
            
        for i in xrange(1, m): #starting point on first col
            singleDiagnal(i, 0)
        return mat
