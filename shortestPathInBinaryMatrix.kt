// fastest kotlin version, notice they used linked list as queue data structure.
// which can save 20+ ms
// also, direction defined as setOf executes WAY slower than two nested intArrayOf(1, 0, -1)
//    for( (dirx, diry) in setOf(0 to 1, 0 to -1, 1 to 0, -1 to 0, 1 to 1, 1 to -1, -1 to 1, -1 to -1)){
// in this problem it can add 100 ms runtime

// class Solution {
//     fun shortestPathBinaryMatrix(grid: Array<IntArray>): Int {
//         if (grid[0][0] == 1) return -1
//         val gridV = Array<BooleanArray>(grid.size) { 
//             BooleanArray(grid.size) { false }
//         }
//         val dir = intArrayOf(-1, 0, 1)
//         val queue = LinkedList<Triple<Int, Int, Int>>()
        
//         fun add(r: Int, c: Int, d: Int) {
//             if (r >= grid.size || r < 0) return
//             if (c >= grid.size || c < 0) return
//             if (grid[r][c] == 1) return
//             if (gridV[r][c]) return
//             queue.offer(Triple(r, c, d + 1))
//             gridV[r][c] = true
//         }

//         queue.offer(Triple(0, 0, 1))
//         gridV[0][0] = true
//         while (queue.isNotEmpty()) {
//             val (x, y, d) = queue.poll()
//             if (x == grid.size - 1 && y == grid.size - 1) return d
//             for (r in dir) { 
//                 for (c in dir) {
//                     add(x + r, y + c, d)
//                 }
//             }
//         }
//         return -1
//     }
// }

// my solution optimized to 22ms
class Solution {
    fun shortestPathBinaryMatrix(grid: Array<IntArray>): Int {
        val m = grid.size
        val n = grid[0].size
        if(grid[0][0] == 1 || grid[m-1][n-1] == 1) return -1
        // var steps = 0
        val dir = intArrayOf(-1, 0, 1)
        val queue = LinkedList<Triple<Int, Int, Int>>()
        queue.offer(Triple(0,0,1))
        while(queue.isNotEmpty()){
            // steps ++
            repeat(queue.size) {
                val curr = queue.poll()
                val currx = curr.first
                val curry = curr.second
                val dist = curr.third
                if(currx == m-1 && curry == n -1) return dist
                for(dirx in dir){
                    for(diry in dir) {
                        val newx = currx + dirx
                        val newy = curry + diry
                        if(newx >= 0 && newx < m && newy >= 0 && newy < n && grid[newx][newy] == 0){
                            queue.offer(Triple(newx, newy, dist+1))
                            grid[newx][newy] = 1
                        }
                    }
                }
            }
        }
        return -1
    }
}
