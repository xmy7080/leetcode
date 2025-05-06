// editorial solution, using a queue and stack and lazy deletion when pop/poll from the top
class MaxStack() {
    // private val queue = PriorityQueue<IntArray>(compareBy<IntArray> {-it[0]}.thenBy{-it[1]})
    private val queue = PriorityQueue<IntArray>{a, b -> if(a[0] == b[0]) b[1] - a[1] else b[0] - a[0]}
    private val stack = Stack<IntArray>()
    private val deleted = mutableSetOf<Int>()
    private var cnt = 0
    fun push(x: Int) {
        val newPair = intArrayOf(x, cnt++)
        queue.add(newPair)
        stack.push(newPair)
    }

    fun pop(): Int {
        while(stack.peek()[1] in deleted){
            stack.pop()
        }
        val pair = stack.pop()
        deleted.add(pair[1])
        return pair[0]
    }

    fun top(): Int {
        while(stack.peek()[1] in deleted){
            stack.pop()
        }
        return stack.peek()[0]
    }

    fun peekMax(): Int {
        while(queue.peek()[1] in deleted){
            queue.poll()
        }
        return queue.peek()[0]
    }

    fun popMax(): Int {
        while(queue.peek()[1] in deleted){
            queue.poll()
        }
        val pair = queue.poll()
        deleted.add(pair[1])
        return pair[0]
    }

}

/**
 * Your MaxStack object will be instantiated and called as such:
 * var obj = MaxStack()
 * obj.push(x)
 * var param_2 = obj.pop()
 * var param_3 = obj.top()
 * var param_4 = obj.peekMax()
 * var param_5 = obj.popMax()
 */
