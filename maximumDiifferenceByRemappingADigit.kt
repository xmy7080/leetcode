class Solution {
    fun minMaxDifference(num: Int): Int {
        val array = num.toString()
        fun replaceNum(digit: Char): Int {
            val replaceChar = array.firstOrNull{digit != it}
            val replacedArray = if(replaceChar != null){
                array.replace(replaceChar!!, digit)
            } else array
            return replacedArray.toInt()
        }
        val maximum = replaceNum('9')
        val minimum = replaceNum('0')
        return maximum - minimum
    }
}
