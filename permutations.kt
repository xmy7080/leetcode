class Solution {
    var n = intArrayOf()
    var result = mutableListOf<List<Int>>()

    fun permute(nums: IntArray): List<List<Int>> {
        this.n = nums
        val picked = HashSet<Int>()
        var temp = mutableListOf<Int>()
        dfs(temp, picked)
        return this.result.toList()

    }

    fun dfs(temp: MutableList<Int>, picked: HashSet<Int>) {
        if (temp.size == this.n.size) {
            this.result.add(temp.toList())
            return
        }
        for (num in n){
            if (num !in picked){
                temp.add(num)
                picked.add(num)
                dfs(temp, picked)
                temp.remove(num)
                picked.remove(num)
            }
        }
    }
}
