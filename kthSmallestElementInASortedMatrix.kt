//the first editorial solution, although the second is faster, it is difficult to reasoning about and much more harder to implement correct
class Solution {
    fun kthSmallest(matrix: Array<IntArray>, k: Int): Int {
        val n = matrix.size
        val queue = PriorityQueue<IntArray>{a,b -> a[0] - b[0]}
        for(i in 0 until minOf(n, k)){
            queue.offer(intArrayOf(matrix[i][0], i, 0))
        }
        var countToK = k
        while(--countToK > 0 && queue.isNotEmpty()){
            val arr = queue.poll()
            val x = arr[1]
            val y = arr[2]
            if(arr[2] + 1 < n)
                queue.offer(intArrayOf(matrix[x][y+1], x, y+1))
        }
        return queue.poll()[0]
    }
}
