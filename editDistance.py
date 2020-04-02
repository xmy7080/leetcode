#jiuzhang two sequence dp solution, very neat and clean approach
#for explaination, see spreadsheet on lesson 6
class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        m, n = len(word1), len(word2)
        dp = [[0] * (n+1) for _ in xrange(m+1)]
        for i in xrange(m + 1):
            for j in xrange(n + 1):
                if not i:
                    dp[i][j] = j
                    continue
                elif not j:
                    dp[i][j] = i
                    continue
                #delete tail, swap tail and add extra to tail
                dp[i][j] = min(dp[i-1][j] + 1, dp[i-1][j-1] + 1, dp[i][j-1] + 1)
                #when last char is the same, no one more step, only update [i-1][j-1]
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = min(dp[i][j], dp[i-1][j-1])
        return dp[m][n]
