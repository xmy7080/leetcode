class Solution {
    fun intervalIntersection(firstList: Array<IntArray>, secondList: Array<IntArray>): Array<IntArray> {
        var firstIdx = 0
        var secIdx = 0
        var result = mutableListOf<IntArray>()
        while (firstIdx < firstList.size && secIdx < secondList.size) {
            val overLap = getOverLap(firstList[firstIdx], secondList[secIdx])
            if (overLap != null) result += overLap!!
            //move up first or second index
            if (firstList[firstIdx][1] > secondList[secIdx][1]) secIdx += 1
            else firstIdx += 1
        }
        // if (firstIdx == firstList.size)
        return result.toTypedArray()
    }

    fun isOverLap(first: IntArray, second: IntArray): Boolean {
        return !(first[1] < second[0] || first[0] > second[1])
    }

    fun getOverLap(first: IntArray, second: IntArray): IntArray? {
        if (!isOverLap(first, second)) return null
        val start = if (first[0] > second[0]) first[0]
            else second[0]
        val end = if (first[1] > second[1]) second[1]
            else first[1]
        return intArrayOf(start, end)
    }
}
