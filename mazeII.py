#https://leetcode.com/articles/the-maze/
#convention bfs way
class Solution(object):
    def shortestDistance(self, maze, start, destination):
        """
        :type maze: List[List[int]]
        :type start: List[int]
        :type destination: List[int]
        :rtype: int
        """
        m, n = len(maze), len(maze[0])
        que = collections.deque()
        que.append( (start[0], start[1]) )
        visited = [[sys.maxint] * n for _ in xrange(m)]
        visited[start[0]][start[1]] = 0
        while que:
            curr = que.popleft()
            a, b = curr[0], curr[1]
            if (a, b) == (destination[0], destination[1]):
                continue
            for d in ((1,0), (0, 1), (-1, 0), (0, -1) ):
                na, nb = a+ d[0], b + d[1] #new a and new b
                step = 0
                while 0<= na < m and 0<=nb < n and not maze[na][nb]:
                    step += 1
                    na += d[0]
                    nb += d[1]
                la, lb = na - d[0], nb - d[1] #last a and b before while stop
                if (visited[a][b] + step < visited[la][lb]):
                    que.append((la, lb) )
                    visited[la][lb] = visited[a][b] + step
        ans = visited[destination[0]][destination[1]]
        return ans if ans != sys.maxint else -1
