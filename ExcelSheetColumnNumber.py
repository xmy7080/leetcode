class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        sum = 0
        for c in s:
            sum = sum*26 + ord(c) - ord('A') + 1
        return sum