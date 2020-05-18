class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        q = collections.deque()
        if not rooms: return None
        m, n = len(rooms), len(rooms[0])
        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    q.append((i, j) )
        
        while q:
            a, b = q.popleft()
            for na, nb in ((a+1, b), (a-1, b), (a, b-1), (a, b+1)):
                if 0<= na < m and 0<= nb < n and rooms[na][nb] == 2147483647:
                    rooms[na][nb] = rooms[a][b] + 1
                    q.append((na, nb) )
        
