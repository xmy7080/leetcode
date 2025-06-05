// refers to editorial solution
class Solution {
    fun nextPermutation(nums: IntArray): Unit {
        var i = nums.size -2
        //find first number drop from the tail, i become the left idx to be swap
        while(i >=0 && nums[i] >= nums[i+1]) i --
        if(i >= 0) { // when nums are not always decreasing
            var j = nums.size -1
            // find the first number larger than nums[i] from right side of nums to i
            while(j > i && nums[j] <= nums[i]) j --
            // when we did find something to swap
            swap(nums, i, j)
            reverse(nums, i + 1)
        } else{
            reverse(nums, 0)
        }
    }

    private fun reverse(nums: IntArray, start: Int){
        var i = start
        var j = nums.size -1
        while(i <j){
            swap(nums, i, j)
            i ++
            j --
        }
    }
    private fun swap(nums: IntArray, i: Int, j: Int){
        val tmp = nums[i]
        nums[i] = nums[j]
        nums[j] = tmp
    }
}
