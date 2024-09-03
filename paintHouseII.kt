class Solution {
    fun minCostII(costs: Array<IntArray>): Int {
        // var colors = Array(costs.size){ Array(2){IntArray(2)} } // for each row, save the min cost and its color number, and second min cost and its color number
        // var colors = Array(2){IntArray(2)} 
        // [0][0], [0][1] stands for        min cost and its color id
        // [1][0], [1][1] stands for second min cost and its color id
        var prevMinCost = 0
        var prevMinColor = -1
        var prevSecMinCost = 0

        costs.forEach{cost ->
            val pq = PriorityQueue<IntArray>(compareBy {-it[0]}) // we are using a max heap here
            cost.forEachIndexed{idx,  price  ->
                if (idx == prevMinColor) // if the color collide with previous house, use the second min cost, otherwise use the min cost strightly
                    pq.add(intArrayOf(price + prevSecMinCost, idx))
                else pq.add(intArrayOf(price + prevMinCost, idx))
                if ( pq.size > 2) pq.poll()
            }
            val secondMinPair = pq.poll() // (cost, idx) color with second min cost on i house
            val minPair = pq.poll() // (cost, idx) color with min cost on i house
            prevMinCost = minPair[0]
            prevMinColor = minPair[1]
            prevSecMinCost = secondMinPair[0]
        }
        return prevMinCost
    }
}
