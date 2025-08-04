class Solution {
    fun maxSubArray(nums: IntArray): Int {
        var result = nums[0]
        var accu = nums[0]
        for(i in 1 until nums.size){
            if(accu < 0) accu = 0
            accu += nums[i]
            result = maxOf(accu, result)
        }
        return result
    }
}
