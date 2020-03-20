#put all possibilities in a set, and check if the digit(s) can form a letter==
class Solution(object):
    s = set()
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        for i in xrange(1, 27):
            self.s.add(str(i) )
        ans = [0] * (len(s)+1)
        ans[0] = 1
        for i in xrange(1, len(s)+1):
            onedigit, twodigit = 0, 0
            if s[i-1] in self.s:
                onedigit = ans[i-1]
            if i-2 >= 0 and s[i-2:i] in self.s:
                twodigit = ans[i-2]
            ans[i] = onedigit + twodigit
        
        return ans[len(s)]
#======complex way to determine if digits(s) can form a letter====
class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s: return 0
        count = [0]*(len(s)+1)
        if s[0] != '0': count[0] = 1
        for i in xrange(1,len(s)+1):
            oneback, twoback = 0, 0
            if '0' < s[i-1] <= '9':
                oneback = count[i-1]
            if i>=2 and ('1' == s[i-2] and '0' <= s[i-1] <= '9') or ('2' == s[i-2] and '0' <= s[i-1] <= '6'):
                twoback = count[i-2]
            count[i] = oneback + twoback
        return count[len(s)]
