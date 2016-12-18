class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        l = len(s)
        longest = 0
        s_save = 0
        e_save = 0
        for c in range(l):
            stt = c
            end = c
            while stt>=0 and end<l and s[stt] == s[end]:
                if longest < end - stt:
                    longest = end-stt
                    s_save = stt
                    e_save = end
                stt-=1
                end+=1
            
            stt = c
            end = c+1
            while stt>=0 and end<l and s[stt] == s[end]:
                if longest < end - stt:
                    longest = end-stt
                    s_save = stt
                    e_save = end    
                stt-=1
                end+=1
        return s[s_save:e_save+1]
            