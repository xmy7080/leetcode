#dfs solution, one click only
#gotcha is, when deep copy a 2d array, do [row[:] for row in board]
class Solution(object):
    ans = []
    m, n = 0, 0
    def updateBoard(self, board, click):
        """
        :type board: List[List[str]]
        :type click: List[int]
        :rtype: List[List[str]]
        """
        self.m, self.n = len(board), len(board[0])
        self.ans = [row[:] for row in board]
        def mines(board, i, j):
            sum = 0
            for d in [[-1,-1],[1,1],[1,0],[0,1],[-1,0],[0,-1],[-1,1],[1,-1]]:
                newi, newj = i + d[0], j + d[1]
                if 0<= newi < self.m and 0<=newj < self.n:
                    sum += 1 if board[newi][newj] == 'M' else 0
            return sum
        
        def helper(i, j):
            if self.ans[i][j] == 'M':
                self.ans[i][j] = 'X'
                return;
            mineCount = mines(board, i, j)
            #empty and no mine surrounded
            if self.ans[i][j] == 'E' and not mineCount:#no mine, can expand
                self.ans[i][j] = 'B'
                for d in [[-1,-1],[1,1],[1,0],[0,1],[-1,0],[0,-1],[-1,1],[1,-1]]:
                    newi, newj = i + d[0], j + d[1]
                    if 0<= newi < self.m and 0<=newj < self.n:
                        helper(newi, newj)
            #when not mine and surrounded by some
            if self.ans[i][j] == 'E':
                self.ans[i][j] = str(mineCount)
                return;
        
        helper(click[0], click[1])
        return self.ans
