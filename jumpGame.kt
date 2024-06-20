class Solution {
    fun canJump(nums: IntArray): Boolean {
        var boolarr = BooleanArray(nums.size) {false}
        boolarr[0] = true
        nums.forEachIndexed{idx, value ->
            if (boolarr[idx]) {
                val minspan = minOf(nums.size-1, idx + value)
                for (j in idx .. minspan) {
                    boolarr[j] = true
                }
            }
        }
        return boolarr[nums.size-1]
    }
}
