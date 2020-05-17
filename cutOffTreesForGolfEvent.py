#lt solution is here
#https://leetcode.com/articles/cutoff-trees-for-golf-event/
#bfs will timeout, only approach better than A* will pass
class Solution(object):
    def cutOffTree(self, forest):
        """
        :type forest: List[List[int]]
        :rtype: int
        """
        m, n = len(forest), len(forest[0])
        from heapq import heappush, heappop
        def astar(sr, sc, tr, tc):
            heap = [(0,0,sr, sc)]
            cost = {(sr, sc): 0}
            while heap:
                _, g, r, c = heapq.heappop(heap)
                if r == tr and c == tc: return g
                for nr, nc in ((r +1, c), (r -1, c), (r, c-1), (r, c+1)):
                    if 0 <= nr < m and 0 <= nc < n and forest[nr][nc]:
                        ncost = g + 1 + abs(nr - tr) + abs(nc - tc)
                        if ncost < cost.get((nr, nc), sys.maxint ):
                            cost[(nr, nc)] = ncost
                            heapq.heappush(heap, (ncost, g+1, nr, nc) )
            return -1
        
#         def bfs(si, sj, ti, tj): #will timeout
#             q = collections.deque()
#             seen = set()
#             q.append((si, sj, 0) )
#             while q:
#                 a, b, step = q.popleft()
#                 if a == ti and b == tj: return step
#                 for dx, dy in ((1,0), (-1,0), (0,-1), (0,1) ):
#                     newa, newb = a + dx, b + dy
#                     if 0 <= newa < m and 0 <= newb < n and forest[newa][newb] and (newa, newb) not in seen:
#                         q.append((newa, newb, step+1) )
#                         seen.add((a, b) )
                        
#             return -1
        
        trees = sorted((v, i, j) for i, row in enumerate(forest) for j, v in enumerate(row) if v > 1 )
        si = sj = ans = 0
        for _, ti, tj in trees:
            d = astar(si, sj, ti, tj)
            if d < 0: return -1
            ans += d
            si, sj = ti, tj
        return ans
