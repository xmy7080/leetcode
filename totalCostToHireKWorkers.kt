// self solution with priority queue, didn't check the editorial solution
class Solution {
    data class Worker(
        val index: Int,
        val cost: Int
    )
    fun totalCost(costs: IntArray, k: Int, candidates: Int): Long {
        val pq = PriorityQueue<Worker>(compareBy ({it.cost}, {it.index}))
        // val hs = HashSet<Worker>()
        // add first round candidates in pq
        var fIndex = 0
        var bIndex = 0
        for(i in 0 until candidates){
            fIndex = i
            bIndex = costs.size - 1 - i
            if(bIndex == fIndex) { // handle (x x x) and candidate = 2 scenario
                pq.add(Worker(cost = costs[i], index = i))
                break
            }
            else if(bIndex < fIndex) break // handle (x x x x) and candidate = 3 scenario

            
            pq.add(Worker(cost = costs[i], index = i))
            // hs.add(Worker(cost = costs[i], index = i))
            pq.add(Worker(cost = costs[bIndex], index = bIndex))
            // hs.add(Worker(cost = costs[bIndex], index = bIndex))
        }
        // pq.forEach{value ->
        //     println("cost " + value.cost + " index " + value.index)
        // }
        var res = 0L
        // run sessions from 1 to k
        for (session in 1 .. k){
            val hired = pq.poll()
            // println("f index is " + fIndex +  " back index is " + bIndex + "  index " + hired.index)
            res += hired.cost
            if(fIndex >= bIndex) continue
            if(hired.index <= fIndex) {
                fIndex ++
                // this condition cannot be >=, because if b == f it means we added one element twice
                if (bIndex > fIndex) pq.add(Worker(cost = costs[fIndex], index = fIndex))
            }
            else if(hired.index >= bIndex) {
                bIndex --
                // this condition cannot be >=, because if b == f it means we added one element twice
                if (bIndex > fIndex) pq.add(Worker(cost = costs[bIndex], index = bIndex))
            }

        }
        return res
    }
}
