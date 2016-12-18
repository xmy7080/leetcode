class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        #reverse the whole string
        self.reverse(s,0,len(s)-1)
        #reverse each word
        start = 0
        for i in xrange(len(s)):
            if s[i] == ' ':
                self.reverse(s,start, i-1)
                start = i+1
        
        #reverse the last word
        self.reverse(s,start,len(s)-1)
        
    def reverse(self, s, start, end):
        while start < end:
            tmp = s[start]
            s[start] = s[end]
            s[end] = tmp
            start += 1
            end -= 1
        
        
        #this way is not okay since extra space is used
        # l = list("".join(s).split(' '))
        # start = 0
        # end = len(l)-1
        # while start<end:
        #     tmp = l[start]
        #     l[start] = l[end]
        #     l[end] = tmp
        #     end -= 1
        #     start += 1
        # s[:] = ' '.join(l)