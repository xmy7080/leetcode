// used the 3rd editorial approach, similar to DoorDash find dashmart but not exactly same
//https://leetcode.com/problems/shortest-distance-from-all-buildings/editorial/ 
class Solution {
    fun shortestDistance(grid: Array<IntArray>): Int {
        val m = grid.size
        val n = grid[0].size
        val dist = Array(m) {Array(n) {0}}
        val houses = mutableListOf<IntArray>()
        for (i in 0 until m){
            for (j in 0 until n){
                if (grid[i][j] == 1) houses.add(intArrayOf(i, j))
            }
        }
        var emptyLandValue = 0
        val dirs = arrayOf(intArrayOf(1, 0), intArrayOf(0, 1), intArrayOf(-1, 0), intArrayOf(0, -1))
        houses.forEach{location ->
            var steps = 0
            val que = ArrayDeque<IntArray>()
            que.add(location)
            while (que.isNotEmpty()){
                steps ++
                for (i in que.size downTo 1){
                    val loc = que.removeFirst()
                    for (dir in dirs){
                        val nr = loc[0] + dir[0]
                        val nc = loc[1] + dir[1]
                        if (nr < m && nr >= 0 && nc < n && nc >= 0 && grid[nr][nc] == emptyLandValue){
                            que.addLast(intArrayOf(nr, nc))
                            grid[nr][nc] --
                            dist[nr][nc] += steps
                        }
                    }
                }
            }
            // println("emptyLandValue: " + emptyLandValue)
            // println(dist.map{it.joinToString(",")}.joinToString("\n"))
            // next house traversal
            emptyLandValue --
        }
        var res = Int.MAX_VALUE
        for (i in 0 until m){
            for (j in 0 until n){
                if (grid[i][j] == emptyLandValue) res = minOf(res, dist[i][j])
            }
        }
        return if( res == Int.MAX_VALUE) -1 else res
    }
}
