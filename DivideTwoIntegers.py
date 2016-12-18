class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if divisor == 0: return sys.maxint
        positive = (dividend <0) is (divisor <0)
        end, sor = abs(dividend), abs(divisor)
        res = 0
        while end >= sor:
            tmp, i = sor, 1
            while end >= tmp:
                end -= tmp
                res += i
                i <<= 1
                tmp <<= 1
        if not positive:
            res = -res
        return min(max(-2147483648, res), 2147483647)
        