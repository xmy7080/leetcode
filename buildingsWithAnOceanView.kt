class Solution {
    fun findBuildings(heights: IntArray): IntArray {
        var result = mutableListOf<Int>()
        var heightWithView = 0
        for (idx in heights.size - 1 downTo 0) {
            if (heights[idx] > heightWithView) {
                result.add(idx)
                heightWithView = heights[idx]
            }
        }
        return result.reversed().toIntArray()
    }
}
