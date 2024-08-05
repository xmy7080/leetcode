class Solution {
    fun swimInWater(grid: Array<IntArray>): Int {
        val lth = grid.size
        var water = 0
        // val visited = HashMap<Int, Boolean>(lth * lth).withDefault{false}
        val visited = BooleanArray(lth*lth)
        println("visited " + visited[0])
        
        val comparator: Comparator<IntArray> = compareBy {grid[it[0]][it[1]]}
        val pq = PriorityQueue<IntArray>(comparator)
        pq.add(intArrayOf(0, 0))
        visited[0] = true
        val dirs = arrayOf(intArrayOf(1, 0), intArrayOf(0, 1), intArrayOf(-1, 0), intArrayOf(0, -1))

        while (pq.isNotEmpty()){
            val curr = pq.poll()
            
            if (water < grid[curr[0]][curr[1]]) water = grid[curr[0]][curr[1]]
            if (curr[0] == lth - 1 && curr[1] == lth -1) return water
            for (dir in dirs){
                val nextR = curr[0] + dir[0]
                val nextC = curr[1] + dir[1]
                if (nextC >= 0 && nextC < lth && nextR >= 0 && nextR < lth && visited[nextR * lth + nextC] == false){
                    pq.add( intArrayOf(nextR, nextC))
                    visited[nextR * lth + nextC] = true
                    
                }
            }
        }
        return -1
    }
}
