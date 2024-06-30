// used the editorial solution, O (n^2)
//https://leetcode.com/problems/making-a-large-island/description/
class Solution {
    fun largestIsland(grid: Array<IntArray>): Int {
        val area = hashMapOf<Int, Int>() // starts with 2 as group number
        dfs(grid, area)
        // println(area.entries.map{" group id " + it.key + " size : " + it.value})
        // println(grid.map {it.joinToString(", ") }.joinToString("\n") )
        var res = 0
        val m = grid.size
        val n = grid[0].size
        val dirs = listOf(intArrayOf(1, 0), intArrayOf(0, 1), intArrayOf(-1, 0), intArrayOf(0, -1))
        for (i in 0 until m) {
            for ( j in 0 until n) {
                if (grid[i][j] == 0){
                    var candidateAreaSize = 1
                    val groups = HashSet<Int>()
                    for (dir in dirs){
                        val nx = i + dir[0]
                        val ny = j + dir[1]
                        if (nx >=0 && nx <m && ny >= 0 && ny <n && grid[nx][ny] != 0){
                            groups.add(grid[nx][ny])
                        }
                    }
                    for (group in groups){
                        candidateAreaSize += area[group]!!
                    }
                    res = maxOf(res, candidateAreaSize)
                }
            }
        }
        return if (res == 0) grid.size * grid.size else res
    }

    data class Cell(val x:Int, val y:Int)
    fun dfs(grid: Array<IntArray>, area: HashMap<Int, Int>) {
        val m = grid.size
        val n = grid[0].size
        // val visited = Array(m) {BooleanArray(n) {false}}
        val dirs = listOf(intArrayOf(1, 0), intArrayOf(0, 1), intArrayOf(-1, 0), intArrayOf(0, -1))
        var groupId = 2 // group id starts at 2, because original island is 1

        for (i in 0 until m){
            for (j in 0 until n){
                if ( grid[i][j] != 1) continue
                var temp = 0
                val que = ArrayDeque<Cell>()
                que.addLast(Cell(i,j))
                grid[i][j] = groupId
                while (que.isNotEmpty()){
                    val curr = que.removeFirst()
                    val x = curr.x
                    val y = curr.y
                    for (dir in dirs){
                        val nx = x+dir[0]
                        val ny = y+dir[1]
                        if (nx >=0 && nx <m && ny >= 0 && ny <n && grid[nx][ny] == 1 ){
                            que.addLast(Cell(nx, ny))
                            grid[nx][ny] = groupId
                        }
                    }
                    temp ++
                }
                area[groupId] = temp
                groupId ++
            }
        }

    }
}
