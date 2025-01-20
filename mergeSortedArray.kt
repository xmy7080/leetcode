class Solution {
    fun merge(nums1: IntArray, m: Int, nums2: IntArray, n: Int): Unit {
        var last = nums1.size - 1
        var idx1 = m - 1
        var idx2 = n - 1
        while(last >= 0){
            if(idx1 < 0){
                nums1[last] = nums2[idx2]
                idx2 --
            } else if(idx2 < 0) {
                nums1[last] = nums1[idx1]
                idx1 --
            } else if(nums1[idx1] > nums2[idx2]){
                nums1[last] = nums1[idx1]
                idx1 --
            } else{
                nums1[last] = nums2[idx2]
                idx2 --
            }
            last --
        }
    }
}
