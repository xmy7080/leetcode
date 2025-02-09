class Solution {
    fun searchMatrix(matrix: Array<IntArray>, target: Int): Boolean {
        val m = matrix.size
        val n = matrix[0].size
        var lr = 0
        var hr = m-1
        while (lr < hr){
            val row = lr + (hr - lr)/2
            if(matrix[row][0] > target) hr = row -1
            else if(matrix[row][n-1] < target) lr = row + 1
            else {
                lr = row
                break
            }
        }
        println("lr is " + lr)
        // after this the lr is the row target could possibily be in
        var lc = 0
        var hc = n -1
        if(matrix[lr][lc] > target || matrix[lr][hc] < target) return false
        while(lc < hc){
            val col = lc + (hc - lc)/2
            // println("lc is " + lc + " hc is " + hc + " col is " + col)
            if(matrix[lr][col] == target) return true
            else if (matrix[lr][col] < target) lc = col + 1
            else hc = col -1
            // println("lc is " + lc + " hc is " + hc)
        }
        return matrix[lr][lc] == target
    }
}
