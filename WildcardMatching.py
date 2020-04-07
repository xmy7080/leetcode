#=====jiuzhang two subsequence solution lesson 6====
class Solution:
    """
    @param s: A string 
    @param p: A string includes "?" and "*"
    @return: is Match?
    """
    #s[m-1] == p[n-1] or p[n-1] == '?'
    #dp[i][j] = dp[i-1][j-1]
    
    #p[n-1] == '*', cases are matched a char in s or not matched at all
    #dp[i][j] = dp[i-1][j] or dp[i][j-1]
    def isMatch(self, s, p):
        # write your code here
        if not s and not p: return True
        if not p: return False
        ls, lp = len(s), len(p)
        #dp[0-ls][0-lp]
        dp = [[False] * (lp+1) for _ in xrange(ls+1)]
        
        for i in xrange(ls+1):
            for j in xrange(lp+1):
                if not i and not j:
                    dp[i][j] = True
                    continue
                if not j:
                    dp[i][j] = False
                    continue
                #when j != 0 , i could be 0
                if p[j-1] != '*':
                    if i > 0 and p[j-1] in ('?', s[i-1]):
                        dp[i][j] = dp[i-1][j-1]
                else: #p[j-1] == '*'
                    dp[i][j] = dp[i][j-1]
                    if i > 0:
                        dp[i][j]  = dp[i][j] or dp[i-1][j]
        
        return dp[ls][lp]
===========
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
