// editorial solution, dp
class Solution {
    fun canPartition(nums: IntArray): Boolean {
        var total = 0
        for(num in nums){
            total += num
        }
        if(total % 2 != 0) return false
        val half = total / 2
        val size = nums.size
        var dp = Array(size+1) {BooleanArray(half+1) {false}}
        dp[0][0] = true
        for(i in 1 .. size){
            val curr = nums[i-1]
            for(j in 0 .. half){
                if(j < curr) dp[i][j] = dp[i-1][j]
                else dp[i][j] = dp[i-1][j] || dp[i-1][j-curr]
            }
        }
        return dp[size][half]
    }
}
