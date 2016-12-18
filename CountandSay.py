class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        a = "1"
        while n>1:
            b = ""
            count = 0
            seq = '0'
            for s in a:
                if seq != s and count != 0:
                    b += str(count) + seq
                    count = 1
                    seq = s
                elif count == 0:
                    count = 1
                    seq = s
                else:
                    count += 1
            b += str(count) + seq
            a = b
            n -= 1
        return a