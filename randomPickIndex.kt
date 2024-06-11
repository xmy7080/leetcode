class Solution(nums: IntArray) {
    val dic = hashMapOf<Int, MutableList<Int>>()
    // val rand = Random(5)
    init {
        nums.forEachIndexed {idx, num ->
            dic.computeIfAbsent(num) {mutableListOf()}.add(idx)
            // if (num !in dic ) dic[num] = mutableListOf(idx)
            // else dic[num]!!.add(idx)
        }
    }
    fun pick(target: Int): Int {
        return dic[target]!!.random()
        // val indexes = dic[target]!!
        // val randomPickIdx = rand.nextInt(indexes.size)
        // return indexes[randomPickIdx]
    }

}

/**
 * Your Solution object will be instantiated and called as such:
 * var obj = Solution(nums)
 * var param_1 = obj.pick(target)
 */
