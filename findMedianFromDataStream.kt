class MedianFinder() {
    val low = PriorityQueue<Int>(compareBy {-it})
    val high = PriorityQueue<Int>()
    fun addNum(num: Int) {
        // add number strategically to two heaps
        if(low.isEmpty() && high.isEmpty()){
            low.add(num) //either is fine
        } else if(low.isEmpty()){
            high.add(num) //we know high is not empty, so it will maintain an order there
        } else if(high.isEmpty()){
            low.add(num)
        } else{ // both are not empty
            when{
                num < high.peek() ->{
                    low.add(num)
                }// be aware of the case when high and low peek are the same number, say 29, then a thrid 29 won't make it
                num >= low.peek() ->{
                    high.add(num)
                }
            }
        }
        //rebalance
        if(high.size == low.size + 2){
            val move = high.poll()
            low.add(move)
        } else if(low.size == high.size + 2){
            val move = low.poll()
            high.add(move)
        }
    }

    fun findMedian(): Double {
        if(low.size == high.size){
            val lowTop = low.peek().toDouble()
            val highBottom = high.peek().toDouble()
            return (lowTop + highBottom)/ 2.0
        } else if(low.size == high.size + 1) return low.peek().toDouble()
        else return high.peek().toDouble()
    }

}

/**
 * Your MedianFinder object will be instantiated and called as such:
 * var obj = MedianFinder()
 * obj.addNum(num)
 * var param_2 = obj.findMedian()
 */
