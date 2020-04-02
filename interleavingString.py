class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        #two pointers, which will fail on 
        #"aabc"
        #"abad"
        #"aabadabc"
        la, lb, lc = len(s1), len(s2), len(s3)
        if la + lb != lc: return False
        pa, pb, pc = la-1, lb -1, lc -1
        while pa >=-1 and pb >=-1 and pc >= 0:
            if pa > -1 and s3[pc] == s1[pa]:#find char in s1
                pa -= 1
            elif pb > -1 and s3[pc] == s2[pb]:#find char in s2
                pb -= 1
            else:
                return False
            pc -= 1
        return pa == -1 and pb == -1 and pc == -1
        
        #jiuzhang two sequence dp solution, 
        la, lb, lc = len(s1), len(s2), len(s3)
        if la + lb != lc: return False
        dp = [[False] * (lb+1) for _ in xrange(la+1)]
        for i in xrange(la + 1):
            for j in xrange(lb + 1):
                if not i and not j:
                    dp[i][j] = True
                    continue
                elif not i:#i is 0
                    dp[i][j] = dp[i][j-1] if s2[j-1] == s3[i + j - 1] else False
                elif not j:#j is 0
                    dp[i][j] = dp[i-1][j] if s1[i-1] == s3[i + j - 1] else False
                else:#i,j != zero
                    dp[i][j] = (dp[i][j-1] if s2[j-1] == s3[i + j - 1] else False) or (dp[i-1][j] if s1[i-1] == s3[i + j - 1] else False)
        return dp[la][lb]
