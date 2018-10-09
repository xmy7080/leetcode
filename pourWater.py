class Solution(object):
    def pourWater(self, heights, V, K):
        """
        :type heights: List[int]
        :type V: int
        :type K: int
        :rtype: List[int]
        """
        for v in xrange(V):
            index = K
            for i in xrange(K-1, -1, -1):
                if heights[i] > heights[index]:
                    break
                elif heights[i] < heights[index]:
                    index = i
            if index != K:
                heights[index] += 1
                continue
            for i in xrange(K+1, len(heights)):
                if heights[i] > heights[index]:
                    break
                elif heights[i] < heights[index]:
                    index = i
            heights[index] += 1
        return heights
