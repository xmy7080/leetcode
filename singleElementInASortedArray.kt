class Solution {
    fun singleNonDuplicate(nums: IntArray): Int {
        val size = nums.size
        // if(size ==1) return nums[0]
        var l = 0
        var r = size-1
        while(l < r){
            val mid = l + (r-l)/2
            when(mid % 2){
                0 -> {
                    if(mid < size -1 && nums[mid] == nums[mid+1]){ //[1 1 mid(2) 2 0] cases, single must be to the right
                        l = mid + 2
                    } else if (mid > 0 && nums[mid] == nums[mid -1]){ //[0 1 mid(1) 2 2] cases, single must be to the left
                        r = mid - 2
                    } else return nums[mid] // if no neighbor equals found, mid must be that single value
                }
                1 ->{
                    if(mid < size -1 && nums[mid] == nums[mid+1]){ //[0 1 1 mid(2) 2] cases, single must be to the left
                        r = mid - 1
                    } else if (mid > 0 && nums[mid] == nums[mid -1]){ //[1 mid(1) 2 2 0] cases, single must be to the right
                        l = mid + 1
                    } else return nums[mid] // if no neighbor equals found, mid must be that single value
                }
            }
            // if( (mid in 1 until size-1 && nums[mid] != nums[mid-1]&& nums[mid] != nums[mid+1]) ||
            //     (mid == 0 && nums[mid] != nums[mid+1]) ||
            //     (mid == size -1 && nums[mid] != nums[mid-1]) ) return nums[mid]
            // if(mid < size-1 && nums[mid] == nums[mid+1]) {
            //     when(mid %2){
            //         0 -> l = mid + 2
            //         1 -> r = mid - 1
            //     }
            // } else if(mid > 0 && nums[mid] == nums[mid-1]){
            //     when(mid-1 %2){
            //         0 -> l = mid + 1
            //         1 -> r = mid - 2
            //     }
            // }

        }
        return nums[l] // at the end of the day, l == r == single index
    }
}
