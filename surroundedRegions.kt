class Solution {
    fun solve(board: Array<CharArray>): Unit {
        val m = board.size
        val n = board[0].size
        var visitedO = BooleanArray(m*n)
        fun dfs(x: Int, y: Int): Unit{
            visitedO[x*n + y] = true
            val dirs = arrayOf(intArrayOf(1,0), intArrayOf(0,1), intArrayOf(-1,0), intArrayOf(0,-1))
            for(dir in dirs){
                val newx = x + dir[0]
                val newy = y + dir[1]
                if(newx >= 0 && newx < m && newy >= 0 && newy < n && board[newx][newy] == 'O' && !visitedO[newx*n + newy]){
                    dfs(newx, newy)
                }
            }
        }
        
        //start dfs from bouundary of the board
        for(i in listOf(0, m-1)){ // first row or last row
            for (j in 0 until n){
                if(board[i][j] == 'O' && !visitedO[i*n + j]){
                    dfs(i, j)
                }
            }
        }
        for(j in listOf(0, n-1)){ // first col or last col
            for (i in 0 until m){
                if(board[i][j] == 'O' && !visitedO[i*n + j]){
                    dfs(i, j)
                }
            }
        }
        
        for(i in 0 until m){ //flip the 'O' which is not accessible from boundary
            for (j in 0 until n){
                if(board[i][j] == 'O' && !visitedO[i*n + j]){
                    board[i][j] = 'X'
                }
            }
        }
    }
}
