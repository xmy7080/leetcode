#====O(nK) time solution
class Solution(object):
    def minCostII(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        if len(costs) == 0: return 0
        m, k = len(costs), len(costs[0])
        #started from second row, reuse the costs array to store our record
        for row in xrange(1, m):
            # find min and secondMin in the cost row before
            minColor, secColor = -1, -1
            for color in xrange(k):
                cost = costs[row-1][color]
                if (minColor == -1 or cost < costs[row-1][minColor]):
                    secColor = minColor
                    minColor = color
                elif (secColor == -1 or cost < costs[row-1][secColor]):
                    secColor = color
            
            #assign cost table in current row
            for color in xrange(k):
                if color == minColor:
                    costs[row][color] += costs[row-1][secColor]
                else:
                    costs[row][color] += costs[row-1][minColor]
        return min(costs[m-1])
