#=====O(n^2) to calculate isPalin, O(n^2) to find partition by dp====
class Solution(object):
    isPalin = []
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        lth = len(s)
        self.isPalin = [[False] * lth for i in xrange(lth)]
        
        def setPalin(a, b, lth):
            while a>=0 and b < lth:
                if s[a] != s[b]:
                    break
                else:
                    self.isPalin[a][b] = True
                a -= 1
                b += 1
        
        for i, c in enumerate(s):
            self.isPalin[i][i] = True
            a, b = i-1, i+1
            setPalin(a, b, lth)
            a, b = i, i+1
            setPalin(a, b, lth)
            
        #dp[i] stands for previous [0:i-1] str palin partitions
        dp = [0] + [sys.maxint] * lth
        for i in xrange(1, lth+1):
            for j in xrange(0, i):
                if self.isPalin[j][i-1]:
                    dp[i] = min(dp[i], dp[j]+ 1)
        return dp[lth] -1
        
        
