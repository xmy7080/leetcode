class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        l = s.split()
        #l.reverse()
        start = 0
        end = len(l)-1
        while start<end:
            tmp = l[start]
            l[start] = l[end]
            l[end] = tmp
            end -= 1
            start += 1
        return " ".join(l)