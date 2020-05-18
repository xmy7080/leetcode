class Solution:
    def orangesRotting(self, rooms: List[List[int]]) -> int:
        q = collections.deque()
        tmpq = collections.deque()
        if not rooms: return None
        m, n = len(rooms), len(rooms[0])
        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 2:
                    q.append((i, j) )
        time = 0
        while True:
            for orgs in q:
                a, b = orgs[0], orgs[1]
                for na, nb in ((a+1, b), (a-1, b), (a, b-1), (a, b+1)):
                    if 0<= na < m and 0<= nb < n and rooms[na][nb] == 1:
                        rooms[na][nb] = 2
                        tmpq.append((na, nb) )
            q = tmpq
            tmpq = collections.deque()
            if not q:
                break
            time += 1
        remains = [v for row in rooms for v in row if v == 1 ]
        if remains: return -1
        return time
                
