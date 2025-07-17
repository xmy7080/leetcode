class Solution {
    fun sortedSquares(nums: IntArray): IntArray {
        val result = IntArray(nums.size)
        var l = 0
        var r = nums.size -1
        var i = nums.size -1
        while(l <= r){
            when(Math.abs(nums[l]) < Math.abs(nums[r]) ){
                true -> {
                    result[i] = nums[r] * nums[r]
                    r--
                }
                false -> {
                    result[i] = nums[l] * nums[l]
                    l++
                }
            }
            i--
        }
        return result
    }
}
