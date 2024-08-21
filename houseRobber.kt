class Solution {
    fun rob(nums: IntArray): Int {
        when(nums.size){
            1 -> return nums[0]
            else -> {
                var foreTwo = IntArray(2) {0}
                foreTwo[0] = 0       // the up-to-date amount previous house did not get robbed
                foreTwo[1] = nums[0] // the up-to-date amount previous house did get robbed

                for ( i in 1 until nums.size){
                    // amount max if not rob the second house, is NN or YN pattern
                    var secondNo = arrayOf(foreTwo[0], foreTwo[1]).max()
                    // amount max if YES rob the second house, is NY pattern
                    var secondYes = foreTwo[0] + nums[i]
                    foreTwo = intArrayOf(secondNo, secondYes)
                }
                return foreTwo.max()
            }
        }
    }
}
