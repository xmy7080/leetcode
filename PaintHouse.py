class Solution(object):
    def minCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        r,b,g = 0,0,0
        for nhouse in costs:
            tmpr = min(b,g) + nhouse[0]
            tmpb = min(r,g) + nhouse[1]
            tmpg = min(r,b) + nhouse[2]
            r,b,g = tmpr,tmpb,tmpg
        return min(r,b,g)