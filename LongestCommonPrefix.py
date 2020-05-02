#leetcode solution
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs: return ""
        elif len(strs) == 1: return strs[0]
        for i in xrange(len(strs[0])):
            char = strs[0][i]
            for s in strs[1:]:
                if len(s) == i or s[i] != char:
                    return s[:i]
        return strs[0]
#old approach
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs: return ""
        pf = strs[0]
        for i in range(1,len(strs)):
            for j in range(len(pf)):
                if j < len(strs[i]) and pf[j] != strs[i][j]:
                    pf = pf[:j]
                    break
                if j == len(strs[i]):
                    pf = strs[i][:j]
        return pf
