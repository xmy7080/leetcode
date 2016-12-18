# Definition for a point.
# class Point(object):
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b

class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        l = len(points)
        res = 0
        for i in xrange(l):
            d = {'i':1}
            samep = 0
            ix, iy = points[i].x, points[i].y
            for j in xrange(i+1,l):#have discuss all lines pass point i, no need to look it back, so j starts at i+1
                jx, jy = points[j].x, points[j].y
                if jx == ix and jy == iy:#same point
                    samep += 1
                    continue
                
                if jx == ix:  # slope is infinity
                    slope = 'i'
                else:           #other slope
                    slope = (jy-iy)* 1.0/(jx-ix)
                if slope in d.keys():
                    d[slope] += 1
                else:
                    d[slope] = 2
            res = max(res, max(d.values())+ samep)
        return res
                