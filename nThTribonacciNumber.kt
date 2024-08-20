class Solution {
    fun tribonacci(n: Int): Int {
        var a = 0
        var b = 1
        var c = 1
        return when (n){
            0 -> 0
            1 -> 1
            2 -> 1
            else -> {
                for (i in 0 .. n-3){
                    var d = a + b + c
                    a = b
                    b = c
                    c = d
                }
                c
            }
        }
    }
}
