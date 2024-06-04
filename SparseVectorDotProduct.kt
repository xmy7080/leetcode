class SparseVector(nums: IntArray) {
    var listPairs: List<Pair<Int, Int>> = mutableListOf<Pair<Int, Int>>()
    init {
        nums.forEachIndexed { idx, value ->
            if (value != 0) listPairs += Pair(idx, value)
        }
    }
    // Return the dotProduct of two sparse vectors
    fun dotProduct(vec: SparseVector): Int {
        var i = 0
        var j = 0
        var result = 0
        while (i < listPairs.size && j < vec.listPairs.size){
            if (listPairs[i].first == vec.listPairs[j].first){
                result += listPairs[i].second * vec.listPairs[j].second
                i++
                j++
            }
            else if (listPairs[i].first < vec.listPairs[j].first) {
                i++
            }
            else {
                j++
            }
        }
        return result
    }
}

/**
 * Your SparseVector object will be instantiated and called as such:
 * var v1 = SparseVector(nums1)
 * var v2 = SparseVector(nums2)
 * val ans = v1.dotProduct(v2)
 */
