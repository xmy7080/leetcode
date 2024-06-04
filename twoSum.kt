class Solution {
    fun twoSum(nums: IntArray, target: Int): IntArray {
        val dict = mutableMapOf<Int, Int>()
        nums.forEachIndexed { idx, value ->
            dict[target - value]?.let { return intArrayOf(it, idx)}
            dict[value] = idx
        }
        return intArrayOf()
    }
}
