class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        res = ['']*numRows
        loc = 0
        length = len(s)
        while loc < len(s):
            i = 0
            while i<numRows and loc < length:
                res[i] += s[loc]
                i+=1
                loc+=1
            i = numRows-2
            while i>0 and loc < length:
                res[i] += s[loc]
                loc+=1
                i-=1
        return ''.join(res)