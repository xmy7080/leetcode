//sample solution
class Solution {
    fun orangesRotting(grid: Array<IntArray>): Int {
        val q = ArrayDeque<Pair<Int, Int>>()
        var time = 0; var fresh = 0

        for (i in 0 until grid.size) {
            for (j in 0 until grid[0].size) {
                if (grid[i][j] == 2) q += i to j
                if (grid[i][j] == 1) fresh++
            }
        }

        val dirs = setOf(0 to 1, 0 to -1, 1 to 0, -1 to 0)
        
        while (q.isNotEmpty() && fresh > 0) {
            for (i in 0 until q.size) {
                val (i, j) = q.removeFirst()
                for ((dr, dc) in dirs) {
                    val ii = dr + i
				    val jj = dc + j
				    if(ii !in grid.indices || jj !in grid[0].indices || grid[ii][jj] != 1) continue
				    fresh--
				    grid[ii][jj] = 2
				    q.add(ii to jj)
			    }
            }
            time++
        }

        return if (fresh == 0) time else -1
    }
}
//my solution
// data class Orange(val x: Int, val y: Int)
// class Solution {
//     fun orangesRotting(grid: Array<IntArray>): Int {
//         val m = grid.size
//         val n = grid[0].size
//         var que = ArrayDeque<Orange>()
//         // var tmp = ArrayDeque<Orange>()
//         var fresh = 0
//         for(i in 0 until m){
//             for(j in 0 until n){
//                 when(grid[i][j]){
//                     2 -> que.addLast(Orange(i, j))
//                     1 -> fresh ++
//                 }
//             }
//         }
//         var steps = 0
//         while(que.isNotEmpty() && fresh > 0){
//             for(i in 0 until que.size){
//                 val curr = que.removeFirst()
//                 for( (dirX, dirY) in setOf(1 to 0, 0 to 1,0 to -1, -1 to 0) ){
//                     val newX = curr.x + dirX
//                     val newY = curr.y + dirY
//                     if(newX >= 0 && newY >= 0 && newX < m && newY < n && grid[newX][newY] == 1){
//                         grid[newX][newY] = 2
//                         fresh --
//                         que.addLast(Orange(newX, newY))
//                     }
//                 }
//             }
//             steps ++
//         }
//         if(fresh == 0) return steps
//         else return -1
//     }
// }
