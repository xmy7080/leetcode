// snap phone interview question
class Solution {
    fun exist(board: Array<CharArray>, word: String): Boolean {
        val m = board.size // 3
        val n = board[0].size // 4
        val visited = BooleanArray(m * n){false}
        fun dfs(x: Int, y:Int, index: Int): Boolean{
            visited[x * n + y] = true
            // println("x " + x +  " y " + y +  " index " + index + " letter " + word[index] + " visited 10 " + visited[1 * n + 0])
            if (index == word.length) return true
            val dirs = arrayOf(intArrayOf(1,0), intArrayOf(0, 1), intArrayOf(-1,0), intArrayOf(0,-1))
            for (dir in dirs){
                val nx = x + dir[0]
                val ny = y + dir[1]
                // println("nx " + nx +  " ny " + ny +  " index " + index + " visited " + visited[nx * n + ny])
                if (nx >= 0 && nx < m && ny >= 0 && ny < n && !visited[nx * n + ny] && word[index] == board[nx][ny]){
                    if (dfs(nx, ny, index + 1)) return true
                }
            }
            
            visited[x * n + y] = false
            return false
        }
        
        
        for ( i in 0 until m){
            for (j in 0 until n){
                if (board[i][j] == word[0]) {
                    // println("starting " + "i " + i +  " j " + j)
                    if (dfs(i, j, 1)) return true
                }
            }
        }
        return false
    }
}
