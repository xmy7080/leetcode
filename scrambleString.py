class Solution(object):
    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if s1 == None or s2 == None or len(s1) != len(s2): return False
        lth = len(s1)
        #the biggest gotcha so far, we should not initial n dimensional array like this, basically it will copy over the reference on each row
        #then any assignment on dp[i][j][k] will apply to each row
        # dp = [ [ [False] * (lth+1) ] * lth ] * lth
        #use the below approach instead
        dp = [[[False]*(lth+1) for i in range (lth)] for j in range (lth)]
        count = 0
        for i in xrange(lth):
            for j in xrange(lth):
                dp[i][j][1] = s1[i] == s2[j]
        #Also, in line 21 and 22, we should include lth-m index, hence the range(lth-m+1)
        for m in xrange(2, lth+1):
            for i in xrange(lth-m+1):
                for j in xrange(lth-m+1):
                    for k in xrange(1, m):
                        if (dp[i][j][k] and dp[i+k][j+k][m-k]) or (dp[i][j + m-k][k] and dp[i+k][j][m-k]):
                            dp[i][j][m] = True
                            break
        
        return dp[0][0][lth]
