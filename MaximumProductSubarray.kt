// consider three parts at each step
// min value, cause a very small negative number can be flipped when another negative number came in
// nums[i] value, cause 0 could appear right before and it nullify all the accumulated product before
// max value is trivial, we want the max anyway
class Solution {
    fun maxProduct(nums: IntArray): Int {
        var maxSofar = IntArray(nums.size)
        var minSofar = IntArray(nums.size)
        maxSofar[0] = nums[0]
        minSofar[0] = nums[0]
        var res = nums[0]
        for (i in 1 until nums.size){
            val a = nums[i] * maxSofar[i-1]
            val b = nums[i] * minSofar[i-1]
            maxSofar[i] = maxOf(a, b, nums[i])
            minSofar[i] = minOf(a, b, nums[i])
            res = maxOf(res, maxSofar[i])
        }

        return maxSofar.maxOrNull() ?: 0
    }
}
