class Solution(object):
    def slidingPuzzle(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        R, C = len(board), len(board[0])
        start = tuple(board[0] + board[1])
        que = collections.deque([(start, start.index(0), 0)])
        seen = {start}
        target = (1,2,3,4,5,0)
        
        while que:
            curBd, pos0, steps = que.popleft()
            if curBd == target: return steps
            for d in (-1, 1, C, -C):
                npos0 = pos0 + d
                if abs(npos0/C - pos0/C) + abs(npos0%C - pos0%C) != 1:
                    continue
                if 0 <= npos0 < R*C:
                    newBd = list(curBd)
                    newBd[pos0] = newBd[npos0]
                    newBd[npos0] = 0
                    key = tuple(newBd)
                    if key not in seen:
                        que.append((key, npos0, steps + 1))
                        seen.add(key)
        return -1
                    
