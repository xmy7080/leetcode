public class Solution {
    public int countBattleships(char[][] board) {
        //optimal way to consider the first 'X' we met when a new ship appear without up and left cell marked as "X"
        //, if they are 'X', then we say we have visited this ship. skip it.
        //it do not change the board, and we can do it in O(3n) time (one cell plus its up and left)
        int m = board.length, n = board[0].length;
        int res = 0;
        for(int i=0;i<m;i++)
            for(int j=0;j<n;j++){
                if(board[i][j] == '.') continue;
                if(i>0 && board[i-1][j] == 'X') continue;
                if(j>0 && board[i][j-1] == 'X') continue;
                res ++;
            }
        return res;
        
        
        //naive way to mark every cell of a ship when found one, and marked it 'o'. which in worst case will have O(5n) time (one cell plus its four surroundings). and it changes the board
        // int m = board.length, n = board[0].length;
        // int res = 0;
        // for(int i=0;i<m;i++)
        //     for(int j=0;j<n;j++){
        //         if(board[i][j] == 'X'){
        //             res ++;
        //             board[i][j] = 'o';
        //             markShips(board,i,j);
        //         }
        //     }
        // return res;
    }
    
    public void markShips(char[][] board, int i,int j){
        int m = board.length, n = board[0].length;
        int leftmost = i-1, rightmost = i+1;
        int downmost = j-1, upmost = j+1;
        for(int lm = i-1;lm >= 0 && board[lm][j] == 'X' ;lm--)
                board[lm][j] = 'o';
        
        for(int rm = i+1;rm < m && board[rm][j] == 'X' ;rm++)
                board[rm][j] = 'o';
        
        for(int dm = j-1;dm >= 0 && board[i][dm] == 'X';dm--)
                board[i][dm] = 'o';
        
        for(int um = j+1;um < n && board[i][um] == 'X';um++)
                board[i][um] = 'o';
        
    }
}