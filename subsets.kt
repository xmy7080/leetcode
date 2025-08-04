class Solution {
    fun subsets(nums: IntArray): List<List<Int>> {
        val tmp = mutableListOf<Int>()
        val result = MutableList<List<Int>>(1){listOf<Int>()}
        // result.add(listOf())
        fun dfs(index: Int) {
            for(i in index until nums.size){
                tmp.add(nums[i])
                result.add(tmp.toList())
                dfs(i+1)
                tmp.removeLast()
            }
        }
        dfs(0)
        return result
    }
}
