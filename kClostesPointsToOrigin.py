#typical heap problem
from heapq import heapify, heappush, heappop
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        def euclideanDist(a: int, b: int) -> int:
            return a ** 2 + b ** 2
        h = []
        for point in points:
            x, y = point[0], point[1]
            eDist = euclideanDist(x, y)
            if len(h) < K:
                heappush(h, (-eDist, x, y))
            elif len(h) == K and h[0][0] < -eDist:
                heappop(h)
                heappush(h, (-eDist, x, y))
        return [[tpl[1], tpl[2]] for tpl in h ]
