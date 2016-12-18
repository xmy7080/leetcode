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