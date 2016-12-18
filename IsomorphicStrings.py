class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        stot, ttos = dict(), dict()
        for i in range(len(s)):
            chars, chart = s[i], t[i]
            if chars in stot.keys():
                if stot[chars] != chart:
                     return False
            else:
                stot[chars] = chart
            if chart in ttos.keys():
                if ttos[chart] != chars:
                     return False
            else:
                ttos[chart] = chars
        return True