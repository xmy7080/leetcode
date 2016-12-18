class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        #check input
        if not len(board):
            return True
        m, n = len(board), len(board[0])
        
        #check rows
        for i in xrange(0,m):
            tmplist = []
            for j in xrange(0,n):
                tmplist.append(board[i][j])
            if not self.helper(tmplist):
                return False
        
        #check cols
        for j in xrange(0,n):
            tmplist = []
            for i in xrange(0,m):
                tmplist.append(board[i][j])
            if not self.helper(tmplist):
                return False
        
        #check 3X3 squares
        for i in xrange(0, m/3):
            for j in xrange(0, n/3):
                tmplist = []
                for a in xrange(i*3,i*3+3):
                    for b in xrange(j*3,j*3+3):
                        tmplist.append(board[a][b])
                if not self.helper(tmplist):
                    return False
        
        return True
        
    def helper(self,tmplist):
        s = set()
        for l in tmplist:
            if l == ".": continue
            else:
                if l in s:
                    return False
                s.add(l)
        return True