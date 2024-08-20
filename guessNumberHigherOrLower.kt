/** 
 * The API guess is defined in the parent class.
 * @param  num   your guess
 * @return 	     -1 if num is higher than the picked number
 *			      1 if num is lower than the picked number
 *               otherwise return 0
 * fun guess(num:Int):Int {}
 */

class Solution:GuessGame() {
    override fun guessNumber(n:Int):Int {
        var low = 1
        var high = Int.MAX_VALUE
        while (low < high){
            var mid = low + (high - low)/2
            when (guess(mid)){
                -1 -> high = mid - 1
                1 -> low = mid + 1
                0 -> {
                    low = mid
                    high = mid
                }
                else -> println("undefined")
            }
        }
        return low
    }
}
