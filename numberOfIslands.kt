class Solution {
    fun numIslands(grid: Array<CharArray>): Int {
        val m = grid.size
        val n = grid[0].size

        fun bfs(a: Int, b: Int): Unit {
            grid[a][b] = '2'
            val dirs = setOf(0 to 1, -1 to 0, 1 to 0, 0 to -1)
            for((xa, xb) in dirs){
                val aa = a + xa
                val bb = b + xb
                if(aa >= 0 && aa < m && bb >= 0 && bb < n && grid[aa][bb] == '1'){
                    bfs(aa, bb)
                }
            }
        }
        var res = 0
        for(i in 0 until m){
            for(j in 0 until n){
                if(grid[i][j] == '1') {
                    bfs(i, j)
                    res ++
                }
            }
        }
        return res
    }

}
