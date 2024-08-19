// binary search solution
class Solution {
    fun minEatingSpeed(piles: IntArray, h: Int): Int {
        fun calculateHours(speed: Long): Long{
            var result = 0L
            piles.forEach{pile ->
                result += ceil(pile.toDouble() / speed).toLong()
            }
            return result
        }
        var min = ceil(piles.sum().toDouble() / h).toLong()
        // this one has to be to double and toLong to avoid floating number accuracy lost and integer overflow
        // var max = ceil(piles.max().toDouble() * piles.size / h).toLong()
        var max = piles.max() * ceil( piles.size.toDouble() / h).toLong()
        // println("min is " + min +  " max is " + max)
        while (min < max){
            var mid = min + (max - min)/2
            if(calculateHours(mid) > h) {
                min = mid + 1
            } else{
                max = mid
            }
        }
        return min.toInt()
    }

}
