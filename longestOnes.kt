class Solution {
    fun longestOnes(nums: IntArray, limit: Int): Int {
        var l = 0
        var r = 0
        var k = limit
        var res = 0
        while(r < nums.size){
            // if r == 1 or k > 0 keep going to the right
            while(r < nums.size && (nums[r] == 1 || k > 0) ) {
                // if r == 0 reduct k by 1
                if(nums[r] == 0) k --
                r ++
            }
            //update res by r-l
            res = if(r - l > res) r - l else res
            // if l is 1, keep going right because it doesn't change the 0 status
            while(l < nums.size && nums[l] == 1){
                l ++
            }
            // if nums[l] == 0, remove 0 at l, add another 0 to the right side, next loop to check if we see a 1 at r+1
            if(l < nums.size && nums[l] == 0) {
                l++
                r++ // we cannot bump k here because it could be 0 to begin with,
                //instead, we know r at the moment must be at a 0 place, therefore bump r is safe
                //also, it keeps r to the equal or right side of l
            }
        }
        return res
    }
}
