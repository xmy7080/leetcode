class Solution(object):
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        h = []
        for p in points:
            if len(h) < K:
                heapq.heappush(h, (self.distance(p), p) )
            elif len(h) == K:
                heapq.heappushpop(h, (self.distance(p), p) )
        return [x[1] for x in h]
        
    def distance(self, point):
        return - (point[0] * point[0] ) - (point[1]* point[1]) 
        
