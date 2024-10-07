class Solution {
    fun largestAltitude(gain: IntArray): Int {
        var curr = 0
        var res = 0
        for(g in gain){
            curr += g
            res = if(curr > res) curr else res
        }
        return res
    }
}
