// look at the editorial solution
// Also, when nums[i] == 0, we need bump i++ as well, because think of case when nums: [0,0,1], i will stay in 0 if we don't bump it and funny thing will happen
class Solution {
    fun sortColors(nums: IntArray): Unit {
        var p0 = 0
        var p2 = nums.size -1
        var i = 0
        while(i <= p2){
            if(nums[i] == 0){
                nums[i++] = nums[p0]
                nums[p0] = 0
                p0++
            } else if(nums[i] == 2){
                nums[i] = nums[p2]
                nums[p2] = 2
                p2--
            } else
                i++
        }
    }
}
