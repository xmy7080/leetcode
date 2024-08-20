class Solution {
    fun findPeakElement(nums: IntArray): Int {
        var l = 0
        var r = nums.size - 1
        while (l < r){
            var mid = l + (r-l)/2
            if (mid + 1 < nums.size && nums[mid] < nums[mid+1]) {
                l = mid + 1
            } else if (mid -1 >= 0 && nums[mid-1] > nums[mid]) {
                r = mid - 1
            } else return mid
        }
        return l
    }
}
