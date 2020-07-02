//https://leetcode.com/problems/read-n-characters-given-read4/discuss/659272/Kotlin-solution
/**
* The read4 API is defined in the parent class Reader4.
* fun read4(buf:CharArray): Int {}
*/

class Solution:Reader4() {
    /**
      * @param buf Destination buffer
      * @param n Number of characters to read
      * @return The number of actual characters read
      */
    override fun read(buf:CharArray, n:Int): Int {
        var buff = CharArray(4)
        var count = 0
        do {
            val lth = Math.min(n - count, read4(buff))
            buff.take(lth).forEach{
                buf.set(count++, it)
            }
        } while (lth >0)
        return count
    }
}
