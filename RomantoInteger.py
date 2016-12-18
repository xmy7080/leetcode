class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        sum = 0
        for i in xrange(len(s)-1,-1,-1):
            if i+1<len(s) and dic[s[i+1]] > dic[s[i]]:
                sum -= dic[s[i]]
            else:
                sum += dic[s[i]]
        return sum