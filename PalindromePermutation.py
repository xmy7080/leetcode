class Solution(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        count = {}
        for c in s:
            count[c] = count.get(c,0)+1
        odds = 0
        for key in count.keys():
            if count.get(key) %2: odds+=1
        return odds<2