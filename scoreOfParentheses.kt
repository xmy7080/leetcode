// editorial solution iii
// note kotlin bit shift left is shl, and kotlin only support pow fun on a double/float
class Solution {
    fun scoreOfParentheses(s: String): Int {
        var level = 0
        var res = 0
        for (i in 0 until s.length){
            if (s[i] == '('){
                level ++
            } else {
                level --
                if (s[i-1] == '(') {
                    res += 1 shl level
                    // res += 1 * (2.0).pow(level).toInt()
                }
            }
        }
        return res
    }
}
