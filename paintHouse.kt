class Solution {
    fun minCost(costs: Array<IntArray>): Int {
        var rgb = IntArray(3)
        costs.forEach{cost ->
            val nextRed   = Math.min(rgb[1], rgb[2]) + cost[0]
            val nextBlue  = Math.min(rgb[0], rgb[2]) + cost[1]
            val nextGreen = Math.min(rgb[0], rgb[1]) + cost[2]
            rgb[0] = nextRed
            rgb[1] = nextBlue
            rgb[2] = nextGreen
        }
        return rgb.min()
    }
}
