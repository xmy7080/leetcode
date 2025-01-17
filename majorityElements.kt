// use the very newly learned boyer moore algorithm, invented in 1981
//https://leetcode.com/problems/majority-element/editorial/?envType=study-plan-v2&envId=top-interview-150
class Solution {
    fun majorityElement(nums: IntArray): Int {
        var major = 0
        var count = 0
        for(n in nums){
             if(count == 0){
                major = n
                count ++
             } else {
                if(n != major) count --
                else count ++
             }
        }
        return major
    }
}
