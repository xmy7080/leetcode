// regarding to tutorial, keep an hashset to dedupe pair of indexes,
// starting with 0,0 pop it from pq and add two more possible least big pairs as 1,0 and 0,1 
// then pop another one and add +1,0 and 0,+1 to the pop out pair, keep the cycle going until find k or exhaust two arrays
class Solution {
    fun kSmallestPairs(nums1: IntArray, nums2: IntArray, k: Int): List<List<Int>> {
        val pq = PriorityQueue<Pair<Int, Int>>(compareBy {nums1[it.first] + nums2[it.second]})
        val hset = HashSet<Pair<Int, Int>>()
        val res = mutableListOf<List<Int>>()
        
        val m = nums1.size
        val n = nums2.size
        pq.add(Pair(0, 0))
        hset.add(Pair(0, 0))
        while(res.size < k && pq.isNotEmpty()){
            val (idx1, idx2) = pq.poll()
            res.add(listOf(nums1[idx1], nums2[idx2]))
            for((x, y) in setOf(1 to 0, 0 to 1)){
                val n1 = idx1 + x
                val n2 = idx2 + y
                if(n1 < m && n2 < n && !hset.contains(Pair(n1, n2)) ){
                    pq.add(Pair(n1, n2))
                    hset.add(Pair(n1, n2))
                }
            }
        }
        return res
    }
}
