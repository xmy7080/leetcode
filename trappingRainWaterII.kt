class Solution {
  // solution https://leetcode.com/problems/trapping-rain-water-ii/solutions/1138028/python3-visualization-bfs-solution-with-explanation
  
    fun trapRainWater(heightMap: Array<IntArray>): Int {
        val que = PriorityQueue<IntArray> (compareBy {heightMap[it[0]][it[1]] })
        val m = heightMap.size
        val n = heightMap[0].size
        val visited = BooleanArray(m*n)
        var res = 0
        
        // put boarder cells into queue
        for (i in 0 until m){
            for (j in 0 until n){
                if(i == m-1 || i == 0 || j == n-1 || j == 0) {
                    que.offer(intArrayOf(i, j) )
                    visited[i*n + j] = true
                }
            }
        }

        while (que.isNotEmpty()){
            val curr = que.poll()
            val row = curr[0]
            val col = curr[1]
            // println("row " + row + " col "+ col +" height " + heightMap[row][col])
            for (delta in arrayOf(intArrayOf(-1, 0), intArrayOf(0, -1), intArrayOf(1, 0), intArrayOf(0, 1))) {
                val newRow = row + delta[0]
                val newCol = col + delta[1]
                if (newRow < m && newRow >= 0 && newCol < n && newCol >= 0 && !visited[newRow * n + newCol]){
                    // println("newRow " + newRow + " newCol "+ newCol +" height " + heightMap[newRow][newCol])
                    visited[newRow * n + newCol] = true
                    res += maxOf(0, heightMap[row][col] - heightMap[newRow][newCol])
                    heightMap[newRow][newCol] = maxOf(heightMap[row][col], heightMap[newRow][newCol])
                    que.offer(intArrayOf(newRow, newCol))
                }
            }
        }
        return res
    }
    // otter ai phone interview
    fun trapRainWaterFromStartingPoint(heightMap: Array<IntArray>): Boolean {
        // val heights = arrayOf(arrayOf<Int>(1,4,3,1,3,2),
        //                       arrayOf<Int>(3,2,1,3,2,4),
        //                       arrayOf<Int>(2,3,3,2,3,1)
        //               )
        val row = 1
        val col = 4
        val m = heightMap.size
        val n = heightMap[0].size
        val visited = BooleanArray(m*n) // stores the x and y of location we visited
        val nextMoves = ArrayDeque<IntArray>()
        nextMoves.add(intArrayOf(row, col))
        val directions = listOf<IntArray>( intArrayOf(-1, 0), intArrayOf(0, -1), intArrayOf(1, 0), intArrayOf(0, 1), )
        val startingHeight = heightMap[row][col]
        while (nextMoves.isNotEmpty()){
            val currR = nextMoves.first()[0]
            val currC = nextMoves.first()[1]
            nextMoves.removeFirst()
            visited[currR * n + currC] = true
            println("row " + currR + " col "+ currC)
            if (currR == m || currR == 0 || currC == n || currC == 0) return false
            for (direction in directions){
                val newRow = currR + direction[0]
                val newCol = currC + direction[1]
                if (newRow < m && newRow >= 0 && newCol < n && newCol >= 0) {
                if (heightMap[newRow][newCol] <= startingHeight && !visited[newRow *m + newCol]) {
                    nextMoves.add(intArrayOf(newRow, newCol))
                }
                }
            }
        }
        return true
    }
}
