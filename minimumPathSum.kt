class Solution {
    fun minPathSum(grid: Array<IntArray>): Int {
        val m = grid.size
        val n = grid[0].size
        val res = IntArray(n){0}
        for(i in 0 until m){
            for(j in 0 until n){
                if(i == 0 && j == 0){
                    res[j] = grid[i][j]
                } else if(i == 0){
                    res[j] = res[j-1] + grid[i][j]
                } else if(j == 0){
                    res[j] = res[j] + grid[i][j]
                } else{
                    if(res[j-1] < res[j]) res[j] = res[j-1] + grid[i][j]
                    else res[j] = res[j] + grid[i][j]
                }
            }
        }
        return res[n-1]
    }
}
