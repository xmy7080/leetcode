class Solution {
    // data class City(num: Int, spend: Int)

    fun findCheapestPrice(n: Int, flights: Array<IntArray>, src: Int, dst: Int, k: Int): Int {
        // adjacent distant map
        val dmap = HashMap<Int, HashMap<Int, Int>>()
        flights.forEach{array ->
            var connects = dmap[array[0]]?: hashMapOf<Int, Int>()
            connects[array[1]] = array[2]
            dmap.put(array[0],  connects)
        }
        // dmap.entries.forEach{entry ->
        //     entry.value.entries.forEach{city ->
        //      println("from " + entry.key + " to " + city.key + " price " + city.value)
        //     }
        // }
        // key: city, value: spent so far
        val spent = HashMap<Int, Int>()
        spent[src] = 0
        var steps = 0
        val queue = ArrayDeque<IntArray>()
        queue.add(intArrayOf(src, 0))
        while (queue.isNotEmpty()){
            // println("steps " + steps + " queue " + queue.toList().joinToString(","))
            for (i in queue.size downTo 1){
                val currCityEntry = queue.removeFirst()
                val currCity = currCityEntry[0]
                val currSpent = currCityEntry[1]
                val possibleNextMove = dmap[currCity]?: hashMapOf<Int, Int>()
                for (nextHop in possibleNextMove.entries.iterator()) {
                    val newSpent = currSpent + nextHop.value

                    // println("from " + currCity + " spent " + spent[currCity]!! +" to " +nextHop.key + " spent " + nextHop.value)
                    if (nextHop.key !in spent || newSpent < spent[nextHop.key]?: 0) {
                        spent[nextHop.key] = newSpent
                        queue.addLast(intArrayOf(nextHop.key,newSpent) )
                    }
                }
            }
            // println("spent list " + spent.entries.map{"key " + it.key + " value " +it.value }.joinToString(","))
            steps ++
            if (steps > k) break
        }
        return spent[dst] ?: -1
    }
}
