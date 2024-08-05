class Solution {
    fun furthestBuilding(heights: IntArray, bricks: Int, ladders: Int): Int {
        var que = PriorityQueue<Int>()
        var bricksRemain = bricks
        for(i in 1 until heights.size){
            if (heights[i] > heights[i-1]){
                val diff = heights[i] - heights[i-1]
                que.add(diff)
                if (que.size > ladders) {
                    bricksRemain -= que.poll()
                }
                if (bricksRemain < 0) return i -1
            }
        }
        return heights.size -1
    }
}
