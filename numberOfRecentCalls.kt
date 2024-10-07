// very straight forward use of queue
class RecentCounter() {
    val calls = ArrayDeque<Int>()
    fun ping(t: Int): Int {
        val prevTime = t - 3000
        while(!calls.isEmpty() && calls.first()!! < prevTime){
            calls.removeFirst()
        }
        calls.addLast(t)
        return calls.size
    }

}

/**
 * Your RecentCounter object will be instantiated and called as such:
 * var obj = RecentCounter()
 * var param_1 = obj.ping(t)
 */
