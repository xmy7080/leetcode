#jiuzhang approach, dp inteval solution, dp[i][j] stands for the longest palindrom subsequence in s[i:j]
#loop from the shortest subsequence, dp[0][1]
class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s: return 0
        l = len(s)
        #initialize all dp[k][k] = 1, also 1 is the smallest possible for every span, hence this line will just work
        dp = [[1] * l for _ in xrange(l)]
        #loop from shorter to longer span
        for span in xrange(2, l+1):
            #i from 0 to l -span, say l = 3, span = 2, we need calculate dp[0][1] and dp[1][2]
            #hence j = i + span -1
            for i in xrange(0, l - span + 1):
                j = i + span -1
                #case of s[i] != s[j]
                dp[i][j] = max(dp[i+1][j], dp[i][j-1])
                if s[i] == s[j]:
                    #case of they equals, also check if i+1 is less or equals than j-1, 
                    #otherwise cause dp[k][k-1] = 1 and it's invalid value, we should treat it as 0
                    inner = 0 if i+1 > j-1 else dp[i+1][j-1]
                    dp[i][j] = max(dp[i][j], inner + 2)
        return dp[0][l-1]
                
