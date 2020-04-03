class Solution(object):
    def isOneEditDistance(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        ls, lt = len(s), len(t)
        if ls > lt:
            return self.isOneEditDistance(t, s)
        if lt - ls > 1:
            return False
        #default ls + 1 = lt
        a, b = 0, 0
        while a <ls:
            if s[a] != t[b]:
                if lt == ls:
                    return s[a+1: ls] == t[b+1: lt]
                else:#ls + 1 == lt
                    return s[a: ls] == t[b+1:lt]
            a += 1
            b += 1
        # If there is no diffs on ns distance
        # the strings are one edit away only if
        # t has one more character. 
        return ls + 1 == lt
