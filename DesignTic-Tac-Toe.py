class TicTacToe(object):

    def __init__(self, n):
        """
        Initialize your data structure here.
        :type n: int
        """
        self.row = [0]*n
        self.col = [0]*n
        self.diagnal = 0
        self.antidiag = 0
        

    def move(self, row, col, player):
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        :type row: int
        :type col: int
        :type player: int
        :rtype: int
        """
        addone = 1 if player == 1 else -1
        self.row[row] += addone
        self.col[col] += addone
        lth = len(self.row)
        if col == row:
            self.diagnal += addone
        if col + row == lth -1:
            self.antidiag += addone
        if abs(self.row[row]) == lth or abs(self.col[col]) == lth or abs(self.diagnal) == lth or abs(self.antidiag)==lth:
            return player
        else:
            return 0
        


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)