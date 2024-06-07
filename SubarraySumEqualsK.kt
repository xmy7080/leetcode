// map contains disctinct array sum from beginning to its appearances, say we got [1,-1,1], then (0 -> 2) because 1 + (-1) = 0 and empty list = 0
class Solution {
    fun subarraySum(nums: IntArray, k: Int): Int {
        var arrSumDic = mutableMapOf<Int, Int>(0 to 1)
        var arrSum = 0
        var result = 0
        nums.forEachIndexed { idx, value ->
            arrSum += value
            if (arrSumDic.contains((arrSum - k)) ){
                result += arrSumDic[arrSum - k]!!
            }
            if (arrSumDic.contains(arrSum)) arrSumDic[arrSum] = arrSumDic[arrSum]!! + 1
            else arrSumDic.put(arrSum, 1)
        }
        return result
    }
}
