class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        m, n = len(haystack), len(needle)
        if not n: return 0
        for i in xrange(m-n+1):
            for j in xrange(n):
                if needle[j] != haystack[i+j]: break
                if j == n-1: return i
        return -1
        
        
        
        
        
        
        
        
        
        
        # n, m = len(needle),len(haystack)
        # if not n: return 0
        # for i in range(0,m-n+1):
        #     for j in range(0,n):
        #         if needle[j] != haystack[i+j]: break
        #         if j == n-1: return i
        # return -1