class Solution {
    fun minMeetingRooms(intervals: Array<IntArray>): Int {
        val times = mutableListOf<Pair<Int, Int>>()
        intervals.forEach{itv ->
            times.add(Pair(itv[0], 1))
            times.add(Pair(itv[1], -1))
        }
        // sortedBy + one field
        // sortedWith + multiple fields
        val countable = times.sortedWith(compareBy ({it.first}, {it.second}))
        var rooms = 0
        var result = 0
        countable.forEach{time ->
            rooms += time.second
            result = maxOf(result, rooms)
        }
        // println("countable is " + countable.map{"time " + it.first + " in/out " + it.second}.joinToString("\n"))
        return result
    }
}
