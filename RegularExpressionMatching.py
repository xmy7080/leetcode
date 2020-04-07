#jiuzhang dp lesson 6, before rolling array===
class Solution:
    # "aab" ->   "aa"  + "b"
    # "c*a*b"-> "c*a*" + "b"
    #case 1 when b[n-1] == a[m-1] or b[n-1] == '.', it stands true only if a[0~ m-2] matches b[0~ n-2]
    #dp[i][j] = dp[i-1][j-1]
    
    # "aa" ->   "a"  + "a"
    # "c*a*"-> "c*"  + "a*"
    #case 2 when b[n-1] == '*', check b[n-2] altogether, here b[n-2] == a[m-1] (or it could be b[n-2] == '.'), 
    #it stands true only if a[0 ~ m-2] matches b[0 ~ n-1]
    #dp[i][j] = dp[i-1][j]
    
    # "ab" ->   "ab"  + ""
    # "c*ba*"-> "c*b"  + "a*"
    #case 3 when b[n-1] == '*' and a[m-1] != b[n-2], hence we forfeit this star pair, it stands only if a[0~ m-1] matches b[0~ n-3]
    #dp[i][j] = dp[i][j-2]
    
    """
    @param s: A string 
    @param p: A string includes "." and "*"
    @return: A boolean
    """
    def isMatch(self, s, p):
        ls, lp = len(s), len(p)
        if not lp: return False
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
                if p[j-1] != '*':
                    if i > 0 and p[j-1] in ('.', s[i-1]):
                        dp[i][j] = dp[i-1][j-1]
                else:
                    if j > 1:
                        dp[i][j] = dp[i][j-2]
                    if i > 0 and j >1 and p[j-2] in ('.', s[i-1]):
                        dp[i][j] = dp[i][j] or dp[i-1][j]
        
        return dp[ls][lp]
                
#===leetcode solution, second dp approach
#https://leetcode.com/articles/regular-expression-matching/
class Solution(object):
    def isMatch(self, s, p):
        sl, pl = len(s), len(p)
        dp = [[False] * (pl + 1) for _ in xrange(sl+1)]
        
        dp[-1][-1] = True
        #i and j all matches to idx in string, hence 0 based
        for i in xrange(sl, -1, -1):
            for j in xrange(pl-1, -1, -1):
                first_match = i < sl and p[j] in (s[i], '.')
                if j+1< pl and p[j+1] == '*':
                    dp[i][j] = dp[i][j+2] or (first_match and dp[i+1][j])
                else:
                    dp[i][j] = first_match and dp[i+1][j+1]
        return dp[0][0]
    
#====my own solution, not sure the reasoning
class Solution(object):
    def isMatch(self, s, p):
        m, n = len(s), len(p)
        dp = [[False]*(n+1) for i in range(m+1)]
        dp[0][0] = True
        for j in range(1,n+1):
            if p[j-1] == '*':
                if dp[0][j-1] or (j > 1 and dp[0][j-2]):
                    dp[0][j] = True
        for i in range(1,m+1):
            for j in range(1,n+1):
                if s[i-1] == p[j-1] or p[j-1] == '.':
                    dp[i][j] = dp[i-1][j-1]
                elif p[j-1] == '*':
                    if p[j-2] != s[i-1] and p[j-2] != '.':
                        dp[i][j] = dp[i][j-2]
                    else:
                        dp[i][j] = dp[i][j-1] or dp[i-1][j] or dp[i][j-2]
        return dp[m][n]
