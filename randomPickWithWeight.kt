class Solution(w: IntArray) {
    val tree = TreeMap<Int, Int>()
    var sum = 0
    val rand = Random(5)
    init {
        for (i in 0 until w.size) {
            tree.put(sum, i)
            sum += w[i]
        }
    }
    fun pickIndex(): Int {
        val ranNum = rand.nextInt(sum)
        return tree.floorEntry(ranNum).value!!
    }

}

/**
 * Your Solution object will be instantiated and called as such:
 * var obj = Solution(w)
 * var param_1 = obj.pickIndex()
 */
