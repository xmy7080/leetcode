// use of monotonic stack
class StockSpanner() {
    val monoStack = ArrayDeque<IntArray>()
    var index = 0
    fun next(price: Int): Int {
        index ++
        while(!monoStack.isEmpty() && monoStack.first()!![0] <= price){
            // println("first price in stack is " + monoStack.first()!![0])
            monoStack.removeFirst()
        }
        // monoStack.forEach{value ->
        //     print("index " + value[1] +  " value " + value[0] + ", ")
        // }
        // println("")
        val days = if(monoStack.isEmpty()) index
        else {
            index - monoStack.first()!![1]
        }
        monoStack.addFirst(intArrayOf(price, index))
        return days
    }

}

/**
 * Your StockSpanner object will be instantiated and called as such:
 * var obj = StockSpanner()
 * var param_1 = obj.next(price)
 */
