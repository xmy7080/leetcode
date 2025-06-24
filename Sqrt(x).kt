class Solution {
    fun mySqrt(x: Int): Int {
        if(x <= 1) return x
        var low = 0L
        var high = x / 2L
        while(low <= high){
            val mid = low + (high - low)/2
            val num = mid * mid
            if(num == x.toLong()) return mid.toInt()
            else if(num > x.toLong()) high = mid - 1
            else low = mid + 1
        }
        return high.toInt()
    }
}
