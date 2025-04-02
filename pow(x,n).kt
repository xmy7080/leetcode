class Solution {
    fun myPow(xval: Double, nval: Int): Double {
        var n: Long = nval.toLong()
        var x = xval
        if(n < 0){
            x = 1 / x
            n = -n
        }
        var res: Double = 1.0
        while(n > 0){
            when{
                (n and 1) == 1L -> {
                    res *= x
                    n --
                }
                else -> {
                    x *= x
                    n = n shr 1
                }
            }
            // println("n= " + n + " res= " + res+ " x= " + x)
        }
        return res
    }
}
