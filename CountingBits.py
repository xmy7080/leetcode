class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        res = [0]
        tmp = num
        while tmp>0:
            res.extend([x+1 for x in res])
            tmp  = tmp >>1
        return res[:num+1]