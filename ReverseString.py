class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        start, end = 0, len(s)-1
        l = list(s)
        while start < end:
            tmp = l[start]
            l[start] = l[end]
            l[end] = tmp
            start += 1
            end -= 1
        return ''.join(l)