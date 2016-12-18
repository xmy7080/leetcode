class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        isneg = False
        if x<0: 
            isneg = True
            x = -x
        reverse = 0
        while x>0:
            reverse = reverse *10 + x%10
            x = x/10
        if abs(reverse) > 0x7FFFFFFF:
            return 0
        return reverse if not isneg else -1*reverse