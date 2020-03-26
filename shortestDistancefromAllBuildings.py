#BFS way with pruning
#https://leetcode.com/problems/shortest-distance-from-all-buildings/discuss/76877/Python-solution-72ms-beats-100-BFS-with-pruning

class Solution(object):
    def shortestDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid or not grid[0]: return -1
        m, n = len(grid), len(grid[0])
        buildings = sum(grid[i][j] for j in xrange(n) for i in xrange(m) if grid[i][j] == 1 )
        distSum = [[0] * n for i in xrange(m)]
        hit = [[0] * n for i in xrange(m)]
        
        def bfs(a, b):
            visited = [[False] * n for i in xrange(m)]
            visited[a][b] = True
            count1 = 1
            queue = collections.deque([(a, b, 0)])
            while queue:
                x, y, dist = queue.popleft()
                for delta in [[1,0], [0,1], [-1, 0], [0,-1] ]:
                    i, j = x + delta[0], y + delta[1]
                    if 0<= i <m and 0<= j <n and not visited[i][j]:
                        visited[i][j] = True
                        if not grid[i][j]: # when it's 0
                            hit[i][j] += 1
                            distSum[i][j] += dist + 1
                            queue.append((i, j, dist + 1) )
                        elif grid[i][j] == 1: #when it's 1
                            count1 += 1
            return count1 == buildings
                            
        
        
        for i in xrange(m):
            for j in xrange(n):
                if grid[i][j] == 1:
                    #if there is one building not able to reach rest of them, means it's no way to go from a 0 spot to reach all building neither, return -1 immediately
                    if not bfs(i, j): return -1
        
        ans = [distSum[i][j] for i in xrange(m) for j in xrange(n) if grid[i][j] == 0 and hit[i][j] == buildings]
        #if there isn't such 0 spot that can reach all buildings, return -1
        return min(ans) if ans else -1
