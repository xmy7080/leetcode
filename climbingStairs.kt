// ways to jump to n = (ways jump to n-2) + (ways jump to n-1)
// it eventually break down to a fibonacci array
class Solution {
    fun climbStairs(n: Int): Int {
        var oneStepAway = 1
        var twoStepAway = 1
        var res = 1
        for (i in 2 .. n){
            res = oneStepAway + twoStepAway
            twoStepAway = oneStepAway
            oneStepAway = res
        }
        return res
    }
}
