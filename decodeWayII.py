class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        def decode1(c):
            if c == '*':
                return 9
            if c == '0':
                return 0
            return 1
        
        def decode2(c1, c2):
            if c1 == '0': #0*, 00-09 cannot form 1 char
                return 0
            if c1 == '1':
                if c2 == '*':#11-19
                    return 9
                return 1 #10-19
            elif c1 == '2':
                if c2 == '*': #21-26
                    return 6
                elif c2 <= '6': #20-26
                    return 1
                else: #27-29 cannot form 1 char
                    return 0
            elif c1 >= '3': #30 or 3* cannot form 1 char
                return 0
            elif c1 == '*':
                if c2 == '*': #11-19 plus 21-26
                    return 15
                elif c2 <= '6': #16 26, 15 25, 14 24, 13 23, 12 22, 11 21, 10 20
                    return 2
                elif c2 >'6': #17, 18, 19
                    return 1
        ans = 0
        if not s: ans = 1
        l = len(s)
        dp = [0] * (l+1)
        dp[0] = 1
        for i in xrange(1, l+1):
            dp[i] = dp[i-1] * decode1(s[i-1])
            if i >1:
                dp[i] += dp[i-2] * decode2(s[i-2], s[i-1])
        ans = dp[l]
        
        return ans % (10**9 + 7)
