class Solution {
    fun topKFrequent(nums: IntArray, k: Int): IntArray {
        val counts = HashMap<Int, Int>()
        nums.forEach{
            val oldCount = counts[it] ?: 0
            counts[it] = oldCount + 1
        }
        val pq = PriorityQueue<IntArray>(compareBy {it[0]})
        counts.forEach{
            pq.add(intArrayOf(it.value, it.key) )
            if (pq.size > k) pq.poll()
        }
        return pq.toList().map{it[1]}.toIntArray()
    }
}
