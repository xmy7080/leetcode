class Solution {
    data class Cell(val x:Int, val y:Int)
    fun maxAreaOfIsland(grid: Array<IntArray>): Int {
        val m = grid.size
        val n = grid[0].size
        val visited = Array(m) {BooleanArray(n) {false}}
        val dirs = listOf(intArrayOf(1, 0), intArrayOf(0, 1), intArrayOf(-1, 0), intArrayOf(0, -1))
        var res = 0
        for (i in 0 until m){
            for (j in 0 until n){
                if ( grid[i][j] == 0 || visited[i][j]) continue
                var temp = 0
                val que = ArrayDeque<Cell>()
                que.addLast(Cell(i,j))
                visited[i][j] = true
                while (que.isNotEmpty()){
                    val curr = que.removeFirst()
                    val x = curr.x
                    val y = curr.y
                    for (dir in dirs){
                        val nx = x+dir[0]
                        val ny = y+dir[1]
                        if (nx >=0 && nx <m && ny >= 0 && ny <n && grid[nx][ny] == 1 && !visited[nx][ny]){
                            que.addLast(Cell(nx, ny))
                            visited[nx][ny] = true
                        }
                    }
                    temp ++
                }
                res = maxOf(res, temp)
            }
        }
        return res
    }
}
