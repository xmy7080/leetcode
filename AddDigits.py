class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if not num:return 0
        return num%9 if num%9 != 0 else 9