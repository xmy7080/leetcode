// Explanation:

// Put all arrivals in one heap and all departures in another heap - this helps us to go by the chronogical order of time
// If smallest time in arrivals heap is less than smallest time in departures heap, then pop from arrivals heap and occupy the 1st available table with the popped element.
// If popped index/friend is the target friend, then return the occupied index
// Else if smallest time in departures heap is less than or equal to smallest time in arrivals heap, then pop from departures heap and vacate the table occupied by the popped element

class Solution {
    fun smallestChair(times: Array<IntArray>, targetFriend: Int): Int {
        val targetTime = times[targetFriend][0]
        val arrivals = PriorityQueue<IntArray>() {a: IntArray, b: IntArray -> a[0] - b[0]} // first element will be time, second will be idx
        val departures = PriorityQueue<IntArray>() {a: IntArray, b: IntArray -> a[0] - b[0]} // same as above
        val availableChairs = PriorityQueue<Int>()
        times.forEachIndexed{idx, ints ->
            arrivals.offer(intArrayOf(ints[0], idx)) // time and index pair
            departures.offer(intArrayOf(ints[1], idx)) // time and index pair
            availableChairs.offer(idx)
        }
        val idxToChair = HashMap<Int, Int>()
        while (true) {
            val topArrival = arrivals.peek()
            val topDeparture = departures.peek()
            if (topArrival[0] < topDeparture[0]) {
                val chairToPick = availableChairs.poll()
                idxToChair[topArrival[1]] = chairToPick
                arrivals.poll()
                if (topArrival[0] == targetTime) return chairToPick
            }
            else {
                val chairToPutBack = idxToChair[topDeparture[1]]
                availableChairs.offer(chairToPutBack)
                departures.poll()
            }
        }
    }
}
