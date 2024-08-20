//first check the editorial solution
class Solution {
    fun findPeakElement(nums: IntArray): Int {
        var l = 0
        var r = nums.size - 1
        while (l < r){
            var mid = l + (r-l)/2
            if (mid + 1 < nums.size && nums[mid] < nums[mid+1]) { 
                // if mid has right neighbor and trending up, no matter what the r node is higher or lower than mid, it has a peak to the right of mid
                l = mid + 1
            } else if (mid -1 >= 0 && nums[mid-1] > nums[mid]) {
                // if mid has left neighbor and trending up, no matter what the l node is higher or lower than mid, it has a peak to the left of mid
                r = mid - 1
            } else return mid
        }
        return l
    }
}
