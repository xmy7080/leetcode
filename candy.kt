//used the editorial solution 2 traverses
class Solution {
    fun candy(ratings: IntArray): Int {
        var left2right = IntArray(ratings.size){1}
        var right2left = IntArray(ratings.size){1}
        for(i in 1 until ratings.size){
            if(ratings[i] > ratings[i-1]) left2right[i] = left2right[i-1] + 1
        }
        var res = 0
        for(i in ratings.size-2 downTo 0){
            if(ratings[i] > ratings[i+1]) right2left[i] = right2left[i+1] + 1
        }
        for(i in 0 until ratings.size){
            res += intArrayOf(left2right[i], right2left[i]).max()
        }
        return res

    }
}
