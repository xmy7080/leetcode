class MovingAverage(size: Int) {
    val capacity = size
    var total: Double = 0.0
    var queue = ArrayDeque<Int>()
    fun next(`val`: Int): Double {
        queue.addLast(`val`)
        total += `val`
        if (queue.size > capacity) {
            val value = queue.removeFirst()
            total -= value
        }
        val result: Double = total / queue.size
        return result
    }

}

/**
 * Your MovingAverage object will be instantiated and called as such:
 * var obj = MovingAverage(size)
 * var param_1 = obj.next(`val`)
 */
