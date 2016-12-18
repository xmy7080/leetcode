class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        l = list(s)
        vows = ['a','e','i','o','u','A','E','I','O','U']
        start, end = 0, len(s)-1
        while start < end:
            if l[start] in vows and l[end] in vows:
                tmp = l[start]
                l[start] = l[end]
                l[end] = tmp
                start += 1
                end -= 1
            while start < end and l[start] not in vows:
                start += 1
            while end > start and l[end] not in vows:
                end -= 1
        return ''.join(l)