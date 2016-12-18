class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s: return 0
        count = [0]*(len(s)+1)
        if s[0] != '0': count[0] = 1
        for i in xrange(1,len(s)+1):
            oneback, twoback = 0, 0
            if '0' < s[i-1] <= '9':
                oneback = count[i-1]
            if i>=2 and ('1' == s[i-2] and '0' <= s[i-1] <= '9') or ('2' == s[i-2] and '0' <= s[i-1] <= '6'):
                twoback = count[i-2]
            count[i] = oneback + twoback
        return count[len(s)]