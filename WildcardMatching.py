class Solution(object):
    def isMatch(self, s, p):
        
        m, n = len(s), len(p)
        if n - p.count('*') > m:
            return False
        mat = [[False]*(n+1) for i in range(m+1)]
        mat[0][0] = True
        for j in xrange(1,n+1):
            mat[0][j] = mat[0][j-1] and p[j-1]=='*'
        for i in xrange(1,m+1):
            for j in xrange(1,n+1):
                if p[j-1] == '*':
                    mat[i][j] = mat[i-1][j-1] or mat[i-1][j] or mat[i][j-1]
                elif p[j-1] == '?':
                    mat[i][j] = mat[i-1][j-1]
                else:
                    mat[i][j] = mat[i-1][j-1] and p[j-1] == s[i-1]
        return mat[m][n]