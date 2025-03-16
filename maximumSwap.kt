// editorial solution 4 https://leetcode.com/problems/maximum-swap/editorial/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days
//basically we scan from right to left, save the highest digit index so far, and whenever we saw a digit to the left to be lower than our highest, we update the swap candidate pair
// if no pair is found, we know the swap is unnecessary
class Solution {
    fun maximumSwap(num: Int): Int {
        val numstr = num.toString().toCharArray()
        val length = numstr.size
        var maxNumberIdxFromRight = -1
        var swapL = -1
        var swapR = -1
        for(i in length-1 downTo 0){
            val currInt = numstr[i].digitToInt()
            if(maxNumberIdxFromRight == -1 || currInt > numstr[maxNumberIdxFromRight].digitToInt())
                maxNumberIdxFromRight = i
            else if (currInt < numstr[maxNumberIdxFromRight].digitToInt()) {
                swapL = i
                swapR = maxNumberIdxFromRight
            }
        }

        if(swapL != -1 && swapR != -1){
            val temp = numstr[swapR]
            numstr[swapR] = numstr[swapL]
            numstr[swapL] = temp
        }
        return numstr.joinToString("").toInt()
    }
}
