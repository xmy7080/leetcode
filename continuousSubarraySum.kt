// map key: mode of array sum to k
// map value: first appearance index of the sum mode
class Solution {
    fun checkSubarraySum(nums: IntArray, k: Int): Boolean {
        var dic = mutableMapOf<Int, Int>(0 to -1)
        var arrSum = 0

        nums.forEachIndexed{idx, value ->
            arrSum += value
            var modArrSum = arrSum.mod(k)
            if (dic.contains( modArrSum ) ){
                if (idx - dic[modArrSum]!! > 1) return true
            }
            else {
                dic.put(modArrSum, idx)
            }
        }
        return false
    }
}
