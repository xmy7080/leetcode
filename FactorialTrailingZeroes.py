class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        return 0 if not n else n/5 + self.trailingZeroes(n/5)