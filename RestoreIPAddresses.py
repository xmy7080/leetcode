class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if(len(s) >12): return []
        res = []
        self.helper(res, s, 0, [])
        return res
        
    def helper(self, res, s, start, tmp):
        if(len(tmp) == 4 and start == len(s)):
            res.append(".".join(tmp))
            return
        for i in xrange(start+1, start+4):
            if i > len(s):#out of range
                break
            substr = s[start:i]
            if self.validIP(substr):
                tmp.append(substr)
                self.helper(res, s, i, tmp)
                tmp.pop()
    
    def validIP(self, str):
        if len(str)>1 and str[0] == '0':#case like 01,020, aren't valid ip 
            return False
        return ((int) (str)) < 256