// editorial solution 1, didn't go for dynamic programming
class Solution {
    fun minFlipsMonoIncr(s: String): Int {
        var m = 0
        for (c in s){
            if (c == '0') m++
        }
        var res = m
        for (c in s){
            if (c == '0'){
                m --
                res = minOf(res, m)
            } else {
                m ++
            }
        }
        return res
    }
}
