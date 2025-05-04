class Solution {
    fun moveZeroes(nums: IntArray): Unit {
        var non0idx = 0
        for(num in nums){
            if(num != 0) {
                nums[non0idx++] = num
            }
        }
        for(i in non0idx until nums.size){
            nums[i] = 0
        }
    }
}
