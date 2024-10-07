//use of monotonic stack
class Solution {
    fun dailyTemperatures(temperatures: IntArray): IntArray {
        val stack = ArrayDeque<IntArray>()
        val res = IntArray(temperatures.size){0}
        for(i in temperatures.size -1 downTo 0){
            while(stack.size > 0 && stack.first()!![0] <= temperatures[i]) {
                stack.removeFirst()
            }
            if(!stack.isEmpty()){
                res[i] = stack.first()!![1] - i
            }
            stack.addFirst(intArrayOf(temperatures[i], i))
        }
        return res
    }
}
