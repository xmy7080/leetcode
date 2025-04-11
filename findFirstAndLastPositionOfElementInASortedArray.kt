class Solution {
    fun searchRange(nums: IntArray, target: Int): IntArray {
        var l = 0
        var r = nums.size-1
        var res = IntArray(2){-1}
        while(l <= r){
            val mid = l + (r - l)/2
            if(nums[mid] < target) l = mid + 1
            else if(nums[mid] > target) r = mid - 1
            else{ // nums[mid] == target
                if(mid == 0) {
                    res[0] = mid
                    break
                }
                else if(nums[mid-1] < target) {
                    res[0] = mid
                    break
                }
                else if(nums[mid-1] == target) {
                    r = mid - 1
                    res[0] = mid - 1
                    }
            }
        }
        l = 0
        r = nums.size-1
        while(l <= r){
            val mid = l + (r - l)/2
            if(nums[mid] < target) l = mid + 1
            else if(nums[mid] > target) r = mid - 1
            else{ // nums[mid] == target
                if(mid == nums.size-1) {
                    res[1] = mid
                    break
                }
                else if(nums[mid+1] > target) {
                    res[1] = mid
                    break
                }
                else if(nums[mid+1] == target) {
                    l = mid + 1
                    res[1] = mid + 1
                }
            }
        }
        return res
    }
}
