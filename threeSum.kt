class Solution {
    fun threeSum(nums: IntArray): List<List<Int>> {
        nums.sort()
        val res = mutableSetOf<List<Int>>() // use set to avoid duplicates
        for(i in 0 until nums.size){
            val target = -1 * nums[i]
            var l = i+1
            var r = nums.size -1
            while(l < r){
                if(nums[l] + nums[r] == target) {
                    res.add(listOf(nums[i], nums[l++], nums[r--]))
                }
                else if (nums[l] + nums[r] < target) l ++
                else r --
            }
        }
        return res.toList()
    }
}
// class Solution {
//     fun threeSum(nums: IntArray): List<List<Int>> {
//         // nums.sort()
//         val res = mutableSetOf<List<Int>>()
//         for(i in 0 until nums.size){
//             val target = -1 * nums[i]
//             val tmp = mutableSetOf<Int>()
//             for(j in i+1 until nums.size){
//                 if( tmp.contains(target - nums[j]) ){
//                     res.add(listOf(nums[i], nums[j], target - nums[j]).sorted())
//                 } else
//                     tmp.add(nums[j])
//             }
//         }
//         return res.toList()
//     }
// }
