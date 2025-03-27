class Solution {
    fun pivotIndex(nums: IntArray): Int {
        val l = nums.size
        //left sum without curr index
        val leftSum = IntArray(l) {0}
        for(i in 1 until l){
            leftSum[i] = nums[i-1]
            leftSum[i] += if(i>1) leftSum[i-1] else 0
        }
        val total = leftSum[l-1] + nums[l-1]
        for(i in 0 until l){
            val rightSum = total - leftSum[i] - nums[i]
            if(rightSum == leftSum[i]) return i
        }
        return -1
    }
}
